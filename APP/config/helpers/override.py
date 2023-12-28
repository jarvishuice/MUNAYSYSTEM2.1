class override:
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        if self.method.__name__ not in dir(owner.__base__):
            raise NameError(f"El método {self.method.__name__} no está en la clase base")
        return self.method.__get__(instance, owner)