# o usuario definira quantas n pessoas abrirão o código (grau do polinômio = n-1)
# o numero primo a ser usado no programa sera 100000007

from random import randint, shuffle 

p=100000007

def gerarpolinomio (q_pessoas): #q_pessoas = quantidade de pessoas que podem abrir segredo
    lista=[]
    k=q_pessoas
    lista.append(randint(1,1000)) # primeiro elemento da lista, o segredo
    while k>1:                  
        lista.append(randint(1,p))
        k -= 1
        # aqui foram gerados os coeficientes. grau do polinomio = q_pessoas-1
    
    return lista
        
def ponto_poli(q_pessoas, t_pessoas): #t_pessoas = quantidade total de pessoas. resulta na quantidade de pontos
    lista=gerarpolinomio(q_pessoas)  #comando para gerar lista com constante na posição [0] e coeficientes
    pontos={}
    x=t_pessoas
   
    secret=lista[0]  #jogando constante na variavel secret, para que depois possamos tirar a constante da lista
    print ("O segredo escolhido é:",secret)
    print("\n")
    del lista[0]
    k=q_pessoas-1 #grau do polinomio
    while x>0: #desta parte, até o final dessa função, corresponde a construção do polinomio
        j=0
        for y in lista: 
            y=(y*(x**k))+j
            j=y
            k-=1
        y=j+secret
        pontos[x]=y   #dicionario: chave é o x (numero do participante), y o valor (de acordo com o numero do participante)
        x-=1
        k=q_pessoas-1
    return pontos #retorna os valores y das chaves x



def parcelas_p_participantes (q_pessoas, t_pessoas):
    #aqui, cada participante receberá um ponto. o x desse ponto será seu número de identificação, e o 
    #y será o valor da função calculada com esse x
    pontos=ponto_poli(q_pessoas, t_pessoas)
    parcelas={}
    x=t_pessoas
    while x>0:
        parcelas[x]=x, pontos[x]
        x-=1
    return parcelas

   
    
def embaralha (q_pessoas, t_pessoas):
    #aqui dois processos importantes são feitos: escolhe aleatoriamente os pontos x e seus respectivos valor y(inseri os dados em lista
    #, e inseri todos os valores x e y na lista2 para posterior verificação na função verificafraude
    dic=parcelas_p_participantes(q_pessoas, t_pessoas)
    lista=[]
    lista2=[]
    for x, y in dic.iteritems():
        lista.append(y)
        lista2.append(y)
    shuffle(lista)  #forma de escolha aleatória escolhida
    k=len(lista)
    q=q_pessoas+1
    while q<=k:
        del lista[0]
        k-=1
    
    return lista, lista2


def verificafraude(Y,X,lista,lista2):
    #Nesta função os parametros são retirados todos da função lagrange. Sua principal ferramenta é retorar uma lista contendo
    #valores booleanos, conforme seguem os calculos na função lagrange.
    X2 = []
    Y2 = []
    lista_booleana = []
    mostra_X = []
    mostra_Y = []
    m, n = 0, 0
    for coisas in lista2:
        m, n = coisas
        X2.append(m)
        Y2.append(n)
    if Y in Y2:
        lista_booleana.append(True)
    else: 
        lista_booleana.append(False)
        mostra_X.append(X)
        mostra_Y.append(Y)
    return lista_booleana
    
def lagrange(q_pessoas, t_pessoas):
    m, n, e, r, c, s = 0, 0, 1.0, 0, 0, 0.0
    lj, k, Y, X, verifica = [], [], [], [], []
    lista, lista2 = embaralha(q_pessoas, t_pessoas)
    u=q_pessoas-1
    for coisas in lista: # retira as chaves e os numero que identifica as pessoas.
        m, n = coisas
        X.append(m)
        Y.append(n)
    for j in X:
        for i in X:
            if j!=i:
                r=float(-i)/float((j)-i)
                k.append(r)
        for j in k:
            e=e*j
        lj.append(e)  #agora temos uma lista com todos os valores Lj(0), basta fazermos a somatória com valores Yj
        k, e = [], 1
    while c<=u: #nesta parte, até o final, existe uma mistura de verificações e calculo do polinmio de lagrange
            verificafraude(Y[c],X[c],lista,lista2)    
            s=s+(Y[c]*lj[c])
            if False in verificafraude(Y[c],X[c],lista,lista2) :
                print ("O usuario",X[c],"foi escolhido e","possui a chave", Y[c], "errada")
                verifica.append(False)
            else:
                print ("O usuario",X[c],"foi escolhido e","possui a chave", Y[c], "correta")
                verifica.append(True)
            c+=1
    print ("\n")
    if False in verifica:
        print ("O valor do segredo combinado:", int(s),"nao é correto")
        return
    else:
        print ("O valor do segredo combinado:", int(s),"é correto")
        return
          
        
lagrange(3,6)