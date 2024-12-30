def main():
    #Pergunta o nome de usuário
    name = input("Olá! Como você se chama? ")
    if not name.strip():
        print("Você não digitou seu nome! Vou chama-lo de 'amigo'.")
    print (f"Olá {name}! Prazer em conhecer você!")
    
    # Validação da idade

    print("Por favor, insira sua idade em números inteiros.")
    while True:
        age_input = input("Quantos anos você tem? ")
        if age_input.isdigit():
            age = int(age_input)
            break
        elif age_input.lower() == "sair":
            print("Encerrando o programa. Até logo!")
            return
        else:
            print("Entrada inválida. Digite um número ou 'sair' para encerrar.")
    
    #Cálculo de diferença de idade

    bot_age = 3
    if age >= bot_age:
        age_difference = age - bot_age
        print(f"Você é {age_difference} anos mais velho que eu haha.")
    else:
        age_difference = bot_age - age
        print(f"Eu sou {age_difference} anos mais velho que você haha.")

    # Pergunta sobre cor favorita

    color = input(f"Qual é a sua cor favorita, {name}? ").strip().capitalize()
    if color:
        print(f"Ah, que bacana! {color} é muito bonita e combina com diversos tons de outras cores!!")
    else:
        print("Parece que você não respondeu. Tudo bem, cores são subjetivas!")

# Esta linha deve estar no nível mais externo, sem indentação
if __name__ == "__main__":
    main()
