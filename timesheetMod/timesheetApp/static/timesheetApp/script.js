function validation() {
    let isValid = true;
    let date_entry = document.getElementById("date_entry").value;
    let description = document.getElementById("description").value;
    let project_id = document.getElementById("project").value;
    let module_id = document.getElementById("module").value;
    let task_id = document.getElementById("task").value;
    let time_entry = document.getElementById("time").value;

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

function setMaxDate() {
    let today = new Date().toISOString().split('T')[0];
    document.getElementById("date_entry").setAttribute("max", today);
}
// Set max date on page load
window.onload = setMaxDate;

//dynamic projects loading
function get_projects() {
    // Simulating an API call (Replace this with actual AJAX fetch)
    fetch('/timesheet/getProjects/')
        .then(response => response.json())
        .then(data => {
            let select = document.getElementById("project");
            select.innerHTML = '<option value="">Select a project</option>';// Clear existing options
            data["projects"].forEach(project => {
                let option = document.createElement("option");
                option.value = project.project_id;
                option.textContent = project.name;
                select.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching projects:", error));
    // let projects = [
    //     { id: 1, name: "Project Alpha" },
    //     { id: 2, name: "Project Beta" },
    //     { id: 3, name: "Project Gamma" }
    // ];

    // projects.forEach(project => {
    //     let option = document.createElement("option");
    //     option.value = project.project_id;
    //     option.textContent = project.name;
    //     select.appendChild(option);
    // });
}
document.getElementById("project").addEventListener("focus", function (event) {
    let task = document.getElementById("task");
    let module = document.getElementById("module");
    task.value = "";
    module.value = "";
    get_projects();
});

//dynamic modules loading
function get_modules(project_id) {
    fetch(`/timesheet/getModules?project_id=${project_id}`)
        .then(response => response.json())
        .then(data => {
            let select_module = document.getElementById("module");
            select_module.innerHTML = '<option value="">Select a module</option>'; // Clear existing options
            data["modules"].forEach(module => {
                let option = document.createElement("option");
                option.value = module.module_id;
                option.textContent = module.name;
                select_module.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching projects:", error));


    // // Simulating an API call (Replace this with actual AJAX fetch)
    // let modules = [
    //     { id: 1, name: "module Alpha" },
    //     { id: 2, name: "module Beta" },
    //     { id: 3, name: "module Gamma" }
    // ];

    // modules.forEach(module => {
    //     let option = document.createElement("option");
    //     option.value = module.id;
    //     option.textContent = module.name;
    //     select_module.appendChild(option);
    // });
}
document.getElementById("module").addEventListener("focus", function (event) {
    let p_id = document.getElementById("project").value;
    if (p_id === "") {
        event.target.blur(); // Remove focus before showing alert
        alert("Select Project!");
    } else {
        get_modules(p_id);
    }
});

//dynamic task loading
function get_tasks(module_id) {
    fetch(`/timesheet/getTasks?module_id=${module_id}`)
        .then(response => response.json())
        .then(data => {
            let select_task = document.getElementById("task");
            select_task.innerHTML = '<option value="">Select a task</option>'; // Clear existing options
            data["tasks"].forEach(task => {
                let option = document.createElement("option");
                option.value = task.task_id;
                option.textContent = task.name;
                select_task.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching projects:", error));
    // let select_task = document.getElementById("task");
    // select_task.innerHTML = '<option value="">Select a task</option>'; // Clear existing options

    // // Simulating an API call (Replace this with actual AJAX fetch)
    // let tasks = [
    //     { id: 1, name: "task Alpha" },
    //     { id: 2, name: "task Beta" },
    //     { id: 3, name: "task Gamma" }
    // ];

    // tasks.forEach(task => {
    //     let option = document.createElement("option");
    //     option.value = task.id;
    //     option.textContent = task.name;
    //     select_task.appendChild(option);
    // });
}
document.getElementById("task").addEventListener("focus", function (event) {
    let m_id = document.getElementById("module").value;
    if (m_id === "") {
        event.target.blur(); // Remove focus before showing alert
        alert("Select module!");
    } else {
        get_tasks(m_id);
    }
});


document.addEventListener("DOMContentLoaded", function () {
    fetch("/timesheet/entries/")  // Adjust the endpoint accordingly
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector("#entriesTable tbody");
            tableBody.innerHTML = ""; // Clear table before inserting new rows

            data.entries.forEach(entry => {
                const row = document.createElement("tr");
                row.innerHTML = `
                            <td>${entry.entry_id}</td>
                            <td>${entry.date_entry}</td>
                            <td>${entry.description}</td>
                            <td>${entry.project__name}</td>
                            <td>${entry.module__name}</td>
                            <td>${entry.task__name}</td>
                            <td>${entry.time_entry}</td>
                            <td>
                                <button class="btn btn-primary btn-sm update-btn" data-id="${entry.entry_id}">Update</button>
                                <button class="btn btn-danger btn-sm delete-btn" data-id="${entry.entry_id}">Delete</button>
                            </td>
                        `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error("Error fetching entries:", error));
});
