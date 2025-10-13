from lxml import etree

# --- 1. Đọc file XML ---
tree = etree.parse("qlquanan.xml")
root = tree.getroot()

# --- 2. Khai báo namespace ---
ns = {"ql": "http://ctut.edu.vn/qlquanan"}

# --- 3. Lấy tất cả bàn ---
bans = root.xpath("//ql:BAN", namespaces=ns)
print("1️⃣ Tất cả bàn:")
for b in bans:
    print(etree.tostring(b, encoding='unicode'))

# --- 4. Lấy tất cả nhân viên ---
nhanviens = root.xpath("//ql:NHANVIEN", namespaces=ns)
print("\n2️⃣ Tất cả nhân viên:")
for nv in nhanviens:
    print(etree.tostring(nv, encoding='unicode'))

# --- 5. Lấy tất cả tên món ---
tenmons = root.xpath("//ql:MON/ql:TENMON", namespaces=ns)
print("\n3️⃣ Tên tất cả món:")
for t in tenmons:
    print("-", t.text)

# --- 6. Lấy tên nhân viên có mã NV02 ---
nv02 = root.xpath("//ql:NHANVIEN[ql:MANV='NV02']/ql:TENV", namespaces=ns)
print("\n4️⃣ Tên nhân viên NV02:", nv02[0].text if nv02 else "Không tìm thấy")

# --- 7. Lấy tên và số điện thoại NV03 ---
nv03 = root.xpath("//ql:NHANVIEN[ql:MANV='NV03']/ql:TENV | //ql:NHANVIEN[ql:MANV='NV03']/ql:SDT", namespaces=ns)
print("\n5️⃣ Tên và số điện thoại NV03:")
for n in nv03:
    print("-", n.text)

# --- 8. Lấy tên món có giá > 50,000 ---
mon_gt_50000 = root.xpath("//ql:MON[number(ql:GIA) > 50000]/ql:TENMON", namespaces=ns)
print("\n6️⃣ Món có giá > 50,000:")
for m in mon_gt_50000:
    print("-", m.text)

# --- 9. Lấy số bàn của hóa đơn HD03 ---
soban_hd03 = root.xpath("//ql:HOADON[ql:SOHD='HD03']/ql:SOBAN", namespaces=ns)
print("\n7️⃣ Số bàn của hóa đơn HD03:", soban_hd03[0].text if soban_hd03 else "Không tìm thấy")

# --- 10. Lấy tên món có mã M02 ---
mon_m02 = root.xpath("//ql:MON[ql:MAMON='M02']/ql:TENMON", namespaces=ns)
print("\n8️⃣ Tên món mã M02:", mon_m02[0].text if mon_m02 else "Không tìm thấy")

# --- 11. Lấy ngày lập hóa đơn HD03 ---
ngay_hd03 = root.xpath("//ql:HOADON[ql:SOHD='HD03']/ql:NGAYLAP", namespaces=ns)
print("\n9️⃣ Ngày lập hóa đơn HD03:", ngay_hd03[0].text if ngay_hd03 else "Không tìm thấy")

# --- 12. Lấy mã món trong hóa đơn HD01 ---
mamon_hd01 = root.xpath("//ql:HOADON[ql:SOHD='HD01']//ql:MAMON", namespaces=ns)
print("\n🔟 Mã món trong hóa đơn HD01:")
for m in mamon_hd01:
    print("-", m.text)

# --- 13. Lấy tên món trong hóa đơn HD01 ---
tenmon_hd01 = root.xpath("//ql:MON[ql:MAMON = //ql:HOADON[ql:SOHD='HD01']//ql:MAMON]/ql:TENMON", namespaces=ns)
print("\n11️⃣ Tên món trong hóa đơn HD01:")
for t in tenmon_hd01:
    print("-", t.text)

# --- 14. Tên nhân viên lập hóa đơn HD02 ---
nv_hd02 = root.xpath("//ql:NHANVIEN[ql:MANV = //ql:HOADON[ql:SOHD='HD02']/ql:MANV]/ql:TENV", namespaces=ns)
print("\n12️⃣ Tên nhân viên lập hóa đơn HD02:", nv_hd02[0].text if nv_hd02 else "Không tìm thấy")

# --- 15. Đếm số bàn ---
count_ban = root.xpath("count(//ql:BAN)", namespaces=ns)
print("\n13️⃣ Số bàn:", int(count_ban))

# --- 16. Đếm số hóa đơn lập bởi NV01 ---
count_hd_nv01 = root.xpath("count(//ql:HOADON[ql:MANV='NV01'])", namespaces=ns)
print("\n14️⃣ Số hóa đơn lập bởi NV01:", int(count_hd_nv01))

# --- 17. Tên món trong hóa đơn bàn số 2 ---
mon_ban2 = root.xpath("//ql:MON[ql:MAMON = //ql:HOADON[ql:SOBAN='2']//ql:MAMON]/ql:TENMON", namespaces=ns)
print("\n15️⃣ Tên món trong hóa đơn bàn số 2:")
for m in mon_ban2:
    print("-", m.text)

# --- 18. Nhân viên phục vụ bàn số 3 ---
nv_ban3 = root.xpath("//ql:NHANVIEN[ql:MANV = //ql:HOADON[ql:SOBAN='3']/ql:MANV]", namespaces=ns)
print("\n16️⃣ Nhân viên phục vụ bàn số 3:")
for nv in nv_ban3:
    print("-", nv.find("ql:TENV", namespaces=ns).text)

# --- 19. Hóa đơn do nhân viên nữ lập ---
hd_nu = root.xpath("//ql:HOADON[ql:MANV = //ql:NHANVIEN[ql:GIOITINH='Nữ']/ql:MANV]", namespaces=ns)
print("\n17️⃣ Hóa đơn do nhân viên nữ lập:")
for h in hd_nu:
    print("-", h.find("ql:SOHD", namespaces=ns).text)

# --- 20. Nhân viên phục vụ bàn số 1 ---
nv_ban1 = root.xpath("//ql:NHANVIEN[ql:MANV = //ql:HOADON[ql:SOBAN='1']/ql:MANV]", namespaces=ns)
print("\n18️⃣ Nhân viên phục vụ bàn số 1:")
for nv in nv_ban1:
    print("-", nv.find("ql:TENV", namespaces=ns).text)

# --- 21. Món được gọi nhiều hơn 1 lần ---
mon_nhieuhon1 = root.xpath("//ql:MON[ql:MAMON = //ql:CTHD[number(ql:SOLUONG) > 1]/ql:MAMON]/ql:TENMON", namespaces=ns)
print("\n19️⃣ Món được gọi > 1 lần:")
for m in mon_nhieuhon1:
    print("-", m.text)

# --- 22. Tên bàn + ngày lập hóa đơn HD02 ---
tenban_ngay_hd02 = root.xpath("//ql:BAN[ql:SOBAN = //ql:HOADON[ql:SOHD='HD02']/ql:SOBAN]/ql:TENBAN | //ql:HOADON[ql:SOHD='HD02']/ql:NGAYLAP", namespaces=ns)
print("\n20️⃣ Tên bàn + ngày lập hóa đơn HD02:")
for t in tenban_ngay_hd02:
    print("-", t.text)

