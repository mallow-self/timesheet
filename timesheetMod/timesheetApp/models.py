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
        return f"{self.name} - {self.project.name}"


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)  # Primary key auto increments
    name = models.CharField(max_length=255)  # Text-based name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return self.name


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)  # Primary key auto increments
    name = models.CharField(max_length=255)  # Text-based name
    effort = models.IntegerField(default=0)  # value in minutes
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # a foreign key referencing teams
    assumption = models.TextField(blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)# a foreign key referencing module
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates - updated on every update
    def __str__(self):
        return self.name 


# entry table model
class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True)  # Primary key auto increments
    date_entry = models.DateField()
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # a foreign key referencing project
    module = models.ForeignKey(Module, on_delete=models.CASCADE)# a foreign key referencing module
    task = models.ForeignKey(Task,on_delete=models.CASCADE) # a foreign key referencing task
    time_entry = models.IntegerField()  # value in minutes
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates - updated on every update
