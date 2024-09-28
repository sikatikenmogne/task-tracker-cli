import json

import typer
from typing_extensions import Annotated

from .task import Task

task_list = []


def load_tasks():
    """
    Loads tasks from a JSON file and populates the global task_list variable.

    This function attempts to read tasks from a file named 'data.json' and
    convert them into Task objects. If the file does not exist or contains
    invalid JSON, the task_list is initialized as an empty list.

    Raises:
        FileNotFoundError: If the 'data.json' file is not found.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    global task_list
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            task_list = [Task.from_dict(task) for task in json.load(f)]
    except FileNotFoundError:
        task_list = []
    except json.JSONDecodeError:
        task_list = []


def add(
    name: Annotated[
        str, typer.Argument(default="New Task", help="Name of the task")
    ]
):
    """
    Adds a new task to the task list.
    This function loads the existing tasks, assigns a new ID to the task,
    appends it to the task list, and saves the updated list to a JSON file.
    Args:
        name (str): The name of the task. Defaults to "New Task".
    Returns:
        None
    """
    load_tasks()  # Load existing tasks

    new_id = 0
    if len(task_list) != 0:
        new_id = int(task_list[-1].get_id()) + 1

    task = Task(name, id=new_id)
    task_list.append(task)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(
            [t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4
        )

    typer.echo(f"Task added successfully (ID: {new_id + 1})")


def update(
    id: Annotated[int, typer.Argument(default=0, help="ID of the task")],
    name: Annotated[
        str,
        typer.Argument(default="Updated Task", help="New name of the task"),
    ],
):
    """
    Update the name of an existing task.
    Args:
        id (int): ID of the task to be updated.
        name (str): New name for the task.
    Returns:
        None
    Side Effects:
        - Loads existing tasks from a data source.
        - Updates the task's name in the task list.
        - Writes the updated task list back to the data source.
        - Outputs a message indicating the task has been updated.
    """
    load_tasks()  # Load existing tasks

    task_list[id - 1].set_description(description=name)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(
            [t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4
        )

    typer.echo(f"Task {id} updated to '{name}'.")


def delete(
    id: Annotated[int, typer.Argument(default=0, help="ID of the task")]
):
    """
    Deletes a task from the task list by its ID.
    Args:
        id (int): The ID of the task to delete. Defaults to 0.
    Raises:
        IndexError: If the provided ID is out of range.
    Side Effects:
        - Modifies the global task list by removing the specified task.
        - Writes the updated task list to 'data.json'.
        - Outputs a message indicating the task has been deleted.
    """
    load_tasks()

    del task_list[id - 1]

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(
            [t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4
        )

    typer.echo(f"Task {id} deleted.")


def mark_in_progress(
    id: Annotated[int, typer.Argument(default=0, help="ID of the task")]
):
    """
    Marks a task as 'in-progress' based on the provided task ID.
    Args:
        id (int): The ID of the task to be marked as in-progress. Defaults to
        0.
    Raises:
        IndexError: If the provided ID is out of range of the task list.
    Side Effects:
        - Loads the current list of tasks.
        - Updates the status of the specified task to 'in-progress'.
        - Writes the updated task list to 'data.json'.
        - Outputs a message indicating the task has been marked as in-progress.
    """
    load_tasks()

    task_list[id - 1].set_status("in-progress")

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(
            [t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4
        )

    typer.echo(f"Task {id} marked as in progress.")


def mark_done(
    id: Annotated[int, typer.Argument(default=0, help="ID of the task")]
):
    """
    Marks a task as done based on the provided task ID.
    Args:
        id (int): The ID of the task to be marked as done. Defaults to 0.
    Raises:
        IndexError: If the provided ID is out of range of the task list.
    Side Effects:
        - Updates the status of the specified task to "done".
        - Writes the updated task list to "data.json".
    Outputs:
        - Prints a message indicating the task has been marked as done.
    """
    load_tasks()

    if task_list[id - 1].get_status() != "done":
        task_list[id - 1].set_status("done")

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(
                [t.to_dict() for t in task_list],
                f,
                ensure_ascii=False,
                indent=4,
            )

    typer.echo(f"Task {id} marked as done.")


def list(
    status: Annotated[
        str, typer.Argument(default=None, help="Status of the tasks to list")
    ] = None
):
    load_tasks()

    if status:
        filtered_tasks = [
            task for task in task_list if task.get_status() == status
        ]
    else:
        filtered_tasks = task_list

    for task in filtered_tasks:
        typer.echo(
            f"{task.get_id()}: {task.get_description()} [{task.get_status()}]"
        )
