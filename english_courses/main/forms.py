from .models import Application, Student, StudentGroup, Lesson, Announcement, Observation, CustomUser
from django.forms import ModelForm, TextInput, NumberInput, Textarea


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
