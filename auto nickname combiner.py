import random

def ask_for_names():
    first_name = input(" What's your first name: ").strip()
    last_name = input(" What's your last name: ").strip()
    return first_name, last_name

def ask_for_style():
    print("\n Choose your nickname style:")
    print("1. Fun ")
    print("2. Short ")
    print("3. Formal ")
    
    choice = input("Enter 1 or 2 or 3: ").strip()
    styles = {"1": "fun", "2": "short", "3": "formal"}
    return styles.get(choice, "fun")

def create_nicknames(first_name, last_name, style="fun"):
    nicknames = []

    nicknames.append(first_name[:3] + last_name[-3:])  
    nicknames.append(first_name + last_name)            
    nicknames.append(last_name + first_name)         
    nicknames.append(first_name[:2] + last_name[:2])      
    nicknames.append(first_name[0] + last_name)           

    #  fun
    if style == "fun":
        extras = ["_X", "24", "King", "Queen", "_99", "_Pro", "_Z"]
        for _ in range(3):
            first_part = random.choice([first_name, last_name])[:random.randint(2, 4)]
            second_part = random.choice([first_name, last_name])[random.randint(1, 3):]
            suffix = random.choice(extras)
            nickname = first_part + second_part + suffix
            nicknames.append(nickname)

    #  Short
    elif style == "short":
        nicknames.extend([
            (first_name[:2] + last_name[:1]).lower(),
            (first_name[:1] + last_name[:2]).lower(),
            (first_name[0] + last_name[0]).lower()
        ])

    #  Formal
    elif style == "formal":
        nicknames.append(first_name.capitalize() + "The" + last_name.capitalize())
        nicknames.append("Mr" + first_name.capitalize())
        nicknames.append("Dr" + last_name.capitalize())

    for _ in range(3):
        mix = ''.join(random.sample(first_name + last_name, min(6, len(first_name + last_name))))
        nicknames.append(mix)

    return list(set(nicknames))

def show_nicknames(nicknames):
    print("\n Here are your cool nickname options:")
    for i, name in enumerate(nicknames, 1):
        print(f"{i}. {name}")

#  Save the nicknames in a text file (optional, if user wants to save it)
def save_nicknames_to_file(nicknames):
    choice = input(" Do you want to save these nicknames to a file? (yes/no): ").lower()
    if choice == 'yes':
        filename = input("ha Enter a file name (e.g., my_nicknames.txt): ").strip()
        with open(filename, 'w') as file:
            for name in nicknames:
                file.write(name + '\n')
        print(f" Nicknames saved to {filename}!")

#  Main function 
def main():
    print(" Welcome to the Auto Nickname Combiner Bot! ")
    
    first, last = ask_for_names()
    style = ask_for_style()
    nicknames = create_nicknames(first, last, style)
    show_nicknames(nicknames)
    save_nicknames_to_file(nicknames)

# Run
if __name__ == "__main__":
    main()
