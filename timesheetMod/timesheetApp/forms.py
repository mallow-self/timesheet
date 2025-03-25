from django import forms
from .models import Entry, Project, Module, Task
from asgiref.sync import sync_to_async

class EntryForm(forms.ModelForm):
    TIME_CHOICES = [
        ('','Select a time duration'),
        ('15', '0:15'),
        ('30', '0:30'),
        ('45', '0:45'),
        ('60', '1:00'),
        ('75', '1:15'),
        ('90', '1:30'),
        ('105', '1:45'),
        ('120', '2:00'),
        ('135', '2:15'),
        ('150', '2:30'),
        ('165', '2:45'),
        ('180', '3:00'),
    ]

    date_entry = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date",
        required=False
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1}),
        label="Description",
        required=False
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'id': 'project-dropdown'}),
        required=False
    )
    module = forms.ModelChoiceField(
        queryset=Module.objects.none(),
        empty_label=None,
        widget=forms.Select(attrs={'id': 'module-dropdown'}),
        required=False
    )
    task = forms.ModelChoiceField(
        queryset=Task.objects.none(),
        empty_label=None,
        widget=forms.Select(attrs={'id': 'task-dropdown'}),
        required=False
    )
    time_entry = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(),
        label="Time",
        required=False
    )

    class Meta:
        model = Entry
        fields = ['date_entry', 'description',
                  'project', 'module', 'task', 'time_entry']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ensure project exists before accessing it
        if self.instance and self.instance.project_id:
            self.fields['module'].queryset = Module.objects.filter(
                project=self.instance.project)
            self.fields['task'].queryset = Task.objects.filter(
                module__project=self.instance.project)
        else:
            self.fields['module'].queryset = Module.objects.none()
            self.fields['task'].queryset = Task.objects.none()

        # Handle dynamically selected project in POST request
        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['module'].queryset = Module.objects.filter(
                    project_id=project_id)
                self.fields['task'].queryset = Task.objects.filter(
                    module__project_id=project_id)
            except (ValueError, TypeError):
                pass  # Keep queryset empty if invalid input
