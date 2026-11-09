student_list = []
def add_student(name, score):
    student_list.append({"name":name,"score":score})
def show_all():
    for s in student_list:
        print(f"学生{s['name']}，分数：{s['score']}")
add_student("张三",90)
show_all()
