# This program will be a work in progress to be  maintained and updated based on accumulated knowledge.
# Key additions will be distinct details that differentiate one student from the other


# Thia program contains, only, the details of the students.
# To ensure it is easy to maintain and update, it must not include calls to the student profiles,
# instead, its code must be written in another file, which also must contain just the students profiles.
# The student object must not be called in the codes too


class Student:
    # This program is to collate the data of students in faculty of management sciences
    # MASSA. It will help in the adequate management of the students file and control
    # of sensitive details
    # Their details will be shared subject to school privacy policies.
    # The details to collect include: Name Age, Sex, Major, Matriculation number, Faculty, GPA, Level, email,
    # phone number,Nationality, State of origin,

    def __init__(self, name, age, sex, faculty, major, mat_num, gpa, level, nationality, state, disability):
        self.name = name
        self.age = age
        self.sex = sex
        self.faculty = faculty
        self.major = major
        self.mat_num = mat_num
        self.gpa = gpa
        self.level = level
        self.nationality = nationality
        self.state = state
        self.disability = disability

    def honour(self):
        if self.gpa >= 4.40:
            print("CONGRATULATIONS!!! With a GPA of ", self.gpa, " Kindly proceed to fill "
                  "and submit the necessary documents")

        else:
            print("Sorry,", self.name + ", you do not have up to the GPA required.")


# The task is to import the detail of the student to another page with referencing only and working with the file: e.g:
# I intend to import the details here and use a conditional statement to determine what to print.
# I also intend to carry that out using functions; I will try all options necessary to achieve that aim.


abel = Student("Abel Edugie", 23, "Male", "Management Sciences", "Business Administration", "MGS1508441",
               4.45, 400, "Nigerian", "Edo state", False)

print(abel.name, end=" ")
abel.honour()
print()

faith = Student("Faith Johnson", 26, "female", "Social Sciences", "Public Administration", "SOS1502382",
                3.45, 200, "Nigerian", "Anambra state", False)

faith.honour()
