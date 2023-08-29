import pytest

try:
    import glob
    import importlib
    script_path = glob.glob('./lab1.py')[0]
    module_path = script_path[2:-3]
    # SCRIPT_PATH = './lab1.py'
    module = importlib.import_module(module_path)
except:
    raise Exception(
        'No script is available. Please follow the assignment instructions.')

try:
    # degrees_to_radians = module.degrees_to_radians
    # vowel_count = module.vowel_count
    triangle_hypotenuse = module.triangle_hypotenuse
except:
    raise Exception(
        'Please ensure all required functions have been implemented.')


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
