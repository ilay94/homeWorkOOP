class MixinInitPrint:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({','.join((f'{value}' for value in self.__dict__.values()))})"
