import uzduotis_1
from uzduotis_1 import apversta, sar_suma, sar_teigiami, rikiuoti, rikiuoti_mazejanciai, rikiuoti_didejant
import pytest

def test_apversta():
    tekstas = 'zodis'
    assert uzduotis_1.apversta(tekstas) == 'sidoz'

def test_apversta_2():
    tekstas = 'labanaktis'
    assert uzduotis_1.apversta(tekstas) == 'sitkanabal'

def test_sar_suma():
    skaiciai = [2,3,7]
    assert uzduotis_1.sar_suma(skaiciai) == 12

def test_sar_suma_2():
    skaiciai = [3,5,6,8,2]
    assert uzduotis_1.sar_suma(skaiciai) == 24

def test_sar_teigiami():
    sarasas = [5,7,-5,8,6,-2,1]
    assert uzduotis_1.sar_teigiami(sarasas) == [5,7,8,6,1]

def test_rikiuoti_mazejanciai():
    assert rikiuoti(rikiuoti_mazejanciai, [4,5,1,3]) == [5,4,3,1]

def test_rikiuoti_didejant():
    assert rikiuoti(rikiuoti_didejant, [4,5,1,3]) == [1,3,4,5]

# nauju uzd testavimas

@pytest.mark.parametrize('a, dalyba', [(9, 'Dalinasi'), (8, 'Nesidalina'), (15, 'Dalinasi')])
def test_dalyba_3(a, dalyba):
    assert uzduotis_1.dalyba_3(a) == dalyba

@pytest.mark.parametrize('zodziai, atsakymas', [(['labas','rytas','kava'], ['labas','kava']), (['vakaras','puodelis','kate'], ['vakaras'])])
def test_rasti_pasikartojancias_raides(zodziai, atsakymas):
    assert uzduotis_1.rasti_pasikartojancias_raides(zodziai) == atsakymas

@pytest.mark.parametrize('a, atsakymas', [(3, True), (4, False), (7, True)])
def test_pirminis(a, atsakymas):
    assert uzduotis_1.pirminis(a) == atsakymas