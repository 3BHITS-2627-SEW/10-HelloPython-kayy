## Dies ist ein kleines Cheat-Sheet fuer die
## verwendung von Python fuer C und C++ Programmierer

# Variablen
## C/C++: int eineZahl = 43;
import os
os.system("cls")

eineVariable = 13
print("Eine Variable: ",eineVariable)
eineVariable = "Bleeehhh"
print("Eine Variable: ",eineVariable)

# Typisierung in Python: Ducktyping

# Daher: bitte immer nach Moeglichkeit typisieren:
eineZweiteVariable : int = 14
print("Eine Zweite Variable: " ,eineZweiteVariable)
eineZweiteVariable = "bweh"
print("Eine Zweite Variable: " ,eineZweiteVariable)

datenTyp = type(eineVariable)
print("Datentyp von einerVariable: ", datenTyp)
eineVariable = 15
datenTyp = type(eineVariable)
print("Datentyp von einerVariable: ", datenTyp)