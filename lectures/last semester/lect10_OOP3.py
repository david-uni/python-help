import datetime


def get_current_year():
    return datetime.datetime.now().year


class Dog:
    def __init__(self, name, birth_year, color):
        self.name, self.birth_year, self.color = name, birth_year, color
        self.playmates = []

    def make_noise(self):
        return "woof! woof!"

    def play_with(self, other):
        if other not in self.playmates:
            self.playmates.append(other)

    def stop_play(self, other):
        if other in self.playmates:
            self.playmates.remove(other)

    def __repr__(self):
        age = get_current_year() - self.birth_year
        result = f"name: {self.name}\nage: {age}\ncolor: {self.color}\n"
        result += "plays with: [\n"
        for playmate in self.playmates:
            result += f"\t {playmate.name}\n"
        result += "]"
        return result


class Shiba:
    def __init__(self, name, birth_year):
        self.name, self.birth_year = name, birth_year
        self.color = "golden"
        self.is_tail_wagging = False
        self.playmates = []

    def make_noise(self):
        return "woof! woof!"

    def wag_tail(self):
        self.is_tail_wagging = True

    def play_with(self, other):
        if other not in self.playmates:
            self.playmates.append(other)

    def stop_play(self, other):
        if other in self.playmates:
            self.playmates.remove(other)

    def __repr__(self):
        age = get_current_year() - self.birth_year
        result = f"name: {self.name}\nage: {age}\ncolor: {self.color}\n"
        result += "plays with: [\n"
        for playmate in self.playmates:
            result += f"\t {playmate.name}\n"
        result += "]"
        if self.is_tail_wagging:
            result += f"\n{self.name} is wagging its tail"
        return result


# encapsulation
class Shiba:
    def __init__(self, name, birth_year):
        self.dog = Dog(name, birth_year, "golden")
        self.is_tail_wagging = False

    def make_noise(self):
        return self.dog.make_noise()

    def wag_tail(self):
        self.is_tail_wagging = True

    def play_with(self, other):
        self.dog.play_with(other)

    def stop_play(self, other):
        self.dog.stop_play(other)

    def __repr__(self):
        result = str(self.dog)
        if self.is_tail_wagging:
            result += f"\n{self.name} is wagging its tail"
        return result


# inheritance
class Shiba(Dog):
    def __init__(self, name, birth_year):
        super().__init__(name, birth_year, "golden")
        self.is_tail_wagging = False

    def wag_tail(self):
        self.is_tail_wagging = True

    def __repr__(self):
        result = super().__repr__()
        if self.is_tail_wagging:
            result += f"\n{self.name} is wagging its tail"
        return result


class Cat:
    def __init__(self, name, birth_year, color):
        self.name, self.birth_year, self.color = name, birth_year, color
        self.playmates = []

    def make_noise(self):
        return "meow! meow!"

    def play_with(self, other):
        if other not in self.playmates and isinstance(other, Cat):
            self.playmates.append(other)

    def stop_play(self, other):
        if other in self.playmates:
            self.playmates.remove(other)

    def __repr__(self):
        age = get_current_year() - self.birth_year
        result = f"name: {self.name}\nage: {age}\ncolor: {self.color}\n"
        result += "plays with: [\n"
        for playmate in self.playmates:
            result += f"\t {playmate.name}\n"
        result += "]"
        return result


# Cats and Dogs inheritance
class Pet:
    def __init__(self, name, birth_year, color):
        self.name, self.birth_year, self.color = name, birth_year, color
        self.playmates = []

    def make_noise(self):
        raise NotImplementedError

    def play_with(self, other):
        if other not in self.playmates:
            self.playmates.append(other)

    def stop_play(self, other):
        if other in self.playmates:
            self.playmates.remove(other)

    def __repr__(self):
        age = get_current_year() - self.birth_year
        result = f"name: {self.name}\nage: {age}\ncolor: {self.color}\n"
        result += "plays with: [\n"
        for playmate in self.playmates:
            result += f"\t {playmate.name}\n"
        result += "]"
        return result


class Dog(Pet):
    def make_noise(self):
        return "woof! woof!"


class Cat(Pet):
    def make_noise(self):
        return "meow! meow!"

    def play_with(self, other):
        if other not in self.playmates and isinstance(other, Cat):
            self.playmates.append(other)


class Shiba(Dog):
    def __init__(self, name, birth_year):
        super().__init__(name, birth_year, "golden")
        self.is_tail_wagging = False

    def wag_tail(self):
        self.is_tail_wagging = True

    def __repr__(self):
        result = super().__repr__()
        if self.is_tail_wagging:
            result += f"\n{self.name} is wagging its tail"
        return result

doge = Dog("doge", 2000, "black")
shiba = Shiba("shib", 2003)
kitty = Cat("Simba", 2005, "white")