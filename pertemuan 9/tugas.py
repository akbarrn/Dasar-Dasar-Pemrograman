# 1.
# def celcius_ke_fahrenheit(celcius):
#     fahrenheit = (celcius * 1.8) + 32
#     return fahrenheit

# print(celcius_ke_fahrenheit(0))
# print(celcius_ke_fahrenheit(100))







#2.
# def is_genap(bilangan_bulat):
#     if bilangan_bulat % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_genap(4))  
# print(is_genap(7))






#3
# def nilai(ipk):
#     if ipk >= 80:
#         print("lulus")
#     else:
#         print("tidak lulus")

# (nilai(80))
# (nilai(60))







#4
def bilangan(bil):
    for i in range(1, bil):
        if i % 2 != 0:
            print(i)
            
bilangan(20)