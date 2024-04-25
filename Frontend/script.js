const baseURL = "http://localhost:8000";
let databaseSelect;

document.addEventListener("DOMContentLoaded", () => {
    databaseSelect = document.getElementById("database");
    const todosContainer = document.getElementById("todos");

    databaseSelect.addEventListener("change", () => {
        fetchTodos(databaseSelect.value);
    });

    document.getElementById("create").addEventListener("click", () => {
        createTodo();
    });

    fetchTodos(databaseSelect.value);
});

async function fetchTodos(database) {
    try {
        const response = await fetch(`${baseURL}/${database}/todos`);
        const todos = await response.json();
        displayTodos(todos);
    } catch (error) {
        console.error("Error fetching todos:", error);
    }
}

async function createTodo() {
    var id=0
    const name = prompt("Enter todo name:");
    const description = prompt("Enter todo description:");
    if (name && description) {
        const newTodo = {id, name, description };
        try {
            const response = await fetch(`${baseURL}/${databaseSelect.value}/todos`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newTodo)
            });
            if (response.ok) {
                fetchTodos(databaseSelect.value); // Fetch updated todos after creating a new one
            } else {
                console.error("Failed to create todo");
            }
        } catch (error) {
            console.error("Error creating todo:", error);
        }
    }
}

async function updateTodo(todoId, currentTitle, currentDescription) {
    
    const newTitle = prompt("Enter new title:", currentTitle);
    const newDescription = prompt("Enter new description:", currentDescription);
    if (newTitle !== null && newDescription !== null) {
        const newId=todoId
        const updatedTodo = {id: newId, name: newTitle, description: newDescription };
        try {
            const response = await fetch(`${baseURL}/${databaseSelect.value}/todos/${todoId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedTodo)
            });
            if (response.ok) {
                fetchTodos(databaseSelect.value); // Fetch updated todos after updating
            } else {
                console.error("Failed to update todo");
            }
        } catch (error) {
            console.error("Error updating todo:", error);
        }
    }
}

async function deleteTodo(todoId) {
    const confirmation = confirm("Are you sure you want to delete this todo?");
    if (confirmation) {
        try {
            const response = await fetch(`${baseURL}/${databaseSelect.value}/todos/${todoId}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                fetchTodos(databaseSelect.value); // Fetch updated todos after deleting
            } else {
                console.error("Failed to delete todo");
            }
        } catch (error) {
            console.error("Error deleting todo:", error);
        }
    }
}

function displayTodos(todos) {
    const todosContainer = document.getElementById("todos");
    todosContainer.innerHTML = "";
    todos.forEach(todo => {
        const todoElement = document.createElement("div");
        todoElement.classList.add("todo");
        todoElement.innerHTML = `
            <strong>${todo.name}</strong>
            <p>${todo.description}</p>
            <button onclick="updateTodo(${todo.id},'${todo.name}','${todo.description}')">Update</button>
            <button onclick="deleteTodo(${todo.id})">Delete</button>
        `;
        todosContainer.appendChild(todoElement);
    });
}
