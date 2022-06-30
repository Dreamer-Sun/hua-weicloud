from django.contrib import admin
from django.urls import path
from . import views
from tnmp.api import get_api
from tnmp.manage import querysites, equipment_alarm
from tnmp.manage import create_site
from tnmp.manage import devicemanagement

from tnmp.manage import create_site, deleteSite, update_site, traffic_statistic

app_name = 'tnmp'

urlpatterns = [
    # path('', views.search, name='search'),
    # path('handle/', views.handle, name='handle'),

    path('show_token/', get_api.show_token),

    path('getdeviceinfo/', devicemanagement.getdeviceinfo),
    path('createdevice/', devicemanagement.createdevice),
    path('deletedevice/', devicemanagement.delete_device),
    path('changedevice/', devicemanagement.change_device),

    path('getSiteData/', querysites.getSiteData),

    path('getsitemap/', querysites.getsitesmap),
    path('getsitetypedata/', querysites.querysitesdata),
    path('queryresultbyquerysitesdata/', querysites.queryresultbyquerysitesdata),

    path('getEquipmentAlarm/', equipment_alarm.getEquipmentAlarm),
    path('getSiteId/', equipment_alarm.getSiteId),
    path('create_site/', create_site.createsite),
    path('delete_site/', deleteSite.deleteSite),
    path('update_site/', update_site.updateSite),

    path('traffic_statistic/', traffic_statistic.trafficStatistic),
    path('queryTag/', traffic_statistic.queryTag)

    # path('user/getinfo', login.getinfo),

]
