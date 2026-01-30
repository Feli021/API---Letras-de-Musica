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
### With Poetry
2.1 - If you have Poetry installed:
- Command: poesia env activate
- Copy the link generated in the terminal by the command above and paste it (into the terminal).

2.2 - If you don't have it installed:
2.2.1 - Install pipx:
## On macOS:
brew install pipx
pipx ensurepath

## On Linux:
### Ubuntu 23.04 or above:
sudo apt update
sudo apt install pipx
pipx ensurepath

### Fedora:
sudo dnf install pipx
pipx ensurepath

### Using pip on other distributions:
python3 -m pip install --user pipx
python3 -m pipx ensurepath


## On Windows:
With Scoop:
Open a PowerShell terminal (version 5.1 or later) and from the PS C:\> prompt, run:
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

Now : 
scoop install pipx
pipx ensurepath


Without Scoop:
# If you installed python using Microsoft Store, replace `py` with `python3` in the next line.
py -m pip install --user pipx

It is possible (even most likely) the above finishes with a WARNING looking similar to this:
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH

If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line (even if you did not get the warning):
.\pipx.exe ensurepath

This will add both the above mentioned path and the %USERPROFILE%\.local\bin folder to your search path. Restart your terminal session and verify pipx does run

2.2.2 - Install Poetry:
pipx install poetry

2.3 - If you are not going to use Poetry:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


3. Install the dependencies:
poetry install

Without poetry:
pip install -r requirements.txt


4. Run the application:
streamlit run app.py

5. Open your browser at:
http://localhost:8501

