import unittest

def add_list_element(my_list, element):
    """Appends specified element to specified list,
IF the element is a string that contains only characters, and can not be
empty, have all the characters be spaces, contain any numbers or be already in the list. """

    if not element or element.isspace():
        print("You have not entered anything!")

    elif any(num in element for num in "0123456789"):
        print("No numbers can be included in the name.")

    elif element.capitalize() not in my_list:
        my_list.append(element.capitalize())
        print(f"Your choice: {element.capitalize()} was successfully added!")

    else:
        print("Already on the list. Try a different option.")
    return my_list


# def my_list():
#     # Arrange
#     element = 'Victor'
#     list_name = []
#     expected = list_name + [element]

#     # act
#     actual = add_list_element(list_name, element)

#     #Assert

#     assert expected == actual

# my_list()


