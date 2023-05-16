# file = open("Student_records.txt", mode="w")
# file.write("001 mariam 75\t")
# file.write("002 david 75\t")
# file.write("003 esther 75\t")
# file.close()
# with open("Student_records.txt", mode="r")as records:
#     for record in records:
#         num, name, score = record.split()
#         print(f"{num:<10} {name: <10} {score: >10}")


with open("students_records.txt", mode="a") as file:
 file.write("099 mariam 78\n")
 file.write("122 maryam 76\n")

# file = open("students_records.txt", mode="r")
