from django import forms
from .models import Student
from django.core import  validators

class StudentRegistration(forms.ModelForm):
    class Meta :
        model=Student
        fields=['name','fatherName','age','dob','rollNumber','address','phone','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'fatherName':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'rollNumber':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'})

        }