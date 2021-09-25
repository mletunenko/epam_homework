import pytest

from homework6.task02 import DeadlineError, HomeworkResult, Student, Teacher


# check if do_homework return HomeworkResult instance
def test_do_homework_return_result():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    good_student = Student('Lev', 'Sokolov')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')

    assert isinstance(result_1, HomeworkResult) is True


# check if homework_result raises exceptions when wrong type of object is given
def test_homework_result_check_type():
    good_student = Student('Lev', 'Sokolov')

    with pytest.raises(TypeError):
        _ = HomeworkResult(good_student, "fff", "Solution")


# check if do_homework raises exceptions when homework is overdue
def test_do_homework_deadline_error_check():
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    expired_homework = teacher.create_homework('Learn functions', 0)

    with pytest.raises(DeadlineError):
        _ = student.do_homework(expired_homework, 'done')


# check if HomeworkResult go to homework_done dict if check_homework
# return True
def test_HomeworkResult_goes_to_homework_done_after_success_check_homework():
    good_student = Student('Lev', 'Sokolov')
    opp_teacher = Teacher('Daniil', 'Shadrin')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    opp_teacher.check_homework(result_1)

    assert result_1 in opp_teacher.homework_done[oop_hw]


# guarantee that homework_done have only unique HomeworkResult
def test_homework_done_have_unique_homework_results():
    good_student = Student('Lev', 'Sokolov')
    opp_teacher = Teacher('Daniil', 'Shadrin')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    opp_teacher.check_homework(result_1)
    first_check = opp_teacher.homework_done[oop_hw]
    opp_teacher.check_homework(result_1)

    assert first_check == opp_teacher.homework_done[oop_hw]


# check if check_homework return true if HomeworkResult answer is
# more than 5 symbols
def test_check_homework_return_true():
    good_student = Student('Lev', 'Sokolov')
    opp_teacher = Teacher('Daniil', 'Shadrin')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    opp_teacher.check_homework(result_1)

    assert opp_teacher.check_homework(result_1)
