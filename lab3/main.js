let todo = {
    construct: function() {
        this.selectElements();
        this.bindEvents();
        this.scanTaskList();
    },
    selectElements: function() {
        this.taskInput = document.getElementById("input-task");
        this.taskList = document.getElementById("tasks");
        this.taskListChildren = this.taskList.children;
        this.addButton = document.getElementById("add-task-btn");
        this.errorMessage = document.getElementById("error");
    },
    buildTask: function() {
        let taskListItem, taskCheckbox, taskValue, taskButton, taskDelete;
        taskListItem = document.createElement("li");
        taskListItem.setAttribute("class", "task");
        taskCheckbox = document.createElement("input");
        taskCheckbox.setAttribute("type", "checkbox");
        taskCheckbox.setAttribute("class","check")
        taskValue = document.createTextNode(this.taskInput.value);
        taskButton = document.createElement("button");
        taskButton.setAttribute("class","delete");
        taskDelete = document.createElement("i");
        taskDelete.setAttribute("class","fa fa-trash-o fa-2x");
        taskButton.appendChild(taskDelete);
        taskListItem.appendChild(taskCheckbox);
        taskListItem.appendChild(taskValue);
        taskListItem.appendChild(taskButton);
        this.taskList.appendChild(taskListItem);
    },
    error: function() {
        this.errorMessage.style.display = "block";
    },
    addTask: function() {
        let taskValue = this.taskInput.value;
        this.errorMessage.style.display = "none";

        if (taskValue === "") {
            this.error();
        }
        else {
            this.buildTask();
            this.taskInput.value = "";
            this.scanTaskList();
        }
    },
    enterKey: function(event) {
        if (event.keyCode === 13 || event.which === 13) {
            this.addTask();
        }
    },
    bindEvents: function() {
        this.addButton.onclick = this.addTask.bind(this);

        this.taskInput.onkeypress = this.enterKey.bind(this);
    },
    scanTaskList: function() {
        let taskListItem, checkBox, deleteButton;
        for (i=0;i<this.taskListChildren.length;i++) {
            taskListItem = this.taskListChildren[i];
            checkBox = taskListItem.getElementsByTagName("input")[0];
            deleteButton = taskListItem.getElementsByTagName("button")[0];

            checkBox.onclick = this.completeTask.bind(this, taskListItem, checkBox);
            deleteButton.onclick = this.deleteTask.bind(this, i);
        }
    },
    deleteTask: function(i) {
        this.taskListChildren[i].remove();
        this.scanTaskList();
    },
    completeTask: function(taskListItem, checkBox) {
        if (checkBox.checked) {
            taskListItem.className = "task-completed";
        }
        else {
            this.incompleteTask(taskListItem);
        }
    },
    incompleteTask: function(taskListItem) {
        taskListItem.className = "task";
    }
};