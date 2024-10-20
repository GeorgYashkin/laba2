import random

def find_multiples():
    while True:
        try:
            size = int(input("Ввведите кол-во чисел в списке: "))
            if size <= 0:
                print("Это число должно быть положительным целым числом. Попробуйте снова.")
                continue

            break
        except ValueError:
            print("Ошибка при вводе числа. Введите положительное целое число.")

    numbers = [random.randint(0,200) for _ in range(size)]

    while True:
        try:
            x = int(input("Введите цифру X (1-9): "))
            if x == 0:
                print("Цифра X не может быть равна 0. Попробуйте снова.")
                continue
            elif x >= 10:
                print("X должно быть цифрой от 1 до 9. Попробуйте снова.")
                continue

            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целую цифру от 1 до 9.")
        
    multiples = list(filter(lambda num: num % x == 0, numbers))

    print("Сгенерированные числа:", numbers)
    print(f"Числа, кратные {x}:", multiples)

find_multiples()
