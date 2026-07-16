sum = 0
while (True):
    numberofshops = int(input("ระบุจำนวนร้านค้า : "))
    for i in range(1, numberofshops + 1):
        price = int(input('เก็บเงินร้านที่ %d : ' % (i)))
        sum += price
    break
print("รวมเงินทั้งหมด %d" % (sum))