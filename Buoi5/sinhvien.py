from lxml import etree

# --- 1. Đọc file XML ---
tree = etree.parse("sinhvien.xml")  
root = tree.getroot()

# --- 2. Lấy tất cả sinh viên ---
students = root.xpath("/school/student")
print("Tất cả sinh viên:")
for s in students:
    print(etree.tostring(s, encoding='unicode'))

# --- 3. Liệt kê tên tất cả sinh viên ---
names = root.xpath("//student/name")
print("\nTên tất cả sinh viên:")
for n in names:
    print(n.text)

# --- 4. Lấy tất cả id của sinh viên ---
ids = root.xpath("//student/id")
print("\nID tất cả sinh viên:")
for i in ids:
    print(i.text)

# --- 5. Lấy ngày sinh của sinh viên có id = "SV01" ---
date_sv01 = root.xpath("//student[id='SV01']/date")
print("\nNgày sinh SV01:", date_sv01[0].text if date_sv01 else "Không tìm thấy")

# --- 6. Lấy các khóa học ---
courses = root.xpath("//enrollment/course")
print("\nCác khóa học:")
for c in courses:
    print(c.text)

# --- 7. Lấy toàn bộ thông tin sinh viên đầu tiên ---
first_student = root.xpath("//student[1]")[0]
print("\nSinh viên đầu tiên:")
print(etree.tostring(first_student, encoding='unicode'))

# --- 8. Lấy mã sinh viên đăng ký khóa Vatly203 ---
sv_vatly203 = root.xpath("//enrollment[course='Vatly203']/studentRef")
print("\nMã sinh viên học Vatly203:")
for sv in sv_vatly203:
    print(sv.text)

# --- 9. Lấy tên sinh viên học môn Toan101 ---
name_toan101 = root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name")
print("\nTên sinh viên học Toan101:")
for n in name_toan101:
    print(n.text)

# --- 10. Lấy tên sinh viên học môn Vatly203 ---
name_vatly203 = root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name")
print("\nTên sinh viên học Vatly203:")
for n in name_vatly203:
    print(n.text)

# --- 11. Lấy tên và ngày sinh của sinh viên sinh năm 1997 ---
sv_1997 = root.xpath("//student[starts-with(date, '1997')]/name | //student[starts-with(date, '1997')]/date")
print("\nSinh viên sinh năm 1997:")
for s in sv_1997:
    print(s.text)

# --- 12. Lấy tên sinh viên sinh trước năm 1998 ---
sv_pre1998 = root.xpath("//student[number(substring(date, 1, 4)) < 1998]/name")
print("\nSinh viên sinh trước 1998:")
for s in sv_pre1998:
    print(s.text)

# --- 13. Đếm tổng số sinh viên ---
count_students = root.xpath("count(//student)")
print("\nTổng số sinh viên:", int(count_students))

# --- 14. Lấy phần tử <date> anh em ngay sau <name> của SV01 ---
date_following = root.xpath("//student[id='SV01']/name/following-sibling::date[1]")
print("\n<Date> sau <name> của SV01:", date_following[0].text if date_following else "Không tìm thấy")

# --- 15. Lấy phần tử <id> anh em ngay trước <name> của SV02 ---
id_preceding = root.xpath("//student[id='SV02']/name/preceding-sibling::id[1]")
print("\n<ID> trước <name> của SV02:", id_preceding[0].text if id_preceding else "Không tìm thấy")

# --- 16. Lấy toàn bộ <course> trong cùng enrollment với SV03 ---
course_sv03 = root.xpath("//enrollment[studentRef='SV03']/course")
print("\nKhóa học của SV03:")
for c in course_sv03:
    print(c.text)

# --- 17. Lấy sinh viên có họ là 'Trần' ---
tran_students = root.xpath("//student[starts-with(name, 'Trần')]/name")
print("\nSinh viên họ Trần:")
for s in tran_students:
    print(s.text)

# --- 18. Lấy năm sinh của SV01 ---
year_sv01 = root.xpath("substring(//student[id='SV01']/date, 1, 4)")
print("\nNăm sinh SV01:", year_sv01)
