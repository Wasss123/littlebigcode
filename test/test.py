import pytest
import extract

expected = {'D1': 'doliprane', 'T2': 'paracetamol'}
def test_extract_drugs(filename = "./resources/drugstest.csv"):
    """
    test_extract_drugs: tests the extract_drugs function in extract.py file

    filename : path of test set

    return:
    """
    result = extract.extract_drugs(filename)
    assert result == expected, f"Test of drugs extraction succeeded"
test_extract_drugs()
