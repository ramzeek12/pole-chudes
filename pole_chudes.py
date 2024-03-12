list0 = ['крик', 'давление', 'гавайи', 'резистор', 'осьминог', 'маракуйя', 'сердце', 'оловянный']
alphabet = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = list0.pop()
word0 = '_' * len(word)
print('Ваше слово:', word0)
print('Начинаем "Поле Чудес", выберите действие:')
print('1. сдаться')
print('2. ввести букву')
print('3. отгадать слово')
number = int(input())
while number != 1 and number != 2 and number != 3:
    print('Вы ввели недопустимое значение!! , попробуйте снова:')
   number = int(input())
if number == 1:
    print('Еще увидимся! :(')
    input()
if number == 3:
    print('Введите слово:')
    answer = input()
  if answer == word:
        ('Вы отгадали слово! Вы настоящий молодец!')
        input()
    elif answer != word:
        print('Увы,вы не отгадали слово..:(')
        print('Хотите попробовать еще раз?')
        print('1. да')
        print('2. нет')
        number = int(input())
        while number != 1 and number != 2:
            print('Вы ввели недопустимое значение, попробуйте снова:')
            number = int(input())
        if number == 2:
            print('Еще увидимся! :(')
            input()
