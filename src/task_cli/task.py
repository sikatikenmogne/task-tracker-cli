import typer
from typing_extensions import Annotated

def add(name: Annotated[str, typer.Argument(default="New Task", help="Name of the task")]):
    typer.echo(f"Task '{name}' added.")

def update(id: Annotated[int, typer.Argument(default=0, help="ID of the task")], name: Annotated[str, typer.Argument(default="Updated Task", help="New name of the task")]):
    typer.echo(f"Task {id} updated to '{name}'.")

def delete(id: Annotated[int, typer.Argument(default=0, help="ID of the task")]):
    typer.echo(f"Task {id} deleted.")

def mark_in_progress(id: Annotated[int, typer.Argument(default=0, help="ID of the task")]):
    typer.echo(f"Task {id} marked as in progress.")

def mark_done(id: Annotated[int, typer.Argument(default=0, help="ID of the task")]):
    typer.echo(f"Task {id} marked as done.")

def list(name: Annotated[str, typer.Argument(default="all", help="Name of the task to list")]):
    typer.echo(f"Listing tasks with name '{name}'.")