from django.urls import path
from api.v1.applier import views

urlpatterns=[
    path("register/",views.register),
    path("login/",views.login),
    path("job/",views.jobs),
    path("add_jobs/",views.add_job),
    path("edit_jobs/<int:id>/",views.edit_job),
    path("delete_jobs/<int:id>/",views.delete_job),
    path("apply/",views.apply),
    path("add_apply/",views.add_apply),
    path("edit_apply/<int:id>/",views.edit_apply),
    path("delete_apply/<int:id>/",views.delete_apply),


]