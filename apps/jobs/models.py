from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date



class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be 2 or more characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be 2 or more characters"
        if len(postData['first_name']) > 30:
            errors['first_name'] = "First name needs to be less then 30 characters"
        if len(postData['last_name']) > 30:
            errors['last_name'] = "Last name needs to be less then 30 characters"
        if not postData['first_name'].isalpha():
            errors['first_name'] = "First name needs to be only letters"
        if not postData['last_name'].isalpha():
            errors['last_name'] = "Last name needs to be only letters"

        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

                
        try:
            postData['username']
        except ValidationError:
            errors['username'] = "Your username is not valid"
        else:
            if User.objects.filter(username=postData['username']):
                errors['username'] = "This username already exists"


        if len(postData['password']) < 4:
            errors['password'] = "Please enter a longer password, needs to be four or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="United States")
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Languages(models.Model):
    name = models.CharField(max_length=1000, default=0)

class PastJobsManager(models.Manager):
    def validate_past(self, postData):
        errors = {}
        today = date.today()
        if str(postData['date_from']) > str(today) or str(postData['date_from']) > str(postData['date_to']):
            errors['date_from'] = "Your starting date is messed up you need to fix it"
        if str(postData['date_to']) > str(today) or str(postData['date_to']) < str(postData['date_from']):
            errors['date_to'] = "Your ending date is messed up you need to fix it"
        if len(postData['job_title']) < 3:
            errors['job_title'] = "You need to have at least 3 for the job title"
        if len(postData['job_title']) > 30:
            errors['job_title'] = "You need to have at most 30 for the job title"
        if len(postData['company']) < 3:
            errors['company'] = "Your need to have at least 3 for the company"
        if len(postData['company']) > 30:
            errors['company'] = "Your need to have at most 30 for the company"
        if len(postData['job_desc']) < 10:
            errors['job_desc'] = "You need to have at least 10 characters for the job description"
        return errors

class PastJobs(models.Model):
    user = models.ForeignKey(User, related_name="profile", on_delete=models.DO_NOTHING)
    date_from = models.DateField(auto_now=False)
    date_to  = models.DateField(auto_now=False)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    job_desc = models.TextField()
    objects = PastJobsManager()

class JobManager(models.Manager):
    def validate_job(self,postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title for the job needs to be 3 or more characters"
        if len(postData['title']) > 100:
            errors['title'] = "Title needs to be less than 100 characters"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description needs to be at least 10 characters"
        if len(postData['requirements']) < 10:
            errors['requirements'] = "Requirements needs to be at least 10 characters"
        return errors

class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    requirements = models.TextField()
    length = models.IntegerField()
    budget = models.IntegerField()
    accepted_terms = models.BooleanField(default=False)
    area = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default="Unknown")
    skill_level = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()

class UserApplied(models.Model):
    user_applied = models.BooleanField(default=True)
    cover_letter = models.TextField()
    amount_charged = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="applicant", on_delete=models.DO_NOTHING)
    job = models.ForeignKey(Job, related_name="job", on_delete=models.DO_NOTHING)

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

class CategoryList(models.Model):
    job = models.ForeignKey(Job, related_name="category_item", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.DO_NOTHING)

class JobList(models.Model):
    job = models.ForeignKey(Job, related_name="items", on_delete=models.DO_NOTHING)
    category_list = models.ForeignKey(CategoryList, related_name="categories", on_delete=models.DO_NOTHING)
