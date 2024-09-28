import datetime


class Task:
    """
    Task class represents a task with a description, status, and timestamps
    for creation and updates.
    Attributes:
        __id (int): Unique identifier for the task.
        __description (str): Description of the task.
        __status (str): Status of the task (e.g., 'to-do', 'in-progress',
        'done').
        __created_at (str): ISO formatted timestamp when the task was created.
        __updated_at (str): ISO formatted timestamp when the task was last
        updated.
    Methods:
        __init__(
        description: str,
        id=None,
        status='to-do',
        created_at=None,
        updated_at=None
        ):
            Initializes a new Task instance.
        get_description() -> str:
            Returns the description of the task.
        get_status() -> str:
            Returns the status of the task.
        get_created_at() -> str:
            Returns the creation timestamp of the task.
        get_id() -> int:
            Returns the unique identifier of the task.
        set_description(description: str):
            Updates the description of the task and sets the updated_at
            timestamp.
        set_status(status: str):
            Updates the status of the task and sets the updated_at timestamp.
        to_dict() -> dict:
            Converts the task instance to a dictionary.
        from_dict(data: dict) -> 'Task':
            Creates a Task instance from a dictionary.
    """

    def __init__(
        self,
        description: str,
        id=None,
        status="to-do",
        created_at=None,
        updated_at=None,
    ):
        self.__id = id if id is not None else 0
        self.__description = description
        self.__status = status
        self.__created_at = (
            created_at if created_at else datetime.datetime.now().isoformat()
        )
        self.__updated_at = (
            updated_at if updated_at else datetime.datetime.now().isoformat()
        )

    def get_description(self):
        """
        Retrieve the description of the task.

        Returns:
            str: The description of the task.
        """
        return self.__description

    def get_status(self):
        """
        Retrieve the current status of the task.

        Returns:
            str: The current status of the task.
        """
        return self.__status

    def get_created_at(self):
        """
        Retrieve the creation timestamp of the task.

        Returns:
            datetime: The timestamp when the task was created.
        """
        return self.__created_at

    def get_id(self):
        """
        Retrieve the unique identifier of the task.

        Returns:
            int: The unique identifier of the task.
        """
        return self.__id

    def set_description(self, description: str):
        """
        Sets the description of the task and updates the timestamp.

        Args:
            description (str): The new description for the task.
        """
        self.__description = description
        self.__updated_at = datetime.datetime.now().isoformat()

    def set_status(self, status: str):
        """
        Set the status of the task and update the timestamp.

        Args:
            status (str): The new status to set for the task.
        """
        self.__status = status
        self.__updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        Converts the task object to a dictionary representation.

        Returns:
            dict: A dictionary containing the task's id, description, status,
                  created_at, and updated_at.
        """
        return {
            "id": str(self.__id),
            "description": self.__description,
            "status": self.__status,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create an instance of the class from a dictionary.

        Args:
            data (dict): A dictionary containing the data to initialize the
            instance.
                - description (str): The description of the task. Defaults to
                    an empty string.
                - id (int): The ID of the task. Defaults to 0.
                - status (str): The status of the task. Defaults to "to-do".
                - created_at (str): The creation timestamp of the task in ISO
                    format. Defaults to the current time.
                - updated_at (str): The last updated timestamp of the task in
                    ISO format. Defaults to the current time.

        Returns:
            An instance of the class initialized with the provided data.
        """
        return cls(
            description=data.get("description", ""),
            id=data.get("id", 0),
            status=data.get("status", "to-do"),
            created_at=data.get(
                "created_at", datetime.datetime.now().isoformat()
            ),
            updated_at=data.get(
                "updated_at", datetime.datetime.now().isoformat()
            ),
        )
