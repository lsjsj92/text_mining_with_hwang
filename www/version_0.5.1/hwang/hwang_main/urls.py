from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'hwangMain'

urlpatterns = [
    url(r'^home/$', views.HwangMain.as_view(), name='home'),
    url(r'^main/$', views.HwangMain.as_view(), name='main'),
    url(r'^input_value/$', views.HwangMain.as_view(), name='input_value'),
    url(r'^$', views.HwangMain.as_view(), name='index'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)