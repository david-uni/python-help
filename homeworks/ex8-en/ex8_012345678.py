''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
class Minibar:
    def __init__(self, drinks, snacks):
        pass

    def __repr__(self):
        pass

    def eat_a_snack(self, snack):
        pass

    def drink_a_drink(self, drink):
        pass

#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        pass # replace this with your implementation
    
    def __repr__(self):
        pass # replace this with your implementation

    def is_occupied(self):
        pass # replace this with your implementation

    def clean(self):
        pass # replace this with your implementation

    def better_than(self, other):
        pass # replace this with your implementation

    def check_in(self, guests):
        pass # replace this with your implementation

    def check_out(self):
        pass # replace this with your implementation
    
    def move_to(self, other):
        pass # replace this with your implementation
   
#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        pass # replace this with your implementation
            
    def __repr__(self):
        pass # replace this with your implementation
                      
    def check_in(self, guests, rank):
        pass # replace this with your implementation

    def check_out(self, guest):
        pass # replace this with your implementation

    def upgrade(self, guest):
        pass # replace this with your implementation

#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
    rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
             Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
    h = Hotel("Dan",rooms)
    test_sep = '\n------------------'
    print('PRINT h:\n', h, test_sep, sep="")
    print(m)
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,  sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    ##test_hotel() ## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the 
    pass