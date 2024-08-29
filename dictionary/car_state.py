from enum import Enum


class CarState(Enum):
    AVAILABLE = "Available"
    BOOKED = "Booked"
    RENTED = "Rented"
    MAINTENANCE = "Maintenance"


class CarAction(Enum):
    BOOK_CAR = "Car Booked"
    PICK_UP_CAR = "Car Picked Up"
    RETURN_CAR = "Car Returned"
    MAINTENANCE_REQUIRED = "Maintenance Required"
    COMPLETE_MAINTENANCE = "Maintenance Completed"
    CANCEL_BOOKING = "Cancel Booking"


class CarStateMachine:
    transitions = {
        CarState.AVAILABLE: {
            CarAction.BOOK_CAR: CarState.BOOKED,
        },
        CarState.BOOKED: {
            CarAction.PICK_UP_CAR: CarState.RENTED,
            CarAction.CANCEL_BOOKING: CarState.AVAILABLE,
        },
        CarState.RENTED: {
            CarAction.RETURN_CAR: CarState.AVAILABLE,
            CarAction.MAINTENANCE_REQUIRED: CarState.MAINTENANCE,
        },
        CarState.MAINTENANCE: {
            CarAction.COMPLETE_MAINTENANCE: CarState.AVAILABLE,
        },
    }

    def __init__(self, initial_state):
        self.state = initial_state

    def perform_action(self, action):
        if action in self.transitions[self.state]:
            self.state = self.transitions[self.state][action]
        else:
            raise ValueError(f"Action {action} cannot be performed from state {self.state}")

    def get_possible_actions(self):
        return list(self.transitions[self.state].keys())


# Example usage
car = CarStateMachine(CarState.AVAILABLE)
print("Initial State:", car.state)

possible_actions = car.get_possible_actions()
print("Possible Actions:", [action.value for action in possible_actions])

car.perform_action(CarAction.BOOK_CAR)
print("State after booking:", car.state)

car.perform_action(CarAction.PICK_UP_CAR)
print("State after picking up:", car.state)

car.perform_action(CarAction.RETURN_CAR)
print("State after returning:", car.state)
