from matematika import sudetis, daugyba, rask_didziausia, pasisveikinimas
import matematika
import pytest

def test_sudetis():
  assert sudetis(1,2) == 3
  
def test_sudetis_neigiami():
  assert sudetis(-1,-5) == -6
def test_daugyba():
  assert daugyba(2,5) == 10
  assert daugyba(5,5) > 0
  assert daugyba(-5,-5) > 0
  assert daugyba(-5, 5) < 0
  
def test_sudetis_2():
  num1, num2 = 5, 3
  results = 8
  faktinis_rezultatas = sudetis(num1, num2)
  assert results == faktinis_rezultatas, f'sudeties testas nepavyko: {num1} + {num2} turetu buti {results}, bet gavome {faktinis_rezultatas}'
 
def test_rask_didziausia():
  num1, num2 = 10, 20
  rezultatas = 20
  faktinis_rezultatas = rask_didziausia(num1,num2)
  assert faktinis_rezultatas == rezultatas 
  
def test_rask_didziausia_2():
  assert rask_didziausia(10,5) == 10
  assert rask_didziausia(5,10) == 10
  assert rask_didziausia(10,10) == 10
def test_pasisveikinimas():
  assert pasisveikinimas('Tomas') == 'Labas, Tomas'
  
def test_pasisveikinimas_2():
  assert matematika.pasisveikinimas('Romas') == 'Labas, Romas'
  
# def pirmas_sarase(sarasas:list):
#     return sarasas[0] if sarasas else None
def test_pirmas_sarase():
  skaiciai = [1,2,3,4,5]
  assert matematika.pirmas_sarase(skaiciai) == 1
  
def test_pirmas_sarase_tekstas():
  raides = ['a', 'b', 'c']
  assert matematika.pirmas_sarase(raides) == 'a'
  
def test_pirmas_tuscias():
  skaiciai = []
  assert matematika.pirmas_sarase(skaiciai) == None
  
def test_pirmas_sarase_tekstas_2():
  tekstas = 'labas'
  assert matematika.pirmas_sarase(tekstas) == 'l'

@pytest.mark.parametrize('sarasas, tiketinas_rezultatas', [
    ([1,2,3,4], 1),
    (['a', 'b', 'c'], 'a'),
    ([], None),
    ([[1,2],[3,4], [5,6]], [1,2])
])
def test_gauti_pirma_elementa(sarasas, tiketinas_rezultatas):
    assert matematika.pirmas_sarase(sarasas)  == tiketinas_rezultatas

@pytest.mark.parametrize('a, b, c, turis', [(1,1,1,1), (2,3,2,12), (5,6,18,540)])

def test_kubo_turis(a, b, c, turis):
    assert matematika.kubo_turis(a,b,c) == turis