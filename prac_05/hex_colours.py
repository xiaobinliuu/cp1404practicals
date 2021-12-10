def main():
    NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                    "Alizarin crimison": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                    "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "antiqueWhite2": "#4eedfcc", "antiquewhite3": "#cdc0b0"}
    # will be easier to enter input if put all character as lower or upper

    name_enter = input("Enter a name for colour code:")  # naming could be clearer, like color or color name.
    while name_enter != "":
        if name_enter in NAME_TO_CODE:
            print("{} is {}".format(name_enter, NAME_TO_CODE[name_enter]))
        else:
            print("Something seems wrong. Please enter value again")
        name_enter = input("Enter a name for colour code:") 
    print("Thank you for using this service XD")


if __name__ == '__main__':
    main()
