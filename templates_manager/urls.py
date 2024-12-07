
from django.urls import path, include
from .views import  templates_list,about_view

app_name ='accounts'
urlpatterns = [
  path("template/", templates_list, name="login"),
  # path('about/', about_view, name='about'),


]
# app_name = 'static'

# urlpatterns = [
#       path('about/', about_view, name='about'),

# ]