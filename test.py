def print_student_name():

    first_name = "ณัฐณิชา"
    last_name = "ไชยวาริน"
    student_id = "66711216205"

    print("=" * 40)
    print("ข้อมูลนักศึกษา") 
    print("=" * 40)
    print(f"ชื่อ: {first_name}")
    print(f"นามสกุล: {last_name}")
    print(f"ชื่อเต็ม: {first_name} {last_name}")
    print(f"รหัสนักศึกษา: {student_id}")
    print("=" * 40)

if __name__ == "__main__":
    print_student_name()