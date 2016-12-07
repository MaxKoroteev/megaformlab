# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import redirect


def site(request):

    applications = [
        {'title': '10 класс — Курс школьной программы (9 месяцев)',
         'format': 'Удалённо',
         'group': 'Индивидуальные занятия',
         'status': 'Совсем маленький',
         'price': 300},
        {'title': '10 класс — Курс школьной программы (3 месяцев)',
         'format': 'У репетитора',
         'group': 'Занятия в группе до 3-ёх человек',
         'status': 'Школьник',
         'price': 1000},
        {'title': '10 класс — Курс школьной программы (6 месяцев)',
         'format': 'У себя',
         'group': 'Занятия в группе до 2-ух человек',
         'status': 'Студент',
         'price': 500},
    ] * 2

    dialogs = [
        {'avatar': 'http://michaelgowin.com/blog/wp-content/uploads/2014/03/strauss.jpg',
         'name': u'Александр Викторович',
         'first_name': u'Александр',
         'time': u'20 минут назад',
         'message': u'Петь, когда занимаемся в следующий раз?',
         'class': u'unread',
         'counter': u'2',
         'my_message': False},
        {'avatar': 'http://www.joblo.com/newsimages1/cool-videos-django-sam-jackson.jpg',
         'name': u'Патрис Лумумба',
         'first_name': u'Патрис',
         'time': u'30 минут назад',
         'message': u'Да, после концерта памяти тупака',
         'class': u'unread',
         'counter': u'1',
         'my_message': False},
        {'avatar': 'http://305hiphop.com/ckfinder/userfiles/images/jacki-o-shoots-goons.jpg',
         'name': u'Снежанна Ивановна',
         'first_name': u'Снежанна',
         'time': u'35 минут назад',
         'message': u'А можно всех посмотреть?',
         'class': u'unread',
         'counter': u'',
         'my_message': True},
        {'avatar': 'http://www.epigami.sg/images/tutor/3761/ashley-chin-tutor-epigami-L.jpg',
         'name': u'Тина Александровна',
         'first_name': u'Тина',
         'time': u'1 час назад',
         'message': u'До завтра, Тина Александровна',
         'class': u'',
         'counter': u'',
         'my_message': True},
        {'avatar': 'http://media.npr.org/programs/tmm/2007/05/serch_200-9b94d2072d0f776f126e7b86cf62cf8cdeb9c18f-s300-c85.jpg',
         'name': u'Тихон Олегович',
         'first_name': u'Тихон',
         'time': u'Вчера в 13:10',
         'message': u'Договорились. Я живу в доме, который налево сразу после трактора.',
         'class': u'',
         'counter': u'',
         'my_message': False},
        {'avatar': 'http://partycity2.scene7.com/is/image/PartyCity/_ml_p2p_pc_badge_taller15?$_ml_p2p_pc_thumb_taller15$=&$product=PartyCity/451438_full&hei=200&wid=200',
         'name': u'Black Table',
         'first_name': u'Black',
         'time': u'Вчера в 11:20',
         'message': u'До встречи бро, слушайся маму',
         'class': u'',
         'counter': u'',
         'my_message': False},
    ]

    hours = [str(i).zfill(2) + u':00' for i in range(24)][8:]

    full_hours = []
    for hour in hours:
        full_hours += [hour, hour.replace(u':00', u':30')]

    actions = [
        u'<span class="history-action-time">13 Сентября \'14, 13:00</span><span class="history-action-name">Иван Петров</span> отменил занятие',
        u'<span class="history-action-time">13 Сентября \'14, 12:14</span><span class="history-action-name">Иван Петров</span> подтвердил изменения',
        u'<span class="history-action-time">12 Сентября \'14, 11:45</span><span class="history-action-name">Александр Викторович</span> изменил время начала занятия',
        u'<span class="history-action-time">11 Сентября \'14, 11:30</span><span class="history-action-name">Иван Петров</span> подтвердил занятие',
        u'<span class="history-action-time">10 Сентября \'14, 11:00</span><span class="history-action-name">Александр Викторович</span> создал занятие',
    ]

    month = [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, '', '', '', ''],
    ]

    subs = [
        u'Русский язык',
        u'Японский язык',
        u'История	Логопед',
        u'Английский язык',
        u'Русский как иностранный',
        u'Обществознание',
        u'Изобразительное искусство',
        u'Немецкий язык',
        u'Математика',
        u'Литература',
        u'Музыка',
        u'Французский язык',
        u'Физика',
        u'География',
        u'Другой',
        u'Итальянский язык',
        u'Информатика и программирование',
        u'Экономика',
        u'Редкие иностранные языки',
        u'Испанский язык',
        u'Химия',
        u'Подготовка к школе',
        u'Спорт и фитнес',
        u'Китайский язык',
        u'Биология',
        u'Начальная школа',
    ]


    return {
        'weekdays': [u'ПН', u'ВТ', u'СР', u'ЧТ', u'ПТ', u'СБ', u'ВС'],
        'month': month,
        'full_hours': full_hours,
        'hours': hours,
        'settings': settings,
        'applications': applications,
        'subjects': ['Математика','Физика','Английский язык','Химия','Русский язык','Обществознание','Информатика','Немецкий язык','История','Французский язык'],
        'dialogs': dialogs,
        'actions': actions,
        'screen': request.session['screen'],
        'subs': subs,
        'url_name': request.resolver_match.url_name,
        # 'form_range': xrange(0, 100)
    }