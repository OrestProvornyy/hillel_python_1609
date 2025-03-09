import pytest
def greeting(name):
    return f'hello {name}'


@pytest.mark.parametrize('name', [
    ('Alex', 'hello Alex'),
    ('Bob', 'hello Bob'),
    ('Den', 'hello Den')],
                         ids=['Alex', 'Bob', 'Den'])
def test_greetings(name, expected):
    actual_result = greeting(name)

    assert  expected_result == actual_result

@pytest.mark.parametrize('name', [
    12, 23.1])
def test_greetings_negative_type_error(name):
    with pytest.raises(TypeError)
        greeting(name)