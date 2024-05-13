from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForms, FilterStudents
from .models import Student
from django.db.models import Q
from django.db.models import Value, CharField
from django.db.models.functions import Concat

# Create your views here.
def home(request):

    if request.method == "POST":
        form = StudentForms(request.POST)
        if(form.is_valid()):

            student = Student(
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                course = form.cleaned_data["course"],
                gender = form.cleaned_data["gender"],
                age = form.cleaned_data["age"]
            )

            student.save()
            return redirect("/")

    #GET
    context = {}
    context["form"] = StudentForms()
    return render(request, 'student_form.html', context)


def filter_table(request):
    students = Student.objects.all() 
    filter_form = FilterStudents() 
    context = {}

    
    if request.method == "POST":
        filter_form = FilterStudents(request.POST) 
        if(filter_form.is_valid()):
            name = filter_form.cleaned_data.get('full_name')
            course = filter_form.cleaned_data.get('course')
            gender = filter_form.cleaned_data.get('gender')
            age_start = filter_form.cleaned_data.get('age_start')
            age_end = filter_form.cleaned_data.get('age_end')

            filters = Q()
            if name:
                filters &= Q(first_name__icontains=name) |  Q(last_name__icontains=name)  | Q(full_name__icontains=name)
            if course:
                filters &= Q(course=course)
            if gender:
                filters &= Q(gender=gender)
            if age_start and age_end:
                filters &= Q(age__range=(age_start, age_end))
                 
            students  = students.annotate(full_name=Concat('first_name',Value(' ') ,'last_name',output_field=CharField())).filter(filters)
            # return render(request, 'student_list.html', {'students': students})
    context = {'students': students, 'filter_form': filter_form}  
    return render(request, 'student_table.html', context)


def delete(request, id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return redirect("/")


def update(request, id):
    context = {}
    stud = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid():
            stud.first_name = form.cleaned_data["first_name"]
            stud.last_name = form.cleaned_data["last_name"]
            stud.course = form.cleaned_data["course"]
            stud.gender = form.cleaned_data["gender"]
            stud.age = form.cleaned_data["age"]
            stud.save()
            return redirect("/")
    else:
        form = StudentForms(initial={
            'first_name': stud.first_name,
            'last_name': stud.last_name,
            'course': stud.course,
            'gender': stud.gender,
            'age': stud.age
        })
    context["form"] = form
    return render(request, 'student_form.html', context)
    