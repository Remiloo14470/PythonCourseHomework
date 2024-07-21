def is_valid_email(email):
    return '@' in email and (email.endswith('.com') or email.endswith('.ru') or email.endswith('.net'))


def send_email(message, recipient, sender='university.help@gmail.com'):

    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f'3. Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('4. Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'1. Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'2. НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки свзяи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
