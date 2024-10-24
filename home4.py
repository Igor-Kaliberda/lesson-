def hello(name: str, age: int) -> str:
    if not isinstance(name, str):
        raise ValueError("Name must be a string")

    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer")

    return f"Hi. My name is {name} and I am {age} years old."



print(hello("Stiv", 30))
print(hello("Hella", 25))