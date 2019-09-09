
# POLIMORFIZM

# Oznacza, że można wysłać ten sam komunikat do obiektów różnych klas powiązanych poprzez dziedziczenie, oraz osiągnąć różne, odpowiednie dla konkretnego obiektu wyniki

print("\tPrzykład 1")


class Zwierze():
	def __str__(self):
		return self.__class__.__name__
	

class Kot(Zwierze):
	pass


z = Zwierze()
print(z)

k = Kot()
print(k)

print("\tPrzykład 1")


class Zwierzak:
	def jedz(self, jedzenie):
		print(self.__class__.__name__, "je", jedzenie)


class Pies(Zwierzak):
	pass


class Kot(Zwierzak):
	pass


def nakarm(zwierzak):
	if not isinstance(zwierzak, Zwierzak):
		raise TypeError("Musi być zwierzak")
	if isinstance(zwierzak, Pies):
		zwierzak.jedz("karme dla psa")
	elif isinstance(zwierzak, Kot):
		zwierzak.jedz("karme dla kota")


kot = Kot()
pies = Pies()

nakarm(pies)
nakarm(kot)
