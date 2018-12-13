from django.db import models
from django.urls import reverse


class Book(models.Model):
    year_choice = (
        ('2017-18', '2017-18'),
        ('2018-19', '2018-19'),
        ('2019-20', '2019-20'),
        ('2020-21', '2020-21'),
        ('2021-22', '2021-22'),
        ('2022-23', '2022-23'),
        ('2023-24', '2023-24'),
        ('2024-25', '2024-25'),
    )
    year = models.CharField(max_length=10, choices=year_choice)
    name = models.CharField(max_length=200)
    childid = models.CharField(max_length=9)
    father = models.CharField( max_length=50)
    cast_choice = (
        ('st', 'ST'),
        ('sc', 'SC'),
        ('obc', 'OBC'),
        ('gn', 'GN'),
    )
    cast = models.CharField(max_length=4, choices=cast_choice)
    cast_name = models.CharField(max_length=50)
    student_class = models.IntegerField()
    brother_sister = models.CharField(max_length=50)
    addmisstion_number = models.IntegerField()
    school_entry_date = models.DateField(auto_now=False, auto_now_add=False)

    chatravs_choice = (
        ('Yes', 'yes'),
        ('NO', 'no'),
       
    )
    chatravs = models.CharField(max_length=5, choices=chatravs_choice)
    divyang_choice = (
        ('Yes', 'yes'),
        ('NO', 'no'),
       
    )
    divyang = models.CharField(max_length=5, choices=divyang_choice)
    occupation_parents = models.CharField( max_length=50)
    annual_income = models.IntegerField()
    current_year_of_exam = models.DateField(auto_now=False, auto_now_add=False)
    current_school_name = models.CharField(max_length=50)
    result = models.DecimalField(max_digits=5, decimal_places=2)
    aadhar_numer = models.CharField(max_length=12)
    ifsc_code = models.CharField( max_length=50)
    account_number = models.IntegerField()
    portel_issued_ammount = models.IntegerField()
    karmkar = models.CharField(max_length=50)
    exp_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashbord:book_edit', kwargs={'pk': self.pk})