from django import forms


class TeacherForm(forms.Form):
    first_name = forms.CharField(label="Teacher name")
    last_name = forms.CharField(label="Teacher surname")
    fathers_name = forms.CharField(label="Teacher fathers name")
    birth_date = forms.DateField(label="Teacher birth date", initial="yyyy-mm-dd")

    # check input
    # def clean_first_name(self):
    #     first_name = self.cleaned_data
    #     if len(first_name) > 50:
    #         raise forms.ValidationError("Max length name equals 50 words")
    #     return None
    #
    # def clean_last_name(self):
    #     last_name = self.cleaned_data
    #     if len(last_name) > 50:
    #         raise forms.ValidationError("Name is too long")
    #
    # def clean_fathers_name(self):
    #     fathers_name = self.cleaned_data
    #     if len(fathers_name) > 50:
    #         raise forms.ValidationError("Name is too long")


class GroupForm(forms.Form):
    name = forms.CharField(label="Group name", max_length=50)
    teacher_id_id = forms.IntegerField(label="Teacher's ID")

    # def clean_name(self):
    #     name = self.cleaned_data
    #     if len(name) > 50:
    #         raise forms.ValidationError("Name is too long")
    #     return None
    #
    # def clean_teacher_id_id(self):
    #     teacher_id_id = self.cleaned_data
    #     # need another validator to foreign key
    #     if len(teacher_id_id) > 50:
    #         raise forms.ValidationError("ID have to be in DB")


class SubjectForm(forms.Form):
    name = forms.CharField(label="Subject name", max_length=50)
    description = forms.CharField(label="Subject description", widget=forms.Textarea)
    score = forms.IntegerField(label="Number of score", max_value=10, min_value=1)
    teacher_id_id = forms.IntegerField(label="Teacher ID")

    # def clean_name(self):
    #     name = self.cleaned_data
    #     if len(name) > 50:
    #         raise forms.ValidationError("Name is too long")
    #     return None
    #
    # def clean_description(self):
    #     description = self.cleaned_data
    #     if len(description) > 200:
    #         raise forms.ValidationError("Name is too long")
    #     return None
    #
    # def clean_score(self):
    #     score = self.cleaned_data
    #     if len(score) > 10:
    #         raise forms.ValidationError("Score is out of range")
    #     return None
