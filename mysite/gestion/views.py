from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Student, Profesor, Secretario
from .forms import StudentForm, GradeForm

# Create your views here.
def index(request):
	return render(request, 'index.html', {'message': 'Hello, world!'})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:student_list')
    else:
        form = StudentForm()
    return render(request, 'templates/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'templates/student_form.html', {'form': form})

def grade_create(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'templates/grade_form.html', {'form': form})

def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'templates/grade_form.html', {'form': form})