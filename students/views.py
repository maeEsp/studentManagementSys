from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForms, FilterStudents, UpdateStudentForms
from .models import Student

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
    students = Student.objects.all()  # Renaming the queryset variable
    filter_form = FilterStudents()  # Creating an instance of the form
    context = {'students': students, 'filter_form': filter_form}  # Adding both to the context
    return render(request, 'student_table.html', context)


def delete(request, id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return redirect("/")

def update(request, id):
    stud = Student.objects.get(id=id)
    return render(request, 'update.html', {'stud': stud})
    # if request.method == "POST":
    #     form = UpdateStudentForms(request.POST)
    #     if(form.is_valid()):

    #         student = Student(
    #             first_name = form.cleaned_data["first_name"],
    #             last_name = form.cleaned_data["last_name"],
    #             course = form.cleaned_data["course"],
    #             gender = form.cleaned_data["gender"],
    #             age = form.cleaned_data["age"]
    #         )

    #         student.save()
    #         return redirect("/")
    # context = {}
    # context["form"] = StudentForms()
    # return render(request, 'update.html', context)

def uprec(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    course = request.POST['course']
    gender = request.POST['gender']
    age = request.POST['age']

    stud = Student.objects.get(id=id)
    stud.first_name = first_name
    stud.last_name = last_name
    stud.course = course
    stud.gender = gender
    stud.age = age

    stud.save()
    return redirect('/')