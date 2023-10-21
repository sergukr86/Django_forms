from django import forms

from .models import Teacher, Subject


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "fathers_name", "birth_date"]


class GroupForm(forms.Form):
    name = forms.CharField(label="Group name", max_length=50)
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description", "score", "teacher"]
