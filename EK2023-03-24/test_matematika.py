from matematika import sudetis, daugyba

def test_sudetis():
    assert sudetis(1,2) == 3

def test_sudetis_neigiami():
    assert sudetis(-1, -5) == -6

def test_daugyba():
    assert daugyba(2,5)
    assert daugyba(5,5) > 0
    assert daugyba(-5,-5) > 0
    assert daugyba(-5, 5) < 0

def test_sudetis_2():
    num1, num2 = 5, 3
    rezultatas = 10
    faktinis_rezultatas = sudetis(num1, num2)
    assert rezultatas == faktinis_rezultatas, f'sudeties testas nepavyko: {num1} + {num2} turetu buti {rezultatas}, bet gavome {faktinis_rezultatas}'

def rask_didziausia(a:int, b:int) -> int:
    return a if a > b else b

def test_rask_didziausia():
    num1, num2 = 10, 20
    rezultatas = 20
    faktinis_rezultatas = rask_didziausia(num1, num2)
    assert faktinis_rezultatas == rezultatas

def test_rask_didziausia_2():
    assert rask_didziausia(10,5) == 10
    assert rask_didziausia(5,10) == 10
    assert rask_didziausia(10, 10) == 10