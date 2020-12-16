from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authapp.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'

        self.fields['password'].widget.attrs['class'] = 'form-control py-4'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'



class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'

        self.fields['email'].widget.attrs['class'] = 'form-control py-4'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите электронную почту'

        self.fields['first_name'].widget.attrs['class'] = 'form-control py-4'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите Ваше имя'

        self.fields['last_name'].widget.attrs['class'] = 'form-control py-4'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите Вашу фамилию'

        self.fields['password1'].widget.attrs['class'] = 'form-control py-4'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password1'].widget.help_text = 'от 8 знаков, должны быть строчные и заглавные буквы и цифры'

        self.fields['password2'].widget.attrs['class'] = 'form-control py-4'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
