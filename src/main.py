''' Objetivo: Criar uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói. Depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo: '''

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata 
# Se XP for entre 6.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000 = Imortal
# Se XP for maior ou igual a 10.001 = Radiante

#Criar um Classificador de Nível de Herói;
# O que deve ser utilizado?
# - Váriaveis (são espaços na memória para armazenar dados);
# - Operadores (como: =, >, <, >=, <=, ==, !=);
# - Laços de repetição (como: if, else, elif);
# - Estruturas de decisão (if, else, elif);
# - Impressão de dados na tela (função print).

# 14 Heróis/Heróinas escolhidos para testar o código:
# 1. Nome: Batman, XP: 950
# 2. Nome: Mulher Maravilha, XP: 1.500
# 3. Nome: Homem de Ferro, XP: 2.500
# 4. Nome: Capitão América, XP: 6.500
# 5. Nome: Thor, XP: 7.500
# 6. Nome: Hulk, XP: 8.500
# 7. Nome: Flash, XP: 9.500
# 8. Nome: Lanterna Verde, XP: 10.500
# 9. Nome: Aquaman, XP: 3.200
# 10. Nome: Arqueiro Verde, XP: 4.800
# 11. Nome: Ciborgue, XP: 5.500
# 12. Nome: Viúva Negra, XP: 11.000
# 13. Nome: Doutor Estranho, XP: 7500
# 14. Nome: Pantera Negra, XP: 2.200 

# Mensagem de Saída:
# "O herói de nome {nome} possui {xp} de XP e está classificado como nível {nível}."

# Declarando o nome dos heróis nas váriaveis e o XP correspondente
herois = [
    ("Batman", 950),
    ("Mulher Maravilha", 1500),
    ("Homem de Ferro", 2500),
    ("Capitão América", 6500),
    ("Thor", 7500),
    ("Hulk", 8500),
    ("Flash", 9500),
    ("Lanterna Verde", 10500),
    ("Aquaman", 3200),
    ("Arqueiro Verde", 4800),
    ("Ciborgue", 5500),
    ("Viúva Negra", 11000),
    ("Doutor Estranho", 7500),
    ("Pantera Negra", 2200)
] 

# Função para classificar o herói com base no XP
def classificar_heroi(nome, xp):
    if xp <= 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    
 # Imprimindo na tela de saída o nome e o nível classificatório de cada herói/heróina
    print(f"O(a) herói(na) de nome {nome} possui {xp} de XP e está classificado como nível {nivel}.") 

# Percorrendo a lista de heróis e chamando a função para cada um
for nome, xp in herois:
    classificar_heroi(nome, xp)