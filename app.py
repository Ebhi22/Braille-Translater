# # app.py
# from flask import Flask, request, render_template
# import pandas as pd
# import joblib



# app = Flask(__name__)

# import pickle

# with open('model.pkl', 'rb') as file:
#     model = pickle.load(file)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     predicted_price = None

#     if request.method == "POST":
#         # Get user input from the HTML form
#         company = request.form["input"]

#         data = pd.DataFrame({
#             "Company": [company]
#      })
    
#     predicted_price = model.predict(data)

#     return render_template("index.html", output=predicted_price)


# if __name__ == '__main__':
#     app.run(debug=True)



#*********************************
#*********************************

# pip install Flask

import pickle
from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from googletrans import Translator

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
  l_model = pickle.load(file)

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv")

cv = CountVectorizer()
X = cv.fit_transform(data["Text"])

translator = Translator()


braille = ['⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔',
			'⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚',
			'⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞',
			'⠥','⠧','⠺','⠭','⠽','⠵',
			'⠱','⠰','⠣','⠿','⠀','⠮','⠐','⠼','⠫','⠩',
			'⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌',
			'⠜','⠹','⠈','⠪','⠳','⠻','⠘','⠸']

english = ['0','1','2','3','4','5','6','7','8','9',
			'a','b','c','d','e','f','g','h','i','j',
			'k','l','m','n','o','p','q','r','s','t',
			'u','v','w','x','y','z',
			':',';','<','=',' ','!','"','#','$','%',
			'&','','(',')','*','+',',','-','.','/',
			'>','?','@','[','\\',']','^','_']


def braille2English(brailleText) :
	return ''.join([english[braille.index(fi)] for ch in brailleText for fi in braille if ch == fi])
def english2Braiile(englishText) :
	return ''.join([braille[english.index(fi)] for ch in englishText.lower() for fi in english if ch == fi])



@app.route('/', methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Get user input from the HTML form
        feature = request.form["feature"]

        # Create a DataFrame with the user input
         
        new_data = pd.DataFrame({
            "Feature": [feature]
        })

        # Make a prediction using the loaded model
         
        user_data = cv.transform(new_data['Feature']).toarray()
        prediction = l_model.predict(user_data)
        print(prediction)

        translation = translator.translate(feature,dest="en")
        T = translation.text
        print(T)

        B = english2Braiile(T)
        print(B)

    return render_template("index.html", prediction=prediction , eng=T , res=B)

if __name__ == "__main__":
    app.run(debug=True)

