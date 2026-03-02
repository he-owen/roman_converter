from types import ModuleType


def test_to_roman(impl: ModuleType):
    assert impl.to_roman(4) == "IV"
    # Minimal and maximal
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(3999) == "MMMCMXCIX"

    # Basic additive numbers
    assert impl.to_roman(2) == "II"
    assert impl.to_roman(3) == "III"
    assert impl.to_roman(6) == "VI"
    assert impl.to_roman(8) == "VIII"
    assert impl.to_roman(11) == "XI"
    assert impl.to_roman(20) == "XX"

    # Subtractive notation
    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    assert impl.to_roman(40) == "XL"
    assert impl.to_roman(90) == "XC"
    assert impl.to_roman(400) == "CD"
    assert impl.to_roman(900) == "CM"

    # Mixed numbers
    assert impl.to_roman(58) == "LVIII"       
    assert impl.to_roman(1994) == "MCMXCIV"  
    assert impl.to_roman(2421) == "MMCDXXI"  


