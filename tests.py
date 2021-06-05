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
