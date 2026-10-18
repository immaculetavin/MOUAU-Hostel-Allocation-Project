class Student:
    def __init__(self, reg_no, name, department, level, gender):
        self.reg_no = reg_no
        self.name = name
        self.department = department
        self.level = level
        self.gender = gender
        self.hostel = None
        self.room = None

    def display(self):
        hostel = self.hostel if self.hostel else "Not Allocated"
        room = self.room if self.room else "-"
        print(f"{self.reg_no} | {self.name} | {self.department} | "
              f"{self.level} | {self.gender} | {hostel} | {room}")


class Room:
    def __init__(self, room_no, capacity):
        self.room_no = room_no
        self.capacity = capacity
        self.students = []

    def is_available(self):
        return len(self.students) < self.capacity

    def add_student(self, student):
        if self.is_available():
            self.students.append(student)
            student.room = self.room_no
            return True
        return False


class Hostel:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def allocate(self, student):
        if student.gender != self.gender:
            return False

        for room in self.rooms:
            if room.is_available():
                room.add_student(student)
                student.hostel = self.name
                return True
        return False

    def available_spaces(self):
        total = 0
        for room in self.rooms:
            total += room.capacity - len(room.students)
        return total


class HostelAllocationSystem:
    def __init__(self):
        self.students = []
        self.hostels = []

    def add_hostel(self, hostel):
        self.hostels.append(hostel)

    def register_student(self):
        reg = input("Registration Number: ")
        name = input("Student Name: ")
        dept = input("Department: ")
        level = input("Level: ")
        gender = input("Gender (Male/Female): ").capitalize()

        student = Student(reg, name, dept, level, gender)
        self.students.append(student)

        print("\nStudent Registered Successfully.")

    def allocate_student(self):
        reg = input("Enter Registration Number: ")

        student = None

        for s in self.students:
            if s.reg_no == reg:
                student = s
                break

        if student is None:
            print("Student not found.")
            return

        if student.hostel:
            print("Student has already been allocated.")
            return

        for hostel in self.hostels:
            if hostel.allocate(student):
                print(f"{student.name} allocated to "
                      f"{student.hostel}, Room {student.room}")
                return

        print("No available hostel.")

    def view_students(self):
        print("\n---------------- STUDENTS ----------------")
        for student in self.students:
            student.display()

    def hostel_status(self):
        print("\n--------------- HOSTEL STATUS ----------------")
        for hostel in self.hostels:
            print(f"{hostel.name}")
            print(f"Gender: {hostel.gender}")
            print(f"Available Spaces: {hostel.available_spaces()}")
            print("-" * 40)


def create_hostels():
    male = Hostel("Male Hostel", "Male")
    female = Hostel("Female Hostel", "Female")

    for i in range(1, 6):
        male.add_room(Room(f"M{i}", 4))

    for i in range(1, 6):
        female.add_room(Room(f"F{i}", 4))

    return male, female


def main():
    system = HostelAllocationSystem()

    male, female = create_hostels()

    system.add_hostel(male)
    system.add_hostel(female)

    while True:

        print("\n========== MOUAU HOSTEL ALLOCATION SYSTEM ==========")
        print("1. Register Student")
        print("2. Allocate Hostel")
        print("3. View Students")
        print("4. View Hostel Status")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            system.register_student()

        elif choice == "2":
            system.allocate_student()

        elif choice == "3":
            system.view_students()

        elif choice == "4":
            system.hostel_status()

        elif choice == "5":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()