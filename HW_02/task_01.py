def my_sum():
    """Just print some text about the func"""
    print("This is my custom sum function!")


if __name__ == "__main__":
    my_list = [1, 3, 3]
    print(sum(my_list))
    sum = my_sum
    sum()
