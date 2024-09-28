"""
This module defines the command-line interface (CLI) for the task tracker
application using Typer.
Commands:
    add: Adds a new task.
    update: Updates an existing task.
    delete: Deletes a task.
    mark_in_progress: Marks a task as in progress.
    mark_done: Marks a task as done.
    list: Lists all tasks.
Modules:
    typer: A library for creating CLI applications.
    task_manager: A module containing task management functions such as add,
    delete, list, mark_done, mark_in_progress, and update.
"""
import typer

from .task_manager import (
    add,
    delete,
    list as list_tasks,
    mark_done,
    mark_in_progress,
    update,
)

app = typer.Typer()

app.command()(add)

app.command()(update)

app.command()(delete)

app.command()(mark_in_progress)

app.command()(mark_done)

app.command()(list_tasks)
