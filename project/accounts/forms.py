from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class CustomSignupForm(SignupForm): # добавляем пользователя в группу (СТ наверно автоматически при регистрации)
    def save(self, request):
        user = super().save(request) # вызываем этот же метод класса-родителя, чтобы необходимые проверки и сохранение в модель User были выполнены
        common_users = Group.objects.get(name="common users") # получаем объект модели группы с названием common users
        user.groups.add(common_users) #  добавляем нового пользователя в эту группу
        return user # Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции.

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

class CustomSignupForm(SignupForm):  # включаем автоматическое добавление пользователя в группу "common users" при его самомстоятельной регистрации
    def save(self, request):
        user = super().save(request)  # вызываем этот же метод класса-родителя, чтобы необходимые проверки и сохранение в модель User были выполнены
        common_users = Group.objects.get(name="common users")  # получаем объект модели группы с названием common users
        user.groups.add(common_users)  # добавляем нового пользователя в эту группу
        return user  # Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции.
