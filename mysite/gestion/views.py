from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Estudiante
from .forms import StudentForm, GradeForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

@permission_required('mysite.add_student')
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'mysite/student_form.html', {'form': form})

@permission_required('mysite.change_student')
def student_update(request, pk):
    student = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'mysite/student_form.html', {'form': form})

@permission_required('mysite.add_grade')
def grade_create(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'mysite/grade_form.html', {'form': form})

@permission_required('mysite.change_grade')
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'myapp/grade_form.html', {'form': form})