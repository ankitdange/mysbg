from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from dashbord.models import Book
from django import forms
from django.http import HttpResponse
from .serializers import Bookserializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','childid','father','year','cast','cast_name','student_class','brother_sister','addmisstion_number',
                'school_entry_date','chatravs','divyang','occupation_parents','annual_income','current_school_name','current_year_of_exam',
                'result','aadhar_numer','ifsc_code','account_number','portel_issued_ammount','karmkar','exp_date',

                
                ]
        labels={
            "year": _("Sesstion"),
            "childid":_("Child Id"),
            "name":_("Student Name"),
            "father":_("Father Name"),
            "cast":_("Choose Catogery"),
            "cast_name":_("Cast Name"),
            "student_class":_("Student Class"),
            "brother_sister":_("Siblings"),
            "addmisstion_number":_("Addmisstion Number"),
            "school_entry_date":_("School Entery Date"),
            "chatravs":_("Hostel"),
            "divyang":_("Divyang"),
            "occupation_parents":_("Parents Work"),
            "annual_income":_("Annual Income"),
            "current_school_name":_("School Name"),
            "current_year_of_exam":_("Current Year Exam"),
            "result":_("Result"),
            "aadhar_numer":_("Aadhar"),
            "ifsc_code":_("IFSC"),
            "account_number":_("A/C"),
            "portel_issued_ammount":_("Portel Issued Amount"),
            "karmkar":_("KarmKar"),
            "exp_date":_("Expiary Date"),

            
        
        
        }
        widgets = {
                'exp_date' : forms.DateInput(attrs={'type':'date'}),
                'current_year_of_exam' : forms.DateInput(attrs={'type':'date'}),
                'school_entry_date' : forms.DateInput(attrs={'type':'date'}),
                
                }


class studentlist(APIView):
    def get(self,request):
        sut1= Book.objects.all()
        serializers=Bookserializers(sut1,many=True)
        return Response(serializers.data)
    def post(self):
        pass
     
@login_required
def book_list(request, template_name='books_fbv/book_list.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

@login_required
def book_create(request, template_name='books_fbv/book_form.html'):
    form = BookForm(request.POST or None)
    stucnt = Book.objects.count()
    if form.is_valid():
        form.save()
        return redirect('books_fbv:book_list')
       
    
    return render(request, template_name, {'form':form,'stucnt':stucnt})
@login_required
def book_update(request, pk, template_name='books_fbv/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    stucnt = Book.objects.count()
    if form.is_valid():
        form.save()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'form':form ,'stucnt':stucnt})

@login_required
def book_delete(request, pk, template_name='books_fbv/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'object':book})   
