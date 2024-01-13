The following project is for the ALX AirBnB clone-the console project, which is the first of the many AirBnB projects series, inside it contains the following python classes and script with their unit tests:

* A class BaseModel that defines all common attributes/methods for other classes
* A re-createtion an instance with this dictionary representation
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

* A recreattion of  a BaseModel from another one by using a dictionary representation
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

* A program called console.py that contains the entry point of the command interpreter
* Updated command interpreter (console.py) to have these commands:

        -> create
        -> show
        -> destroy
        -> all
        -> update

* A class User that inherits from BaseMode, with public attributes:
        -> email
        -> password
        -> first_name
        -> last_name

* All the classes that inherit from BaseModel:
        -> State
        -> City
        -> Amenity
        -> Place
        -> Review
*     1. Updated fileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and         Review
      2. Updated your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes 
         created previously

* Updated command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all()
* Updated command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count()
* Updated command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>)
* Updated command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>)
* Updated command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>)
* Updated command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>)
* All unittests for console.py, all features!


















 
