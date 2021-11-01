NLP CHALLENGE - COMPOUND NOUNS
==============================

*the folder contains the following files:
	- predict_icd.py
	- downloads.py
	- templates/input.html
	- server_url.PNG
	- web_page.PNG
	- README.md


*The proposed application runs on python >= 3.6

*To run the prediction script you need to install the following packages (the indicated version has been tested):
	- nltk 			== 3.6.5
	- python-Levenshtein 	== 0.12.2
	- Flask                 == 2.0.1
 
* To test the application follow these steps:
	1. Run the script 'predict_icd.py' with the command "python predict_icd.py"
	2. Open a browser and navigate to the url: "http://127.0.0.1:5000/"
	3. Under Description in the text field enter the description (e.g. 'Riss der Arterie')
	4. Press the botton 'GET'. This will lead you to another web page with the corresponding ICD code.

N.B:
* If you face a problem in loading nltk modules, please run the script 'downloads.py' only once.

