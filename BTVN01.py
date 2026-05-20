total_amount = int(input("Nhập tổng tiền hóa đơn: "))

if total_amount >= 500000:

    discount = total_amount * 0.10

else:

    discount = 0

final_amount = total_amount - discount

print("Số tiền giảm giá:", discount, "VND")
print("Số tiền khách phải trả:", final_amount, "VND")