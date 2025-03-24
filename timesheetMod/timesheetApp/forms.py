from django import forms
from .models import Entry, Project, Module, Task


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

        # Get project ID from POST data if available
        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['module'].queryset = Module.objects.filter(
                    project_id=project_id)
                self.fields['task'].queryset = Task.objects.filter(
                    module__project_id=project_id)
            except (ValueError, TypeError):
                pass  # If project_id is invalid, keep queryset empty
