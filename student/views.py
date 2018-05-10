from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Student,Score
from base.models import ClassProfile
from .forms import StudentForm
import xlrd

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        #schoolprofile_cd = schoolprofile_form.cleaned_data()
        if student_form.is_valid():
            new_studeent = student_form.save()
            return HttpResponse('添加学生信息成功！')
        else:
            return HttpResponse('学生信息没有成功添加！')
    else:
        student_form = StudentForm()
        return render(request,'student/student.html',{'form':student_form})

def upload(request):
    if request.method == 'POST':
        f = request.FILES.get('uploadfile')
        basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filedir = os.path.join(basedir,'upload')
        filename = os.path.join(filedir,f.name)
        # 上传文件部分主要代码
        fobj = open(filename,'wb')
        for chunk in f.chunks():
            fobj.write(chunk)
        fobj.close()
        return HttpResponse('文件上传成功！！！')
    else:
        return render(request,'student/upload.html')




# 遇到了一个大坑，没有考虑数据可能为空的情况，在实际情况中可以考虑先行预处理数据，提出改进数据，以便符合数据的要求
def upxls(request):
    if request.method == 'POST':
        f = request.FILES.get('uploadfile')
        wb = xlrd.open_workbook(
            filename=None,file_contents = f.read()
        )
        table = wb.sheets()[0]
        row = table.nrows
        for col in range(1,row):
            data = table.row_values(col)
            name = data[0]
            now_in_class = data[1]
            # studentdic = {'name':name,'now_in_class':now_in_class}
            # student = Student(**studentdic)
            classname = ClassProfile.objects.get(id = now_in_class)
            student =Student()
            student.name = name
            student.now_in_class = classname
            student.save()
        return HttpResponse("成功导入数据")
    else:
        return render(request, 'student/upload.html')

def upscore(request):
    if request.method == 'POST':
        f = request.FILES.get('uploadfile')
        wb = xlrd.open_workbook(
            filename=None,file_contents = f.read()
        )
        table = wb.sheets()[0]
        rows = table.nrows
        for row in range(1,rows):
            columns = table.row_values(row)
            name = columns[0]
            classid = columns[1]
            chinese = float(columns[2])
            math = float(columns[3])
            english = float(columns[4])
            sum = chinese+math+english
            classname = ClassProfile.objects.get(id=classid)
            score = Score()
            score.name =name
            score.classname = classname
            score.chinese = chinese
            score.math = math
            score.english = english
            score.sum = sum
            score.save()
        return HttpResponse('数据导入成功')
    else:
        return render(request, 'student/upload.html')