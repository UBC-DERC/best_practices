from best_practices import sample_function

def test_package_load():
    assert sample_function(1)
    assert sample_function(0) is False
