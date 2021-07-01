# The console_AirBnB clone (#hbnb$ ) 
## Description - 0x00. AirBnB clone - The console :spiral_notepad:
This is first project about clone the AirBnB. In this occasion, creates a one console that permissions manage objects via command interpreter. That is, create a data model with the data that are introduced for command interpreter or console, what is the present project.
Each data introduces is allocated or store in one powerful system of storage: JSON file.

> We create a connection between the objects that are created by the command line and their storage and persistence of data in a JSON file!! :cool:

### Organization of the files :open_file_folder:
In this repository your find multiple files that permissive interactive with the instances/objects, hence:

* are have one file that created a class base (called [base_model.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/base_model.py)) from it all the classes that are used in AirBnB will be created (they inherit from that class): [user.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/user.py), [state.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/state.py), [review.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/review.py), [place.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/place.py), [city.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/city.py) and [amenity.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/amenity.py)

* file of the storage: [file_storage.py](https://github.com/dianaparr/AirBnB_clone/blob/main/models/engine/file_storage.py)

> All project works with a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
## Console usage :memo:
Our console works by means of commands entered in the console (hbnb ). This is a step-by-step guide on how to use this console:
1. Clone this repository on your local machine: `https://github.com/dianaparr/AirBnB_clone.git`
2. Run file [console.py](https://github.com/dianaparr/AirBnB_clone/blob/main/console.py), as well: `python3 console.py` or if the file has execute permissions, do it like this `./console.py`
3. If this promp appears `(hbnb )`, it is because you are already inside the console!

### Run console :fire:
To start using the console, you must take into account that you will handle instances of the different classes of this clone (explained above), for that, take into account the following commands:
##### Commands :computer:

|**Name**|**Description**|
|--------|--------|
| `help` |shows the different console commands|
| `EOF` and `quit` |exit the console|
| `all` |prints all string representation of all instances based or not on the class name|
| `show` |prints the string representation of an instance based on the class name and `id`|
| `create` |creates a new instance|
| `update` |updates an instance based on the class name and `id` by adding or updating attribute|
| `destroy` |deletes an instance based on the class name and `id`|

### Examples of usage :100:
This is how the commands are used:
#### Mode interactive
**`create`**

> (hbnb) create User
> d4d0e872-8bb3-4c0f-842d-e34b660135d0
> (hbnb) 

**`all`**

> (hbnb) all
> ["[User] (d4d0e872-8bb3-4c0f-842d-e34b660135d0) {'id': 'd4d0e872-8bb3-4c0f-842d-e34b660135d0', 'created_at': datetime.datetime(2021, 6, 30, 23, 41, 40, 495400), 'updated_at': datetime.datetime(2021, 6, 30, 23, 41, 40, 495460)}", "[City] (063f1704-164a-4738-bf67-9787c55738ea) {'id': '063f1704-164a-4738-bf67-9787c55738ea', 'created_at': datetime.datetime(2021, 6, 30, 23, 45, 16, 633744), 'updated_at': datetime.datetime(2021, 6, 30, 23, 45, 16, 633781)}", "[Place] (4749ca95-7594-42bb-9f94-87c52dec48fb) {'id': '4749ca95-7594-42bb-9f94-87c52dec48fb', 'created_at': datetime.datetime(2021, 6, 30, 23, 45, 22, 109526), 'updated_at': datetime.datetime(2021, 6, 30, 23, 45, 22, 109593)}"]
> (hbnb) 

*Note*: This command works by itself and displays all instances that have been created in the different classes. On the contrary, `show`, shows an instance of a specific class with its corresponding id.

**`update` and `show`**

> (hbnb) update Place 4749ca95-7594-42bb-9f94-87c52dec48fb number_rooms 5
> (hbnb) show Place 4749ca95-7594-42bb-9f94-87c52dec48fb
> [Place] (4749ca95-7594-42bb-9f94-87c52dec48fb) {'id': '4749ca95-7594-42bb-9f94-87c52dec48fb', 'created_at': datetime.datetime(2021, 6, 30, 23, 45, 22, 109526), 'updated_at': datetime.datetime(2021, 6, 30, 23, 45, 22, 109593), 'number_rooms': '5'}
> (hbnb) 

**`destroy`**

> (hbnb) destroy Place 4749ca95-7594-42bb-9f94-87c52dec48fb
> (hbnb) all
> ["[User] (d4d0e872-8bb3-4c0f-842d-e34b660135d0) {'id': 'd4d0e872-8bb3-4c0f-842d-e34b660135d0', 'created_at': datetime.datetime(2021, 6, 30, 23, 41, 40, 495400), 'updated_at': datetime.datetime(2021, 6, 30, 23, 41, 40, 495460)}", "[City] (063f1704-164a-4738-bf67-9787c55738ea) {'id': '063f1704-164a-4738-bf67-9787c55738ea', 'created_at': datetime.datetime(2021, 6, 30, 23, 45, 16, 633744), 'updated_at': datetime.datetime(2021, 6, 30, 23, 45, 16, 633781)}"]
> (hbnb) 

As you can see, what is shown is a string representation of the instance and a dictionary with the attributes of that instance (all the methods in the base_model.py file). The file that stores ("file.json"), is a JSON string representation in a dictionary.

#### Mode no-interactive
**`help`**

> (hbnb) `echo "help" | ./console.py`
> Documented commands (type help <topic>):
> ========================================
> EOF  all  create  destroy  help  quit  show  update
> (hbnb) %


## Run tests :checkered_flag: 

Tests should be executed by using this command:

     python3 -m unittest discover tests


## Authors :registered:
:woman_technologist: **Diana Parra**
* [GitHub](https://github.com/dianaparr)
* [Twitter](https://twitter.com/dianaparra017)

:man_technologist: **Victor Cuartas**
* [GitHub](https://github.com/vicuartas230)
* [Twitter](https://twitter.com/vicuartas230)

:man_technologist: **Alexander Rodríguez**
* [GitHub]()
* [Twitter]()
