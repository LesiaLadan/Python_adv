from typing import Iterable, Union, Any


def my_len(my_object) -> int:
    """Custom lenght function"""
    if hasattr(my_object, "__len__"):
        return my_object.__len__()
    elif isinstance(my_object, int):
        return len(str(abs(my_object)))
    elif isinstance(my_object, float):
        return len(str(abs(my_object)).replace(".", ""))
    elif hasattr(my_object, "__iter__"):
        counter = 0
        for i in my_object:
            counter += 1
        return counter
    else:
        raise TypeError("Object isnt supported my_len()")


def my_sum(my_object: Any) -> Union[float, int]:
    """Custom sum function"""
    if hasattr(my_object, "__sum__"):
        return my_object.__sum__()
    if hasattr(my_object, "__iter__"):
        total = 0
        for item in my_object:
            total += item
    elif hasattr(my_object, "__getitem__"):
        total = 0
        ind = 0
        try:
            while True:
                total += my_object[ind]
                ind += 1
        except IndexError:
            return total
    else:
        raise TypeError("Object isnt supported my_sum()")
    return total


def my_min(my_object: Iterable[Any]) -> Any:
    """Custom min function"""
    if hasattr(my_object, "__iter__") or hasattr(my_object, "__getitem__"):
        sorted_obj = sorted(my_object)
        return sorted_obj[0]
    else:
        raise TypeError("bject isnt supported my_min()")


if __name__ == "__main__":
    assert my_len([1, 2, 3]) == 3
    assert my_len((1, 2, 3, 4)) == 4
    assert my_len("hello") == 5
    assert my_len(12345) == 5
    assert my_len(-98) == 2
    assert my_len(12.347890) == 7
    assert my_len([]) == 0
    assert my_len("") == 0
    assert my_len(()) == 0
    assert my_len(0) == 1
    assert my_len(-1234) == 4
    assert my_len(0.0) == 2
    gen = (x for x in range(4))
    assert my_len(gen) == 4

    assert my_sum([1, 2, 3]) == 6
    assert my_sum((10, 20, 30)) == 60
    assert my_sum(range(5)) == 10
    assert my_sum([5]) == 5
    assert my_sum([]) == 0
    assert my_sum([7]) == 7
    assert my_sum([-1, -2, -3]) == -6
    assert my_sum([1, -2, 3, -4]) == -2
    gen = (x for x in range(5))
    assert my_sum(gen) == 10

    assert my_min([5, 2, 8, 1]) == 1
    assert my_min((10, 3, 7)) == 3
    assert my_min(range(5)) == 0
    assert my_min("python z-z-z") == " "
    assert my_min([42]) == 42
    assert my_min([-5, -10, -3]) == -10
    assert my_min([3, 3, 3]) == 3
    assert my_min("banana") == "a"
    assert my_min(range(-5, 5)) == -5

    print("Tests passed")
