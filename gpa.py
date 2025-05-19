import re

def main () -> int :
    no_of_courses = get_int("How many courses do you have? ")
    points = 0
    total_units = 0
    courses = []
    for i in range(no_of_courses):
        print(f"Course {i + 1}:")
        course_name = get_course_name()
        course_units = get_course_unit("How many units is the course? ")
        total_units = total_units + course_units
        course_grade = get_grade()
        points = points + (course_units * get_grade_points(course_grade))
        courses.append({
            "name": course_name,
            "units": course_units,
            "grade": course_grade,            
        })
    gpa = round(float(points / total_units), 2)
    print("From your current Results: ")
    for course in courses:
        print(f"{course['name']} - {course['units']} units - {course['grade']}")
    print(f"Your GPA is {gpa} out of 5.0")
    return 0
    
    
    
    
def get_int(message: str) -> int:
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
         
def get_course_unit(message: str) -> int:
    while True:
        unit = get_int(message)
        if unit <= 6:
            return unit
        print("Courses can't have more than 6 units.")   
        
def get_grade() -> str:
    while True:
        grade = input("What Grade did you get(don't lie ooo )? ")
        grade = grade.upper()
        if grade in ['A', 'B', 'C', 'D', 'F']:
            return grade
        print("Please enter a valid grade (A, B, C, D, F).")
        
def get_grade_points(grade: str) -> int:
    match grade:
        case 'A':
            return 5
        case 'B':
            return 4
        case 'C':
            return 3
        case 'D':
            return 2
        case 'F':
            return 0
        
def get_course_name() -> str:
    pattern = r'^[A-Za-z]{3}\d{3}$'
    while True:
        course_name = input("What is the name of the course? ")
        if len(course_name) > 0 and re.match(pattern, course_name):
            course_name = course_name.upper()
            return course_name
        print("Please enter an actual course name.")

if __name__ == "__main__":
    main()