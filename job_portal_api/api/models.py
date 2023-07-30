# api/models.py
from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')])

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_profile = models.URLField()

    def __str__(self):
        return self.name


class Internship(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    duration_months = models.PositiveIntegerField()
    stipend = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField()
    instructor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.PositiveIntegerField(default=0)
    is_discounted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount_percent = models.PositiveIntegerField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        return self.code


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.user.username
    

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, null=True, blank=True)
    internship = models.ForeignKey(
        Internship, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark by {self.user.username}"
