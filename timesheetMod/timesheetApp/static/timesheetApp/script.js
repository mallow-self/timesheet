function setMaxDate() {
    let today = new Date().toISOString().split('T')[0];
    document.getElementById("date_entry").setAttribute("max", today);
}

//dynamic projects loading
function get_projects() {
    let select = document.getElementById("project");
    select.innerHTML = '<option value="">Select a project</option>'; // Clear existing options

    // Simulating an API call (Replace this with actual AJAX fetch)
    let projects = [
        { id: 1, name: "Project Alpha" },
        { id: 2, name: "Project Beta" },
        { id: 3, name: "Project Gamma" }
    ];

    projects.forEach(project => {
        let option = document.createElement("option");
        option.value = project.id;
        option.textContent = project.name;
        select.appendChild(option);
    });
}
document.getElementById("project").addEventListener("focus", function (event) {
    get_projects();
});

//dynamic modules loading
function get_modules() {
    let select_module = document.getElementById("module");
    select_module.innerHTML = '<option value="">Select a module</option>'; // Clear existing options

    // Simulating an API call (Replace this with actual AJAX fetch)
    let modules = [
        { id: 1, name: "module Alpha" },
        { id: 2, name: "module Beta" },
        { id: 3, name: "module Gamma" }
    ];

    modules.forEach(task => {
        let option = document.createElement("option");
        option.value = task.id;
        option.textContent = task.name;
        select_module.appendChild(option);
    });
}
document.getElementById("module").addEventListener("focus", function (event) {
    get_modules();
});

//dynamic task loading
function get_tasks() {
    let select_task = document.getElementById("task");
    select_task.innerHTML = '<option value="">Select a task</option>'; // Clear existing options

    // Simulating an API call (Replace this with actual AJAX fetch)
    let tasks = [
        { id: 1, name: "task Alpha" },
        { id: 2, name: "task Beta" },
        { id: 3, name: "task Gamma" }
    ];

    tasks.forEach(task => {
        let option = document.createElement("option");
        option.value = task.id;
        option.textContent = task.name;
        select_task.appendChild(option);
    });
}
document.getElementById("task").addEventListener("focus", function (event) {
    get_tasks();
});

//validation on submit
function validation(){
    //validate here client side
    return true;
}
// Set max date on page load
window.onload = setMaxDate;