from cons_nil import ConsNilList, Cons, Nil

def test_example():
    assert 1 == 1

def test_to_string():
    assert 'Nil' == str(Nil())
    assert 'Cons(1, Nil)' == str(Cons(1, Nil()))
    assert 'Cons(1, Cons(2, Nil))' == str(Cons(1, Cons(2, Nil())))

def test_length():
    assert 0 == len(Nil())
    assert 1 == len(Cons(1, Nil()))
    assert 2 == len(Cons(1, Cons(2, Nil())))

def test_equals():
    assert Nil() == Nil()
    assert Cons(1, Nil()) == Cons(1, Nil())
    assert Cons(1, Nil()) != Cons(2, Nil())
    assert Cons(1, Nil()) != Cons(1, Cons(2, Nil()))

def test_append():
    list = Nil()
    assert list == Nil()
    list = list.append(1)
    assert list == Cons(1, Nil())
    list = list.append(5)
    assert list == Cons(1, Cons(5, Nil()))
    list = list.append(-3)
    assert list == Cons(1, Cons(5, Cons(-3, Nil())))

def test_pop():
    list = Cons(1, Cons(2, Cons(7, Nil())))
    list = list.pop()
    assert list == Cons(2, Cons(7, Nil()))
    list = list.pop()
    assert list == Cons(7, Nil())
    list = list.pop()
    assert list == Nil()
    list = list.pop()
    assert list == Nil()

def test_insert():
    list = Nil()
    assert list.insert(1, 0) == Cons(1, Nil())
    assert list.insert(1, 1) == Cons(1, Nil())
    assert list.insert(1, 8) == Cons(1, Nil())

    list = list.insert(1, 0).insert(4, 0)
    assert list == Cons(4, Cons(1, Nil()))
    assert list.insert(7, 0) == Cons(7, Cons(4, Cons(1, Nil())))
    assert list.insert(7, 1) == Cons(4, Cons(7, Cons(1, Nil())))
    assert list.insert(7, 2) == Cons(4, Cons(1, Cons(7, Nil())))

def test_remove():
    list = Cons(1, Cons(2, Cons(7, Nil())))
    assert list.remove(0) == Cons(2, Cons(7, Nil()))
    assert list.remove(1) == Cons(1, Cons(7, Nil()))
    assert list.remove(2) == Cons(1, Cons(2, Nil()))
    assert list.remove(3) == Cons(1, Cons(2, Cons(7, Nil())))

def test_count():
    list = Cons(3, Cons(2, Cons(-1, Cons(3, Cons(3, Cons(-1, Cons(3, Nil())))))))
    assert list.count(7) == 0
    assert list.count(2) == 1
    assert list.count(3) == 4
    assert list.count(-1) == 2

def test_reverse():
    assert Nil().reverse() == Nil()
    list = Cons(1, Nil())
    assert list.reverse() == list
    list = Cons(1, Cons(2, Cons(3, Nil())))
    assert list.reverse() == Cons(3, Cons(2, Cons(1, Nil())))
