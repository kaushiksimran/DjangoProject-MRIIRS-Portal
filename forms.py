from dataclasses import fields
from django import forms
from .models import Employee

# creating a form
class EmployeeForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Employee
        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "img",
        ]


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["email",]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name",
                "last_name",
                "email",
                "phone",]