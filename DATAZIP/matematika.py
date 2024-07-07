
def sudetis(a, b):
  return a + b
def daugyba(a: int, b: int) -> int:
  """
  si funkcija sudaugina du pateiktus skaicius ir gazina sveikaji skaiciu (int).
  """
  return a * b
def rask_didziausia(a:int, b:int) -> int:
  return a if a > b else b
def pasisveikinimas(vardas):
  return f'Labas, {vardas}'
def pirmas_sarase(sarasas:list):
  return sarasas[0] if sarasas else None
  # if sarasas: # False, None , [], {}, ()

def kubo_turis(a,b,c):
    return a * b * c