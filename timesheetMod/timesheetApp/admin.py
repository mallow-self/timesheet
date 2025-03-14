from django.contrib import admin
from django.utils.timezone import localtime

# Register your models here.
from .models import Project,Module,Task,Team

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("name", "status")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ["created_at", "updated_at"]
    list_editable = ["status"]
    list_display = ["project_id","name", "status", "formatted_created_at","formatted_updated_at"]
    list_filter = ["name", "status", "created_at","updated_at"]
    search_fields = ["name"]
    def formatted_created_at(self, obj):
        return localtime(obj.created_at).strftime("%d/%m/%y %H:%M:%S")

    def formatted_updated_at(self, obj):
        return localtime(obj.updated_at).strftime("%d/%m/%y %H:%M:%S")

    formatted_created_at.admin_order_field = "created_at"
    formatted_created_at.short_description = "Created At"

    formatted_updated_at.admin_order_field = "updated_at"
    formatted_updated_at.short_description = "Updated At"


# admin.site.register(Project,ProjectAdmin)
admin.site.register(Module)
admin.site.register(Team)
admin.site.register(Task)