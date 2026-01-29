# Buscador de Letras de Música
Aplicação desenvolvida para buscar letras de músicas a partir do nome da banda/artista e da música.

A interface gráfica foi construída com **Streamlit**, enquanto as requisições HTTP para a API externa são feitas utilizando a biblioteca **requests**.

////

This application was developed to search for song lyrics based on the band/artist name and the song title.

The graphical interface was built using **Streamlit**, while HTTP requests to the external API are handled with the **requests** library.


## Tecnologias Usadas
- Python
- Streamlit
- Requests
- API Lyrics.ovh

## Funcionamento
O usuário informa:
- o nome da banda ou artista
- o nome da música

A aplicação realiza uma requisição HTTP para a API **Lyrics.ovh** e exibe a letra da música na interface.

Para garantir que nomes com espaços, acentos ou caracteres especiais funcionem corretamente nas URLs, foi utilizada a função `quote` do módulo `requests.utils`, responsável por realizar o **URL encoding** dos dados informados pelo usuário.

////

The user provides:
- the band or artist name
- the song title

The application sends an HTTP request to the **Lyrics.ovh** API and displays the song lyrics in the interface.

To ensure that names containing spaces, accents, or special characters work correctly in URLs, the `quote` function from the `requests.utils` module is used. This function performs **URL encoding**, converting user input into a valid URL format.


## Observações:
- O projeto trata erros de resposta da API (status code diferente de 200).
- A aplicação foi desenvolvida com foco em simplicidade e clareza do código.

////

- The project handles API response errors (status codes different from 200).
- The application was developed with a focus on simplicity, readability, and clean code.

## ▶️ How to Run the Project