"""
Tema4 - 40% din nota finala
Creati o functie care poate lua ca argument un obiect iterabil ce poate contine alte obiecte iterabile sau
ne iterabile. Se va itera peste toate obiectele iterabile de la orice nivel si se va crea o lista cu toate obiectele
ce nu pot si iterte sau in cazul string-urilor daca lungimea lor este 1
Nu uitati ca puteti folosi recursivitate

ex:
funtia primeste: [(1, 5), 'abc', {'x': 'y'}, [[[3]]], set()]
funtia returneaza [1, 5, 'a', 'b', 'c', 'x', 'y', 3]

"""
input = [(1, 5), 'abc', {'x': 'y'}, [[[3]]], set()]
output = [1, 5, 'a', 'b', 'c', 'x', 'y', 3]


def flatten(data):
    result = []
    for item in data:
        if not hasattr(item, '__iter__'):
            result.append(item)
        elif isinstance(item, str):
            for item2 in item:
                result.append(item2)
        elif isinstance(item, dict):
            result = result + (flatten(list(item.items())))
        else:
            for item2 in item:
                if hasattr(item2, '__iter__'):
                    result= result + (flatten(item2))
                else:
                    result.append(item2)

    return result


assert flatten(input) == output

