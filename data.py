import csv
import logging

FILE_NAME = "student.csv"

# LOGGING CONFIGURATION

logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def write_csv():
    """
    Writes predefined student data into a CSV file.
    """
    try:

        students = [
["Roll No", "Name", "Science", "Maths", "English", "History", "Computer", "City", "Sports"],

[1, "Om", 85, 90, 88, 75, 92, "Delhi", "Cricket"],
[2, "Ram", 78, 82, 80, 70, 85, "Mumbai", "Football"],
[3, "Shyam", 45, 29, 49, 40, 25, "Pune", "Hockey"],
[4, "Aarav", 88, 91, 85, 80, 87, "Delhi", "Cricket"],
[5, "Riya", 65, 70, None, 72, 75, "Jaipur", "Badminton"],
[6, "Karan", 110, 85, 80, 75, 90, "Mumbai", "Football"],
[7, "Neha", 90, 95, 92, 89, 93, "Chennai", "Tennis"],
[8, "Rohit", -10, 60, 55, 58, 62, "Kolkata", "Cricket"],
[9, "Ankit", 72, 75, 70, 68, 74, "Indore", "Kabaddi"],
[10, "Pooja", 35, 88, 19, 32, 120, "Bhopal", "Badminton"],
[11, "Suresh", 95, 87, 85, 88, 92, "Delhi", "Cricket"],
[12, "Meena", 55, 60, 58, None, 62, "Surat", "Volleyball"],
[13, "Amit", 40, -5, 50, 48, 55, "Agra", "Football"],
[14, "Kavya", 88, 90, 87, 85, 89, "Noida", "Tennis"],
[15, "Rahul", None, None, None, None, None, "Patna", "Cricket"],
[16, "Tina", 92, 94, 91, 90, 93, "", "Basketball"],
[17, "Mohan", 73, 75, 70, 68, 74, "Gwalior", "football"],
[18, "Priya", 23, 328, 26, 24, 10, "Amritsar", "Hockey"],
[19, "Sanjay", 60, 65, 62, 58, 66, "Udaipur", "Swimming"],
[20, "Ritu", 78, 80, 79, 75, 82, "Kanpur", "Cricket"],
[21, "Vikas", 82, 85, 83, 80, 88, "Delhi ", "Badminton"],
[22, "Nikhil", 68, 70, 65, 60, 72, "Ranchi", "Kabaddi"],
[23, "Aarti", 95, 97, 94, 92, 96, "Faridabad", "Tennis"],
[24, "Deepak", 58, 55, 60, 57, 62, "Hisar", "Volleyball"],
[25, "Sunita", 18, 190, 37, 25, 12, "Panipat", "Hockey"],
[26, "Ajay", 72, 74, 70, 68, 75, "Rohtak", "Cricket"],
[27, "Monika", 80, 82, 78, 75, 85, "Gurugram", "Basketball"],
[28, "Harsh", 90, 92, 88, 85, 91, "Meerut", "Badminton"],
[29, "Pankaj", 65, 60, 62, 58, 67, "Alwar", "Football"],
[30, "Simran", 87, 89, 85, 83, 90, "Jodhpur", "Tennis"],
[31, "Yash", 23, 23, 12, 56, 450, "Kota", "Cricket"],
[32, "Naina", 92, 94, 90, 88, 95, "Ujjain", "Swimming"],
[33, "Rakesh", 84, 86, 82, 80, 88, "Dewas", "Kabaddi"],
[34, "Preeti", 79, 81, 78, 75, 85, "Rewa", "Hockey"],
[35, "Arjun", 29, 19, 32, 40, 16, "Satna", "Tennis"],
[36, "Komal", 61, 63, 60, 58, 65, "Sagar", "Volleyball"],
[37, "Aman", 70, 72, 68, 65, 75, "Tikamgarh", "Cricket"],
[38, "Bhavna", 88, 90, 87, 85, 92, "Morena", "Badminton"],
[39, "Varun", 54, 50, 52, 48, 55, "Shivpuri", "Football"],
[40, "Sneha", 97, 99, 95, 93, 98, "Guna", "Tennis"],
[10, "RAM", 85, 88, 86, 84, 90, "Bhopal", "Cricket"]
]


        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)

        logging.info("Student data written successfully")

        return "Student data written successfully."

    except Exception as e:

        logging.error("Error while writing file")
        return "Error while writing file."


def read_csv():
    """
    Reads student data from CSV file.
    """
    try:

        rows = []

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                rows.append(row)

        logging.info("Student data read successfully")

        return rows

    except Exception as e:

        logging.error("Error while reading file")
        return "Error while reading file."


def append_csv():
    """
    Appends new student data.
    """
    try:

        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        city = input("Enter City: ")
        sports = input("Enter Sports: ")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll, name, None, None, None, None, None, city, sports])

        logging.info(f"New student appended: Roll No {roll}")

        return "Student data appended successfully."

    except Exception as e:

        logging.error("Error while appending data")
        return "Error while appending data."


def Menu():
    """
    Displays menu.
    """
    try:

        while True:

            print("\n----- Student CSV Menu -----")
            print("1. Write Student Data")
            print("2. Read Student Data")
            print("3. Append Student Data")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                print(write_csv())

            elif choice == "2":

                result = read_csv()

                if isinstance(result, list):
                    for row in result:
                        print(row)
                else:
                    print(result)

            elif choice == "3":

                print(append_csv())

            elif choice == "4":

                logging.info("Program exited by user")
                print("Program exited.")
                break

            else:

                print("Invalid choice!")
                logging.warning("Invalid menu choice entered")

    except Exception as e:

        logging.critical("Program crashed")
        print("Program crashed due to an error.")
