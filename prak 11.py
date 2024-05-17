class Person:
    def __init__(self, first_name, last_name, title, nim):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.nim = nim

    def get_full_name(self):
        return f"Full name: {self.title} {self.first_name} {self.last_name} {self.nim}"

# Example usage
person = Person(first_name="Calista", last_name="Azzahra", title="Ms.", nim="064002300008")
print(person.get_full_name())
