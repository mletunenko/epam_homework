from homework6.task01 import instances_counter


def test_instances_counter_positive_get_two_instance():
    @instances_counter
    class SomeClass:
        def __init__(self, some_attribute):
            self.some_attribute = some_attribute

    _ = SomeClass(1)
    _ = SomeClass(2)
    assert SomeClass.get_created_instances() == 2


def test_instances_counter_positive_get_zero_instance():
    @instances_counter
    class SomeClass:
        def __init__(self, some_attribute):
            self.some_attribute = some_attribute

    assert SomeClass.get_created_instances() == 0


def test_instances_counter_positive_reset_counter():
    @instances_counter
    class SomeClass:
        def __init__(self, some_attribute):
            self.some_attribute = some_attribute

    _ = SomeClass(1)
    SomeClass.reset_instances_counter()
    assert SomeClass.get_created_instances() == 0


def test_instances_counter_positive_check_reset_return_value():
    @instances_counter
    class SomeClass:
        def __init__(self, some_attribute):
            self.some_attribute = some_attribute

    _ = SomeClass(1)
    assert SomeClass.reset_instances_counter() == 1


def test_instances_counter_positive_counter_after_reset():
    @instances_counter
    class SomeClass:
        def __init__(self, some_attribute):
            self.some_attribute = some_attribute

    _ = SomeClass(1)
    SomeClass.reset_instances_counter()
    _ = SomeClass(1)
    assert SomeClass.get_created_instances() == 1
