#!/usr/bin/env python
# -*- coding: latin1 -*-


# esse script já está no estilo de codificação do python


# jogo da velha com IA
# o tabuleiro eh um vetor de 0 ate 8 assim:
# 0 1 2
# 3 4 5
# 6 7 8


# algoritmo por Lucas Lima e Matheus Boy
# script em python por Matheus Boy


# release final do projeto TicTacToe


# BTW, ainda bem que fiz essa parada em python
# se fosse em C eu ia desistir no primeiro segfault


# o script foi testado exaustivamente, creio que não existem mais bugs
# este programa é um exemplo de que IA 
#pode ser^H^H^H^H^H^H^H^H é um monte de if's MWAHAHAHA


# na verdade, esse programa é muito sacana
# foi escrito de forma que uma possível vitória do jogador 
# não aparece explicitamente no código
# uma vitória seria na verdade um bug no código


# bibliotecas inclusas com o release padrão do python
import random
# para limpar o terminal:
import os

# funções

def vence(jogador, grid):
    """
    
    Decide o lugar para jogar para vencer ou obstruir uma jogada,
    se não houver lugar passível de vitória, retorna -1
    
    O parâmetro jogador identifica se é humano ou IA
    
    O parâmetro grid é a lista que representa o tabuleiro
    
    
    """
    
    # tudo feito no braço: todos os 24 casos passíveis de vitória
    # exemplo do Gambi Design Pattern "Eficiência primeiro" 
    #(evite escrever em várias linhas o que pode ser feito em uma)
    lista = [[0,1,2],[0,2,1],[1,2,0],[3,4,5],[3,5,4],[4,5,3],[6,7,8],[6,8,7],
            [7,8,6],[0,3,6],[0,6,3],[3,6,0],[1,4,7],[1,7,4],[4,7,1],[2,5,8],
            [2,8,5],[5,8,2],[0,4,8],[0,8,4],[4,8,0],[2,4,6],[2,6,4],[4,6,2]]
    # vale lembrar que em python, um modo POG de se simular uma matriz é fazer 
    # uma lista de listas LOL
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
    
    # essa função é meio POG...

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
    # código meio holístico, mas na verdade imprime o tabuleiro
    # um loop seria mais bonito que esse monte de parametros no print
    # mas não sei se rola fazer...
    print ("\n%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s\n" % 
            (t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8]))
    
def info(op=0):
    """
    
    Imprime as instruções de jogo na tela
    
    O parâmetro op é opcional para definir se imprime a apresentação 
    de começo de jogo
    
    """

    # limpada no terminal, só funciona no bash, se for command prompt nem funfa
    # tem como fazer essa parada ficar inteligente, verificando a versão do OS
    # mas eu to de boa de fazer isso por enquanto
    os.system("clear")
    if op == 1:
        print "Bem vindo ao jogo da velha assitido por IA."
    print "O tabuleiro é ordenado da seguinte forma:"
    print " "
    print "0|1|2"
    print "-+-+-"
    print "3|4|5"
    print "-+-+-"
    print "6|7|8"
    print " "
    print "Onde cada número corresponde a casa do tabuleiro."
    print "Para jogar você deve digitar o numero da casa em que quer jogar."
    print "X == IA; O == Você"
    if op == 1:
        print "Você começa jogando..."
    print " "
    print " "
    
    
def scan(grid):
    """
    
    Função para entrada de dados no programa, evitando erros e bugs.
    
    Serve basicamente para deixar o programa bullet-proof.    
    
    """
        
    pos = -1
    msg = "Entrada invalida. Por favor entre com valor válido:"

    while (pos < 0) or (pos > 8) or (grid[pos] != 0):
        try:
            pos = int(raw_input())
            while (pos < 0) or (pos > 8) or (grid[pos] != 0):
                print msg
                pos = int(raw_input())
        except ValueError:
            print msg
        # SystemExit é uma forma "bonita" - a.k.a. menos feia - 
        # de se encerrar a execução do script
        except EOFError:
            os.system("clear")
            raise SystemExit
        except KeyboardInterrupt:
            os.system("clear")
            raise SystemExit
    return pos

# nesta versão o usuário sempre começará jogando

# agora começa a brincadeira

# ajustes iniciais
quinas = [0, 2, 6, 8]
# flag faz parte de uma pog
flag = 1
cont = 9
# j também faz parte de uma pog
j = -1
# jeito meio pog de criar uma lista
grid = range(0, 9)
for i in range(0, 9):
    grid[i] = 0
    
info(1)    
  
pos = scan(grid)

# humano entrou com uma posicao valida

grid[pos] = 1
tela(grid)
cont -= 1

# usar in é mais elegante que um monte de and's e or's
if pos in quinas:
    # este foi o último algoritmo codificado
    # tem partes no código mais elegantes
    # o cara jogou na quina
    ini = pos
    info()
    grid[4] = -1
    print "A IA jogou em 4 Onde voce vai jogar?"
    cont -= 1
    tela(grid)
    pos = scan(grid)
    # humano entrou com uma posicao valida
    grid[pos] = 1
    sec = pos
    cont -= 1
    tela(grid)
    
    if (vence(1,grid) != -1):     
        info()   
        print "A IA jogou em " + str(vence(1,grid)) + " Onde voce vai jogar?"
        grid[vence(1,grid)] = -1
        cont -= 1
        tela(grid)
        pos = scan(grid)
        # humano entrou com uma posicao valida
        grid[pos] = 1
        cont -= 1
        tela(grid)
        
        # passo 4.1.2 do algoritmo II
        if (vence(-1,grid) != -1):
            info()
            print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
            grid[vence(-1,grid)] = -1
            tela(grid)
            flag = 0
        elif (vence(1,grid) != -1):
            info()   
            print ("A IA jogou em " + str(vence(1,grid)) + 
                    " Onde voce vai jogar?")
            grid[vence(1,grid)] = -1
            cont -= 1
            tela(grid)
            pos = scan(grid)
            # humano entrou com uma posicao valida
            grid[pos] = 1
            cont -= 1
            tela(grid)
            if (vence(-1,grid) != -1):
                info()
                print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
                grid[vence(-1,grid)] = -1
                tela(grid)
                flag = 0
            # passo 4.1.3.1.3    
            elif (vence(1,grid) != -1):
                info()   
                print ("A IA jogou em " + str(vence(1,grid)) + 
                        " Onde voce vai jogar?")
                grid[vence(1,grid)] = -1
                cont -= 1
                tela(grid)
            else:
                j = random.randrange(0, 9)
                while(grid[j] != 0):
                    j = random.randrange(0, 9)
                grid[j] = -1
                info()   
                print "A IA jogou em " + str(j) + " Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            if flag != 0:
                pos = scan(grid)
                # humano entrou com uma posicao valida
                grid[pos] = 1
                cont -= 1
                tela(grid)
        # passo 4.1.3.2
        else:
            lat = [1, 3, 5, 6]
            for l in lat:
                if grid[l] == 0:
                    grid[l] = -1
                    info()
                    print "A IA jogou em " + str(l) + " Onde voce vai jogar?"
                    break
            cont -= 1
            tela(grid)
            # passo 4.1.3.2.1
            pos = scan(grid)
            # humano entrou com uma posicao valida
            grid[pos] = 1
            cont -= 1
            tela(grid)
            # reaproveitando código =/
            if (vence(-1,grid) != -1):
                info()
                print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
                grid[vence(-1,grid)] = -1
                tela(grid)
                flag = 0
            elif (vence(1,grid) != -1):
                info()   
                print ("A IA jogou em " + str(vence(1,grid)) + 
                        " Onde voce vai jogar?")
                grid[vence(1,grid)] = -1
                cont -= 1
                tela(grid)
            else:
                j = random.randrange(0, 9)
                while(grid[j] != 0):
                    j = random.randrange(0, 9)
                grid[j] = -1
                info()   
                print "A IA jogou em " + str(j) + " Onde voce vai jogar? "
                cont -= 1
                tela(grid)
            if flag != 0:
                pos = scan(grid)
                # humano entrou com uma posicao valida
                grid[pos] = 1
                cont -= 1
                tela(grid)
    # passo 4.2
    else:
        # usar in é mais inteligente e elegante que um monte de condições
        # obrigado, python!
        if (ini in quinas) and (sec in quinas):
            laterais = [1, 3, 5, 7]
            ale = random.randrange(0,4)
            grid[laterais[ale]] = -1
            info()   
            print ("A IA jogou em " + str(laterais[ale]) + 
                    " Onde voce vai jogar? ")
            cont -= 1
            tela(grid)
            pos = scan(grid)
            # humano entrou com uma posicao valida
            grid[pos] = 1
            cont -= 1
            tela(grid)
            # famigerado loop de jogo...
            while (cont > 0) and (flag != 0):
                if vence(-1,grid) != -1:
                    info()
                    print ("A IA jogou em " + str(vence(-1,grid)) + 
                            " Voce perdeu!")
                    grid[vence(-1,grid)] = -1
                    tela(grid)
                    flag = 0
                elif vence(1, grid) != -1:
                    info()
                    if cont > 1:
                        print ("A IA jogou em " + str(vence(1,grid)) + 
                                " Onde voce vai jogar?")
                    grid[vence(1,grid)] = -1
                    cont -= 1
                    tela(grid)
                else:
                    info()
                    j = random.randrange(0, 9)
                    while(grid[j] != 0):
                        j = random.randrange(0, 9)
                    grid[j] = -1
                    print "A IA jogou em " + str(j) + " Onde voce vai jogar?"
                    cont -= 1
                    tela(grid)
                if flag != 0:
                    pos = scan(grid)
                    # humano entrou com uma posicao valida
                    grid[pos] = 1
                    cont -= 1
                    tela(grid)    
        else:
            # passo 4.2.2
            # uma solução um pouco mais elegante
            # representa maior maturidade de código
            if ini == 0:
                if sec == 5:
                    joga = 7
                else:
                    joga = 5
            elif ini == 2:
                if sec == 3:
                    joga = 7
                else:
                    joga = 3
            elif ini == 6:
                if sec == 5:
                    joga = 1
                else:
                    joga = 5
            else:
                if sec == 3:
                    joga = 1
                else:
                    joga = 3        
            info()
            grid[joga] = -1
            print "A IA jogou em " + str(joga) + " Onde voce vai jogar?"
            cont -= 1
            tela(grid) 
            pos = scan(grid)
            # humano entrou com uma posicao valida
            grid[pos] = 1
            cont -= 1
            tela(grid)
            # famigerado loop de jogo...
            while (cont > 0) and (flag != 0):
                if vence(-1,grid) != -1:
                    info()
                    print ("A IA jogou em " + str(vence(-1,grid)) + 
                            " Voce perdeu!")
                    grid[vence(-1,grid)] = -1
                    tela(grid)
                    flag = 0
                elif vence(1, grid) != -1:
                    info()
                    if cont > 1:
                        print ("A IA jogou em " + str(vence(1,grid)) + 
                                " Onde voce vai jogar?")
                    grid[vence(1,grid)] = -1
                    cont -= 1
                    tela(grid)
                else:
                    info()
                    j = random.randrange(0, 9)
                    while(grid[j] != 0):
                        j = random.randrange(0, 9)
                    grid[j] = -1
                    print "A IA jogou em " + str(j) + " Onde voce vai jogar?"
                    cont -= 1
                    tela(grid)
                if flag != 0:
                    pos = scan(grid)
                    # humano entrou com uma posicao valida
                    grid[pos] = 1
                    cont -= 1
                    tela(grid)        
elif (pos % 2):
    # este foi o primeiro algoritmo codificado
    # o cara jogou na borda
    # tem que armazenar a posição inicial
    ini = pos
    grid[4] = -1
    info()
    print "A IA jogou em 4 Onde voce vai jogar?"
    cont -= 1
    tela(grid)
    pos = scan(grid)
    # humano entrou com uma posicao valida
    grid[pos] = 1
    cont -= 1
    tela(grid)
    while (cont > 0) and (flag != 0):
        if vence(-1,grid) != -1:
            info()
            print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
            grid[vence(-1,grid)] = -1
            tela(grid)
            flag = 0
        elif vence(1, grid) != -1:
            info()
            if cont > 1:
                print ("A IA jogou em " + str(vence(1,grid)) + 
                        " Onde voce vai jogar?")
            grid[vence(1,grid)] = -1
            cont -= 1
            tela(grid)
        else:
            info()
            if (ini == 1) and (grid[0] == 0):
                grid[0] = -1
                print "A IA jogou em 0 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 1) and (grid[2] == 0):
                grid[2] = -1
                print "A IA jogou em 2 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 3) and (grid[0] == 0):
                grid[0] = -1
                print "A IA jogou em 0 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 3) and (grid[6] == 0):
                grid[6] = -1
                print "A IA jogou em 6 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 5) and (grid[2] == 0):
                grid[2] = -1
                print "A IA jogou em 2 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 5) and (grid[8] == 0):
                grid[8] = -1
                print "A IA jogou em 8 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 7) and (grid[6] == 0):
                grid[6] = -1
                print "A IA jogou em 6 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            elif (ini == 7) and (grid[8] == 0):
                grid[8] = -1
                print "A IA jogou em 8 Onde voce vai jogar?"
                cont -= 1
                tela(grid)
            else:
                # isso tá pouco eficiente, até mesmo quase uma pog...
                # exemplo de gambi design pattern "My Way"
                if ((grid[0] != 0) and (grid[2] != 0) and (grid[6] != 0)
                    and (grid[8] != 0)):
                    j = random.randrange(0, 9)
                    while(grid[j] != 0):
                        j = random.randrange(0, 9)
                    grid[j] = -1
                else:
                    rand = randnumedge()
                    while (grid[rand] != 0):
                        rand = randnumedge()
                    grid[rand] = -1
                if j != -1:
                    rand = j            
                print "A IA jogou em " + str(rand) + " Onde voce vai jogar?"
                cont -= 1
                tela(grid)
        # isso tá um pouco pog...
        if flag != 0:
            pos = scan(grid)
            # humano entrou com uma posicao valida
            grid[pos] = 1
            cont -= 1
            tela(grid)   
else:
    # este foi o segundo algoritmo codificado
    # nesse caso pos == 4
    rand = randnumedge()
    while (grid[rand] != 0):
        rand = randnumedge()
    grid[rand] = -1
    info()
    print "A IA jogou em " + str(rand) + " Onde voce vai jogar?"
    cont -= 1
    tela(grid)
    pos = scan(grid)
    # humano entrou com uma posicao valida
    grid[pos] = 1
    cont -= 1
    tela(grid)
    while (cont > 0) and (flag != 0):
        if vence(-1,grid) != -1:
            info()
            print "A IA jogou em " + str(vence(-1,grid)) + " Voce perdeu!"
            grid[vence(-1,grid)] = -1
            tela(grid)
            flag = 0
        elif vence(1, grid) != -1:
            info()
            if cont > 1:
                print ("A IA jogou em " + str(vence(1,grid)) + 
                        " Onde voce vai jogar?")
            grid[vence(1,grid)] = -1
            cont -= 1
            tela(grid)
        else:
            info()
            if ((grid[0] != 0) and (grid[2] != 0) and (grid[6] != 0)
                and (grid[8] != 0)):
                j = random.randrange(0, 9)
                while(grid[j] != 0):
                    j = random.randrange(0, 9)
                grid[j] = -1
            else:
                rand = randnumedge()
                while (grid[rand] != 0):
                    rand = randnumedge()
                grid[rand] = -1
            if j != -1:
                rand = j            
            print "A IA jogou em " + str(rand) + " Onde voce vai jogar?"
            cont -= 1
            tela(grid)
        # isso tá um pouco pog
        if flag != 0:
            pos = scan(grid)
            # humano entrou com uma posicao valida
            grid[pos] = 1
            cont -= 1
            tela(grid)
# a última jogada sempre é do humano...            
if cont == 0:
    print "Empate!"
print " "
print " "
