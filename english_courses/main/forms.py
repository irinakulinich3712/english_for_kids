from django.core.exceptions import ValidationError

from .models import Application, Student, StudentGroup, Lesson, Announcement, Observation, CustomUser
from django.forms import ModelForm, TextInput, NumberInput, Textarea, EmailInput


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


class CreateLessonForm(ModelForm):
    class Meta:
        model = Lesson
        exclude = ("created_at", "student_group")
        fields = ["task"]
        widgets = {
            "task": Textarea(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the task"
            }),
        }


class EditLessonForm(ModelForm):
    class Meta:
        model = Lesson
        exclude = ("created_at", "group")
        fields = ["task"]
        widgets = {
            "task": Textarea(attrs={
                'id': 'edit-lesson-task',
                'class': 'modal-form__input',
                'placeholder': "Enter the task"
            }),
        }


class CreateObservationForm(ModelForm):
    class Meta:
        model = Observation
        exclude = ("created_at", "student")
        fields = ["observation"]
        widgets = {
            "observation": Textarea(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter an observation"
            }),
        }


class EditObservationForm(ModelForm):
    class Meta:
        model = Observation
        exclude = ("created_at", "student")
        fields = ["observation"]
        widgets = {
            "observation": Textarea(attrs={
                'id': 'edit-observation',
                'class': 'modal-form__input',
                'placeholder': "Enter an observation"
            }),

        }


class CreateAnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        exclude = ("created_at",)
        fields = ["announcement"]
        widgets = {
            "announcement": Textarea(attrs={
                'class': 'modal-form__input',
                'placeholder': "Enter the announcement"
            }),
        }


class EditAnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        exclude = ("created_at",)
        fields = ["announcement"]
        widgets = {
            "announcement": Textarea(attrs={
                'id': 'edit-announcement',
                'class': 'modal-form__input',
                'placeholder': "Enter the announcement"
            }),
        }


class CreateApplicationForm(ModelForm):

    def clean_f_name(self):
        f_name = self.cleaned_data["f_name"]

        if not f_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return f_name

    def clean_l_name(self):
        l_name = self.cleaned_data["l_name"]

        if not l_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return l_name

    def clean_parent_tel_numb(self):
        parent_tel_numb = self.cleaned_data["parent_tel_numb"]

        if not parent_tel_numb.isdecimal():
            raise ValidationError("Telephone number should only contain digits")
        return parent_tel_numb

    def clean_parent_f_name(self):
        parent_f_name = self.cleaned_data["parent_f_name"]

        if not parent_f_name.isalpha():
            raise ValidationError("The first name should only contain letters")
        return parent_f_name

    def clean_parent_patronimic(self):
        parent_patronimic = self.cleaned_data["parent_patronimic"]

        if not parent_patronimic.isalpha():
            raise ValidationError("The patronimic should only contain letters")
        return parent_patronimic

    def clean_parent_l_name(self):
        parent_l_name = self.cleaned_data["parent_l_name"]

        if not parent_l_name.isalpha():
            raise ValidationError("The last name should only contain letters")
        return parent_l_name

    class Meta:

        model = Application
        exclude = ('created_at',)
        fields = ["f_name", "l_name", "age", "parent_tel_numb", "parent_email", "parent_f_name",
                  "parent_patronimic", "parent_l_name"]

        widgets = {
            "f_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the child's first name",
                'label': "Child's first name"
            }),

            "l_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the child's last name",
                'label': "Child's last name"
            }),

            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the child's age",
                'label': "Child's age"
            }),


            "parent_tel_numb": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the parent's telephone number",
                'label': "Parent's telephone number",
                'minlength': 10
            }),

            "parent_email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the parent's email",
                'label': "Parent's e-mail"
            }),

            "parent_f_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the parent's first name",
                'label': "Parent's first name"
            }),

            "parent_patronimic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the parent's patronimic",
                'label': "Parent's patronimic"
            }),

            "parent_l_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the parent's last name",
                'label': "Parent's last name"
            }),
        }
