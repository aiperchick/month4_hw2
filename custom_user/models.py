from django.db import models
from django.contrib.auth.models import User
ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, 'VIPClient'),
    (CLIENT, 'CLIENT')
)

MALE = 1
FEMALE = 2
OTHERS = 3

GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHERS, 'OTHERS')

)

INTJ = 1
INTP = 2
ENTJ = 3
ENTP = 4
INFJ = 5
INFP = 6
ENFJ = 7
ENFP = 8
ISTJ = 9
ISFJ = 10
ESTJ = 11
ESFJ = 12
ISTP = 13
ISFP = 14
ESTP = 15
ESFP = 16

MBTI_TYPE = (
    (INTJ, 'INTJ'),
    (INTP, 'INTP'),
    (ENTJ, 'ENTJ'),
    (ENTP, 'ENTP'),
    (INFJ, 'INFJ'),
    (INFP, 'INFP'),
    (ENFJ, 'ENFJ'),
    (ENFP, 'ENFP'),
    (ISTJ, 'ISTJ'),
    (ISFJ, 'ISFJ'),
    (ESTJ, 'ESTJ'),
    (ESFJ, 'ESFJ'),
    (ISTP, 'ISTP'),
    (ISTP, 'ISTP'),
    (ESTP, 'ESTP'),
    (ESFP, 'ESFP'),

)

YES = 1
NO = 2

ICE_CREAM_TYPE = (
    (YES, 'YES'),
    (NO, 'NO'),
)

PEPSI = 1
COLA = 2

DRINK_TYPE = (
    (PEPSI, 'PEPSI'),
    (COLA, 'COLA'),
)

BEKEND = 1
FRONTEND = 2
IOS = 3
ANDROID = 4

RAZRAB_TYPE = (
    (BEKEND, 'BEKEND'),
    (FRONTEND, 'FRONTEND'),
    (IOS, 'IOS'),
    (ANDROID, 'ANDROID')
)


class CustomUser(User):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField('номер телефона', max_length=16)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='пол')
    mbti_test = models.IntegerField(choices=MBTI_TYPE, verbose_name='ваш тип личности', null=True)
    ice_cream = models.IntegerField(choices=ICE_CREAM_TYPE, verbose_name='вы любите мороженое?', null=True)
    color = models.CharField('ваш любимый цвет', max_length=30, null=True)
    lunch = models.CharField('что вы кушали сегодня на обед?', max_length=100, null=True)
    pepsi_or_cola = models.IntegerField(choices=DRINK_TYPE, verbose_name='выбирайте', null=True)
    developer = models.IntegerField(choices=RAZRAB_TYPE, verbose_name='какой ты разработчик?', null=True)
