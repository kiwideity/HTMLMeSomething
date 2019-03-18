from helpers import alphabet_position, rotate_character

def encrypt(text, key):

    code = []
    index = 0

    for i in text:

        rotation = alphabet_position(key[index])


        if i.isalpha() == False:
            code.append(i)
            index -= 1
        elif i.isalpha():
            code.append(rotate_character(i, rotation))



        if index == (len(key) - 1):
            index = 0
        else:
            index += 1

    return ''.join(code)


def main():
    text = input("Enter your phrase for encrytion:")
    key = input("Enter a cipher key:")

    print(encrypt(text,key))



if __name__ == "__main__":
  main()
