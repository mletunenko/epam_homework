from homework3.task03 import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "age": "18",
        "sex": "male",
    },
    {
        "name": "Maria",
        "last_name": "Let",
        "age": "18",
        "sex": "female",
    }
]


def test_apply_method_positive_even_numbers():
    filters = Filter([lambda a: a % 2 == 0, lambda a: a > 0,
                      lambda a: isinstance(a, int)])
    assert filters.apply(range(10)) == [2, 4, 6, 8]


def test_apply_method_non_existing_keyword():
    assert make_filter(hobby='Let').apply(sample_data) == []


def test_apply_method_no_suotable_obj():
    assert make_filter(age='50').apply(sample_data) == []
