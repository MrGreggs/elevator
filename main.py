import copy

import elevator

# while True:
#     n = int(input("Enter number of floors in total (must be > 2): "))
#     if n <= 2:
#         print("Number of floors must be greater than 2. Please try again.")
#     else:
#         break
#
# while True:
#     elevatorCapacity = int(input("Enter elevator capacity (must be > 0): "))
#     if elevatorCapacity <= 0:
#         print("Elevator capacity must be greater than 0. Please try again.")
#     else:
#         break
#
# peopleArray = [[] for _ in range(n)]
#
# # manually create floors and people
# for i in range(n):
#     print(f"For floor {i}:")
#     num_people = int(input("Enter the number of people for this floor: "))
#     for j in range(num_people):
#         while True:
#             destination_floor = int(input(f"Enter the destination floor for person {j + 1}: "))
#             if 0 <= destination_floor < n and destination_floor != i:
#                 break
#             print("Invalid destination floor. Please enter a valid floor within range and different from the current floor.")
#         peopleArray[i].append(destination_floor)
#
# print("People array:", peopleArray)


# set values of floors, capacity and queues' order inside main function
n = 9
elevatorCapacity = 5
peopleArray = [[1, 1, 4, 8],
               [3, 7, 0],
               [5, 4, 6],
               [1, 8, 5],
               [2, 1, 7],
               [3, 1, 1],
               [0, 8],
               [5, 2],
               [7, 4]]

# create building and populate it with people
building = elevator.Building(elevatorCapacity, n)
for i in range(len(peopleArray)):
    building.floors[i].createFloorQueue(peopleArray[i])
# use elevator
building.basicElevatorFunction()

