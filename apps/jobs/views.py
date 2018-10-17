# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from .filters import JobFilter
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
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=hashed_pw)
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
    # job = Job.objects.get(user=user)
    # profile = Profile.objects.get(user=user)
    # past_jobs = PastJobs.objects.get(profile=profile)
    context = {
        "user": user,
        # "jobs": job,
        # "profile": profile,
        # "past_jobs": past_jobs
    }
    return render(request, 'jobs/dashboard.html', context)

def jobs_list(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

    if 'id' in request.session == None:
        return redirect('/')
    job = Job.objects.all()
    category_list = CategoryList.objects.all()
    jobs = JobList.objects.get(job=job, category_list=category_list)
    context = {
        "jobs":jobs
    }
    return render(request, 'jobs/jobs.html', context)

def add_job(request):
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
        Job.objects.create(title=title, desc=desc, requirements=requirements, length=length, budger=budget, area=area, skill_level=skill_level, pay_type=pay_type)
        messages.success(request, "Successfully Added Job")
        return redirect('/jobs')

        
def search(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'job/job_list.html', {'filter': job_filter})
