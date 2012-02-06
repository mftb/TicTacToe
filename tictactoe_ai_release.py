#!/usr/bin/env python
# -*- coding: latin1 -*-


# preciso deixar esse script no estilo de codificação do python...



# jogo da velha com IA
# o tabuleiro eh um vetor de 0 ate 8 assim:
# 0 1 2
# 3 4 5
# 6 7 8

# algoritmo por Lucas Lima e Matheus Boy
# script em python por Matheus Boy

# ainda bem que resolvi fazer isso em python...

import random

# para poder usar a função "system" do c
import ctypes
clib = ctypes.cdll.LoadLibrary("libc.so.6")


# funções

def vence(jogador, grid):
    """
    
    Decide o lugar para jogar para vencer ou obstruir uma jogada,
    se não houver lugar passível de vitória, retorna -1
    
    O parâmetro jogador identifica se é humano ou IA
    
    O parâmetro grid é a lista que representa o tabuleiro
    
    
    """
    
    # tudo feito na mão: todos os 24 casos passíveis de vitória
    lista = [[0,1,2],[0,2,1],[1,2,0],[3,4,5],[3,5,4],[4,5,3],[6,7,8],[6,8,7],
            [7,8,6],[0,3,6],[0,6,3],[3,6,0],[1,4,7],[1,7,4],[4,7,1],[2,5,8],
            [2,8,5],[5,8,2],[0,4,8],[0,8,4],[4,8,0],[2,4,6],[2,6,4],[4,6,2]]
    for i in range(0, 24):
        if (grid[lista[i][0]] == jogador and grid[lista[i][1]] == jogador
            and grid[lista[i][2]] == 0):
            return lista[i][2]
    # se chegar aqui é porque não tem possibilidade alguma de vitória
    return -1

def randnumedge():
    """
    
    Retorna uma quina aleatória
    
    """
    
    rand = random.randrange(0, 100)
    rand = rand % 4
    
    # se for 0 ou 2 fica sendo ele mesmo
    
    if rand == 1:
        rand = 6
    elif rand == 3:
        rand = 8
    return rand

def tela(grid):
    """
    
    Imprime o tabuleiro na tela
    
    O parâmetro grid é o tabuleiro de jogo, no caso, uma lista
    
    """
    t = []
    for i in range(0, 9):
        t.append(" ")
    i = 0
    for i in range(0, 9):
        if grid[i] == -1:
            t[i] = "X"        
        if grid[i] == 1:
            t[i] = "O"
    print ("\n%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s\n" % 
            (t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8]))
    
def info(op=0):
    """
    
    Imprime as instruções de jogo na tela
    
    O parâmetro op é opcional para definir
    se imprime a apresentação de começo de jogo
    
    """

    # limpada no terminal
    clib.system("clear")
    if op == 1:
        print "Bem vindo ao jogo da velha assitido por IA."
    print "O tabuleiro é ordenado da seguinte forma:"
    print " "
    print "0 1 2"
    print "3 4 5"
    print "6 7 8"
    print " "
    print "Onde cada número corresponde a casa do tabuleiro."
    print "Para jogar você deve digitar o numero da casa em que quer jogar."
    print "X == IA; O == Você"
    if op == 1:
        print "A IA começa jogando..."
    print " "
    print " "


def scan(grid):
    """
    
    Função para entrada de dados no programa, evitando erros e bugs.
    
    Serve basicamente para deixar o programa bullet-proof.    
    
    """
    
    pos = -1
    msg = "Entrada invalida. Por favor entre com valor válido: "

    while (pos < 0) or (pos > 8) or (grid[pos] != 0):
        try:
            pos = int(raw_input())
            while (pos < 0) or (pos > 8) or (grid[pos] != 0):
                print "Entrada invalida. Por favor entre com valor válido: "
                pos = int(raw_input())
        except ValueError:
            print msg
        # SystemExit é uma forma "bonita" - a.k.a. menos feia
        # de se encerrar a execução do script
        except EOFError:
            clib.system("clear")
            raise SystemExit
        except KeyboardInterrupt:
            clib.system("clear")
            raise SystemExit
    return pos



# ajustes iniciais        
flag = 1
cont = 9
grid = range(0, 9)
for i in range(0, 9):
    grid[i] = 0



    
# aqui considera-se a IA jogando primeiro    
info(1)
# passo 1 do algoritmo

rand = randnumedge()
   
# IA: -1 // Humano: 1  // Vazio: 0

grid[rand] = -1

cont = cont - 1

print "A IA jogou em " + str(rand) + " Onde voce vai jogar? "
tela(grid)
# passo 2 do algoritmo

pos = scan(grid)
# humano entrou com uma posicao valida

grid[pos] = 1
tela(grid)
cont = cont - 1

# agora comeca a IA
# passo 2.1 do algoritmo

if (pos == 0) or (pos == 2) or (pos == 6) or (pos == 8):

    # passo 2.1.1 do algoritmo
    
    rand = randnumedge()
    while (grid[rand] != 0):
        rand = randnumedge()
    grid[rand] = -1
    
    
    info()
    print "A IA jogou em " + str(rand) + " Onde voce vai jogar? "
    tela(grid)
    # passo 2.1.2
    
    pos = scan(grid)
    grid[pos] = 1
    tela(grid)
    
    # passo 2.1.3
    # testa se o humano eh burro
    if vence(-1,grid) != -1:
        info()
        print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
        grid[vence(-1,grid)] = -1
        tela(grid)
    # se chegou até aqui o cabra não é burro
    else:
        # passo 2.1.4
        for i in [0,2,6,8]:
            if grid[i] == 0:
                rand = i
        grid[rand] = -1
        info()
        print "A IA jogou em " + str(rand) + " Onde voce vai jogar? "
        tela(grid)
        # passo 2.1.5
        pos = scan(grid)
        grid[pos] = 1
        tela(grid)
        # passo 2.1.6
        info()
        print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
        grid[vence(-1,grid)] = -1
        tela(grid)        
            
# passo 2.2 do algoritmo
elif ((pos % 2) == 1):
    rnd = random.randrange(0,100)
    rnd = rnd % 2
    # passo 2.2.1
    info()
    if (rand == 0):
        if (pos != 1) and (pos != 3):
            if (rnd):
                grid[2] = -1
                print "A IA jogou em 2" + " Onde voce vai jogar? "
            else:
                grid[6] = -1
                print "A IA jogou em 6" + " Onde voce vai jogar? "
        if (pos == 1):
            grid[6] = -1
            print "A IA jogou em 6" + " Onde voce vai jogar? "
        if (pos == 3):
            grid[2] = -1
            print "A IA jogou em 2" + " Onde voce vai jogar? "
    elif (rand == 2):
        if (pos != 1) and (pos != 5):
            if (rnd):
                grid[0] = -1
                print "A IA jogou em 0" + " Onde voce vai jogar? "
            else:
                grid[8] = -1
                print "A IA jogou em 8" + " Onde voce vai jogar? "
        if (pos == 1):
            grid[8] = -1
            print "A IA jogou em 8" + " Onde voce vai jogar? "
        if (pos == 5):
            grid[0] = -1
            print "A IA jogou em 0" + " Onde voce vai jogar? "
    elif (rand == 6):
        if (pos != 3) and (pos != 7):
            if (rnd):
                grid[0] = -1
                print "A IA jogou em 0" + " Onde voce vai jogar? "
            else:
                grid[8] = -1
                print "A IA jogou em 8" + " Onde voce vai jogar? "
        if (pos == 3):
            grid[8] = -1
            print "A IA jogou em 8" + " Onde voce vai jogar? "
        if (pos == 7):
            grid[0] = -1
            print "A IA jogou em 0" + " Onde voce vai jogar? "        
    else:
        if (pos != 5) and (pos != 7):
            if (rnd):
                grid[2] = -1
                print "A IA jogou em 2" + " Onde voce vai jogar? "
            else:
                grid[6] = -1
                print "A IA jogou em 6" + " Onde voce vai jogar? "
        if (pos == 5):
            grid[6] = -1
            print "A IA jogou em 6" + " Onde voce vai jogar? "
        if (pos == 7):
            grid[2] = -1
            print "A IA jogou em 2" + " Onde voce vai jogar? "        
    # passo 2.2.2     
    tela(grid)
    pos = scan(grid)
    grid[pos] = 1
    tela(grid)
    # passo 2.2.3
    if vence(-1,grid) != -1:
        info()
        print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
        grid[vence(-1,grid)] = -1
        tela(grid)
    else:
        # passo 2.2.4
        grid[4] = -1
        info()
        print "A IA jogou em 4" + " Onde voce vai jogar? "
        tela(grid)
    
        # passo 2.2.5
        pos = scan(grid)
        grid[pos] = 1
        tela(grid)
        # passo 2.2.6
        info()
        print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
        grid[vence(-1,grid)] = -1
        tela(grid)
# agora fudeu último passo do algoritmo
# passo 2.3
elif (pos == 4):
    # passo 2.3.1
    info()
    if (rand == 0):
        grid[8] = -1
        print "A IA jogou em 8" + " Onde voce vai jogar? "
    elif (rand == 8):
        grid[0] = -1
        print "A IA jogou em 0" + " Onde voce vai jogar? "
    elif (rand == 2):
        grid[6] = -1
        print "A IA jogou em 6" + " Onde voce vai jogar? "
    elif (rand == 6):
        grid[2] = -1
        print "A IA jogou em 2" + " Onde voce vai jogar? "
    cont = cont - 1
    tela(grid)
    # passo 2.3.2
    pos = scan(grid)
    grid[pos] = 1
    tela(grid)
    cont = cont -1
    # passo 2.3.3
    # a.k.a. prevencao de vitoria do adversário
    info()
    print "A IA jogou em " + str(vence(1,grid)) + " Onde voce vai jogar? "
    grid[vence(1,grid)] = -1
    tela(grid)
    cont = cont - 1
    # passo 2.3.4
    while (cont > 0) and (flag != 0):
        pos = scan(grid)
        grid[pos] = 1
        tela(grid)
        cont = cont -1       
        # passo 2.3.4.1    
        # verificar se a IA pode vencer, se puder, vença senão 
        # verificar se o humano pode vencer, se puder, obstrua
        if vence(-1,grid) != -1:
            info()
            print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
            grid[vence(-1,grid)] = -1
            tela(grid)
            # essa merda existe porque tô com preguiça de corrigir a identação
            flag = 0
                
        # testa onde o humano pode vencer para obstruir a jogada
        if (flag != 0):
            if (cont > 1):
                info()
                print ("A IA jogou em " + str(vence(1,grid)) 
                        + " Onde voce vai jogar? ")
                grid[vence(1,grid)] = -1
                tela(grid)
            else:
                info()
                if (grid[0] == 1) and (grid[8] == 0):
                    grid[8] = -1
                    print "A IA jogou em 8" + " Empate!"
                elif (grid[2] == 1) and (grid[6] == 0):    
                    grid[6] = -1
                    print "A IA jogou em 6" + " Empate!"
                elif (grid[6] == 1) and (grid[2] == 0):    
                    grid[2] = -1
                    print "A IA jogou em 2" + " Empate!"    
                elif (grid[8] == 1) and (grid[0] == 0):    
                    grid[0] = -1
                    print "A IA jogou em 0" + " Empate!" 
                elif (grid[1] == 1) and (grid[7] == 0):    
                    grid[7] = -1
                    print "A IA jogou em 7" + " Empate!" 
                elif (grid[3] == 1) and (grid[5] == 0):    
                    grid[5] = -1
                    print "A IA jogou em 5" + " Empate!" 
                elif (grid[5] == 1) and (grid[3] == 0):    
                    grid[3] = -1
                    print "A IA jogou em 3" + " Empate!" 
                elif (grid[7] == 1) and (grid[1] == 0):    
                    grid[1] = -1
                    print "A IA jogou em 1" + " Empate!" 
                tela(grid)
            cont = cont - 1
print " "
print " "
