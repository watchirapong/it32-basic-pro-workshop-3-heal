sum = 0
Count = 0
while (True):
    numberofshops = int(input("ระบุจำนวนเงินที่ต้องการจะเก็บ : "))
    while (sum < numberofshops):
        Count += 1
        price = int(input('เก็บเงินร้านที่ %d : ' % (Count)))
        sum += price
    break