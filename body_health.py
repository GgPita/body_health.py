#!/usr/bin/python3

from sklearn import tree

print(f"\nBem vindo ao programa Body health. Ele irá dizer como estará seu corpo em 30 anos de acordo com seus hábitos\n")

diariamente = "1"
esporadicamente = "2"
nunca = "3"
saudável = "1"
normal = "2"
estragado = "3"

saude=[["10", "30", diariamente, diariamente, diariamente], ["15", "5", esporadicamente, esporadicamente, esporadicamente], ["4", "7", nunca, nunca, nunca]]

resultado=[saudável, normal, estragado]

classificador=tree.DecisionTreeClassifier()
classificador=classificador.fit(saude,resultado)

atividade_fisica=input("Digite a porcentagem do seu tempo que voce passa fazendo atividade física: ")
sono_tempo=input("Digite a porcentagem do seu tempo que voce passa dormindo: ")
comer_frutas=input("Digite a frenquencia que come frutas 1-diariamente, 2-esporadicamente ou 3-nunca): ")
refeiçoes=input("Digite a frequencia que faz 3 refreições 1-diariamente 2-esporadicamente ou 3-nunca): ")
tomar_sol=input("Digite a frequencia que toma sol 1-diariamente, 2-esporadicamente ou 3-nunca): ")

resultadousuario=classificador.predict([[atividade_fisica, sono_tempo, comer_frutas, refeiçoes, tomar_sol]])


if resultadousuario == "1":
    print(f"\nSeu corpo estará saudavel daqui 30 anos")
elif resultadousuario == "2":
    print(f"\nSeu corpo estará normal daqui 30 anos")
elif resultadousuario == "3":
    print(f"\nSeu corpo estará estragado daqui 30 anos")
else:
    print("resultado invalido")
