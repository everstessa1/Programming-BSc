# object oriented programming voila

class Dog:
    species = "cannis"

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        return f"{self.name} of the dog and the {self.age}" #print('hello')s1

# This works when doing the following code in the terminal
    # https://youtu.be/JeznW_7DlB0
    # from dog import Dog
    # st = Dog("dh",2)
    # print(st.display())