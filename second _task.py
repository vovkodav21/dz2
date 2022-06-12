# Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (Прогалини важливі!). Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:

    # Please enter an integer number: 1234
    # Next number for number 1234 is 1235.
    # Previous number for number 1234 is 1233.


first_inp = int(input("Please enter an integer number: "))
next_num = input("Nex number for number " + str(first_inp) + " is " + str(first_inp + 1))
previous_num = first_inp - 1
print(next_num)

print("Previous number for number " + str(first_inp) + " " + "is " + str(previous_num))


