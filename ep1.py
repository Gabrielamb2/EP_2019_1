# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Antonio Fonseca, antonioarf@al.insper.edu.br
# - aluno B: Gabriela Moreno Boriero, gabrielamb2@al.insper.edu.br
import json
import random
#import colorama 
#from colorama import Fore
#print(Fore.(cor)+...)

with open ('cenario.json' , 'r', encoding="utf8") as arquivo:
     cenario= json.load(arquivo)
    
#print (cenario['inicio'])como chamar o json 

def main():
    nome_cenario_atual = "inicio"
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
    
    game_over = False
    while not game_over:
        cenario_atual = cenario[nome_cenario_atual]
        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        print()
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
            if escolha == "lutar":
                break
            elif escolha in opcoes:
                nome_cenario_atual = escolha
                contadores[escolha] +=1
                if contadores["inicio"]==2:
                    print()
                    print("Você esqueceu sua carterinha e terá que falar com a recepcionista, você perde 15 pontos de vida")
                    cenario["seu perfil"]["pontos de combate"]["pontos de vida"]-=15
                    print("Assim,você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    contadores["inicio"]+=1
                    print()
                    print()
                elif contadores["Hall predio 2"]==3:
                    print()
                    print("Você estava com pressa e esqueceu da catraca e ela bateu em você, fazendo com que se machucasse e perdesse 2 pontos de vida")
                    cenario["seu perfil"]["pontos de combate"]["pontos de vida"]-=2
                    print("Assim,você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    contadores["Hall predio 2"]+=1
                    print()
                    print()
                elif contadores["sala professor"]==1:
                    print()
                    print("Você foi a sala dos professores na intenção do seu professor ter voltado pra lá mas quem você encontrou foi o Hage, seu professor de Modsm que foi reclamar da sua nota na Pi")
                    cenario["seu perfil"]["pontos de combate"]["pontos de vida"]-=5
                    print("Assim,você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    contadores["sala professor"]+=1
                    print()
                    print()
                elif contadores["andar professor"]==2:
                    print()
                    print("Você encontrou um veterano de administração")
                    cenario["seu perfil"]["pontos de combate"]["pontos de vida"]-=3
                    print("Assim,você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    contadores["andar professor"]+=1
                    print()
                    print()
                elif contadores["biblioteca"]==3:
                    print()
                    print("Você lembrou que esta com um livro atrasado e perderá 2 pontos de vida")
                    cenario["seu perfil"]["pontos de combate"]["pontos de vida"]-=2
                    print("Assim, você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    contadores["biblioteca"]+=1
                    print()
                    print()
                elif contadores["atendimento dos ninjas"]==2:
                    print()
                    print("Você encontrou um veterano de engenharia que te deu algumas dicas para o Ep, assim aumentando 5 pontos de vida")
                    cenario["seu perfil"]["pontos de combate"]["pontos de vida"]+=5
                    print("Assim,você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
                    contadores["atendimento dos ninjas"]+=1
                    print()
                    print()
                if cenario["seu perfil"]["pontos de combate"]["pontos de vida"]<=0:
                    game_over = True 
                    
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    
    if escolha == "lutar" :      
        print ()
        print ("VAMOS LUTAR")
        print ()

        vida_prof = cenario["professor"]["pontos de combate"]["pontos de vida"]
        vida_player = cenario["seu perfil"]["pontos de combate"]["pontos de vida"]
        defesa_prof = cenario["professor"]["pontos de combate"]["defesa"]
        desefa_player = cenario["seu perfil"]["pontos de combate"]["defesa"]
        while vida_prof > 0 and vida_player >0:
            qual_ataque = random.randint(0,2)
            ataque = cenario["professor"]["pontos de combate"]["ataques"][qual_ataque]
            if ataque > desefa_player:
                vida_player -= ataque
                print ("Voce foi atacado")
            elif ataque == desefa_player:
                vida_player -= ataque/2
                print ("Voce foi atacado")
            print (cenario["seu perfil"]["pontos de combate"]["ataques"])
            aaataque = input("escolha seu ataque")
            contra_ataque = cenario["seu perfil"]["pontos de combate"]["ataques"][aaataque]
            if contra_ataque > defesa_prof:
                vida_prof -= ataque
                print ("Voce atacou com sucesso")
            elif ataque == defesa_prof:
                vida_prof -= ataque/2
                print ("Voce atacou com sucesso")

    if vida_prof <= 0:
        print ("PARABENS, VOCE VENCEU")
        print ("A EP FOI ADIADA POR SUA CAUSA")
        print ("!!!!!!!!!!!")
    elif game_over == True or vida_player <= 0:      
        print("Você morreu!")
        print("GAME OVER")
        print("ZEROU O TRABALHO")




# Programa principal.
if __name__ == "__main__":
    main()
