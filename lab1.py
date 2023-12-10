def factorial(n):
        if (n == 1):
            return 1
        elif (n <= 0):
            raise Exception("Нету отрицательного факториала")
        else:
            return (n * factorial(n - 1))

def fibonacci(n):
        if (n == 1):
            return 0
        if (n == 2):
            return 1
        if (n < 1):
            raise Exception("Нету отрицательного ряда")
        else:
            return (fibonacci(n-1) + fibonacci(n-2))


def stepen(a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        elif b < 0:
            return 1 / stepen(a, -b)
        elif 0 < b < 1:
            return pow(a , b)
        return a * stepen(a, b - 1)
class Tests:

    @staticmethod
    def Sortirovka(array):
        swapped = False
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if swapped:
                swapped = False
            else:
                break
        return array

    @staticmethod
    def Polindrom(str):
        for i in range(0, int(len(str) / 2)):
            if str[i] != str[len(str) - i - 1]:
                return False
        return True

    @staticmethod
    def prostoe(a):
        for i in range(2, a // 2+1):
            if (a % i == 0):
                return False
        return True
