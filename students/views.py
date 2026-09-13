from django.shortcuts import render, redirect , get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    students = Student.objects.all()
    return render(request, 'students/home.html', {'form': form, 'students': students})

def edit_student(request,id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/form.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'students/delete.html', {'student': student})