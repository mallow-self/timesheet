from django.contrib import admin
from django.utils.timezone import localtime

# Register your models here.
from .models import Project, Module, Task, Team, Skill, Entry


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ("Basic Info", {"fields": ("name", "status")}),
    #     ("Timestamps", {"fields": ("created_at", "updated_at")}),
    # )
    readonly_fields = ["created_at", "updated_at"]
    list_editable = ["status"]
    list_display = [
        "project_id",
        "name",
        "status",
        "formatted_created_at",
        "formatted_updated_at",
    ]
    list_filter = ["status", "created_at", "updated_at"]
    search_fields = ["name"]

    def formatted_created_at(self, obj):
        return localtime(obj.created_at).strftime("%d/%m/%y %H:%M:%S")

    def formatted_updated_at(self, obj):
        return localtime(obj.updated_at).strftime("%d/%m/%y %H:%M:%S")

    formatted_created_at.admin_order_field = "created_at"
    formatted_created_at.short_description = "Created At"

    formatted_updated_at.admin_order_field = "updated_at"
    formatted_updated_at.short_description = "Updated At"


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "module_id",
        "project",
        "formatted_created_at",
        "formatted_updated_at",
    ]
    readonly_fields = ["created_at", "updated_at"]
    # list_editable = ["project"]
    list_filter = ["project", "created_at", "updated_at"]
    search_fields = ["name", "project__name"]

    def formatted_created_at(self, obj):
        return localtime(obj.created_at).strftime("%d/%m/%y %H:%M:%S")

    def formatted_updated_at(self, obj):
        return localtime(obj.updated_at).strftime("%d/%m/%y %H:%M:%S")

    formatted_created_at.admin_order_field = "created_at"
    formatted_created_at.short_description = "Created At"

    formatted_updated_at.admin_order_field = "updated_at"
    formatted_updated_at.short_description = "Updated At"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ("skills",)
    list_display = ["name", "get_skills", "formatted_updated_at"]

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])

    get_skills.short_description = "Skills"
    list_filter = ["created_at", "updated_at"]
    search_fields = ["name", "skills__name"]

    def formatted_updated_at(self, obj):
        return localtime(obj.updated_at).strftime("%d/%m/%y %H:%M:%S")

    formatted_updated_at.admin_order_field = "updated_at"
    formatted_updated_at.short_description = "Updated At"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "task_id",
        "name",
        "team",
        "module_name",
        "module_project_name",
        "effort",
        "assumption",
        "formatted_updated_at",
    ]
    list_filter = ["team", "module__project__name", "created_at", "updated_at"]
    search_fields = ["name", "module__project__name", "team", "module_name"]

    def module_name(self, obj):
        return obj.module.name

    module_name.short_description = "Module"

    def module_project_name(self, obj):
        return obj.module.project.name

    module_project_name.short_description = "Project"

    def formatted_updated_at(self, obj):
        return localtime(obj.updated_at).strftime("%d/%m/%y %H:%M:%S")

    formatted_updated_at.admin_order_field = "updated_at"
    formatted_updated_at.short_description = "Updated At"

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display=["entry_id","date_entry","description","project","module","task","time_entry"]
    
# admin.site.register(Project,ProjectAdmin)
# admin.site.register(Module)
# admin.site.register(Team)
# admin.site.register(Task)
# admin.site.register(Entry)