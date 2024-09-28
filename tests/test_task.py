import pytest
from task_cli.task import Task
import datetime

def test_task_initialization():
    description = "Test Task"
    task = Task(description=description)
    
    assert task.get_description() == description
    assert task.get_status() == "to-do"
    assert task.get_id() == 0
    assert task.get_created_at() is not None
    assert task.to_dict()["description"] == description

def test_task_set_description():
    task = Task(description="Initial Description")
    new_description = "Updated Description"
    task.set_description(new_description)
    
    assert task.get_description() == new_description
    assert task.to_dict()["description"] == new_description

def test_task_set_status():
    task = Task(description="Test Task")
    new_status = "in-progress"
    task.set_status(new_status)
    
    assert task.get_status() == new_status
    assert task.to_dict()["status"] == new_status

def test_task_to_dict():
    description = "Test Task"
    status = "to-do"
    task = Task(description=description, status=status)
    task_dict = task.to_dict()
    
    assert task_dict["description"] == description
    assert task_dict["status"] == status
    assert "created_at" in task_dict
    assert "updated_at" in task_dict

def test_task_from_dict():
    data = {
        "description": "Test Task",
        "id": 1,
        "status": "done",
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat()
    }
    task = Task.from_dict(data)
    
    assert task.get_description() == data["description"]
    assert task.get_id() == data["id"]
    assert task.get_status() == data["status"]
    assert task.get_created_at() == data["created_at"]
    assert task.to_dict()["updated_at"] == data["updated_at"]