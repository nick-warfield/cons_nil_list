import typing

class ConsNilList:
    pass

class Cons(ConsNilList):
    def __init__(self, value: int, next: ConsNilList):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Cons(' + str(self.value) + ', ' + str(self.next) + ')'
    
    def __len__(self) -> int:
        return 1 + len(self.next)

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.next == other.next

    def append(self, value: int) -> ConsNilList:
        return Cons(self.value, self.next.append(value))

    def insert(self, value: int, index: int) -> ConsNilList:
        if index != 0:
            return Cons(self.value, self.next.insert(value, index - 1))
        else:
            return Cons(value, self)

    def pop(self) -> ConsNilList:
        return self.next

    def remove(self, index: int) -> int:
        pass

    def count(self, value: int) -> int:
        pass

    def reverse(self) -> ConsNilList:
        pass

    def sort(self) -> ConsNilList:
        pass

class Nil(ConsNilList):
    def __str__(self) -> str:
        return 'Nil'

    def __len__(self) -> int:
        return 0

    def __eq__(self, other) -> bool:
        return type(self) == type(other)

    def append(self, value) -> ConsNilList:
        return Cons(value, Nil())

    def insert(self, value: int, index: int) -> ConsNilList:
        return Cons(value, self)

    def pop(self) -> ConsNilList:
        return Nil()
