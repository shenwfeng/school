from django import forms
from .models import SchoolTerm,Schoolprofile,ClassProfile,Course

class SchoolprofileForm(forms.ModelForm):
    class Meta:
        model = Schoolprofile
        fields = ('schoolname','schoolinfo')

class SchooltermForm(forms.ModelForm):
    class Meta:
        model = SchoolTerm
        fields = ('schoolyearname','is_in_year','term','starttime','endtime')



class ClassprofileForm(forms.ModelForm):
    class Meta:
        model = ClassProfile
        fields = ('classname','schoolterm','classtype','remark')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('coursename',)