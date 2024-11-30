
from django.urls import path, include
from .views import  templates_list

app_name ='accounts'
urlpatterns = [
  path("template/", templates_list, name="login"),
]
