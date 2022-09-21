from random import random
from django.db import models
from random import randrange

# Create your models here.
# manager_id, man_name, number, -> manager model

# stu_name, id, number, course -> student model

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Manager(Base):
    manager_name = models.CharField(max_length=50)
    manager_phone = models.CharField(max_length=12)

    def __str__(self):
        return self.manager_name

# choices = (("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5"),("6", "6"),("7", "7"),("8", "8"))

class Student(Base):

    def rand_manager():
        n = Manager.objects.count()
        return Manager.objects.all()[randrange(n)]

    course_choice = (("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5"),("6", "6"))
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT, default=rand_manager)
    student_name = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=12)
    student_course = models.CharField(max_length=1,choices=course_choice)

    
    # def save(self,*args, **kwargs):
    #     # random.randint(a,b)
    #     managers = Manager.objects.all()
    #     for manager in managers:
    #         rand_num = random.randrange(1,len(managers)+1)

        # super(Student,self).save(self,*args, **kwargs)

    def __str__(self):
        return self.student_name

    
