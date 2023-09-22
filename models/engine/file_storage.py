#!/usr/bin/python3
"""
    json type stroage
    This module defines a class to manage file storage for hbnb clone
"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            cdict = {}
            for k, v in FileStorage.__objects.items():
                if k.startswith(cls.__name__):
                    cdict[k] = v
            return cdict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        s = {}
        for k, v in self.__objects.items():
            s[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(s, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''delete objects'''
        if obj:
            try:
                ob = f"{obj.__class__.__name__}.{obj.__dict__['id']}"
                del FileStorage.__objects[ob]
                self.save()
            except Exception as e:
                pass

    def close(self):
        "restart storage"
        self.reload()
