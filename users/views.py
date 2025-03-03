from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from projects.models import Project, Submission
from classes.models import Class

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    context = {}
    
    if request.user.user_type == 'student':
        enrolled_classes = Class.objects.filter(students=request.user)
        submissions = Submission.objects.filter(student=request.user)
        active_projects = submissions.filter(status='draft').count()
        completed_projects = submissions.filter(status='graded').count()
        
        context.update({
            'enrolled_classes_count': enrolled_classes.count(),
            'active_projects_count': active_projects,
            'completed_projects_count': completed_projects,
            'recent_activities': submissions.order_by('-submitted_at')[:5],
            'upcoming_deadlines': Project.objects.filter(assigned_class__in=enrolled_classes).order_by('due_date')[:5]
        })
    
    elif request.user.user_type == 'teacher':
        classes = Class.objects.filter(teacher=request.user)
        projects = Project.objects.filter(created_by=request.user)
        submissions = Submission.objects.filter(project__created_by=request.user)
        
        context.update({
            'classes_count': classes.count(),
            'total_students': sum(c.students.count() for c in classes),
            'projects_count': projects.count(),
            'pending_submissions': submissions.filter(status='submitted').count(),
            'recent_activities': submissions.order_by('-submitted_at')[:5],
            'upcoming_deadlines': projects.order_by('due_date')[:5]
        })
    
    return render(request, 'users/dashboard.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
        'recent_activities': [],  # Add logic to get user's recent activities
    }
    
    if request.user.user_type == 'student':
        submissions = Submission.objects.filter(student=request.user)
        context.update({
            'enrolled_classes_count': Class.objects.filter(students=request.user).count(),
            'active_projects_count': submissions.filter(status='draft').count(),
            'completed_projects_count': submissions.filter(status='graded').count(),
            'current_submissions': submissions.filter(status__in=['draft', 'submitted']).order_by('project__due_date')[:5]
        })
    else:
        classes = Class.objects.filter(teacher=request.user)
        context.update({
            'classes_count': classes.count(),
            'total_students': sum(c.students.count() for c in classes),
            'projects_count': Project.objects.filter(created_by=request.user).count(),
            'current_classes': classes.order_by('-created_at')[:5]
        })
    
    return render(request, 'users/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})
