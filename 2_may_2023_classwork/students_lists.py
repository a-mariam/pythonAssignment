
student_list = [{"Name": "Student1", "ID": 211, "Score": (50, 90, 23)},
            {"Student2": "Name", "ID": 324, "Score": ( 54, 21, 45)},
            {"Name": "Student3", "ID": 652, "Score": (65, 56, 76)},
            {"Name": "Student4", "ID": 456, "Score": (63, 33, 32)},
            {"Name": "Student5", "ID": 768, "Score": (62, 22, 22)}
            ]

student1_name = input("Enter your Name: ")
student_list[0][1] = student1_name
student_list.append(student1_name)
#student_list.insert(0, student1_name)
print(student_list)