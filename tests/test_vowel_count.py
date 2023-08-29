import pytest

try:
    import glob
    import importlib
    # script_path = glob.glob('./../lab1.py')[0]
    # module_path = script_path[2:-3]
    # module = importlib.import_module(module_path)

    SCRIPT_PATH = './../lab1.py'
    module = importlib.import_module(SCRIPT_PATH)
except:
    raise Exception(
        'No script is available. Please follow the assignment instructions.')

try:
    # degrees_to_radians = module.degrees_to_radians
    vowel_count = module.vowel_count
    # triangle_hypotenuse = module.triangle_hypotenuse
except:
    raise Exception(
        'Please ensure all required functions have been implemented.')


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
