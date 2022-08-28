from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProfileModel(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='نام')
    family = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, verbose_name='عکس نمایه')

    # male = 1
    # female = 2
    # gender_choices = (
    #     ('male','مرد'),
    #     ('female','زن')
    # )
    gender_choices = (
        (1,'مرد'),
        (2,'زن')
    )
    gender = models.IntegerField(choices= gender_choices, verbose_name='جنسیت')

    credit = models.IntegerField(verbose_name='اعتبار', default=0)

    class Meta:
        # verbose_name = 'کنسرت'
        verbose_name_plural= 'کاربر'

    def __str__(self) -> str:
        return f'Full Name : {self.name} {self.family}'