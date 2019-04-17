# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Antonio Fonseca, antonioarf@al.insper.edu.br
# - aluno B: Gabriela Moreno Boriero, gabrielamb2@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "Hall predio 2": "atravesse a rua e procure o professor no predio novo",
                "sala professor": "Vá para o Prédio 2 e suba para o terceiro andar ",
                "atendimento dos ninjas": "Vamos ver se os ninjas tem noticia do professor no atendimento"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "biblioteca": "descer para o Térreo e entrar na bilbioteca",
                "Hall predio 2": "descer, atravessar a rua até o prédio novo", 
                "sala professor": "Vá para o Prédio 2 e suba para o terceiro andar ",
                "atendimento dos ninjas": "Vamos ver se os ninjas tem noticia do professor no atendimento"
            }
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "Hall predio 2": "Atravesse a rua até o prédio novo", 
                "sala professor": "Vá para o Prédio 2 e suba para o terceiro andar ",
                "atendimento dos ninjas": "Vamos ver se os ninjas tem noticia do professor no atendimento",
                "andar professor": "Tomar o elevador para o andar do professor"
            }
        },
          "Hall predio 2":{
                  "titulo":" Uma Nova Esperanca",
                  "descricao":"Seja muito bem vindo ao novo predio",
                  "opcoes":{
                      "sala professor":"subir procurar pelo professor no terceiro andar",
                      "inicio": "tente procurar no predio 1",
                      "atendimento dos ninjas":"talvez eles tenham noticias do professor",
                      "andar professor": "Tomar o elevador para o andar do professor",
                      "biblioteca": "ir para o prédio 1 e entrar na bilbioteca"
                      }
                  },  
            "sala professor":{
                "titulo":"cupula do mal",
                "descricao":"se entrar, devera enfrentar todos os professores de uma vez",
                "opcoes":{
                    "Hall predio 2": "Volte ao terrio e repense sua busca",
                    "atendimento dos ninjas":"talvez eles tenham noticias do professor",
                    "inicio": "tente procurar no predio 1",
                    "biblioteca": "ir para o prédio 1 e entrar na bilbioteca",
                    "sala professor":"subir procurar pelo professor no terceiro andar"
                        }
                },
            "atendimento dos ninjas":{
                "titulo": "",
                "descricao": "",
                "opcoes": {
                        "inicio": "Voltar para o saguao de entrada", 
                        "andar professor": "Tomar o elevador para o andar do professor",
                        "biblioteca":"Ir para a biblioteca",
                        "Hall predio 2":"Volte ao terrio e repense sua busca", 
                        "Sala professor":"subir procurar pelo professor no terceiro andar" }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        
        "seu perfil" : {
            "classe":"voce e bixo, veteranos tem vantagem contra voce, mas o nivel de do do professor cresce",
            "itens" :{},
            "pontos de combate" : {
                    "pontos de vida":100, 
                    "ataques":{"implorar por compaixao":8, "desculpa sou bixo nao sabia":5, "mano e uma looonga historia, mas juro q n foi culpa minha": 12}, 
                    "defesa" : 9}
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

#transformando o dicionário em um arquivo (json)
#import json
#with open("nome do doc", "r")as f:
#    c= jason.load(f)


def main():
    contadores= {"inicio": 1,"Hall predio 2": 0, "sala professor":0, "andar professor":0, "biblioteca": 0, "atendimento dos ninjas": 0, "professor": 0 }
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    

    cenarios, nome_cenario_atual = carregar_cenarios()
    
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        print (cenario_atual["titulo"])
        print ("-"*len(cenario_atual["titulo"]))
        print (cenario_atual["descricao"])      
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            print()
            print("suas opções são:")
            for e in cenario_atual["opcoes"]:
                print("{0}: {1}".format(e,cenario_atual["opcoes"][e]))
            escolha = input("Para onde você quer ir agora?").strip()
            if escolha in opcoes:
                nome_cenario_atual = escolha
                contadores[escolha] +=1
                if contadores["inicio"]==2:
                    print()
                    print("Você esqueceu sua carterinha e terá que falar com a recepcionista, você perde 15 pontos de vida")
                    cenarios["seu perfil"]["pontos de combate"]["pontos de vida"]-=15
                    print("você tem {0} pontos de vida".format(cenarios["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    print()
                    print()
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                
    print("Você morreu!")



# Programa principal.
if __name__ == "__main__":
    main()
