from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Class
from .forms import ClassForm, AddStudentsForm
from users.models import CustomUser

@login_required
def class_list(request):
    if request.user.user_type == 'student':
        classes = Class.objects.filter(students=request.user)
    elif request.user.user_type == 'teacher':
        classes = Class.objects.filter(teacher=request.user)
    else:
        classes = Class.objects.all()
    
    return render(request, 'classes/class_list.html', {'classes': classes})

@login_required
def class_detail(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    
    if request.user.user_type == 'student' and not class_obj.students.filter(id=request.user.id).exists():
        return HttpResponseForbidden("You are not enrolled in this class.")
    
    if request.user.user_type == 'teacher' and request.user != class_obj.teacher:
        return HttpResponseForbidden("You don't have access to this class.")
    
    return render(request, 'classes/class_detail.html', {'class': class_obj})

@login_required
def class_create(request):
    if request.user.user_type == 'student':
        return HttpResponseForbidden("Students cannot create classes.")
    
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            class_obj = form.save(commit=False)
            class_obj.teacher = request.user
            class_obj.save()
            messages.success(request, 'Class created successfully!')
            return redirect('class_detail', pk=class_obj.pk)
    else:
        form = ClassForm()
    
    return render(request, 'classes/class_form.html', {
        'form': form,
        'title': 'Create Class'
    })

@login_required
def class_edit(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    
    if request.user != class_obj.teacher and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to edit this class.")
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class updated successfully!')
            return redirect('class_detail', pk=class_obj.pk)
    else:
        form = ClassForm(instance=class_obj)
    
    return render(request, 'classes/class_form.html', {
        'form': form,
        'title': 'Edit Class'
    })

@login_required
def class_delete(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    
    if request.user != class_obj.teacher and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to delete this class.")
    
    if request.method == 'POST':
        class_obj.delete()
        messages.success(request, 'Class deleted successfully!')
        return redirect('class_list')
    
    return render(request, 'classes/class_confirm_delete.html', {'class': class_obj})

@login_required
def class_add_students(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    
    if request.user != class_obj.teacher and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to add students to this class.")
    
    if request.method == 'POST':
        form = AddStudentsForm(request.POST)
        if form.is_valid():
            selected_students = form.cleaned_data['students']
            class_obj.students.add(*selected_students)
            messages.success(request, 'Students added successfully!')
            return redirect('class_detail', pk=class_obj.pk)
    else:
        # Exclude already enrolled students
        available_students = CustomUser.objects.filter(user_type='student').exclude(classes_enrolled=class_obj)
        form = AddStudentsForm()
        form.fields['students'].queryset = available_students
    
    return render(request, 'classes/add_students.html', {
        'form': form,
        'class': class_obj
    })

@login_required
def class_remove_student(request, class_pk, student_pk):
    class_obj = get_object_or_404(Class, pk=class_pk)
    student = get_object_or_404(CustomUser, pk=student_pk)
    
    if request.user != class_obj.teacher and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to remove students from this class.")
    
    if request.method == 'POST':
        class_obj.students.remove(student)
        messages.success(request, f'{student.get_full_name()} has been removed from the class.')
    
    return redirect('class_detail', pk=class_obj.pk)
