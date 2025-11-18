from student import Student

class StudentManager:
    def __init__(self):
        self.student_list = []

    def find_student(self, student_id):
        for st in self.student_list:
            if st.student_id == student_id:
                return st
        return None

    def generate_id(self):
        max_id = 1
        if len(self.student_list) > 0:
            max_id = max(st.student_id for st in self.student_list) + 1
        return max_id

    def add_student(self):
        student_id = self.generate_id()
        full_name = input("Enter student's full name: ")
        gender = input("Enter student's gender: ")
        major = input("Enter student's major: ")

        while True:
            try:
                gpa = float(input("Enter student's GPA (0–10): "))
                if 0 <= gpa <= 10:
                    break
                else:
                    print("GPA must be between 0 and 10.")
            except ValueError:
                print("Please enter a valid number.")

        st = Student(student_id, full_name, gender, major, gpa)
        self.classify_academic_rank(st)
        self.student_list.append(st)

        print(f"Student with ID {student_id} added successfully!")

    def update_student(self, student_id):
        st = self.find_student(student_id)
        if st:
            print(f"Updating student: {st.full_name}")

            full_name = input("New full name (Enter to keep current): ")
            if full_name:
                st.full_name = full_name

            gender = input("New gender (Enter to keep current): ")
            if gender:
                st.gender = gender

            major = input("New major (Enter to keep current): ")
            if major:
                st.major = major

            new_gpa = input("New GPA (Enter to keep current): ")
            if new_gpa:
                st.gpa = float(new_gpa)

            self.classify_academic_rank(st)
            print("Update successful!")

        else:
            print("Student ID not found.")

    def delete_by_id(self, student_id):
        st = self.find_student(student_id)
        if st:
            self.student_list.remove(st)
            return True
        return False

    def sort_by_id(self):
        self.student_list.sort(key=lambda st: st.student_id)

    def sort_by_name(self):
        self.student_list.sort(key=lambda st: st.full_name)

    def sort_by_gpa(self):
        self.student_list.sort(key=lambda st: st.gpa)

    def find_by_name(self, name):
        return [st for st in self.student_list if name.lower() in st.full_name.lower()]

    def classify_academic_rank(self, st: Student):
        if st.gpa >= 9:
            st.academic_rank = "Excellent"
        elif st.gpa >= 8:
            st.academic_rank = "Very Good"
        elif st.gpa >= 6.5:
            st.academic_rank = "Good"
        elif st.gpa >= 5:
            st.academic_rank = "Average"
        else:
            st.academic_rank = "Poor"

    def show_students(self, list_st):
        print("{:<10} {:<25} {:<10} {:<20} {:<10} {:<15}".format(
            "ID", "Full Name", "Gender", "Major", "GPA", "Rank"))
        print("-" * 90)

        if list_st:
            for st in list_st:
                print("{:<10} {:<25} {:<10} {:<20} {:<10} {:<15}".format(
                    st.student_id, st.full_name, st.gender, st.major, st.gpa, st.academic_rank))
        else:
            print("Empty list!")

        print("\n")
