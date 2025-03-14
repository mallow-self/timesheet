from django.db import models


# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)  # Primary key auto increments
    name = models.CharField(max_length=255)  # Text-based name
    status = models.BooleanField(default=True)  # Boolean field ,true if project in progress
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates - updated on every update
    def __str__(self):
        return self.name


class Module(models.Model):
    module_id = models.AutoField(primary_key=True)  # Primary key auto increments
    name = models.CharField(max_length=255)  # Text-based name
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # foreign key reference project table
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates - updated on every update
    def __str__(self):
        return self.name


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)  # Primary key auto increments
    name = models.CharField(max_length=255)  # Text-based name
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.TextField()# relevant skills
    def __str__(self):
        return self.name


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)  # Primary key auto increments
    name = models.CharField(max_length=255)  # Text-based name
    effort = models.IntegerField(default=0)  # value in minutes
    teams = models.ForeignKey(Team, on_delete=models.CASCADE)  # a foreign key referencing teams
    assumption = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)# a foreign key referencing module
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates - updated on every update
