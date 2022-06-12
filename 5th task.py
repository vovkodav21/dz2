#У математиці функцію `sign(x)` (знак числа) визначено так:
#``

 # sign(x) = 1, якщо x > 0,



 # sign(x) = -1, якщо x < 0,



#  sign(x) = 0 якщо x = 0.

 # ``

 # Для цього числа x виведіть значення sign(x). Це завдання бажано вирішити за допомогою каскадних інструкцій if... elif... else.

a_value = "sign(x)"
input_x = int(input("Введіть ціле число X: "))

if input_x == 0:
 print( "sign(x)" + "= 0")
elif input_x > 0:
 print("sign(x)" + "= 1")
else:
 print("sign(x)" + "= -1")