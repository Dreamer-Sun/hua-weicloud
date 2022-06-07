from django.contrib import admin
from django.urls import path
from . import views
from tnmp.api import get_api
app_name = 'tnmp'

urlpatterns = [
    # path('', views.search, name='search'),
    # path('handle/', views.handle, name='handle'),

    path('show_token/', get_api.show_token),
    # path('user/getinfo', login.getinfo),

]
