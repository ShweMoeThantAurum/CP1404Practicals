NAME_TO_CODE = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff", "ALIZARIN CRIMSON":
                "#e32636", "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7",
                "APRICOT": "fbceb1", "AQUA": "00ffff"}
is_valid_input = False
while not is_valid_input:
    try:
        color_name = input("Enter color name: ").upper()
        if color_name == "":
            break
        color_code = NAME_TO_CODE[color_name]
        print(f"{color_name.upper()}'s color_code is {color_code}")
    except KeyError:
        print("Invalid color name")
