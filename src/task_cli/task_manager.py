from .task import Task
import typer
from typing_extensions import Annotated
import json

task_list = []

def load_tasks():
    global task_list
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            task_list = [Task.from_dict(task) for task in json.load(f)]
    except FileNotFoundError:
        task_list = []
    except json.JSONDecodeError:
        task_list = []
            
def add(name: Annotated[str, typer.Argument(default="New Task", help="Name of the task")]):
    load_tasks()  # Load existing tasks
    
    new_id = 0
    if len(task_list) != 0:
        new_id = int(task_list[-1].get_id()) + 1
        
    task = Task(name, id=new_id)
    task_list.append(task)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump([t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4)
    
    typer.echo(f"Task added successfully (ID: {new_id + 1})")

def update(id: Annotated[int, typer.Argument(default=0, help="ID of the task")], name: Annotated[str, typer.Argument(default="Updated Task", help="New name of the task")]):
    load_tasks()  # Load existing tasks
    
    task_list[id - 1].set_description(description=name) 

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump([t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4)
    
    typer.echo(f"Task {id} updated to '{name}'.")

def delete(id: Annotated[int, typer.Argument(default=0, help="ID of the task")]):
    load_tasks()
    
    del task_list[id - 1]
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump([t.to_dict() for t in task_list], f, ensure_ascii=False, indent=4)
    
    typer.echo(f"Task {id} deleted.")

def mark_in_progress(id: Annotated[int, typer.Argument(default=0, help="ID of the task")]):
    typer.echo(f"Task {id} marked as in progress.")

def mark_done(id: Annotated[int, typer.Argument(default=0, help="ID of the task")]):
    typer.echo(f"Task {id} marked as done.")

def list(name: Annotated[str, typer.Argument(default="all", help="Name of the task to list")]):
    typer.echo(f"Listing tasks with name '{name}'.")