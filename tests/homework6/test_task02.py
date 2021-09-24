from homework6.task02 import Student, Teacher, Homework, \
    HomeworkResult, DeadlineError


def test_class_homework_check_is_active():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)

    assert student.do_homework(oop_homework) == oop_homework


def test_class_homework_check_is_inactive():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)

    assert student.do_homework(expired_homework) is None

# check if do_homework return HomeworkResult instance
def test_do_homework_return_result():
    pass

# check if homework_result raises exceptions when wrong type of object is given
def test_homework_result_check_type():
    pass

# check if do_homework raises exceptions when homework is overdue
def test_do_homework_deadlineError_check():
    pass

def

