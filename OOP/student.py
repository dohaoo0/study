# Tạo một class tên sinhvien với các thuộc tính:
# hoten, ma_sinh_vien, que_quan

class Student():
    def __init__(self, name=None, student_id=None, hometown=None):
        self.name = name
        self.student_id = student_id
        self.hometown = hometown
    
    def input_information_student(self):
        """ Nhập thông tin từ bàn phím """
        self.name = input("Enter your name: ")
        self.student_id = input("Enter your id: ")
        self.hometown = input("Enter your hometown: ")
     

# Student_1 = Student("Hảo", 123, "Hà Nội")
# Student_2 = Student("Hà", 234, "Nghệ An")
# Student_3 = Student("Linh", 167, "Hà Nội")
Student_4 = Student()
Student_4.input_information_student()
print(
    """Sinh viên 1 có tên là: {},
    mã sinh viên là: {},
    quê ở {}""".format(
        Student_4.name, 
        Student_4.student_id, 
        Student_4.hometown
    )
)