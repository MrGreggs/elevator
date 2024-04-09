import queue
import time
PAUSE = True


class Floor:
	def __init__(self, id):
		# queue of people waiting
		self.queue = queue.Queue()
		self.ID = id

	# create the queue of the floor based on an array input
	# each "person" is a number that indicates the floor-destination
	def createFloorQueue(self, peopleArray):
		for person in peopleArray:
			self.queue.put(person)

	# dequeue people from the floor that are eligible to onboard the elevator
	def dequeue(self, currentFloor, elevator):
		# create a temporary queue that helps maintain the correct order of the queue
		temp_queue = queue.Queue()
		# iterate through all the people in the queue
		while not self.queue.empty():
			# remove person from initial queue
			person = self.queue.get()
			if ((person - currentFloor > 0 and elevator.direction == 1) or
					(person - currentFloor < 0 and elevator.direction == -1)):
				# if person and elevator have the same direction
				if elevator.currentCapacity > 0:
					# if the elevator is not full
					elevator.addPersonToElevator(person)
				else:
					# else put him in the temporary queue
					temp_queue.put(person)
			else:
				# if the person has different direction, put him in the temporary queue
				temp_queue.put(person)
		self.queue = temp_queue
		elevator.people.sort()


class Building:
	# construct a building with a certain number of empty floors from user input
	def __init__(self, elevatorCapacity, floors):
		self.floors = [Floor(i) for i in range(floors)]
		self.elevator = Elevator(elevatorCapacity, floors)

	# check all floors' queues in order to end the program if they are all empty
	def checkAllFloors(self):
		# check if there are people waiting on any floor
		for floor in self.floors:
			if not floor.queue.empty():
				return False
		# check if there are people in the elevator
		if self.elevator.people:
			return False
		# if both conditions are false, return True
		print("All people have reached their destination, elevator returns to ground-floor")
		self.elevator.currentFloor = 0
		return True

	def basicElevatorFunction(self):
		# while there are people who have not reached their destination, keep going
		while not self.checkAllFloors():
			print(f"FLOOR: {self.elevator.currentFloor}")
			currentFloor = self.elevator.currentFloor
			if self.elevator.direction == 1:
				print(f"Direction: UP")
			else:
				print(f"Direction: DOWN")
			if self.elevator.direction == 1:
				print(f'At first: {self.elevator.people} on floor {self.elevator.currentFloor}')
			else:
				print(f'At first: {list(reversed(self.elevator.people))} on floor {self.elevator.currentFloor}')
			print(f"Queue of floor {self.elevator.currentFloor}:")
			for person in self.floors[self.elevator.currentFloor].queue.queue:
				print(f"Person {person} - Destination: Floor {person}")
			if self.floors[self.elevator.currentFloor].queue.empty():
				print("empty queue")
			# remove people from elevator who have reached their destination
			# and onboard people from the floor's queue with the same direction as the elevator
			self.elevator.removePeople()
			self.floors[currentFloor].dequeue(currentFloor, self.elevator)

			# check if there are people inside the elevator with the same direction as the elevator
			if self.elevator.direction == 1:  # upwards
				nextFloorFromInside = self.elevator.floors - 1
				nextFloorFromOutside = self.elevator.floors - 1
				for person in self.elevator.people:
					if person > currentFloor:
						nextFloorFromInside = min(person, nextFloorFromInside)
				# check higher floors for people who want to go higher
				for floor in self.floors:
					for person in floor.queue.queue:
						if person > currentFloor and floor.ID > self.elevator.currentFloor:
							floorOfPerson = floor.ID
							nextFloorFromOutside = min(floorOfPerson, nextFloorFromOutside)
				# go to the nearest floor that either has a person who wants to go higher
				# or is a destination from at least one of the people inside the elevator
				if min(nextFloorFromInside, nextFloorFromOutside) > self.elevator.currentFloor:
					self.elevator.currentFloor = min(nextFloorFromInside, nextFloorFromOutside)
				else:
					# if there are no people who have the same direction as the elevator
					# change elevator's direction
					self.elevator.direction = -1
			elif self.elevator.direction == -1:  # downwards
				nextFloorFromInside = 0
				nextFloorFromOutside = 0
				for person in self.elevator.people:
					if person < currentFloor:
						nextFloorFromInside = max(person, nextFloorFromInside)
				# check lower floors for people who want to go lower
				for floor in self.floors:
					for person in floor.queue.queue:
						if person < currentFloor and floor.ID < self.elevator.currentFloor:
							floorOfPerson = floor.ID
							nextFloorFromOutside = max(floorOfPerson, nextFloorFromOutside)
				# go to the nearest floor that either has a person who wants to go lower
				# or is a destination from at least one of the people inside the elevator
				if max(nextFloorFromInside, nextFloorFromOutside) < self.elevator.currentFloor:
					self.elevator.currentFloor = max(nextFloorFromInside, nextFloorFromOutside)
				else:
					# if there are no people who have the same direction as the elevator
					# change elevator's direction
					self.elevator.direction = 1
			if self.elevator.direction == 1:
				print(f'Finally: {self.elevator.people} heading on floor {self.elevator.currentFloor}')
			else:
				print(f'Finally: {list(reversed(self.elevator.people))} heading on floor {self.elevator.currentFloor}')
			print("********************************")
			if PAUSE:
				time.sleep(1)


class Elevator:
	def __init__(self, elevatorCapacity, floors):
		# elevator is described by: the floor it currently is, its currentCapacity,
		# the direction (upwards == 1, downwards == -1) and an array of people-numbers
		# that indicate the floor-destination
		self.floors = floors
		self.maxCapacity = elevatorCapacity
		self.currentCapacity = elevatorCapacity
		self.currentFloor = 0
		self.direction = 1
		self.people = []

	# add people to the elevator
	def addPersonToElevator(self, person):
		self.people.append(person)
		self.currentCapacity -= 1

	# remove people from the elevator that have reached their destination
	def removePeople(self):
		# create a copy of the people list to iterate over
		people_to_remove = self.people[:]
		# iterate over the copy and remove people who have reached their destination
		for person in people_to_remove:
			if self.currentFloor == person:
				self.people.remove(person)
				self.currentCapacity = self.maxCapacity - len(self.people)
