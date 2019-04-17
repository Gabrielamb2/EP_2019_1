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
                "Hall predio 2": "atravesse a rua e procure o professor no predio novo" 
            }
        },
          "Hall predio 2":{
                  "titulo":" Uma Nova Esperanca",
                  "descricao":"Seja muito bem vindo ao novo predio",
                  "opcoes":{
                      "sala dos professores":"subir procurar pelo professor no terceiro andar",
                      "inicio": "tente procurar no predio 1",
                      "atendimento dos ninjas":"talvez eles tenham noticias do professor"
                      }
                  },  
        "sala dos professores":{
                "titulo":"cupula do mal",
                "descricao":"se entrar, devera enfrentar todos os professores de uma vez",
                "opcoes":{
                    "Hall predio 2": "Volte ao terrio e repense sua busca",
                    "atendimento dos ninjas":"talvez eles tenham noticias do professor",
                    "lutar":"tente a sorte, se ganhar sera muito bem recompensado"
                        }
                },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
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
            print("suas opções são:")
            for e in cenario_atual["opcoes"]:
                print("{0}: {1}".format(e,cenario_atual["opcoes"][e]))
            escolha = input("Para onde você quer ir agora?")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")



# Programa principal.
if __name__ == "__main__":
    main()
