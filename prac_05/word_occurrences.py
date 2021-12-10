def main():
    user_string = input("Text:")
    words = user_string.split()
    Word_To_Number = {}

    for word in words:
        Word_To_Number[word] = Word_To_Number.get(word, 0) + 1

    for word, value in Word_To_Number.items():
        print("{:6} : {:5}".format(word, value))
# code all good, but the output is not sort. 

if __name__ == '__main__':
    main()
