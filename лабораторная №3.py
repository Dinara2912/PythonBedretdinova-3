def task181():
    def printShrugSmile():
        smile = '¯\_(ツ)_/¯'
        print(smile)
    def printKtulhuSmile():
        smile = '{:€ '
        print(smile)
    def printHappySmile():
        smile = '(͡° ͜ʖ ͡°)'
        print(smile)

def task182():
    i = 0
    password = "password"
    while True:
        s = input()
        i += 1
        if s == password and i <= 3:
            print("Пароль принят")
            i += 3
        elif i == 3:
            print("В доступе отказано")

def task183(i):
    a, b = 0, 1
    n = 1
    while n <= i:
        a, b = b, a + b
        n += 1
        if n == i - 1:
            b1 = b
    return (b1 / b)
    print(task183(int(input())))

def task184():
    stt = input()
    res = "NO"

    def test(test_str):
        global res
        for i in [0]:
            opened = 0
            test_arr = list(test_str)
            if test_arr[0] == ")" or test_arr[-1] == "(":
                res = "NO"
                break
            for b in test_arr:
                if b == "(":
                    opened += 1
                elif b == ")":
                    opened -= 1
                else:
                    res = "error"
                    break
            if opened == 0 and res != "error":
                res = "YES"

    test(stt)
    print(res)

def task185():
    def equation(xy1, xy2):
        x1 = int(xy1.split(";")[0])
        y1 = int(xy1.split(";")[1])
        x2 = int(xy2.split(";")[0])
        y2 = int(xy2.split(";")[1])
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        print(k, b)

    equation(input(), input())

def task186():
    def line(s, t):
        x = float(t[:t.index(';')])
        y = float(t[t.index(';') + 1:])
        k = float(s[:s.index('x')])
        b = float(s[s.index('x') + 1:])
        print((k * x + b) == y)

    line(input(), input());

def task191():
    def month_name(num, lan):
        arr_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                  'июль', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
        arr_en = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']
        if lan == 'ru':
            return arr_ru[num - 1]
        else:
            return arr_en[num - 1]

    print(month_name(int(input()), input()))

def task192():
    def t2c(f):
        a = f[:1]
        b = f[1:]
        r = int(b)
        c = 'ABCDEFGH'.find(a) + 1
        return (c, r)

    def c2t(k):
        (c, r) = k
        return 'ABCDEFGH'[c - 1] + str(r)

    def possible_turns(f):
        (c, r) = t2c(f)
        tmp = []
        tmp.append((c + 2, r + 1))
        tmp.append((c + 2, r - 1))
        tmp.append((c - 2, r + 1))
        tmp.append((c - 2, r - 1))
        tmp.append((c + 1, r + 2))
        tmp.append((c - 1, r + 2))
        tmp.append((c + 1, r - 2))
        tmp.append((c - 1, r - 2))
        res = []
        for (a, b) in tmp:
            if (a > 0) & (b > 0) & (a <= 8) & (b <= 8):
                res += [c2t((a, b))]
        return sorted(res)

    print(str(possible_turns(input())))

def task193():
    import math

    def roots_of_quadratic_equation(a, b, c):
        if a == 0 and b == 0 and c == 0:
            return ['all']
        elif a == 0 and b == 0:
            return []
        elif a == 0:
            return [(c * (-1)) / b]
        elif b == 0:
            return [math.sqrt((-1 * b) / a)]
        elif c == 0:
            return [0, (-1 * b) / a]
        else:
            q = b ** 2
            w = -4 * a * c
            D = q + w
            if D < 0:
                return []
            elif D == 0:
                return [(-1 * b) / (2 * a)]
            else:
                D = math.sqrt(D)
                return [int(((-1 * b) - D) / (2 * a)), ((-1 * b) + D) / (2 * a)]

    a, b, c = input().strip().split()

    result = roots_of_quadratic_equation(int(a), int(b), int(c))
    print(*sorted(result))

def task194():
    def palindrome(data):
        data = data.replace(' ', '').lower()
        return 'Палиндром' if data == data[::-1] else 'Не палиндром'

    print(palindrome(input()))

def task195():
    def prime(number):
        n = number
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return 'Простое число' if count == 2 else 'Составное число'

    print(prime(int(input())))

def task196():
    def catalan(n):
        if n >= 2:
            c = ((2 * ((2 * n) - 1)) / (n + 1)) * catalan(n - 1)
            return int(c)
        return 1

    print(catalan(int(input())))

def task201():
    def translate(text):
        lett = 'ыёуеаоэяию.,?-;:ЫЁУЕАОЭЯИЮ'
        res = ''
        for i in text:
            if i not in lett:
                res += i
        return ' '.join(res.split())

    print(translate(input()))

def task202():
    def setup_profile(name, vacationDates):
        global Name
        Name = name
        global date
        date = vacationDates

    def print_application_for_leave():
        print('Заявление на отпуск в период', date + '.', Name)

    def print_holiday_money_claim(amount):
        print('Прошу выплатить', amount, 'отпускных денег', Name)

    def print_attorney_letter(toWhom):
        print('На время отпуска в период', date, 'моим заместителем назначается',
              toWhom + '.', Name)

    setup_profile("Иван Петров", "1 июня – 20 июня")
    print_application_for_leave()
    print_application_for_leave()
    print_holiday_money_claim("15 тысяч пиастров")
    print_attorney_letter("Елена Елева")

def task203():
    list1 = []

    def print_only_new(message):
        global prev
        if message != prev:
            list1.append(message)
            return message
        prev = message

    prev = ''
    print_only_new(input())
    print_only_new(input())
    print_only_new(input())
    print_only_new(input())
    print_only_new(input())
    print_only_new(input())
    print_only_new(input())

    list1 = list(set(list1))
    for i in list1:
        print(i)


def task204():
    base = ['Иван', 'Юлия Иванкова']

    def hello(name):
        print('Здравствуйте, ', name, '! Вашу карту ищут...', sep='')

    def search_card(name):
        if name in base:
            print('Ваша карта с номером', base.index(name) + 1, ' найдена', sep='')
        else:
            print('Ваша карта не найдена')

    hello('Иван')
    search_card('Иван')
    hello('Юлия Иванова')
    search_card('Юлия Иванова')

def task205():
    def lucky(s):
        if sum([int(char) for char in s[:3]]) == sum([int(char) for char in s[-3:]]):
            return "Счастливый"
        else:
            return "Несчастливый"

    print(lucky(input()))

def task206():
    horses = []
    for i in range(10):
        horses.append(0)

    def do_bet(num, bet):
        if 10 >= num > 0 and bet != 0 and not horses[num - 1]:
            horses[num - 1] = bet
            print('Ваша ставка в размере ', bet, ' на лошадь ', num - 1, ' принята', sep='')
        else:
            print('Что-то пошло не так, попробуйте еще раз')

    do_bet(1, 10)
    do_bet(1, 100)
    do_bet(2, 0)
    do_bet(2, 200)

def task211():
    def from_string_to_list(string, container):
        res = string.split(' ')
        for i in res:
            container.append(i)

def task212():
    def transpose(matrix):
        matrix[:] = [list(x) for x in zip(*matrix)]

def task213():
    def swap(first, second):
        third = first[:]
        for i in range(len(first)): first.pop()
        first.extend(second)
        for i in range(len(second)): second.pop()
        second.extend(third)

def task214():
    def defractalize(fractal):
        while fractal in fractal:
            fractal.remove(fractal)

def task215():
    def fractal_print(obj):
        print('[' + ', '.join(map(str, obj)) + ']')


if __name__ == '__main__':
    task183()