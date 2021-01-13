''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################


class Minibar:
    def __init__(self, drinks, snacks, bill=0.0):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = bill

    def __repr__(self):
        return f'The minibar contains the drinks: {list(self.drinks.keys())}\n' + \
            f'And the snacks: {list(self.snacks.keys())}\n' + \
            f'The bill for the minibar is: {self.bill}'

    def __charge_by_lowercase(self, items, item, typ='drink'):
        for itm in items:
            if item.lower() == itm.lower():
                self.bill += items.pop(itm)
                return
        raise ValueError(f'The {typ} is not in the minibar')

    def eat_a_snack(self, snack):
        self.__charge_by_lowercase(self.snacks, snack, 'snack')

    def drink_a_drink(self, drink):
        self.__charge_by_lowercase(self.drinks, drink, 'drink')


#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    # A subclass of Exception that defines a new error type
    # DO NOT change this class
    pass


class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.guests = [guest.lower() for guest in guests]
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = float(satisfaction)
        self.validate()

    def validate(self):
        if not (isinstance(self.clean_level, int) and isinstance(self.rank, int) and isinstance(self.satisfaction, (int, float))):
            raise TypeError()
        if not (0 < self.clean_level < 11 and 0 < self.rank < 4 and 1 <= self.satisfaction <= 5):
            raise ValueError()

    def __repr__(self):
        guests_repr = ', '.join(self.guests) or 'empty'
        return f'{self.minibar}\n' + \
            f'floor: {self.floor}\n' + \
            f'number: {self.number}\n' + \
            f'guests: {guests_repr}\n' + \
            f'clean_level: {self.clean_level}\n' + \
            f'rank: {self.rank}\n' + \
            f'satisfaction: {round(self.satisfaction, 1)}'

    def is_occupied(self):
        return bool(self.guests)

    def clean(self):
        self.clean_level = min(self.clean_level + self.rank, 10)

    def better_than(self, other):
        if not isinstance(other, Room):
            raise TypeError('Other must be an instance of Room')
        return (self.rank, self.floor, self.clean_level) > (other.rank, other.floor, other.clean_level)

    def check_in(self, guests):
        if self.guests:
            raise RoomError('Cannot check-in new guests to an occupied room')
        self.guests = [guest.lower() for guest in guests]
        self.satisfaction = 1.0
        return self

    def check_out(self):
        if not self.guests:
            raise RoomError('Cannot check-out an empty room')
        self.guests = []
        return self

    def move_to(self, other):
        if not self.guests:
            raise RoomError('Cannot move guests from an empty room')
        if other.guests:
            raise RoomError('Cannot move guests into an occupied room')

        other.guests = self.guests
        if other.better_than(self):
            other.satisfaction = min(self.satisfaction + 1.0, 5.0)
        else:
            other.satisfaction = self.satisfaction
        self.guests = []
        return other


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def __repr__(self):
        return f'{self.name} hotel has:\n' + f'{len(self.rooms)} rooms\n' + \
            f'{len(self.get_occupied_rooms())} occupied rooms'

    def get_empty_rooms(self):
        return [room for room in self.rooms if not room.is_occupied()]

    def get_occupied_rooms(self):
        return [room for room in self.rooms if room.is_occupied()]

    def get_guest_room(self, guest):
        for room in self.get_occupied_rooms():
            if guest.lower() in room.guests:
                return room

    def check_in(self, guests, rank):
        for room in self.get_empty_rooms():
            if room.rank == rank:
                return room.check_in(guests)

    def check_out(self, guest):
        room = self.get_guest_room(guest)
        if room != None:
            return room.check_out()

    def upgrade(self, guest):
        room = self.get_guest_room(guest)
        if room != None:
            for new_room in self.get_empty_rooms():
                if new_room.better_than(room):
                    return room.move_to(new_room)

#########################################
# Question 3 supplement - do not delete this comment
#########################################


def test_hotel():
    m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
    rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
             Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
    h = Hotel("Dan", rooms)
    test_sep = '\n------------------'
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n',
          h.check_out("Ronen"), test_sep,  sep="")
    print('CALL: h.check_out("Ronen")\n',
          h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(
        ["Alice", "Wonder"], 2), test_sep, sep="")
    print('CALL: h.check_in(["Alex"], 3)\n',
          h.check_in(["Alex"], 3), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 3)\n',
          h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 1)\n',
          h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    test_hotel()  # After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the
    pass
