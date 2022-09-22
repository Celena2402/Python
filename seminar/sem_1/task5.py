# 5. Напишите программу, которая принимает на вход число и 
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.

print("input N")
num=int(input())
#if ((num%5==0 and num%10==0) or num %15==0) and not num%30==0:
#    print("кратно")
#else:
#    print("не кратно")

print(bool(num%5==0 and num%10==0) or num %15==0) and num%30 !=0
