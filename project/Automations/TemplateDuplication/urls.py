
from . import views
from django.urls import path

urlpatterns = [
    # path('', views.home,name='home'),
    path('',views.home,name="home"),
    path('TemplateDuplication',views.TemplateDuplication,name="TemplateDuplication"),
    path('TemplateDuplication1',views.TemplateDuplication1,name="TemplateDuplication1")
]