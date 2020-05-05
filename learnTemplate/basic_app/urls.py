from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basic_app import views


app_name="basic_app";
urlpatterns = [
    url(r"^relative/$",views.relative,name="RELative"),
    url(r"^other/$",views.otherpage,name="otherpage")
]
