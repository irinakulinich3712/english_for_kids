from .models import Application, Student, StudentGroup, Lesson, Announcement, Observation, CustomUser
from django.forms import ModelForm, TextInput, NumberInput


class CreateGroupForm(ModelForm):
    class Meta:
        model = StudentGroup
        fields = ["year", "name"]

        widgets = {
            "year": NumberInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the year of studies"
            }),
            "name": TextInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the group name"
            }),
        }


class EditGroupForm(ModelForm):
    class Meta:
        model = StudentGroup
        fields = ["year", "name"]
        widgets = {
            "year": NumberInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the year of studies"
            }),
            "name": TextInput(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the group name"
            }),
        }