# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Antonio Fonseca, antonioarf@al.insper.edu.br
# - aluno B: Gabriela Moreno Boriero, gabrielamb2@al.insper.edu.br
import random
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar do professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "Hall predio 2": "atravesse a rua e procure o professor no predio novo",
                "sala professor": "Vá para o Prédio 2 e suba para o terceiro andar ",
                "atendimento dos ninjas": "Vamos ver se os ninjas tem noticia do professor no atendimento"
            }
        },
        "andar do professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "biblioteca": "descer para o Térreo e entrar na bilbioteca",
                "Hall predio 2": "descer, atravessar a rua até o prédio novo", 
                "sala dos professores": "Vá para o Prédio 2 e suba para o terceiro andar ",
                "atendimento dos ninjas": "Vamos ver se os ninjas tem noticia do professor no atendimento"
            }
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "Hall predio 2": "Atravesse a rua até o prédio novo", 
                "sala dos professores": "Vá para o Prédio 2 e suba para o terceiro andar ",
                "atendimento dos ninjas": "Vamos ver se os ninjas tem noticia do professor no atendimento",
                "andar do professor": "Tomar o elevador para o andar do professor"
            }
        },
          "Hall predio 2":{
                  "titulo":" Uma Nova Esperanca",
                  "descricao":"Seja muito bem vindo ao novo predio",
                  "opcoes":{
                      "sala dos professores":"subir procurar pelo professor no terceiro andar",
                      "inicio": "tente procurar no predio 1",
                      "atendimento dos ninjas":"talvez eles tenham noticias do professor",
                      "andar do professor": "Tomar o elevador para o andar do professor",
                      "biblioteca": "ir para o prédio 1 e entrar na bilbioteca"
                      }
                  },  
            "sala dos professores":{
                "titulo":"cupula do mal",
                "descricao":"se entrar, devera enfrentar todos os professores de uma vez",
                "opcoes":{
                    "Hall predio 2": "Volte ao terrio e repense sua busca",
                    "atendimento dos ninjas":"talvez eles tenham noticias do professor",
                    "inicio": "tente procurar no predio 1",
                    "biblioteca": "ir para o prédio 1 e entrar na bilbioteca",
                    "sala dos professores":"subir procurar pelo professor no terceiro andar"
                        }
                },
            "atendimento dos ninjas":{
                "titulo": "",
                "descricao": "",
                "opcoes": {
                        "inicio": "Voltar para o saguao de entrada", 
                        "andar do professor": "Tomar o elevador para o andar do professor",
                        "biblioteca":"Ir para a biblioteca",
                        "Hall predio 2":"Volte ao terrio e repense sua busca", 
                        "Sala dos professores":"subir procurar pelo professor no terceiro andar" }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {"lutar":"lamento"},
            "pontos de combate" : {
                    "pontos de vida":80, 
                    "ataques":{1:8, 2:5, 3: 12}, 
                    "defesa" : 12}
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


contador_mostros=0
def main():
    contadores= {"inicio": 1,"Hall predio 2": 0, "sala dos professores":0, "andar do professor":0, "bilioteca": 0, "atendimento dos ninjas": 0, "professor":0, "lutar":0}
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
            contadores[escolha] +=1

            if escolha == "lutar":
                break
                    
            elif escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
#saimos do loop (chance de vencer o jogo)                
    if escolha == "lutar":           
        print ("Seu perfil de luta:")
        print ("-------------------")
        print ("classe:")
        print (cenarios["seu perfil"]["classe"])
        for e in cenarios["seu perfil"]["pontos de combate"]:
            print (e +":" + str(cenarios["seu perfil"]["pontos de combate"][e]))

        print ()
        print ("Seu oponente:")
        print ("-------------------")
        print (cenarios["professor"]["titulo"])
        print (cenarios["professor"]["descricao"])
        print ()
        for e in cenarios["professor"]["pontos de combate"]:
            if e == "ataques":
                print (e +":seus ataques sao segredo kkkk" )
            else:
                print (e +":" + str(cenarios["professor"]["pontos de combate"][e]))
        print ()
        print ("VAMOS LUTAR")
        print ()
        
        vida_prof = cenarios["professor"]["pontos de combate"]["prontos de vida"]
        vida_player = cenarios["seu perfil"]["pontos de combate"]["prontos de vida"]
        defesa_prof = cenarios["professor"]["pontos de combate"]["prontos de defesa"]
        desefa_player = cenarios["seu perfil"]["pontos de combate"]["prontos de defesa"]
        while vida_prof > 0 and vida_player >0:
            qual_ataque = random.randint(4)
            ataque = cenarios["professor"]["pontos de combate"]["ataques"][qual_ataque]
            if ataque > desefa_player:
                vida_player -= ataque
            elif ataque == desefa_player:
                vida_player -= ataque/2
            print (cenarios["seu perfil"]["pontos de combate"]["ataques"])
            aaataque = input("escolha seu ataque")
            contra_ataque = cenarios["seu perfil"]["pontos de combate"]["ataques"][aaataque]
            if contra_ataque > defesa_prof:
                vida_prof -= ataque
            elif ataque == defesa_prof:
                vida_prof -= ataque/2
            
    if vida_prof <= 0:
        print ("PARABENS, VOCE VENCEU")
        print ("A EP FOI ADIADA POR SUA CAUSA")
        print ("!!!!!!!!!!!")
    elif game_over == True or vida_player <= 0:      
        print("Você morreu!")



# Programa principal.
if __name__ == "__main__":
    main()
