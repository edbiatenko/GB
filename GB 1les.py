# print('Task 1')
# print('Привет, меня зовут Егор')
# print('Я из Череповца','дата моего рождения', 28,'.',5,'.',1996)
# print('а как зовут тебя?')
# name = input()
# print('Привет, ', name)
# print('А сколько тебе лет?')
# age = int (input())
# print('*'*100)

# print('*'*100)
# print('Task 2')
#
# print('Предлагаю тебе сыграть в игру')
# print('Напиши "Да" или "Нет"')
# answer = input()
# if answer == 'Да' or 'да' or 'ДА': #Как обойти регистр без прописания вариантов? А можно подключить какой-нибудь словарь, который будет определять варианты "да"?
#     print('Введи любое число секунд, а я переведу это в часы, минуты и секунды' )
#     user_sec = int(input())
#     hours = user_sec // 3600
#     min = (user_sec - hours * 3600) // 60
#     sec = round(user_sec % 60, 2)
#     print('Вот, что получилось:' ,  int(hours), 'часов', int(min), 'минут', int(sec), 'секнуд')
#     print(hours, min, sec)
# else:
#     print('Очень жаль :(')
# print('*'*100)

# print('*'*100)
# print('Task 3')
#
# print('Предлагаю тебе сыграть в еще одну игру')
# print('Сорян, выбора не будет :)')
# print('Введи число')
# user_answer = str(input())
# magic = int(user_answer)+int(user_answer+user_answer)+int(user_answer+user_answer+user_answer)
# print('А вот и ответ:', magic)
# print('А магия в том, что цифра получилось по прнципу "n+nn+nnn", где n - твое число')
# print('*'*100)

# print('*'*100)
# print('Task 4')
#
# print('Введите число')
# user_answer = abs(int(input()))
# answer = user_answer % 10
# while user_answer >= 1:
#     user_answer = user_answer // 10
#     if user_answer % 10 > answer:
#         answer = user_answer % 10
#     if user_answer > 9:
#         continue
#     else:
#         print('Самая большая цифра в числе ', answer)
#         break
#print('*'*100)

print('*'*100)
print('Task 5+6')

profit = float(input('Укажите выручку компании '))
print('Выручка = ', profit)
cost = float(input('Укажите издержки компании '))
print('Издержки = ', cost)
if profit > cost:
    print(f'Компания работает с прибылью. Рентабельность составила {profit / cost:.2f}')
    workers = int(input('Введите количество сотрудников компании '))
    print(f'прибыль, в расчете на 1 сторудника = {profit / workers:.2f}')
elif profit == cost:
    print('Компания работает в ноль, такое себе')
else:
    print('Компания работает в убыток. Зайди на hh.ru и найди себе новую работу')
