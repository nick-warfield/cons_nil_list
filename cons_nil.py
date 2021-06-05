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

    def append(self, value: int):
        pass

    def insert(self, value: int, index: int):
        pass

    def pop(self) -> int:
        pass

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
