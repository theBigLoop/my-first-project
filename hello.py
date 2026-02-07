
#Счетчики
right_answer = 0
how_many_rights = 0

#Программа здоровается
print('Привет! Предлагаю проверить свои знания английского!')
name = input('Напиши, как тебя зовут.')

#Программа считывает имя пользователя
print(f'Привет, {name}, начинаем тренировку')

#Цикл по вопросам
print('My name ___ Vova')
answer1 = input('Твой ответ? ')

#ПЕРВЫЙ вопрос
if answer1 == 'is':
    print('Верно!') 
    right_answer += 10
    how_many_rights += 1
else:
    print('Wrong! Correct answer is - is')

#ВТОРОЙ вопрос
print('I ___ a coder.')
answer2 = input('Твой ответ? ')
if answer2 == 'am':
    print('Верно!') 
    right_answer += 10
    how_many_rights += 1
else:
    print('Wrong! Correct answer is - am')

#ТРЕТИЙ вопрос
print('I live ___ Moscow.')
answer3 = input('Твой ответ? ')
if answer3 == 'in':
    print('Верно!') 
    right_answer += 10
    how_many_rights += 1
else:
    print('Wrong! Correct answer is - in')


#Подсчет результатов
percent = (how_many_rights / right_answer) * 100



print(f'Всего баллов {right_answer} !')
print(f'Всего верно {how_many_rights} ответов!')
print(f'Это {percent} процентов')





