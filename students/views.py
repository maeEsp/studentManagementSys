from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForms

# Create your views here.
def home(request):

    if request.method == "POST":
        form = StudentForms(request.POST)
        if(form.is_valid()):
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]
            gender = form.cleaned_data["gender"]
            course = form.cleaned_data["course"]
            return HttpResponse(f"Thank You, {first_name} {last_name} {age} {gender} {course}")

    #GET
    context = {}
    context["form"] = StudentForms()
    return render(request, 'student_form.html', context)
