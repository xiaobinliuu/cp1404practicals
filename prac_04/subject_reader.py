FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_course(data)


def get_data():
  # this shows the subject,lecturer,number of students.
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        data.append(parts)

    input_file.close()
    return data

def display_course(data):
    for courses in data:
        print("{} is taught by {:12} and has {:3} students".format(courses[0],courses[1],courses[2]))


main()
#