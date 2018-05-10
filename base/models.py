from django.db import models

def getcourse(request):
    courses = Course.objects.all()
    return course


class Schoolprofile(models.Model):
    schoolname = models.CharField(max_length=100,unique=True)
    schoolinfo =  models.TextField()
    def __str__(self):
        return self.schoolname

class SchoolTerm(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('11-12','2011-12学年度'),
        ('12-13','2012-13学年度'),
        ('13-14','2013-14学年度'),
        ('14-15','2014-15学年度'),
        ('15-16','2015-16学年度'),
        ('16-17','2016-17学年度'),
        ('17-18','2017-18学年度'),
        ('18-19','2018-19学年度'),
        ('19-20','2019-20学年度'),
        ('20-21','2020-21学年度'),
        ('21-22','2021-22学年度'),
        ('22-23','2022-23学年度'),
        ('23-24','2023-24学年度'),
    )
    TERM_CHOICE = (
        ('1','上学期'),
        ('2','下学期'),
    )
    schoolyearname = models.CharField(max_length=8,choices=YEAR_IN_SCHOOL_CHOICES,null=False,blank=False,verbose_name='学年')
    is_in_year = models.BooleanField(default=False,verbose_name='是否当前学期')
    term = models.CharField(max_length=1,choices=TERM_CHOICE,default= '1',verbose_name='学期')
    starttime = models.DateField(blank=True,verbose_name='开学时间',null=True)
    endtime = models.DateField(blank=True,verbose_name='结束时间',null=True)

    class Meta:
        unique_together = ('term','schoolyearname')

    def __str__(self):
        term = '%s%s'%(self.get_schoolyearname_display(),self.get_term_display())
        return term

class ClassProfile(models.Model):
    CLASS_CHOICE = (
        ('高一',
            (
                ('11','高一1'),
                ('12','高一2'),
                ('13','高一3'),
                ('14','高一4'),
                ('15','高一5'),
                ('16','高一6'),
                ('17','高一7'),
                ('18','高一8'),
                ('19','高一9'),
            )


        ),
        ('高二',(
             ('21', '高二1'),
             ('22', '高二2'),
             ('23', '高二3'),
             ('24', '高二4'),
             ('25', '高二5'),
             ('26', '高二6'),
             ('27', '高二7'),
             ('28', '高二8'),
             ('29', '高二9'),
             )
         ),
        ('高三', (
            ('31', '高三1'),
            ('32', '高三2'),
            ('33', '高三3'),
            ('34', '高三4'),
            ('35', '高三5'),
            ('36', '高三6'),
            ('37', '高三7'),
            ('38', '高三8'),
            ('39', '高三9'),
        )
         ),
    )

    CLASSTYPE_CHOICE = (
        ('00','普通班'),
        ('12','物化班'),
        ('13','物生班'),
        ('16','物地班'),
        ('15','物政班'),
        ('45','史政班'),
        ('56','史地班'),
        ('09','艺术班'),
        ('99','综合高中班'),
        ('11','其他'),
    )

    classname = models.CharField(max_length=3,choices=CLASS_CHOICE)
    schoolterm = models.ForeignKey(SchoolTerm,on_delete=False)
    classtype = models.CharField(max_length=2,choices=CLASSTYPE_CHOICE)
    remark = models.CharField(max_length=100,blank=True)

    def __str__(self):
        name = '%s'%(self.get_classname_display())
        return name

class Course(models.Model):
    coursename = models.CharField(max_length=20,blank=False,null=False,unique=True)

    def __str__(self):
        return self.coursename

# def getcourse():
#     course = Course.objects.all()
#     return course


class ExamType(models.Model):
    EXAMTYPE_CHOICE = (
        ('周练','周练'),
        ('作业','作业'),
        ('练习', '练习'),
        ('校统考', '校统考'),
        ('市统考', '市统考'),
    )
    examtypename = models.CharField(max_length=30,choices=EXAMTYPE_CHOICE,unique=True)

    def __str__(self):
        return self.examtypename


