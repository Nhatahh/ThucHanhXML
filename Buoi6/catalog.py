from lxml import etree
import mysql.connector
import os

# 1. Đường dẫn file XML và XSD
XML_FILE = "catalog.xml"
XSD_FILE = "catalog.xsd"

# 2. Hàm kiểm tra hợp lệ XML
def validate_xml(xml_path, xsd_path):
    try:
        xml_doc = etree.parse(xml_path)
        xsd_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xsd_doc)

        if xmlschema.validate(xml_doc):
            print("File XML hợp lệ với XSD!")
            return xml_doc
        else:
            print("File XML không hợp lệ!")
            for error in xmlschema.error_log:
                print(f" - Dòng {error.line}: {error.message}")
            return None
    except Exception as e:
        print("Lỗi khi đọc/validate XML:", e)
        return None

# 3. Kết nối MySQL
def connect_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="",    
            database="catalog"  
        )
        print("Kết nối MySQL thành công!")
        return conn
    except Exception as e:
        print("Kết nối MySQL thất bại:", e)
        return None

# 4. Tạo bảng
def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id VARCHAR(10) PRIMARY KEY,
            name VARCHAR(100)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id VARCHAR(10) PRIMARY KEY,
            name VARCHAR(100),
            price DECIMAL(10,2),
            currency VARCHAR(10),
            stock INT,
            categoryRef VARCHAR(10),
            FOREIGN KEY (categoryRef) REFERENCES categories(id)
        )
    """)

# 5. Lấy dữ liệu từ XML và chèn vào DB
def insert_data(xml_doc, conn):
    cursor = conn.cursor()
    create_tables(cursor)

    # Lấy danh mục (categories)
    for cat in xml_doc.xpath("//categories/category"):
        cat_id = cat.get("id")
        cat_name = cat.text.strip()

        # Kiểm tra trùng ID → update
        cursor.execute("""
            INSERT INTO categories (id, name)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE name = VALUES(name)
        """, (cat_id, cat_name))

    # Lấy sản phẩm (products)
    for prod in xml_doc.xpath("//products/product"):
        prod_id = prod.get("id")
        name = prod.findtext("name")
        price = float(prod.findtext("price"))
        currency = prod.find("price").get("currency")
        stock = int(prod.findtext("stock"))
        cat_ref = prod.get("categoryRef")

        cursor.execute("""
            INSERT INTO products (id, name, price, currency, stock, categoryRef)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name=VALUES(name),
                price=VALUES(price),
                currency=VALUES(currency),
                stock=VALUES(stock),
                categoryRef=VALUES(categoryRef)
        """, (prod_id, name, price, currency, stock, cat_ref))

    conn.commit()
    print("Đã lưu dữ liệu vào bảng categories và products!")

# 6. Export database ra file .sql 
def export_database_simple(host, user, password, database, output_file):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        with open(output_file, "w", encoding="utf-8") as f:
            for (table_name,) in tables:
                # Xuất cấu trúc bảng
                cursor.execute(f"SHOW CREATE TABLE {table_name}")
                create_stmt = cursor.fetchone()[1]
                f.write(f"\n-- Cấu trúc bảng {table_name}\n")
                f.write(f"DROP TABLE IF EXISTS `{table_name}`;\n")
                f.write(f"{create_stmt};\n\n")

                # Xuất dữ liệu
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                if rows:
                    columns = [desc[0] for desc in cursor.description]
                    for row in rows:
                        values = []
                        for value in row:
                            if value is None:
                                values.append("NULL")
                            else:
                                values.append("'" + str(value).replace("'", "''") + "'")
                        f.write(f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES ({', '.join(values)});\n")
                f.write("\n")

        cursor.close()
        conn.close()
        print(f"Đã export database '{database}' ra file '{output_file}'!")
    except Exception as e:
        print("Lỗi khi export database:", e)

# 7. Chạy chương trình
xml_path = "catalog.xml"
xsd_path = "catalog.xsd"

xml_doc = validate_xml(xml_path, xsd_path)
if xml_doc is not None:
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        create_tables(cursor)
        insert_data(xml_doc, conn)
        export_database_simple(
            host="localhost",
            user="root",
            password="",
            database="catalog",
            output_file="backup_catalog.sql"
        )
        conn.close()
