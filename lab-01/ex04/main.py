from student_manager import StudentManager

manager = StudentManager()

while True:
    print("----- STUDENT MANAGEMENT PROGRAM -----")
    print("1. Add student")
    print("2. Update student")
    print("3. Show student list")
    print("4. Sort students by ID")
    print("5. Search students by name")
    print("6. Delete student by ID")
    print("7. Exit")

    choice = input("Choose an option (1–7): ")

    if choice == '1':
        manager.add_student()

    elif choice == '2':
        try:
            student_id = int(input("Enter student ID to update: "))
            manager.update_student(student_id)
        except ValueError:
            print("Student ID must be a number!")

    elif choice == '3':
        manager.show_students(manager.student_list)

    elif choice == '4':
        manager.sort_by_id()
        print("-> Students sorted by ID.")
        manager.show_students(manager.student_list)

    elif choice == '5':
        name = input("Enter name to search: ")
        result = manager.find_by_name(name)
        print(f"-> Found {len(result)} students:")
        manager.show_students(result)

    elif choice == '6':
        try:
            student_id = int(input("Enter student ID to delete: "))
            if manager.delete_by_id(student_id):
                print("-> Student deleted successfully.")
            else:
                print("-> Student ID not found.")
        except ValueError:
            print("Student ID must be a number!")

    elif choice == '7':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
