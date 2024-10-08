from movies.repository import MoviesRepository


class MoviesService:
    def __init__(self):
        self.movies_repository = MoviesRepository()

    def get_movies(self):
        return self.movies_repository.get_movies()
    
    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        return self.movies_repository.create_movie(movie)
    
    def get_movie_stats(self):
        return self.movies_repository.get_muvie_stats()
    



    
# Este código define uma classe chamada `MoviesService` dentro do módulo `movies`. Esta classe serve como uma camada de serviço para gerenciar filmes. Ela interage com a classe `MoviesRepository` para executar operações CRUD (Criar, Ler, Atualizar, Excluir) nos dados de filmes.

# Aqui está uma explicação detalhada do código:

# 1. A classe `MoviesService` é definida com um método `__init__` que inicializa uma instância da classe `MoviesRepository`. Essa instância é armazenada no atributo `movies_repository` do objeto `MoviesService`.

# 2. O método `get_movies` é definido dentro da classe `MoviesService`. Ele chama o método `get_movies` da instância `movies_repository` e retorna o resultado. Este método recupera todos os filmes do repositório.

# 3. O método `create_movie` é definido dentro da classe `MoviesService`. Ele recebe cinco parâmetros: `title`, `release_date`, `genre`, `actors` e `resume`. Ele cria um dicionário chamado `movie` com esses parâmetros e chama o método `create_movie` da instância `movies_repository`, passando o dicionário `movie` como argumento. Este método cria um novo filme no repositório.

# 4. A classe `MoviesService` encapsula a lógica de negócios para gerenciar filmes, separando-a da camada de acesso a dados fornecida pela classe `MoviesRepository`. Isso melhora a organização e a manutenibilidade do código.

# Em resumo, o código fornece uma camada de serviço para gerenciar filmes, interagindo com a classe `MoviesRepository` para executar operações CRUD.