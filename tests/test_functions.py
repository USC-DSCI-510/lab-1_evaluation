import pytest

try:
    import glob
    import importlib
    script_path = glob.glob('./lab1.py')[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except:
    raise Exception(
        'No script is available. Please follow the assignment instructions.')

try:
    degrees_to_radians = module.degrees_to_radians
    vowel_count = module.vowel_count
    triangle_hypotenuse = module.triangle_hypotenuse
except:
    raise Exception(
        'Please ensure all required functions have been implemented.')


@pytest.mark.parametrize('degree, radian', [
    (1, 0.017),
    (108, 1.885),
    (0, 0),
    (360, 6.283),
    (180, 3.142),
    (90, 1.571),
    (45, 0.785),
    (30, 0.524),
    (60, 1.047),
    (120, 2.094),
    (150, 2.618),
    (240, 4.189),
    (270, 4.712),
    (300, 5.236),
    (330, 5.759),
    (45, 0.785),
    (135, 2.356),
    (225, 3.927),
    (315, 5.498),
    (405, 7.069),
])
def test_degrees_to_radians(degree, radian):
    assert pytest.approx(degrees_to_radians(degree), abs=1e-3) == radian


@pytest.mark.parametrize('s, count', [
    ('sentence', 3),
    ('aeiou', 5),
    ('', 0),
    ('bcdfghjklmnpqrstvwxyz', 0),
    ('aeiouAEIOU', 10),
    ('aeiouAEIOUbcdfghjklmnpqrstvwxyz', 10),
    ('aeiouAEIOUbcdfghjklmnpqrstvwxyzaeiouAEIOU', 20),
    ('aeiouAEIOUbcdfghjklmnpqrstvwxyzaeiouAEIOUaeiouAEIOUbcdfghjklmnpqrstvwxyz', 30),
    ('aeiouAEIOUbcdfghjklmnpqrstvwxyzaeiouAEIOUaeiouAEIOUbcdfghjklmnpqrstvwxyzaeiouAEIOU', 40),
    ('test', 1),
    ('TEST', 1),
    ('tEst', 1),
    ('tESt', 1)
])
def test_vowel_count(s, count):
    assert vowel_count(s) == count


@pytest.mark.parametrize('base, height, result', [
    (3, 4, 5),
    (1, 1, 1.414),
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 2, 2.828),
    (3, 3, 4.243),
    (4, 4, 5.657),
    (5, 5, 7.071)
])
def test_triangle_hypotenuse(base, height, result):
    assert pytest.approx(triangle_hypotenuse(base, height), abs=1e-3) == result
