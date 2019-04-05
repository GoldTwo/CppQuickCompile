# Tyler Rajotte
# The Auto Compiler, started out simple and now it become a project of its own for
# something that was supposed to be simple

import os
from pynput import keyboard
import time

class keyintbuilder:
    def __init__(self):
        self.currentkeys = ["a", "b"]
        self.watchfile = None
        print("Key Intercept Builder Initalized!")

    @staticmethod
    def __compile(currentfile, lines):
        if lines:
            print("-" * 20)

        print("Compiling: g++ " + currentfile + ".cpp -o " + currentfile + ".o")
        os.system("g++ " + currentfile + ".cpp -o " + currentfile + ".o")

        print("Executing: ./" + currentfile + ".o")
        print("")
        os.system("./" + currentfile + ".o")
        print("")

    def __watchfilesetup(self):
        quickcheck = input("Input your watchfile (No Extentions): ")

        if quickcheck.lower() == "none":
            print("Watchfile disabled")
            self.watchfile = None
        else:
            print("Your watchfile is, " + quickcheck)
            self.watchfile = quickcheck

    def __activated(self):
        print("\n" * 50)
        time.sleep(0.25)

        if self.watchfile is not None:
            self.__compile(self.watchfile, False)
        else:
            directory = os.listdir(".")
            hasrun = False

            for file in directory:
                file = file.split(".")
                try:
                    if file[1] == "cpp":
                        self.__compile(file[0], hasrun)
                        hasrun = True
                except IndexError:
                    continue

    def keypressed(self, key):
        try:
            k = key.char
        except AttributeError:
            k = key.name

        # print(self.currentkeys)
        self.currentkeys.append(k)
        del self.currentkeys[0]

        if self.currentkeys == ["ctrl", "f9"]:
            self.__watchfilesetup()

        if self.currentkeys == ["ctrl", "s"]:
            self.__activated()

if __name__ == "__main__":
    program = keyintbuilder()
    lis = keyboard.Listener(on_press=program.keypressed)
    lis.start()
    lis.join()
