from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/", views.teacher_form, name="teacher"),
    path("teachers/", views.teachers, name="teachers"),
    path("group/", views.group_form, name="group"),
    path("groups/", views.groups, name="groups"),
    path("subject/", views.subject_form, name="subject"),
    path("subjects/", views.subjects, name="subjects"),
]
