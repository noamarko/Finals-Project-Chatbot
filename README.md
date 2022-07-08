# Interactive Chat-Bot Project 
## Description
In this project we present to you our interactive chatbot - a chatbot that can make small talks with the user.
This chatbot not only reacts to the users input but can also analyze the user's facial expression (can "see" the user).
This solution came to our minds after seeing the struggle many people had with loneliness during the COVID-19 pandemic.



## Installation
To install the project, first you need to have python3 installed  
To check if you already have python3 installed, run on terminal:  
`python --version`  
If not, download the suitable version for your machine from [here](https://www.python.org/downloads/), and run the installer.  
Then, run again on terminal: `python --version`, and it should show you the version you just installed.

Next, we need NodeJS  
To check if you already have NodeJS installed, run on terminal:  
`node -v`  
If not installed, then download Node from [here](https://nodejs.org/en/download/)  
Then open terminal in the client folder and run:  
`npm install` to install all client dependencies

Then open terminal in the server folder and run:  
`pip install requirements.txt` to install all server dependencies

## Usage  
Open terminal in the client folder and run:  
`npm start`  
Open terminal in the server folder and run:   
`python3 app.py` if it doesn't work then try: `python app.py`  

**NOTE:** There are several locations that are paths to specific folders, in order to run the program - change the paths to your own directory
The locations are in chat_model.py and load_model_and_predict.py
