# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from .filters import *
from .models import *
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'jobs/index.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode('utf-8'), user[0].password.encode('utf-8'))
        if is_pass:
            request.session['id'] = user[0].id
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/')
    else:
        messages.error(request, "User does not exist")
    return redirect('/')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        location = request.POST['location']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(first_name=first_name, last_name=last_name, location=location, username=username, email=email, password=hashed_pw)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')


def dashboard(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    applied = UserApplied.objects.filter(user=user)
    past_jobs = PastJobs.objects.filter(user=user)
    users = User.objects.all().count()
    count_jobs = Job.objects.all().count()
    applied_count = UserApplied.objects.filter(user=user).count()
    context = {
        "user": user,
        "jobs": applied,
        "past_jobs": past_jobs,
        "jobs_amount": count_jobs,
        "applied_amount": applied_count,
        "users": users
    }
    return render(request, 'jobs/dashboard.html', context)

def jobs_list(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    jobs = Job.objects.all().order_by('-created_at')
    context = {
        "jobs":jobs
    }
    return render(request, 'jobs/jobs.html', context)


def add_job(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    return render(request, 'jobs/add-job.html')

def process_job(request):
    errors = Job.objects.validate_job(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    else:
        title = request.POST['title']
        desc = request.POST['desc']
        requirements = request.POST['requirements']
        length = request.POST['length']
        budget = request.POST['budget']
        area = request.POST['area']
        skill_level = request.POST['skill_level']
        pay_type = request.POST['pay_type']
        company = request.POST['company']
        Job.objects.create(title=title, desc=desc, requirements=requirements, length=length, budget=budget, area=area, skill_level=skill_level, pay_type=pay_type, company=company)
        messages.success(request, "Successfully Added Job")
        return redirect('/jobs')

def add_past_jobs(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    return render(request, 'jobs/add-past-jobs.html')

def process_past_jobs(request):
    errors = PastJobs.objects.validate_past(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['id'])
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        job_title = request.POST['job_title']
        company = request.POST['company']
        job_desc = request.POST['job_desc']
        PastJobs.objects.create(user=user, date_from=date_from, date_to=date_to, job_title=job_title, company=company, job_desc=job_desc)
        messages.success(request, 'Added past job, want to add another?')
        return redirect('/dashboard')

def delete_past_job(request, id):
    item = PastJobs.objects.get(id=id)
    item.delete()
    messages.success(request, 'Past job deleted')
    return redirect('/dashboard')


def apply_for_job(request, id):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    job = Job.objects.get(id=id)
    context = {
        "job": job
    }
    return render(request, 'jobs/apply-for-job.html', context)

def process_apply(request, id):
    user = User.objects.get(id=request.session['id'])
    job = Job.objects.get(id=id)
    cover_letter = request.POST['cover_letter']
    amount_charged = request.POST['amount_charged']
    UserApplied.objects.create(user=user, job=job, cover_letter=cover_letter, amount_charged=amount_charged)
    messages.success(request, 'Applied Successfully')
    return redirect('/dashboard')

def job_single(request, id):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    job = Job.objects.get(id=id)
    context = {
        "job": job
    }
    return render(request, 'jobs/job.html', context)

def delete_job(request, id): 
    item = UserApplied.objects.get(id=id)
    item.delete()
    messages.success(request, 'Applied job successfully deleted')
    return redirect('/dashboard')

def search(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'jobs/job_list.html', {'filter': job_filter})

def search_for_developer(request):
    developers = User.objects.all()
    developer_filter = DeveloperFilter(request.GET, queryset=developers)
    return render(request, 'jobs/search-for-developer.html', {'filter': developer_filter})

def developers(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'jobs/developers.html', context)

def developer_profile(request, id):
    user = User.objects.get(id=id)
    past_jobs = PastJobs.objects.filter(user=user)
    context = {
        "user": user,
        "past_jobs": past_jobs
    }
    return render(request, 'jobs/developer-profile.html', context)