#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    student = Student("John", "Doe", 23)
    print(student.to_json())  
    
    
    new_data = {"first_name": "Jane", "last_name": "Smith", "age": 30}
    student.reload_from_json(new_data)
    print(student.to_json())  
