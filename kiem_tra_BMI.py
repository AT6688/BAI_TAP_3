w = float(input("nhap vao can nang cua ban ? kg: "))
h = float(input("nhap vao chieu cao cua ban ? m: "))

BMI = w/(h**2)

if(BMI > 40):
    print("béo phì cấp độ III")
elif(35 <= BMI < 40):
    print("béo phì cấp độ II")
elif(30 <= BMI < 35):
    print("béo phì cấp độ I")
elif(25 <= BMI < 30):
    print("thừa cân")
elif(18.5 <= BMI < 25):
    print("bình thường")
elif(17 <= BMI < 18.5):
    print("gầy cấp độ I")
elif(16 <= BMI < 17):
    print("gầy cấp độ II")
elif(BMI < 16):
    print("gầy cấp độ III")