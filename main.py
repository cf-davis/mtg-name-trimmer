import sys

# Primarily indended for a list that is copy/pased from moxfield.com 
# into a text file. Enter the filename containing list of card names
# (each on newlines) as argument. The resulting card list will be
# written to a file called "modified.txt" in the same directory as 
# the script.
def main():
    if len(sys.argv) != 2:
        print("enter filename")
        return

    filename = sys.argv[1]

    deck_list = open(filename, "rt", encoding="UTF-16")
    modified_list = open("modifed.txt", "wt", encoding="UTF-16")

    for card_name in deck_list:
        truncate_index = card_name.find('(')

        if truncate_index != -1:
            card_name = card_name[0:truncate_index]
        
        modified_list.write(card_name.strip() + '\n')
        

    deck_list.close()
    modified_list.close()


if __name__ == "__main__":
    main()