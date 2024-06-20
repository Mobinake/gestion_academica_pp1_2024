from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Estudiante
from .forms import StudentForm

@permission_required('myapp.add_student')
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'myapp/student_form.html', {'form': form})

@permission_required('myapp.change_student')
def student_update(request, pk):
    student = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'myapp/student_form.html', {'form': form})