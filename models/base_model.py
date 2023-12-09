#!/usr/bin/python3
"""Main class that serves as base for other models"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializing the class BaseModel
        """
        if kwargs.keys():
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != __class__:
                        self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Should Print:[<class name>]
       (<self.id>)
       <self.__dict__>
       """
        classname = type(self).__name__
        return f"[{classname}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns all keys/values of __dict__ of the instance"""
        key_dict = self.__dict__.copy()

        key_dict['__class__'] = type(self).__name__
        key_dict['created_at'] = self.created_at.isoformat()
        key_dict['updated_at'] = self.updated_at.isoformat()

        return key_dict
