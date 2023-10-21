from django.shortcuts import render, redirect

from .forms import TeacherForm, GroupForm, SubjectForm

from .models import Teacher, Group, Subject


def index(request):
    return render(request, "index.html")


def teacher_form(request):
    if request.method != "POST":
        # if not POST we create a blank form
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})

    form = TeacherForm(request.POST)
    if form.is_valid():
        Teacher.objects.create(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            fathers_name=form.cleaned_data["fathers_name"],
            birth_date=form.cleaned_data["birth_date"],
        )
        return redirect("teachers")

    return render(request, "teacher_form.html", {"form": form})


def teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": all_teachers})


def group_form(request):
    if request.method != "POST":
        # if not POST we create a blank form
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST)
    if form.is_valid():
        Group.objects.create(
            name=form.cleaned_data["name"],
            teacher=form.cleaned_data["teacher"],
        )
        return redirect("groups")

    return render(request, "group_form.html", {"form": form})


def groups(request):
    all_groups = Group.objects.all()
    return render(request, "groups.html", {"groups": all_groups})


def subject_form(request):
    if request.method != "POST":
        # if not POST we create a blank form
        form = SubjectForm()
        return render(request, "subject_form.html", {"form": form})

    form = SubjectForm(request.POST)
    if form.is_valid():
        Subject.objects.create(
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            score=form.cleaned_data["score"],
            teacher=form.cleaned_data["teacher"],
        )
        return redirect("subjects")

    return render(request, "subject_form.html", {"form": form})


def subjects(request):
    all_subjects = Subject.objects.all()
    return render(request, "subjects.html", {"subjects": all_subjects})
