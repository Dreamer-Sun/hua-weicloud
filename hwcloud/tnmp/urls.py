from django.contrib import admin
from django.urls import path
from . import views
from tnmp.api import get_api
from tnmp.manage import querysites
app_name = 'tnmp'

urlpatterns = [
    # path('', views.search, name='search'),
    # path('handle/', views.handle, name='handle'),

    path('show_token/', get_api.show_token),

    path('getSiteData/', querysites.getSiteData),
    path('getsitemap/', querysites.getsitesmap),
    path('getsitetypedata/', querysites.querysitesdata),
    path('queryresultbyquerysitesdata/', querysites.queryresultbyquerysitesdata),
    # path('user/getinfo', login.getinfo),

]
