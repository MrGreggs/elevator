# elevator
A program that imitates the function of an elevator.


This repository contains a Python program simulating the functionality of an elevator system within a building. The program is designed to showcase a basic elevator algorithm that efficiently transports passengers between floors while considering their destination and the elevator's capacity.

Program Components:
elevator.py: This module contains the classes Floor, Building, and Elevator, which together simulate the elevator system.
main.py: This script initializes the building, defines the number of floors, elevator capacity, and the initial queue of people waiting on each floor. It then executes the elevator simulation using the defined parameters.
Usage:
Clone the repository to your local machine.
Ensure you have Python installed (the program was developed using Python 3.x).
Open a terminal or command prompt and navigate to the directory containing the cloned repository.
Run the main.py script using the command python main.py.
Follow the prompts to input the number of floors, elevator capacity, and the destination floors for people waiting on each floor. Alternatively, you can modify the peopleArray variable directly in the main.py file to define the queues of people.
Observe the simulation output, which displays the current floor, elevator direction, the queue of people on the current floor, and the status of the elevator (people inside and their destinations).
Program Logic:
The elevator algorithm follows a basic logic:
The elevator moves in a single direction until there are no more people waiting in that direction.
It stops at each floor to pick up or drop off passengers based on their destination and the direction of the elevator.
The elevator changes direction when there are no more passengers waiting in its current direction of travel.
The simulation continues until all passengers have reached their destinations.
Customization:
Users can adjust the number of floors and elevator capacity by modifying the respective variables in the main.py script.
The initial queues of people waiting on each floor can be defined by modifying the peopleArray variable in the main.py script.
Notes:
The program includes an optional pause feature (PAUSE variable) to control the speed of the simulation. Set it to True to enable pauses between steps, or False to run the simulation without pauses.
Input validation is not included in the simulation. Users should ensure that inputs for the number of floors, elevator capacity, and destination floors are valid integers and within the appropriate ranges.
Author:
This program was written by [Your Name] and [Co-author's Name] as a demonstration of basic elevator simulation in Python.

License:
This project is licensed under the MIT License - see the LICENSE file for details
