import time
import os

def soma():
  os.system('cls')
  n1 = float(input("Primeiro numero: "))
  n2 = float(input("Segundo numero: "))
  print("Resultado da Soma: ",n1+n2)
  time.sleep(3)
  os.system('cls')

def sub():
  os.system('cls')
  n1 = float(input("Primeiro numero: "))
  n2 = float(input("Segundo numero: "))
  print("Resultado da Subtração: ",n1-n2)
  time.sleep(3)
  os.system('cls')

def mult():
  os.system('cls')
  n1 = float(input("Primeiro numero: "))
  n2 = float(input("Segundo numero: "))
  print("Resultado da Multiplicação: ",n1*n2)
  time.sleep(3)
  os.system('cls')

def div():
  os.system('cls')
  n1 = float(input("Primeiro numero: "))
  n2 = float(input("Segundo numero: "))
  print("Resultado da Divisão: ",n1/n2)
  time.sleep(3)
  os.system('cls')

while True:
  os.system('cls')
  print("-------------- CALCULADORA --------------")
  print("1. Somar")
  print("2. Subtrair")
  print("3. Multiplicação")
  print("4. Divisão ")
  print("0. Sair")
  menu = int(input("Opção: "))

  if(menu==1):
    soma()
  if(menu==2):
    sub()
  if(menu==3):
    mult()
  if(menu==4):
    div()
  if(menu==0):
    os.system('cls')
    raise SystemExit
  print("-----------------------------------------")