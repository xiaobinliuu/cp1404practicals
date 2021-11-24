
OUTPUT_FILE = "name.txt"
output_file = open('name.txt', 'w')
users_name = input("Enter name: ")
output_file.write(users_name)
output_file.close()

input_file = open('name.txt', 'r')
name = input_file.read()
input_file.close()
print("Your name is: ", name)

IN_FILE = "Number.txt"
in_file = open("Number.txt", "r")
num_one = int(in_file.readline())
num_two = int(in_file.readline())
print(num_one + num_two)
in_file.close()


