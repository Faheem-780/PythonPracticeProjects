
full_dot = '😍'
empty_dot = '😒'
def create_character(name, strength, intelligence, charisma):
    # 1. Name Validations
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == '':
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return "The character name should not contain spaces"

    # 2. Stat Validations
    stats = [strength, intelligence, charisma]
    
    for s in stats:
        if not isinstance(s, int) or isinstance(s, bool): # bool is a subclass of int in Python
            return "All stats should be integers"

    for s in stats:
        if s < 1:
            return "All stats should be no less than 1"
        if s > 10:
            return "All stats should be no more than 10"

    if sum(stats) > 30:
        return "The character should start with 30 points"

    # 3. Formatting the output
    # We subtract the current stat from 10 to get the correct number of empty dots
    str_line = f"STR {full_dot * strength}{empty_dot * (10 - strength)}"
    int_line = f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
    cha_line = f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"

    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"

name=str(input("Enter the character name: "))
strength=int(input("Enter the strength stat (1-10): "))
intelligence=int(input("Enter the intelligence stat (1-10): "))
charisma=int(input("Enter the charisma stat (1-10): "))  
result = create_character(name=name,strength=strength,intelligence=intelligence,charisma=charisma)
print(result)