from spell import spell

def test_single_digits():
    assert spell(0) == 'zero'
    assert spell(1) == 'one'
    assert spell(2) == 'two'
    assert spell(3) == 'three'
    assert spell(4) == 'four'
    assert spell(5) == 'five'
    assert spell(6) == 'six'
    assert spell(7) == 'seven'
    assert spell(8) == 'eight'
    assert spell(9) == 'nine'

def test_teens():
    assert spell(10) == 'ten'
    assert spell(11) == 'eleven'
    assert spell(12) == 'twelve'
    assert spell(13) == 'thirteen'
    assert spell(14) == 'fourteen'
    assert spell(15) == 'fifteen'
    assert spell(16) == 'sixteen'
    assert spell(17) == 'seventeen'
    assert spell(18) == 'eighteen'
    assert spell(19) == 'nineteen'

def test_tens():
    assert spell(20) == 'twenty'
    assert spell(21) == 'twenty one'
    assert spell(30) == 'thirty'
    assert spell(55) == 'fifty five'
    assert spell(99) == 'ninety nine'

def test_hundreds():
    assert spell(100) == 'one hundred'
    assert spell(101) == 'one hundred and one'
    assert spell(117) == 'one hundred and seventeen'
    assert spell(500) == 'five hundred'
    assert spell(523) == 'five hundred and twenty three'
    assert spell(999) == 'nine hundred and ninety nine'

def test_thousands():
    assert spell(1000) == 'one thousand'
    assert spell(1001) == 'one thousand and one'
    assert spell(1010) == 'one thousand and ten'
    assert spell(1500) == 'one thousand five hundred'
    assert spell(1520) == 'one thousand five hundred and twenty'
    assert spell(1525) == 'one thousand five hundred and twenty five'
    assert spell(10000) == 'ten thousand'
    assert spell(15432) == 'fifteen thousand four hundred and thirty two'
    assert spell(99999) == 'ninety nine thousand nine hundred and ninety nine'

def test_millions():
    assert spell(1000000) == 'one million'
    assert spell(1000001) == 'one million and one'
    assert spell(9876543) == 'nine million eight hundred and seventy six thousand five hundred and forty three'
