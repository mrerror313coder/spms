from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Project, Submission
from .forms import ProjectForm, SubmissionForm, GradeSubmissionForm
from classes.models import Class

# Create your views here.

@login_required
def project_list(request):
    if request.user.user_type == 'student':
        classes = Class.objects.filter(students=request.user)
        projects = Project.objects.filter(assigned_class__in=classes)
    elif request.user.user_type == 'teacher':
        projects = Project.objects.filter(created_by=request.user)
    else:
        projects = Project.objects.all()
    
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user.user_type == 'student':
        if not project.assigned_class.students.filter(id=request.user.id).exists():
            return HttpResponseForbidden("You don't have access to this project.")
        submission = Submission.objects.filter(project=project, student=request.user).first()
    else:
        submission = None
    
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'submission': submission
    })

@login_required
def project_create(request):
    if request.user.user_type == 'student':
        return HttpResponseForbidden("Students cannot create projects.")
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {
        'form': form,
        'title': 'Create Project'
    })

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user != project.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to edit this project.")
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_form.html', {
        'form': form,
        'title': 'Edit Project'
    })

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user != project.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to delete this project.")
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

@login_required
def submission_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    
    if not project.assigned_class.students.filter(id=request.user.id).exists():
        return HttpResponseForbidden("You don't have access to this project.")
    
    submission = Submission.objects.filter(project=project, student=request.user).first()
    if submission and submission.status == 'graded':
        messages.error(request, 'You cannot modify a graded submission.')
        return redirect('project_detail', pk=project.pk)
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.project = project
            submission.student = request.user
            submission.status = 'submitted'
            submission.save()
            messages.success(request, 'Project submitted successfully!')
            return redirect('project_detail', pk=project.pk)
    else:
        form = SubmissionForm(instance=submission)
    
    return render(request, 'projects/submission_form.html', {
        'form': form,
        'project': project,
        'title': 'Submit Project'
    })

@login_required
def submission_list(request):
    if request.user.user_type == 'student':
        submissions = Submission.objects.filter(student=request.user)
    else:
        submissions = Submission.objects.filter(project__created_by=request.user)
    
    return render(request, 'projects/submission_list.html', {'submissions': submissions})

@login_required
def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    
    if request.user != submission.student and request.user != submission.project.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to view this submission.")
    
    return render(request, 'projects/submission_detail.html', {'submission': submission})

@login_required
def submission_grade(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    
    if request.user != submission.project.created_by and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to grade this submission.")
    
    if request.method == 'POST':
        form = GradeSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.status = 'graded'
            submission.save()
            messages.success(request, 'Submission graded successfully!')
            return redirect('submission_detail', pk=submission.pk)
    else:
        form = GradeSubmissionForm(instance=submission)
    
    return render(request, 'projects/grade_submission.html', {
        'form': form,
        'submission': submission
    })
