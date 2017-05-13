import doctest


def test_all():
    """Run all tests."""
    return doctest.DocFileSuite('README.rst')
