import pytest

try:
    import glob
    import importlib
    # script_path = glob.glob('./../lab1.py')[0]
    # module_path = script_path[2:-3]
    # module = importlib.import_module(module_path)

    SCRIPT_PATH = './lab1.py'
    module = importlib.import_module(SCRIPT_PATH, package="lab1")
except:
    raise Exception(
        'No script is available. Please follow the assignment instructions.')

try:
    degrees_to_radians = module.degrees_to_radians
    # vowel_count = module.vowel_count
    # triangle_hypotenuse = module.triangle_hypotenuse
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
