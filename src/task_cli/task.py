import datetime
import uuid

class Task:
    def __init__(self, description: str, id=None, status='to-do', created_at=None, updated_at=None):
        self.__id = id if id is not None else 0
        self.__description = description
        self.__status = status
        self.__created_at = created_at if created_at else datetime.datetime.now().isoformat()
        self.__updated_at = updated_at if updated_at else datetime.datetime.now().isoformat()
        
    def get_description(self):
        return self.__description()
    
    def get_status(self):
        return self.__status()
    
    def get_created_at(self):
        return self.__created_at()
    
    def get_id(self):
        return self.__id
    
    def set_description(self, description: str):
        """
        update task description
        """
        self.__description = description
        self.__updated_at = datetime.datetime.now()
        
    def set_status(self, status: str):
        """
        update task status
        """
        self.__description = status
        self.__updated_at = datetime.datetime.now()

    def to_dict(self):
        return {
            'id': str(self.__id),
            'description': self.__description,
            'status': self.__status,
            'created_at': self.__created_at,
            'updated_at': self.__updated_at
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data.get('description', ''),
            id=data.get('id', 0),
            status=data.get('status', 'to-do'),
            created_at=data.get('created_at', datetime.datetime.now().isoformat()),
            updated_at=data.get('updated_at', datetime.datetime.now().isoformat())
        )