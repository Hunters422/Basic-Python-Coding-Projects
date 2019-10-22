
import os

for file in os.listdir("C:\\Users\\addie\\Desktop\\GitHub\\Python\\Basic Python Coding Projects\\"):
    if file.endswith(".txt"):
        print(os.path.join("C:\\Users\\addie\\Desktop\\GitHub\\Python\\Basic Python Coding Projects\\", file))
        print(os.path.getmtime("C:\\Users\\addie\\Desktop\\GitHub\\Python\\Basic Python Coding Projects\\"))
