# Searcher of lyrics's musics
This application was developed to search for song lyrics based on the band/artist name and the song title.

The graphical interface was built using **Streamlit**, while HTTP requests to the external API are handled with the **requests** library.


## Used Technologies 
- Python
- Streamlit
- Requests
- API Lyrics.ovh

## It works:
The user provides:
- the band or artist name
- the song title

The application sends an HTTP request to the **Lyrics.ovh** API and displays the song lyrics in the interface.

To ensure that names containing spaces, accents, or special characters work correctly in URLs, the `quote` function from the `requests.utils` module is used. This function performs **URL encoding**, converting user input into a valid URL format.


## Observations:
- The project handles API response errors (status codes different from 200).
- The application was developed with a focus on simplicity, readability, and clean code.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Feli021/API---Letras-de-Musica
   cd API---Letras-de-Musica
2. Creating and Activating a Virtual Environment
### With Poetry:

- Command: poetry env activate
- Copy the link generated in the terminal by the command above and paste it (into the terminal).


### Without poetry:

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows


3. Install the dependencies:

poetry install

### Without poetry:

pip install -r requirements.txt


4. Run the application:

streamlit run app.py

5. Open your browser at:

http://localhost:8501

