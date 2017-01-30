# Grupo: tg009
# Antonio Terra, 84702
# Miguel Viegas, 84747

#=======================#
#---Variaveis Globais---#
#=======================#

votacoes = ((0, 15729, 220408, 1297, 0, 3040, 993, 0, 1354, 1046, 0, 3284, 99652, 19327, 0), (0, 19000, 23173, 255, 0, 532, 201, 0, 306, 232, 0, 1980, 22307, 3890, 0), (0, 23731, 244971, 1959, 0, 2710, 1465, 0, 1094, 1114, 0, 4264, 159476, 20488, 0), (0, 1956, 47716, 282, 0, 0, 175, 0, 165, 247, 0, 417, 19728, 1732, 0), (0, 5384, 52325, 403, 0, 770, 543, 0, 428, 0, 0, 1454, 38317, 4609, 0), (0, 14138, 113419, 662, 0, 2535, 600, 0, 591, 557, 0, 2014, 66199, 13034, 0), (0, 18967, 31260, 237, 0, 649, 216, 0, 168, 207, 0, 1810, 25010, 4225, 0), (0, 17255, 99745, 2076, 0, 3285, 0, 0, 1069, 700, 0, 3160, 46082, 16347, 0), (0, 3299, 53450, 251, 0, 520, 199, 0, 178, 191, 0, 755, 26263, 3114, 0), (0, 12351, 148762, 977, 0, 3029, 633, 0, 595, 453, 0, 2502, 51518, 0, 0), (0, 111661, 560365, 4135, 0, 16913, 2410, 0, 5897, 4270, 0, 14419, 322034, 66874, 0), (0, 7910, 26257, 176, 0, 333, 162, 0, 151, 135, 0, 1031, 19963, 2753, 0), (0, 61832, 488402, 2413, 0, 9072, 3386, 0, 1551, 1525, 0, 9640, 318113, 51002, 0), (0, 21347, 118028, 1454, 0, 2220, 692, 0, 832, 726, 0, 3413, 61194, 13712, 0), (0, 82159, 156444, 1682, 0, 6282, 1133, 0, 1595, 847, 0, 0, 112764, 29667, 0), (0, 6648, 76961, 384, 0, 926, 0, 0, 213, 331, 0, 1473, 35327, 5928, 0), (0, 3656, 71840, 304, 0, 617, 254, 0, 147, 574, 0, 675, 34825, 2784, 0), (0, 5810, 123184, 696, 0, 1229, 465, 0, 266, 626, 0, 1456, 54107, 5786, 0), (0, 2288, 53518, 314, 0, 756, 293, 0, 219, 271, 0, 669, 23189, 3965, 0), (0, 5096, 87597, 2560, 0, 2385, 2992, 0, 617, 538, 0, 1967, 20360, 5568, 0), (0, 803, 6306, 101, 0, 192, 83, 0, 48, 50, 0, 132, 7205, 602, 0), (0, 127, 8938, 87, 0, 0, 0, 0, 64, 47, 0, 52, 2714, 165, 0))


# A lista circuitos contem o numero de deputados a atribuir em cada circuito
#   eleitural estando estes ordenados pela seguinte ordem:
# Aveiro, Beja, Braga, Braganca, Castelo Branco, Coimbra, Evora, Faro, 
# Guarda, Leiria, Lisboa, Portalegre, Porto, Santarem, Setubal, 
# Viana do Castelo, Vila Real, Viseu, Acores, Madeira, Europa, Fora da Europa.

circulos=[16,3,19,3,4,9,3,9,4,10,47,2,39,9,18,6,5,9,5,6,2,2]

partidos = [('PDR\tPartido Democratico Republicano'),\
            ('PCP-PEV\tCDU - Coligacao Democratica Unitaria'),\
            ('PPD/PSD-CDS/PP\tPortugal a Frente'), ('MPT\tPartido da Terra'),\
            ('L/TDA\tLIVRE/Tempo de Avancar'),\
            ('PAN\tPessoas-Animais-Natureza'), ('PTP-MAS\tAgir'),\
            ('JPP\tJuntos pelo Povo'), ('PNR\tPartido Nacional Renovador'),\
            ('PPM\tPartido Popular Monarquico'), ('NC\tNos, Cidadaos!'),\
            ('PCTP/MRPP\tPartido Comunista dos Trabalhadores Portugueses'),\
            ('PS\tPartido Socialista'), ('B.E.\tBloco de Esquerda'),\
            ('PURP\tPartido Unido dos Reformados e Pensionistas')]

#============================#
#-----Funcoes Auxiliares-----#
#============================#



def soma(x,y):
    '''Calcula a soma entre os valores de cada indice entre duas listas
    do mesmo tamanho.'''
    from operator import add
    return (list(map(add,x,y)))


#============================#
#-----Funcoes Principais-----#
#============================#


def mandatos(nr_mandatos,nr_votos):
    '''Determina qual a distribuicao de mandatos consoantes o numero de votos
    oor partido de acordo com o metodo de D'Hondt.'''
    
    nr_votos = list(nr_votos)  
    nr_votosdivididos = nr_votos[:]
    nr_votosdividos = list(nr_votosdivididos)
    # nr_votosdivididos e a lista que guarda os valores criados a partir da
        # nr_votos para calcular os maximos e distribuir os mandatos
    
    dep = [] 
    
    while len(dep) < len(nr_votos):
        dep.append(0)
        # Acrecentar a lista de forma a ficar com o mesmo tamanho 
            # da lista de nr_votos        
        
    def pos_maior(x):
        #Funcao que determina a posicao na lista do seu elemento maximo
        
        # Nao se definiu fora da funcao mandatos,
             # porque a variavel nr_votos e local
        
        idx = 0
        for i in range(len(x)):
            if x[i] > x[idx]:
                idx = i
            elif x[i] == x[idx]:
                if nr_votos[i] < nr_votos[idx]:
                    idx = i       
        return idx               
    
    for i in range(1,nr_mandatos+1):
        ind = pos_maior(nr_votosdivididos) # Serve para facilitar a escrita
        nr_votosdivididos[ind] = nr_votosdivididos[ind]/(dep[ind]+1)
        dep[ind] = dep[ind]+1
                
    return tuple(dep) # Torna a lista em tuple



def assembleia(votacoes):
    assembleia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        # Guarda os valores ja somados de deputados para cada partido
    for i in range(0,len(votacoes)):
        assembleia_votacoes = mandatos(circulos[i],votacoes[i])
        assembleia_votacoes = list(assembleia_votacoes) 
            # Serve para garantir que a operacao seguinte e executada com listas
        assembleia = soma(assembleia, assembleia_votacoes) 
            # Faz a soma entre os deputados ja atribuidos e os novos deputados
    return tuple(assembleia)
    
def max_mandatos(votacoes):
    idx = 0
    empate = 0
    for i in range(len(assembleia(votacoes))):
        if assembleia(votacoes)[i] > assembleia(votacoes)[idx]:
            idx = i
        if max(assembleia(votacoes)) == assembleia(votacoes)[i]: 
            empate += 1
            # Se houver pelo menos 2 partidos com o mesmo numero maximo
                #de deputados ele termina a funcao com "Empate Tecnico"
            if empate == 2:   
                return "Empate tecnico"
    
    return partidos[idx]