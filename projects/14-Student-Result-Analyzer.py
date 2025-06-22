#14 My Project - Student Result Analyzer
def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 40:
        return 'D'
    else:
        return 'F'

def main():
    students = []
    print("📊 Welcome to the Student Result Analyzer CLI Tool 📊")
    print("----------------------------------------------------")

    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            mark = float(input(f"Enter marks for {name} (out of 100): "))
            if mark < 0 or mark > 100:
                print("❌ Invalid marks. Please enter between 0 and 100.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter numeric marks.")
            continue

        grade = get_grade(mark)
        status = "Pass" if grade != 'F' else "Fail"
        students.append({'name': name, 'marks': mark, 'grade': grade, 'status': status})

    print("\n📝 Summary Report:")
    print("------------------")
    total_students = len(students)
    if total_students == 0:
        print("No data entered.")
        return

    failed_students = [s for s in students if s['status'] == "Fail"]
    passed_students = [s for s in students if s['status'] == "Pass"]
    topper = max(students, key=lambda x: x['marks'])
    avg_marks = sum(s['marks'] for s in students) / total_students
    lowest = min(students, key=lambda x: x['marks'])

    print(f"Total Students     : {total_students}")
    print(f"Passed             : {len(passed_students)}")
    print(f"Failed             : {len(failed_students)}")
    print(f"Pass Percentage    : {(len(passed_students) / total_students) * 100:.2f}%")
    print(f"Average Marks      : {avg_marks:.2f}")
    print(f"Topper             : {topper['name']} ({topper['marks']} marks)")
    print(f"Lowest Scorer      : {lowest['name']} ({lowest['marks']} marks)")

    print("\n📋 Detailed Student Results:")
    print("-----------------------------")
    for s in students:
        print(f"{s['name']} - {s['marks']} marks - Grade {s['grade']} - {s['status']}")

if __name__ == "__main__":
    main()
grh
