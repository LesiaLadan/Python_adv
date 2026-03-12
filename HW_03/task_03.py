class Person:
    def __init__(self, name: str, age: int) -> None:
        """"Initialize a person with parametrs:\n
        - name\n
        - age
        """
        self.name = name
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """Compare persons by age - less than"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __gt__(self, other: "Person") -> bool:
        """Compare persons by age - greater than"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age

    def __eq__(self, other) -> bool:
        """Compare persons by age"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

    def __repr__(self) -> str:
        """Return a string-representation of a Person"""
        return f"Person(name='{self.name}', age={self.age})"


if __name__ == "__main__":

    u1 = Person("Anna", 20)
    u2 = Person("Ivan", 30)

    print(u1 < u2)
    print(u1 > u2)
    print(u1 == u2)

    u3 = Person("Anton", 26)
    u4 = Person("Ira", 27)
    u5 = Person("Olha", 31)

    l1 = [u1, u2, u3, u4, u5]

    def sorting(persons: list[Person]):
        return sorted(persons, key=lambda person: person.age)

    print(sorting(l1))
