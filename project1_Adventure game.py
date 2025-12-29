# Text Adventure Game - Haunted House
# Author: Lê Bảo Nghi

def check_inventory(inventory):
    """
    Function to check and display the player's inventory.
    Can be called at any point in the game.
    """
    print("You open your backpack. It contains:")
    for item in inventory:
        print(f"- {item}")
    print("")  # Empty line for readability


def bedroom(health, inventory, pin_only=False):
    """
    The player enters the bedroom.
    Can pick up a flashlight and/or pin depending on previous actions.
    Returns updated health and inventory.
    """
    print("You return to the bedroom.", end=" ")
    if pin_only:
        print("Only the pin remains on the bed.")
        while True:
            action = input(
                "What do you do? (take pin / leave / check backpack): ")
            if action == "take pin":
                if "pin" not in inventory:
                    inventory.append("pin")
                    print("You pick up the pin.")
                else:
                    print("You already have the pin.")
                break
            elif action == "leave":
                print("You leave the pin on the bed.")
                break
            elif action == "check backpack":
                check_inventory(inventory)
            else:
                print("Invalid choice, please enter again.")
        return health, inventory

    print("You see a bed, a small drawer, and something shiny on the pillow.")
    while True:
        action = input(
            "What do you do? (take flashlight / leave / check backpack): ")
        if action == "take flashlight":
            if "flashlight" not in inventory:
                inventory.append("flashlight")
                print("You pick up the flashlight.")
            else:
                print("You already have the flashlight.")
            break
        elif action == "leave":
            print("You ignore it and step back.")
            break
        elif action == "check backpack":
            check_inventory(inventory)
        else:
            print("Invalid choice, please enter again.")

    print("There’s also a pin on the bed.")
    while True:
        action = input("What do you do? (take pin / leave / check backpack): ")
        if action == "take pin":
            if "pin" not in inventory:
                inventory.append("pin")
                print("You pick up the pin.")
            else:
                print("You already have the pin.")
            break
        elif action == "leave":
            print("You leave the pin on the bed.")
            break
        elif action == "check backpack":
            check_inventory(inventory)
        else:
            print("Invalid choice, please enter again.")

    return health, inventory


def kitchen(health, inventory):
    """
    The player enters the kitchen.
    Can pick up an apple for HP recovery.
    Returns updated health and inventory.
    """
    print("You walk into the kitchen. There’s a faint smell of something rotten.")
    while True:
        action = input(
            "You see an apple on the counter. What do you do? (take apple / leave / check backpack): ")
        if action == "take apple":
            if "apple" not in inventory:
                inventory.append("apple")
                print("You pick up the apple.")
            else:
                print("You already took the apple earlier.")
            break
        elif action == "leave":
            print("You leave the apple on the counter.")
            break
        elif action == "check backpack":
            check_inventory(inventory)
        else:
            print("Invalid choice, please enter again.")
    return health, inventory


def basement(health, inventory):
    """
    The player enters the basement.
    Multiple paths exist depending on items (flashlight + pin) or health.
    Returns updated health and inventory.
    """
    print("You arrive at the basement door. It is completely dark inside...")

    while True:
        enter = input(
            "Do you want to go down to the basement? (go down / don’t go / check backpack): ")
        if enter == "go down":
            break
        elif enter in ["don’t go", "stay", "no"]:
            print(
                "You hesitate and try to avoid it, but there’s nowhere else to go. You’re trapped.")
            print("You must go down eventually...")
        elif enter == "check backpack":
            check_inventory(inventory)
        else:
            print("Invalid choice, please enter again.")

    # Logic for flashlight and pin interaction
    if "flashlight" in inventory:
        while True:
            action = input(
                "What do you do? (turn on flashlight / go in dark / check backpack): ")
            if action == "turn on flashlight":
                if "pin" in inventory:
                    print("You fix the flashlight with the pin and go down safely.")
                else:
                    print(
                        "You try to turn it on, but it doesn’t work — you need a pin to fix it.")
                    while True:
                        back = input(
                            "What do you do? (go back / stay / check backpack): ")
                        if back == "go back":
                            print(
                                "You go back to the bedroom. The long way makes you tired. Minus 10 HP.")
                            health -= 10
                            health, inventory = bedroom(
                                health, inventory, pin_only=True)
                            return basement(health, inventory)
                        elif back == "stay":
                            print(
                                "You go in the dark without fixing the flashlight. Minus 20 HP.")
                            health -= 20
                            break
                        elif back == "check backpack":
                            check_inventory(inventory)
                        else:
                            print("Invalid choice, please enter again.")
                break
            elif action == "go in dark":
                print("You go in the dark. Minus 20 HP.")
                health -= 20
                break
            elif action == "check backpack":
                check_inventory(inventory)
            else:
                print("Invalid choice, please enter again.")

    elif "pin" in inventory:
        print("You have a pin but no flashlight to use it with.")
        while True:
            back = input("What do you do? (go back / stay / check backpack): ")
            if back in ["go back", "return to bedroom", "back"]:
                print(
                    "You go back to the bedroom. The long way makes you tired. Minus 10 HP.")
                health -= 10
                health, inventory = bedroom(health, inventory)
                return basement(health, inventory)
            elif back == "stay":
                print("You decide to go down in the dark. Minus 20 HP.")
                health -= 20
                break
            elif back == "check backpack":
                check_inventory(inventory)
            else:
                print("Invalid choice, please enter again.")

    else:
        print("You have neither flashlight nor pin. It's completely dark.")
        while True:
            back = input("What do you do? (go back / stay / check backpack): ")
            if back == "go back":
                print(
                    "You go back to the bedroom. The long way makes you tired. Minus 10 HP.")
                health -= 10
                health, inventory = bedroom(health, inventory)
                return basement(health, inventory)
            elif back == "stay":
                print("You walk in total darkness. Minus 20 HP.")
                health -= 20
                break
            elif back == "check backpack":
                check_inventory(inventory)
            else:
                print("Invalid choice, please enter again.")

    print("In the basement, you find a rusty key and an exit door.")
    print("While escaping, you scratch your arm. Minus 10 HP.")
    health -= 10

    if health <= 0:
        print(f"Your HP is {health}. You collapse and never wake up again.")
        print("Game Over.")
    else:
        print(
            f"You escape the haunted house with {health} HP left! You survive!")
        print("GAME COMPLETED. Congratulations!")
        exit()
    return health, inventory


def haunted_house():
    """
    Main function to run the game.
    Initializes health and inventory, and provides player choices.
    """
    health = 50
    inventory = ["bag"]
    print("You wake up in a dark house with 50 HP. You have a small bag with you.")

    while True:
        print(f"Current HP: {health}")
        print(f"Inventory: {inventory}")
        choice = input(
            "Where do you go? (kitchen/bedroom/basement/eat/check backpack/quit): ")

        if choice == "kitchen":
            health, inventory = kitchen(health, inventory)
        elif choice == "bedroom":
            health, inventory = bedroom(health, inventory)
        elif choice == "basement":
            health, inventory = basement(health, inventory)
        elif choice == "eat":
            if "apple" in inventory:
                print("You eat the apple and regain 10 HP.")
                health += 10
                inventory.remove("apple")
            else:
                print("You have nothing to eat.")
        elif choice == "check backpack":
            check_inventory(inventory)
        elif choice == "quit":
            print("You decide to quit the game. Goodbye!")
            break
        else:
            print("Invalid choice, please enter again.")


haunted_house()
