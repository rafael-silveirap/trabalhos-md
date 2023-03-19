import datetime

start = datetime.datetime.now()

arquivo = open("output.txt", "a")
A = [1,2,3,4,5]

def classifica(conjunto):
    clas = ""
    if len(conjunto) == 0:
        clas += "STI"
    else:
        #verifica se é simétrica
        s = True
        for x, y in conjunto:
            if (y,x) not in conjunto:
                s = False
                break
        if s:
            clas += "S"
        #verifica se é transitiva
        t = True
        for x, y in conjunto:
            for w, z in conjunto:
                if y == w and (x,z) not in conjunto:
                    t = False
                    break
        if t:
            clas += "T"
        #verifica se é reflexiva
        r = True
        for n in A:
            if (n,n) not in conjunto:
                r = False
                break
        if r:
            clas += "R"
        #verifica se é equivalência
        if r and s and t:
            clas += "E"
        #verifica se é irreflexiva
        i = True
        for n in A:
            if (n,n) in conjunto:
                i = False
                break
        if i:
            clas += "I"
        #verifica se é função
        f = True
        func = [-1]*6
        for x,y in conjunto:
            if func[x] == -1:
                func[x] = y
            elif func[x] != -1 and func[x] != y: #caso onde existe mais de um valor para um mesmo x
                f = False
                break
        if f:
            restantes = 0
            for c in func:
                if c == -1:
                    #numeros nao verificados no dominio
                    restantes += 1
            if restantes < 2: #restantes deve ser sempre 1 para ser funcao pois é o caso onde so x=0 nao ocorreu, e apenas criei ele pra ficar mais fiel a x e y verdadeiro do conjuntop
                clas += "F"
                #verifica se é sobrejetora e injetora
                fs = True
                imagem = []
                fi = True
                for i in range(1,6):
                    if func[i] not in imagem:
                        imagem.append(func[i])
                    else:
                        fi = False #caso onde ja func[i] ja esta na imagem logo dois x tem o mesmo valor de y
                if len(imagem) != 5: #se a imagem nao tiver os 5 numeros (1,2,3,4,5) nao é sobrejetora
                    fs = False
                if fs and fi:
                    clas += "FbFsFi"
                else:
                    if fs:
                        clas += "Fs"
                    if fi:
                        clas += "Fi"

    return clas

def pot_conj(n):
    for subconj in range(2**(n*n)):
        atual = conj_pares(subconj, n)
        classificacao = classifica(atual)
        #escreve no arquivo o elemento e sua classificacao
        arquivo.write(f"{atual}  {classificacao}\n")
    return

def conj_pares(s, n):
    conj = []
    for i in range(n):
        for j in range(n):
            if bit_ligado(i,j,n,s):
                conj.append((i+1,j+1)) #somei 1 para tirar o 0 do conjunto A, ficando somente com 1,2,3,4,5
    return conj

def bit_ligado(i,j,n,s):
    return s & (1<<(i*n + j)) != 0

pot_conj(5)

arquivo.close()

end = datetime.datetime.now()
tempo = end-start
print(tempo.total_seconds())