from .main import CreateJob


def test_summary():
    obj_test = CreateJob(1, 2)
    assert obj_test.get_summary() == 3
