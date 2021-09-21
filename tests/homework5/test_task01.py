from homework5.task01 import Student, Teacher


def test_class_homework_is_active():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)

    assert student.do_homework(oop_homework) == oop_homework


def test_class_homework_is_inactive():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)

    assert student.do_homework(expired_homework) is None
