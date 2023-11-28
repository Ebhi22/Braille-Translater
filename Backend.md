
# Braille Transcriptor

This is a web service that allows you to transcribe text to Braille. 

## Installation

1. Read the csv file https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv
2. Create a virtual environment with `python -m venv venv`.
3. Activate the virtual environment.
4. Install the dependencies with `pip install flask`, and 'pip install scikit-learn'.


## Usage

### Starting the server

To start the server, run `python app.py` from the root of the project. This will start the server on `http://localhost:5000` or 127.0.0.1:5000.

### Transcribing text

To transcribe text, make a POST request to `http://localhost:5000` with the following parameters:

- `feature`: The text to transcribe.
- `source`: The language of the text.
- `target`: Braille to use for the transcription.

The server will respond with the transcribed text.

- `result` (string): The transcribed Braille text.


### Getting a list of supported languages and grades


- `languages` : The csv file of languages.
- `grades` : The list of supported braille grades.

    
## Acknowledgements
This API is built with FlaskAPI.