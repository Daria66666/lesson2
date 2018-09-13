def task1(number):
    while True:
        choice = input("""
Перевести в байты - b
Перевести в килобайты - k
""")
        if choice == 'b':
            return number*1024
            break
        elif choice == 'k':
            return number/1024
            break
        else:
            print('Неправильный ввод')
    
    
def task2(number):
    summa = 0
    pr = 1
    while number > 0:
        rest = number % 10
        number = number // 10
        summa += rest
        pr *= rest
    return summa, pr

    
    
def task3(minimum, maximum, inter):
    print("""
_______________________________
               |               
       x       |       y       
_______________|_______________""")
    for x in range(minimum, maximum, inter):
        y = -1.24*(x**2)+x
        print("""               |               
      """, x, """      |    """, y, """
_______________|_______________""")


def task4(number):
    number = str(number)
    answer = None
    for i in range(len(number) // 2):
        if number[i] != number[-i-1]:
            answer = False
            break
        else:
            answer = True
    return answer


def task5(arr):
    s = 0
    n = 0
    for x in arr:
        if x > 0:
            s += x
            n += 1
    return s / (n or 1)
