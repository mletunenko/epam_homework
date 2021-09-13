from homework4.task03 import my_precious_logger


def test_precious_logger_positive_err(capsys):
    my_precious_logger('error: some error')
    captured = capsys.readouterr()
    assert captured.err == 'error: some error'


def test_precious_logger_positive_ok(capsys):
    my_precious_logger('OK')
    captured = capsys.readouterr()
    assert captured.out == 'OK'
