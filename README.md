Project Title: To-Do List Web Application
🔹 Description

This is a simple Django-based To-Do List web application where users can log in, manage their personal tasks, and keep track of what’s pending or completed.
It follows a user-authenticated system, meaning every user only sees their own tasks after logging in.

Deployed on [PythonAnywhere](https://aqsa23.pythonanywhere.com/).

🔹 Features

User Authentication

Login & logout functionality.

Each user has a personal task list.

Task Management

Add new tasks directly from the homepage.

View all tasks in a clean list format.

Completed tasks are marked with a ✔, while pending ones are labeled "Pending".

Search/Filter

Search for tasks by keyword using a search bar.

Admin Panel

Admins can log in at /admin/ to manage users and tasks.

Add, edit, or delete tasks directly from the admin interface.

Responsive UI

The interface uses Bootstrap for a simple and modern design.

🔹 Technical Details

Framework: Django 5

Database: SQLite (default Django DB)

Frontend: HTML + Bootstrap

Deployment: Hosted on PythonAnywhere

🔹 How it Works (Flow)

User visits the homepage → redirected to login if not logged in.

After login, user sees their own tasks.

User can:

Add a new task using the input form.

Search tasks using the search bar.

Check task status (✔ for completed, Pending otherwise).

Admin has full control via /admin/.
