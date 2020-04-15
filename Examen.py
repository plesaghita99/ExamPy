"""
Modulul următor are ca scop diferentierea mașinilor produse intr-o singura zi in loturi (pana in 20), in funcție de poziția volanului  și de serie
"""
 # Documentatie: 20p
 # 	a) adaugati type hits 5p
	# a) documentati modulul 5p
	# b) documentati clasele 5p
	# c) documentati metodele 5p
class Fabrica:
    """
    O clasa care reprezinta o fabrica

    ...

    Atribute
    ---------
    start_serie : int
        seria de inceput
    numar_total : int
        numarul de bucati

    Metode
    ------
    volan_pe_stanga()
        Functia primeste o valoare si o verifica daca este para, daca este para o incrementeaza pentru a fi impara, dupa care initializeaza valoarea maxima si returneaza
        o lista mergand cu step-ul de 2
    volan_pe_dreapta()
        Functia primeste o valoare si o verifica daca este impara, daca este para o incrementeaza pentru a fi para,dupa care initializeaza valoarea maxima si returneaza
        o lista mergand cu step-ul de 2


    """
  def __init__(self, start_serie:int, numar_total:int):
    # Salveaza valorile
    self.start_serie = start_serie
    self.numar_total = numar_total

  def volan_pe_stanga(self) -> int:
    # Initializeaza valoare de la care se porneste
    start = self.start_serie
    # Daca este para se incrementeaza pentru a fi impara
    if start % 2 == 0:
      start += 1
    # Initializeaza valoarea maxima
    final = self.start_serie + self.numar_total
    # Se returneaza o lista - mergand din 2 in 2
    return list(range(start, final))[::2]

  def volan_pe_dreapta(self) -> int:
    # Initializeaza valoare de la care se porneste
    start = self.start_serie
    # Daca este impara se incrementeaza pentru a fi para
    if start % 2 == 1:
      start += 1
    # Initializeaza valoarea maxima
    final = self.start_serie + self.numar_total
    # Se returneaza o lista - mergand din 2 in 2
    return list(range(start, final))[::2]

  def __iter__(self):
    # Initializare seria de la care se porneste
    self.serie_generata = self.start_serie
    return self

  def __next__(self) -> int:
    # Numarul maxim la care poate ajunge seria
    maxim = self.start_serie + self.numar_total
    # Se testeaza daca s-a generat si ultima serie
    if self.serie_generata < maxim:
      # Se verifica daca poatae genera un lot intreg - 20 de serii
      if self.serie_generata + 20 < maxim:
        start = self.serie_generata
        stop = self.serie_generata + 20
        self.serie_generata = stop
        lot = list(range(start, stop))
        return lot
      else:
        # Se genereaza pana la ultima serie posibila
        start = self.serie_generata
        stop = maxim
        self.serie_generata = maxim
        lot = list(range(start, stop))
        return lot
    else:
      raise StopIteration

if _name_ == '_main_':
  fabrica = Fabrica(13589, 50)
  serii = fabrica.volan_pe_dreapta()
  print(serii)
  serii = fabrica.volan_pe_stanga()
  print(serii)
  loturi = iter(fabrica)
  with open('fisier', 'w+') as file:
    for lot in loturi:
      file.write(str(lot))