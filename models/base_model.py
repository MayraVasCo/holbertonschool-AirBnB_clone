#!/usr/bin/python3

import uuid
import models
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())  # Generate a unique identifier
            self.created_at = datetime.now()  # Set the creation time
            self.updated_at = datetime.now()  # Set the update time
            models.storage.new(self)

    def __str__(self):
        # Return a string representation of the object
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        # Update the 'updated_at' attribute with the current datetime
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        # Return a dictionary containing all keys/values of __dict__ of the instance
        instance_dict = self.__dict__.copy()

        # Convert 'created_at' and 'updated_at' to string objects in ISO format
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        # Add a key '__class__' to the dictionary with the class name of the object
        instance_dict['__class__'] = self.__class__.__name__

        return instance_dict
