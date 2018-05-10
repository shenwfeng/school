from django.conf.urls import url,include
from . import views


app_name='base'

urlpatterns = [
    url(r'^schoolprofile/$',views.school_profile,name='schoolprofie'),
    url(r'^addschoolterm/$',views.add_shoolterm,name='addschoolterm'),
    url(r'^addclassprofile/$',views.add_classprofile,name='addclassprofile'),
    url(r'^addcourse/$',views.add_course,name='addcourse'),
]