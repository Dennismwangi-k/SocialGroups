from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")


    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-update']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-update']

    def __str__(self):
        return self.body[0:50]


JOBTYPE = [
    ('Fulltime', 'Fulltime'),
    ('Parttime', 'Parttime'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
    ('Temporary', 'Temporary'),
    ('Volunteer', 'Volunteer'),
    ('Other', 'Other'),
]

REMOTE_ONSITE = [
    ('Remote', 'Remote'),
    ('Onsite', 'Onsite'),
    ('Hybrid', 'Hybrid'),
]


class Jobs(models.Model):
    company = models.CharField(max_length=200,default="")
    title = models.CharField(max_length=200)
    description = models.TextField()
    job_link = models.URLField(max_length=200,default="")
    job_type = models.CharField(choices=JOBTYPE,max_length=200,default="")
    remote_onsite = models.CharField(choices=REMOTE_ONSITE,max_length=200,default="")
    experience = models.CharField(max_length=200,default="")
    logo = models.ImageField(null=True, default="avatar.svg")
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_length=200,decimal_places=2, default=0.00, max_digits=10)
    deadline = models.DateField(default='')
    created = models.DateTimeField(auto_now_add=True)
   
    

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title