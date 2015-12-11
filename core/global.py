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

    hours = [unicode(i).zfill(2) + u':00' for i in range(24)][8:]

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

    string = """Apple ! 724,773.1
Exxon Mobil ! 356,548.7
Berkshire Hathaway ! 356,510.7
Google ! 345,849.2
Microsoft ! 333,524.8
PetroChina ! 329,715.1
Wells Fargo ! 279,919.7
Johnson &amp; Johnson ! 279,723.9
Industrial &amp; Commercial Bank of China ! 275,389.1
Novartis ! 267,897
China Mobile ! 267,252.3
Wal-Mart Stores ! 265,107.3
General Electric ! 249,774.4
Nestle ! 243,701.8
Toyota Motor ! 238,924.8
Roche ! 237,747.6
JP Morgan Chase ! 225,861.1
Procter &amp; Gamble ! 221,279.6
Samsung Electronics ! 214,039.7
Pfizer ! 213,621.9
China Construction Bank ! 209,139.8
Verizon Communications ! 198,035.3
Chevron ! 197,381.3
Bank of China ! 197,225.6
Anheuser-Busch InBev ! 196,554.3
Royal Dutch Shell ! 192,134.9
Agricultural Bank of China ! 189,297.4
Oracle ! 188,438.8
Facebook ! 183,860.1
Walt Disney ! 178,267.1
Tencent ! 177,960.6
Coca-Cola ! 177,142.3
Amazon.com ! 172,797.3
AT&amp;T ! 169,458.8
HSBC ! 164,249.6
Merck ! 163,139.3
Bank of America ! 161,908.8
IBM ! 158,642
China Life Insurance ! 157,029.7
Citigroup ! 156,359.8
Home Depot ! 148,533.1
Intel ! 148,094.7
Gilead Sciences ! 145,532.9
Comcast ! 142,798.5
PepsiCo ! 141,742.7
Cisco Systems ! 140,507.8
Sanofi ! 130,260
Visa ! 128,455.3
Volkswagen ! 124,335.3
Bayer ! 124,157.7
BHP Billiton ! 122,335.4
Amgen ! 121,303.9
Taiwan Semiconductor Manufacturing ! 120,577.1
Actavis ! 120,536.1
Sinopec ! 119,104.8
Unilever ! 118,902.5
Total ! 118,541.9
BP ! 118,345.6
CVS Caremark ! 117,170.8
Philip Morris International ! 116,693.1
Commonwealth Bank of Australia ! 115,688.2
Qualcomm ! 114,380.5
Ping An Insurance ! 113,119
Novo Nordisk ! 112,977.6
UnitedHealth Group ! 112,812.6
GlaxoSmithKline ! 111,649.6
Medtronic ! 111,140.9
Bristol Myers Squibb ! 107,500.1
Schlumberger ! 106,628.4
United Technologies ! 106,470.3
Banco Santander ! 105,960.3
Boeing ! 105,032.2
3M ! 104,795.4
Daimler ! 103,741
L'Oreal ! 103,279.4
Inditex ! 100,013.2
Biogen Idec ! 99,063.5
Altria Group ! 98,505.2
British American Tobacco ! 96,536.7
Mastercard ! 96,001.8
Union Pacific ! 95,451.8
Westpac Banking ! 93,870.4
McDonald's ! 93,651.4
Abbvie ! 93,204.1
Walgreen ! 92,298.9
Celgene ! 92,292
Basf ! 91,489.5
Ambev ! 90,732.6
Kinder Morgan ! 90,622.5
Siemens ! 90,196.5
LVMH ! 89,497.4
SAP ! 88,793.3
Mitsubishi UFJ Financial ! 87,866.4
Royal Bank Canada ! 86,842.8
AstraZeneca ! 86,763.1
Vodafone Group ! 86,760.2
SabMiller ! 84,939.6
Deutsche Telekom ! 83,314
Lloyds Banking Group ! 82,941
Goldman Sachs ! 81,883.6"""
    for i in string.splitlines():
        print i.replace(' ! ',' - ')


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
        'form_range': xrange(0, 100)
    }