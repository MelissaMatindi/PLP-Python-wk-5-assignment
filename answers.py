# This program demonstrates core principles of Object-Oriented Programming (OOP)
# in Python, including class creation, attributes, methods, inheritance,
# and polymorphism.

# --- Assignment 1: Designing a Base Class and Inheritance ---

class Superhero:
    """
    A base class representing a generic superhero.

    It includes a constructor to initialize attributes and a method
    to display a hero's basic information.
    """
    def __init__(self, name, secret_identity, power, weakness):
        """
        The constructor method to initialize a new Superhero object.

        Args:
            name (str): The name of the superhero.
            secret_identity (str): The hero's civilian identity.
            power (str): The primary superpower.
            weakness (str): The hero's weakness.
        """
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.weakness = weakness
        print(f"{self.name} has been created!")

    def display_info(self):
        """
        A method to print a summary of the superhero's information.
        """
        print(f"\n--- {self.name} ---")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Primary Power: {self.power}")
        print(f"Weakness: {self.weakness}")

    def move(self):
        """
        A generic move method for the base class.
        This will be overridden by child classes to demonstrate polymorphism.
        """
        raise NotImplementedError(
            "The 'move' method must be implemented by subclasses."
        )

# --- Creating Child Classes (Inheritance) ---

class FlyingHero(Superhero):
    """
    A specialized class for a superhero who can fly.
    This class inherits all attributes and methods from the Superhero class.
    """
    def __init__(self, name, secret_identity, power, weakness, flight_speed):
        """
        Constructor for the FlyingHero. Calls the parent class constructor
        and adds a unique attribute: flight_speed.
        """
        super().__init__(name, secret_identity, power, weakness)
        self.flight_speed = flight_speed

    def move(self):
        """
        Overrides the generic move() method to specify the hero's movement.
        This is a key part of demonstrating polymorphism.
        """
        print(f"{self.name} is soaring through the sky at {self.flight_speed} mph!")


class Speedster(Superhero):
    """
    A specialized class for a superhero with super speed.
    This class inherits from the Superhero class.
    """
    def __init__(self, name, secret_identity, power, weakness, top_speed):
        """
        Constructor for the Speedster. Calls the parent class constructor
        and adds a unique attribute: top_speed.
        """
        super().__init__(name, secret_identity, power, weakness)
        self.top_speed = top_speed

    def move(self):
        """
        Overrides the generic move() method to specify this hero's movement.
        """
        print(f"{self.name} is running faster than the speed of sound!")


# --- Assignment 2: Polymorphism Challenge ---

def demonstrate_polymorphism(heroes):
    """
    A function that demonstrates polymorphism by iterating through a list
    of different hero objects and calling their shared 'move' method.
    """
    print("\n--- Polymorphism in Action! ---")
    for hero in heroes:
        # The same method call, hero.move(), behaves differently
        # depending on the type of object it is.
        hero.move()


if __name__ == "__main__":
    # Create instances of the specialized hero classes
    superman = FlyingHero(
        name="Superman",
        secret_identity="Clark Kent",
        power="Flight, Super Strength",
        weakness="Kryptonite",
        flight_speed=2000
    )

    the_flash = Speedster(
        name="The Flash",
        secret_identity="Barry Allen",
        power="Super Speed",
        weakness="Intangibility",
        top_speed=767  # speed of sound in mph
    )

    # Display information for each hero
    superman.display_info()
    the_flash.display_info()

    # Create a list of the hero objects
    team_of_heroes = [superman, the_flash]

    # Call the function to demonstrate polymorphism
    demonstrate_polymorphism(team_of_heroes)
