"""Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4"""

def points(games):
    i = 0
    for game in games:
        if game[0] > game[2]:
            i += 3
        elif game[0] == game[2]:
            i += 1
    return i
print(points(["3:1", "2:2", "0:1", "1:1", "3:3", "2:2", "1:1", "0:0", "3:2", "1:0"]))
    #return sum(3 if x > y else 1 if x == y else 0 for x, y in (map(int, game.split(':')) for game in games) ) 
#aqui se hace un split de los dos valores de cada string y se convierten a enteros, luego se hace la comparacion y se suman los puntos

def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))

lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
for i in range(0, len(lista)):
    lista2.append(lista[i*2])
    return lista2

#Given an array of integers, return a new array with each value doubled.
def maps(a):
    return [i*2 for i in a]

"""Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in."""
def century(year):
    return (year + 99) // 100   #se suma 99 para que el resultado sea el siglo correcto

"""Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel."""
def disemvowel(string): 
    return string.translate(None, "aeiouAEIOU") #se usa translate para eliminar las vocales