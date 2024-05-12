from django import forms

COURSES = (
    ("BS-CS","Computer Science"),
    ("BS-IT","Information Technology"),
    ("BS-DS","Data Science"),
    ("BS-IS","Information Systems"),
)

GENDER = (
    ("F", "Female"),
    ("M", "Male")
)

class StudentForms(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True, min_value=1)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, required=True)
    course = forms.ChoiceField(choices=COURSES, widget=forms.Select, required=True)
