from helpers import alphabet_position, rotate_character

def encrypt(new_list, rot):
  a = []
  b = []
  #print(new_list)

  for i in new_list:

    b.append(rotate_character(i,rot))
  #print(i)
  #print(a)
  s = "".join(b)
  print(s, end='')
  return s
  print()

#encrypt("Play, The # Game", 26)

def main():

  txt = str(input(" Enter your phrase to be encrypted "))
  rot = int(input("Enter a number "))


  encrypt(txt, rot)



if __name__ == "__main__":
  main()
