import time
import random

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark cave...")
    time.sleep(1)
    print("You can see two paths ahead of you.")
    time.sleep(1)

def choose_path():
    while True:
        print("\nWhich path will you take? (1 or 2)")
        choice = input(">> ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def explore_path(path):
    if path == 1:
        print("\nYou chose path 1.")
        time.sleep(1)
        print("You encounter a group of bats!")
        time.sleep(1)
        print("How would you like to deal with the bats?")
        print("1. Fight them off")
        print("2. Try to sneak past them")
        choice = input(">> ")
        if choice == "1":
            print("\nYou decide to fight the bats.")
            time.sleep(1)
            print("After a brief struggle, you manage to defeat them.")
        elif choice == "2":
            print("\nYou decide to try to sneak past the bats.")
            time.sleep(1)
            print("You move carefully and manage to avoid disturbing them.")
        else:
            print("Invalid choice. The bats attack while you hesitate!")
    elif path == 2:
        print("\nYou chose path 2.")
        time.sleep(1)
        print("You find a treasure chest!")
        time.sleep(1)
        print("What would you like to do with the treasure chest?")
        print("1. Open it")
        print("2. Leave it alone")
        choice = input(">> ")
        if choice == "1":
            print("\nYou decide to open the treasure chest.")
            time.sleep(1)
            print("Inside, you find some gold coins.")
        elif choice == "2":
            print("\nYou decide to leave the treasure chest alone.")
            time.sleep(1)
            print("You continue on your journey, leaving the treasure behind.")
        else:
            print("Invalid choice. The treasure chest disappears in a puff of smoke!")
    else:
        print("Invalid path.")

def main():
    intro()
    path = choose_path()
    explore_path(path)

if __name__ == "__main__":
    main()
