#!/usr/bin/env python3
# -*- coding: utf-8 -*-

msg ="Bem vindo ao calculador de massa corporal"
print(msg)
altura = input("Qual a sua altura? ")
altura = float(altura)
peso = input("Qual o seu peso? ")
peso = float(peso)
mc = peso /(altura ** 2)
print("Seu valor de IMC � de ",mc)

# Condi��es para classifica��o do IMC
if mc < 18.5:
    print('Esta valor � classificado como Baixo peso.')
elif 18.5 <= mc <= 24.9:
    print('Este valor � classificado como Peso normal.')
elif 25 <= mc <= 29.9:
    print('Este valor � classificado como Sobrepeso.')
elif 30 <= mc <= 34.9:
    print('Este valor � classificado como Obesidade grau I.')
elif 35 <= mc <= 39.9:
    print('Este valor � classificado como Obesidade grau II.')
else:
    print('Este valor � classificado como Obesidade grau III.')
