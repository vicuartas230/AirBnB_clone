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



#### Mode no-interactive
**`help`**
`echo "help" | ./console.py`
> (hbnb) 
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
