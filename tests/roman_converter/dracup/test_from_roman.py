from types import ModuleType

def test_from_roman(impl: ModuleType):
    # Minimal and maximal
    assert impl.from_roman("I") == 1
    assert impl.from_roman("MMMCMXCIX") == 3999

    # Basic additive numbers
    assert impl.from_roman("II") == 2
    assert impl.from_roman("III") == 3
    assert impl.from_roman("VI") == 6
    assert impl.from_roman("VIII") == 8
    assert impl.from_roman("XI") == 11
    assert impl.from_roman("XX") == 20

    # Subtractive notation
    assert impl.from_roman("IV") == 4
    assert impl.from_roman("IX") == 9
    assert impl.from_roman("XL") == 40
    assert impl.from_roman("XC") == 90
    assert impl.from_roman("CD") == 400
    assert impl.from_roman("CM") == 900

    # Mixed numbers
    assert impl.from_roman("LVIII") == 58
    assert impl.from_roman("MCMXCIV") == 1994
    assert impl.from_roman("MMCDXXI") == 2421