import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk

def read_csv():  #open and read data csv (with training and test data)
    data = pd.read_csv("data.csv", on_bad_lines='skip')
    return data

def convert_strength_num_to_string(data):  #convert csv numbers to strings
    data = data.dropna().copy()
    data["strength"] = data["strength"].map({0: "Weak", 
                                             1: "Medium", 
                                             2: "Strong"})
    return data

def cleaned_data_output():
    data = read_csv()
    cleaned_data = convert_strength_num_to_string(data)
    return cleaned_data

def pwstrength_training_model():  #split data to training and testing
    data = cleaned_data_output()

    x = np.array(data["password"])  
    y = np.array(data["strength"])  

    vectorizer = TfidfVectorizer(analyzer='char')  
    x = vectorizer.fit_transform(x)

    xtrain, xtest, ytrain, ytest = train_test_split(x, 
                                                    y,
                                                    test_size=0.1, 
                                                    random_state=50)

    print(f"Training samples: {xtrain.shape[0]}, Testing samples: {xtest.shape[0]}")

    model = RandomForestClassifier(n_estimators=50, random_state=25, n_jobs=-1)
    model.fit(xtrain, ytrain)    
    print('ML model is ready!')
    return model, vectorizer

model, vectorizer = pwstrength_training_model()

########_________________________________________________________________##########
#making a GUI


window = tk.Tk()
window.geometry("500x300")
window.title("Password Strength Checker")
passw_var = tk.StringVar()

def check_pw():
    """Get user input, process it through the model, and display the strength."""
    user_password = passw_var.get().strip()
    if not user_password:
        strength_label.config(text="Please enter a password!", fg="red")
        return
    
    data = vectorizer.transform([user_password]).toarray()
    prediction = model.predict(data)[0]
    color_map = {"Weak": "red", "Medium": "orange", "Strong": "green"}
    text_color = color_map.get(prediction, "black")
    
    strength_label.config(text=f"Password Strength: {prediction}", 
                          fg=text_color)

description = tk.Label(window, 
                       text="Enter a password below to test its strength", 
                       font=("calibre", 14, "bold"))
description.place(x=10,
                  y=10)

passw_label = tk.Label(window, 
                       text="Password", 
                       font=("calibre", 10, "bold"))
passw_label.place(x=100,
                  y=100)

passw_entry = tk.Entry(window, 
                       textvariable=passw_var, 
                       font=("calibre", 10, "normal"))
passw_entry.place(x=200,
                  y=100)

test_button = tk.Button(text="Test", 
                        command=check_pw)
test_button.place(x=200,
                  y=150)

strength_label = tk.Label(window, font=("calibre", 10, "bold"))
strength_label.place(x=200,
                     y=200)

window.mainloop()
