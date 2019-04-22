
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Antonio Fonseca, antonioarf@al.insper.edu.br
# - aluno B: Gabriela Moreno Boriero, gabrielamb2@al.insper.edu.br

import json
import random
import colorama 
from colorama import Back, Fore

with open ('cenario1.json' , 'r', encoding="utf8") as arquivo:
     cenario= json.load(arquivo)

def main():
    nome_cenario_atual = "inicio"
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP")
    print()
    print("Procure bem pelo professor, e saiba que nem sempre uma olhada apenas basta...")
    print ("Boa Sorte")
    print()
    
    game_over = False
    while not game_over:
        cenario_atual = cenario[nome_cenario_atual]
     
        print()
        print (Fore.GREEN+cenario_atual["titulo"])
        print ("-"*len(cenario_atual["titulo"]))
        print (cenario_atual["descricao"])      
        opcoes = cenario_atual['opcoes']
       

        print()
        print(Fore.BLUE+"suas opções são:")
        for e in cenario_atual["opcoes"]:
            print("{0}: {1}".format(e,cenario_atual["opcoes"][e]))
        escolha = input(Fore.BLACK+"Para onde você quer ir agora?").strip()
        if escolha == "lutar":
            break
        elif escolha in opcoes:
            inventario(escolha)
            nome_cenario_atual = encontro(escolha)
            
            if cenario["seu perfil"]["pontos de combate"]["pontos de vida"]<=0:
                game_over = True 
                    
        else:
            print(Back.RED+"Sua indecisão foi sua ruína!")
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
            print ("Ele tentara um ataque")
            if ataque > desefa_player:
                vida_player -= ataque
                print ("Voce foi atacado")
            elif ataque == desefa_player:
                vida_player -= ataque/2
                print ("Voce foi atacado")
            else:
                print ("Voce se defendeu, sua vez")
            print ("Suas opcoes de ataque:")
            for e in cenario["seu perfil"]["pontos de combate"]["ataques"]:
                print (e)
            ataque = input("escolha seu ataque:")
            contra_ataque = cenario["seu perfil"]["pontos de combate"]["ataques"][ataque]
            if contra_ataque > defesa_prof:
                vida_prof -= contra_ataque
                print ("Voce atacou com sucesso")
            elif ataque == defesa_prof:
                vida_prof -= contra_ataque/2
                print ("Voce atacou com sucesso")
            else:
                print ("ele se defendeu")
        
    if game_over == True or vida_player <= 0:      
        print(Back.RED+"Você morreu!")
        print("GAME OVER")
        print("ZEROU O TRABALHO")
    else:
        print (Back.GREEN+"PARABENS, VOCE VENCEU")
        print ("A EP FOI ADIADA POR SUA CAUSA")
        print ("!!!!!!!!!!!")
def encontro(local):
    cenario["contador"][local]+=1
    if cenario["contador"]["sala dos professores"]==2:
      print()
      print("FINALMENTE!")
      print ("Agora voce se ve frente a frente com o profesor")
      print("Para o combate você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
      print()
      novo_local = "professor"
      return novo_local
    elif local == "atendimento dos ninjas" and cenario["contador"][local]== 2:
        print()
        print("você encontrou um teletransporte")
        print("Tome cuidado para escrever o local da maneira correta, nao quer se perder pela faculdade")
        teletransporte = input("Para onde você quer ir agora?").strip()
        return teletransporte
    elif cenario["contador"][local] >= cenario[local]["reacoes"]["start at"]: 
        cenario["seu perfil"]["pontos de combate"]["pontos de vida"] += cenario[local]["reacoes"]["dano"]
        print ()
        print ()
        print("__________________")
        print (cenario[local]["reacoes"]["frase"])
        print("Assim,você tem {0} pontos de vida".format(cenario["seu perfil"]["pontos de combate"]["pontos de vida"]))
        print("__________________")
        return local
    else:
        return local
def inventario(local):
    if local == "atendimento dos ninjas":
        if cenario["seu perfil"]["item"]== cenario[local]["reacoes"]["chave"]:
            cenario [local] ["reacoes"] 
            print("como voce trouxe comida, eles ajudam em dobro")
            cenario["seu perfil"]["pontos de combate"]["pontos de vida"] += cenario[local]["reacoes"]["dano"]
       
    else:
        if cenario["seu perfil"]["item"] == cenario[local]["reacoes"]["chave"]:
            print ("Para sua sorte, voce tinha {0} entao nao sofrera dano dessa vez".format(cenario[local]["reacoes"]["chave"]))
        else:
            cenario [local] ["reacoes"] 
            if cenario["seu perfil"]["item"] == "":
                print ("Voce esqueceu sua mochila hoje, entao so pode carregar um item por vez")
                print ("Quando encontrar algo, pode escolher leva-lo com vc ou deixar la")
                print("__________________")
                print ()
            print("Ao sair, voce encontrou {0}".format(cenario[local]["reacoes"]["item"]))
            sim_ou_nao = input("voce deseja levar com voce? (y/n)").strip()
            if sim_ou_nao == "y":
                cenario["seu perfil"]["item"] = cenario[local]["reacoes"]["item"]
            else:
                print ("entao voce continua carregando {0}".format(cenario["seu perfil"]["item"]))
# Programa principal.
if __name__ == "__main__":
    main()
