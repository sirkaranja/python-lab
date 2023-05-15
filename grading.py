def grading_system():
    mark = float(input("Enter your mark:"))
    if mark >= 80 and mark<=100:
        print('Grade A')
    elif mark >=70 and mark <80:
        print('Grade B')
    elif mark >=60 and mark <70:
        print('Grade C')
    elif mark >=40 and mark < 60:
        print('Grade D')
    elif mark <40 and mark >0:
        print('Pull up your socks')
    else:
        print('Enter a valid mark...')

grading_system()