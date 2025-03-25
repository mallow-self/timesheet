$(document).ready(function () {
    $('#project-dropdown').change(function () { // Trigger on project selection
        let project_id = $(this).val(); // Get selected project ID

        if (!project_id) {
            alert("Please select a project first.");
            return;
        }

        $.get(`http://127.0.0.1:8000/getModules/?project_id=${project_id}`, function (data) {
            let moduleDropdown = $("#module-dropdown");
            moduleDropdown.empty(); // Clear previous options
            moduleDropdown.append('<option value="" selected>Select a module</option>'); // Default option

            let taskDropdown = $("#task-dropdown");
            taskDropdown.empty();
            taskDropdown.append('<option value="" selected>Select a task</option>');

            $.each(data.modules, function (index, module) {
                moduleDropdown.append(`<option value="${module.module_id}">${module.name}</option>`);
            });
        });
    });

    $('#module-dropdown').change(function () { // Trigger on project selection
        let module_id = $(this).val(); // Get selected project ID

        if (!module_id) {
            alert("Please select a module first.");
            return;
        }

        $.get(`http://127.0.0.1:8000/getTasks/?module_id=${module_id}`, function (data) {
            let taskDropdown = $("#task-dropdown");
            taskDropdown.empty(); // Clear previous options
            taskDropdown.append('<option value="" selected>Select a task</option>'); // Default option

            $.each(data.tasks, function (index, task) {
                taskDropdown.append(`<option value="${task.task_id}">${task.name}</option>`);
            });
        });
    });

});

function validation() {
    let isValid = true;
    let date_entry = $('#id_date_entry').val();
    let description = $('#id_description').val();
    let project_id = $('#project-dropdown').val();
    let module_id = $('#module-dropdown').val();
    let task_id = $('#task-dropdown').val();
    let time_entry = $('#id_time_entry').val();

    let dobInput = new Date(date_entry);
    let today = new Date();
    if (date_entry == "") {
        alert("Enter date!");
        isValid = false;
        return false;
    } else if (dobInput > today) {
        alert("Don't Enter future dates");
        isValid = false;
        return false;
    }
    if (description == "") {
        alert("Enter description!");
        isValid = false;
        return false;
    }
    if (project_id == "") {
        alert("Enter project!");
        isValid = false;
        return false;
    }
    if (module_id == "") {
        alert("Enter module!");
        isValid = false;
        return false;
    }
    if (task_id == "") {
        alert("Enter task!");
        isValid = false;
        return false;
    }
    if (time_entry == "") {
        alert("Enter time!");
        isValid = false;
        return false;
    }
    if (isValid) {
        return true;
    } else {
        return false;
    }
}

