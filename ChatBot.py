import requests

# Função de recomendações de filmes
def get_movies_recommendations(genre_id):
    api_key = "abc6caad16fa78754d8645eea11374e4" 
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&language=pt-BR"

    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()['results']
        recommendations = [movie['title'] for movie in movies[:5]] 
        return recommendations
    else:
        return ["Não consegui encontrar recomendações no momento."]

# Função de gênero com base na idade
def get_genre_by_age(age):
    if age <= 12:
        return 16, "Animação"  # Animação
    elif 13 <= age <= 17:
        return 14, "Aventura"  # Aventura
    elif 18 <= age <= 25:
        return 35, "Comédia"  # Comédia
    else:
        return 28, "Ação"  # Ação

# Função principal
def main():
    name = input("Olá! Como você se chama? ").strip()
    if not name:
        name = "amigo"
        print("Você não digitou seu nome! Vou chamá-lo de 'amigo'.")
    print(f"Olá, {name}! Prazer em conhecer você!")

    print("Por favor, insira sua idade em números inteiros.")
    while True:
        age_input = input("Quantos anos você tem? ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        elif age_input.lower() == "sair":
            print("Encerrando o programa. Até logo!")
            return
        else:
            print("Entrada inválida. Digite um número ou 'sair' para encerrar.")

    bot_age = 3
    if age >= bot_age:
        age_difference = age - bot_age
        print(f"Você é {age_difference} anos mais velho que eu haha.")
    else:
        age_difference = bot_age - age
        print(f"Eu sou {age_difference} anos mais velho que você haha.")

    color = input(f"Qual é a sua cor favorita, {name}? ").strip().capitalize()
    if color:
        print(f"Ah, que bacana! {color} é muito bonita e combina com diversos tons de outras cores!")
    else:
        print("Parece que você não respondeu. Tudo bem, cores são subjetivas!")

    # Recomendação de filmes com base na idade
    genre_id, genre_name = get_genre_by_age(age)
    print(f"Baseado na sua idade, acho que você gostaria de filmes do gênero {genre_name}.")
    movies = get_movies_recommendations(genre_id)
    print("Aqui estão alguns filmes que você pode gostar:")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")

    # Opção para escolher outro gênero
    print("\nSe você quiser recomendações de outro gênero, veja a lista abaixo:")
    genre_options = {
        28: "Ação",
        12: "Aventura",
        16: "Animação",
        35: "Comédia",
        18: "Drama",
        10751: "Família",
        14: "Fantasia",
        27: "Terror",
        10749: "Romance",
        878: "Ficção Científica"
    }
    for genre_id, genre_name in genre_options.items():
        print(f"{genre_id}: {genre_name}")

    new_genre_input = input("Digite o número do gênero que você deseja (ou 'sair' para encerrar): ").strip()
    if new_genre_input.isdigit():
        new_genre_id = int(new_genre_input)
        if new_genre_id in genre_options:
            print(f"Buscando filmes do gênero {genre_options[new_genre_id]}...")
            movies = get_movies_recommendations(new_genre_id)
            print("Aqui estão alguns filmes que você pode gostar:")
            for i, movie in enumerate(movies, start=1):
                print(f"{i}. {movie}")
        else:
            print("Gênero inválido.")
    elif new_genre_input.lower() == "sair":
        print("Encerrando o programa. Até logo!")
    else:
        print("Entrada inválida. Encerrando o programa.")

# Verificação de execução direta
if __name__ == "__main__":
    main()
