import unittest
from unittest.mock import mock_open, patch

from task_cli.task_manager import add, load_tasks, list as task_list
from unittest.mock import mock_open, patch, MagicMock


from task_cli.task_manager import (
    add,
    load_tasks,
    update,
    delete,
    mark_in_progress,
    mark_done,
    list,
    task_list,
)


class TestTaskManager(unittest.TestCase):

    @patch("task_cli.task_manager.load_tasks")
    @patch("task_cli.task_manager.task_list", [MagicMock(id=1, name="Task to Delete")])
    @patch("builtins.open", new_callable=mock_open)
    def test_delete(self, mock_open, mock_load_tasks):
        delete(1)
        self.assertEqual(len(task_list), 0)

    @patch("task_cli.task_manager.load_tasks")
    @patch("task_cli.task_manager.task_list", [
        MagicMock(id=1, status="done", get_id=lambda: 1, get_description=lambda: "Task 1", get_status=lambda: "done"),
        MagicMock(id=2, status="in-progress", get_id=lambda: 2, get_description=lambda: "Task 2", get_status=lambda: "in-progress")
    ])
    def test_list(self, mock_load_tasks):
        with patch("typer.echo") as mock_echo:
            list("done")
            mock_echo.assert_called_once_with("1: Task 1 [done]")

if __name__ == "__main__":
    unittest.main()
