from django.conf.urls import url,include
from . import views

app_name = 'student'

urlpatterns = [
    url(r'^addstudent/$',views.add_student,name='addstudent'),
    url(r'^uploadfile/$',views.upload,name='uploadfile'),
    url(r'^upxls/$',views.upxls,name='upxls'),
    url(r'^upscore/$',views.upscore,name='upscore'),


]