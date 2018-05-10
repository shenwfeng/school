from django.shortcuts import render
from django.http import HttpResponse
from .forms import SchoolprofileForm,SchooltermForm,ClassprofileForm,CourseForm
from .models import Schoolprofile,Course

# Create your views here.
def school_profile(request):
    if request.method == 'POST':
        schoolprofile_form = SchoolprofileForm(request.POST)
        #schoolprofile_cd = schoolprofile_form.cleaned_data()
        if schoolprofile_form.is_valid():
            new_schoolprofile = schoolprofile_form.save()
            return HttpResponse('添加学校信息成功！')
        else:
            return HttpResponse('学校信息没有成功添加！')
    else:
        schoolprofile_form =  SchoolprofileForm()
        return render(request,'base/schoolprofile.html',{'form':schoolprofile_form})


def add_shoolterm(request):
    if request.method == 'POST':
        schoolterm_form = SchooltermForm(request.POST)
        if schoolterm_form.is_valid():
            new_schoolterm = schoolterm_form.save()
            return HttpResponse('添加学期信息成功！')
        else:
            return HttpResponse('学期信息没有成功添加！')
    else:
        schoolterm_form =  SchooltermForm()
        return render(request,'base/addschoolterm.html',{'form':schoolterm_form})

def add_classprofile(request):
    if request.method == 'POST':
        classprofile_form = ClassprofileForm(request.POST)
        if classprofile_form.is_valid():
            new_classprofile = classprofile_form.save()
            return HttpResponse('添加班级信息成功！')
        else:
            return HttpResponse('班级信息没有成功添加！')
    else:
        classprofile_form = ClassprofileForm()
        return render(request,'base/addclassprofile.html',{'form':classprofile_form})


def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            new_course = course_form.save()
            return HttpResponse('课程添加成功！')
        else:
            return HttpResponse('课程添加不成功！')
    else:
        course_form = CourseForm()
        return  render(request,'base/addcourse.html',{'form':course_form})
