#First exercise

first_num = int(input("Please type first number: ")) #користувач вводить перше число
second_num = int(input("Please type second number: "))#користувач вводить друге число

print(first_num + second_num)#виводиться результат

#Second exercise
number=int(input("How many numbers will you use: "))#користувач вводить розмір комірки
list=[]#комірка в якій будуть зберігатись наші числа
for n in range(number):
    list.append(int(input(":")))#користувач вводить числа
list_2=sorted(list)#сортуємо
print(sorted(list))#виводимо список чисел
print("Minimum:",list_2[0])#виводимо мінімальне значення
print("Maximum:",list_2[-1])#виводимо максимальне знаачення

#Third exercise

world=input("Enter a world: ")#користувач вводить слово
reversed="".join(reversed(world))#слово розвертається
print(reversed)#виводимо розвернуте слово