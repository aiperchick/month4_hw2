from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    user_type = forms.ChoiceField(required=True, choices=USER_TYPE)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    mbti_test = forms.ChoiceField(choices=MBTI_TYPE, required=True)
    ice_cream = forms.ChoiceField(choices=ICE_CREAM_TYPE, required=True)
    color = forms.CharField(required=True)
    lunch = forms.CharField(required=True)
    pepsi_or_cola = forms.ChoiceField(choices=DRINK_TYPE, required=True)
    developer = forms.ChoiceField(choices=RAZRAB_TYPE, required=True)

    class Meta:
        models = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'mbti_test',
            'ice_cream',
            'color',
            'lunch',
            'pepsi_or_cola',
            'developer',

        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
