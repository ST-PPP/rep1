from django import forms
from django.contrib.auth.forms import UserCreationForm
from simpleapp.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

class CustomSignupForm(SignupForm): # добавляем пользователя в группу (СТ наверно автоматически при регистрации) # включаем автоматическое добавление пользователя в группу "common users" при его самомстоятельной регистрации
    email_2 = forms.EmailField(label='Адрес электронной почты 2') # СТ для вывода второго поля для второго имеила

    def save(self, request):
        user = super().save(request) # вызываем этот же метод класса-родителя, чтобы необходимые проверки и сохранение в модель User были выполнены
        common_users = Group.objects.get(name="common users") # получаем объект модели группы с названием common users
        user.groups.add(common_users) #  добавляем нового пользователя в эту группу
        user.email_2 = request.POST.get('email_2') # СТ сохраняем второй имеил пользователя СТ выводим второе поле для второго имеила СТ то есть обновляем данные юзера в БД, так как первой строчкой в текущей функции (user = super().save(request)) он уже сохранён
        user.save() # СТ сохраняем второй имеил пользователя

        send_mail( # СТ Автоматическое отиправление письма новому пользователю на указанную им при регистрации @
            subject='Добро пожаловать в наш интернет-магазин!', # СТ тема письма
            message=f'{user.username}, вы успешно зарегистрировались!', # СТ текст письма
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email, user.email_2], # СТ список имеилов для рассылки. Там должен быть только тот который укажет новый пользователь. Термин список наверно намекает на то, что указать можно больше одного имеила.
        )

        return user # Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции.

    def clean_email_2(self): # СТ при регистрации нового пользователя проверяем второй его имеил на уникальность
        email = self.cleaned_data.get('email_2') # СТ введёный имеил проверяем на правильность написания
        user = User.objects.filter(email_2=email).exist() # СТ ищем такой же имеил в БД
        if user: # СТ если нашли то:
            raise forms.ValidationError('Пользователь с таким email_2 уже существует') # СТ выводим ошибку
        return email

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
         )

