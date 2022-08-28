from tkinter import CASCADE
from django.db import models
from jalali_date import datetime2jalali,date2jalali
from accounts.models import ProfileModel
# Create your models here.

class ConcertModel(models.Model):

    name = models.CharField(max_length=100, verbose_name='نام کنسرت')
    singer_name = models.CharField(max_length=100, verbose_name='نام خواننده')
    lenght = models.IntegerField(verbose_name='مدت زمان')
    poster = models.ImageField(upload_to='poster_pics', null=True, verbose_name='عکس پوستر')

    class Meta:
        # verbose_name = 'کنسرت'
        verbose_name_plural= 'کنسرت ها'
    def __str__(self) -> str:
        return self.singer_name

class LocationModel(models.Model):
    id_number = models.IntegerField(primary_key=True, verbose_name='کد محل')
    name = models.CharField(max_length=100, verbose_name='نام محل')
    address = models.CharField(max_length=500, verbose_name='آدرس')
    phone = models.CharField(max_length=11,null=True, verbose_name='شماره تلفن')
    capacity = models.IntegerField(verbose_name='ظرفیت')

    class Meta:
        # verbose_name = 'کنسرت'
        verbose_name_plural= 'محل برگزاری'

    def __str__(self) -> str:
        return self.name

class TimeModel(models.Model):
    concert_model = models.ForeignKey(to=ConcertModel,on_delete=models.PROTECT, verbose_name='کنسرت')
    # concert_model = models.ForeignKey('ConcertModel',on_delete=models.PROTECT)
    location_model = models.ForeignKey(to=LocationModel, on_delete=models.PROTECT, verbose_name='محل برگزاری')
    start_date_time = models.DateTimeField(verbose_name='تاریخ و ساعت برگزاری')
    seats = models.IntegerField(verbose_name='تعداد صندلی')

    # start_s= 1
    # end_s = 2
    # cancel_s = 3
    # sales_s = 4
    status_choices = (
                    (1,'فروش بلیط شروع شده است'),
                    (2,'فروش بلیط تمام شده است!'),
                    (3,'این سانس کنسل شده است'),
                    (4,'در حال فروش بلیط'),
                    )
    status = models.IntegerField(choices=status_choices, verbose_name='وضعیت')

    class Meta:
        # verbose_name = 'کنسرت'
        verbose_name_plural= 'سانس'

    def __str__(self) -> str:
        return f'Time: {self.start_date_time} Concet Name: {self.concert_model} Location: {self.location_model}'

    def get_jalali_date(self):
        return datetime2jalali(self.start_date_time)

class TicketModel(models.Model):
    ticket_number = models.IntegerField(null=False, verbose_name='شماره بلیط')
    profile = models.ForeignKey(ProfileModel,on_delete=models.PROTECT, verbose_name='کاربر')
    ticket_pic = models.ImageField(upload_to='ticket_pics', blank=True, verbose_name='عکس بلیط')
    time = models.ForeignKey('TimeModel',on_delete=models.PROTECT, verbose_name='سانس')

    Name = models.CharField(max_length=100, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')

    class Meta:
        # verbose_name = 'کنسرت'
        verbose_name_plural= 'بلیط'

    def __str__(self) -> str:
        # return f'Ticket Information : \n Number : {ticket_number} \n Profile : {ProfileModel.__str__()} \n Concert Information: \n Singer: {ConcertModel.__str__()} \n Location : {LocationModel.__str__()} \n Time: {TimeModel.__str__()}'
        return f'Ticket Information : \n Number : {self.ticket_number} \n Profile : {ProfileModel.__str__()} \n Concert Information: \n Singer: {TimeModel.__str__()}'
        # return f'Ticket Information : \n Number : {ticket_number} \n Profile : {profile} \n Concert Information: \n Singer: {time}'
