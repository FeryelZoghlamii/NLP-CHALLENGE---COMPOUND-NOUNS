# NLP-CHALLENGE---COMPOUND-NOUNS
The problem consists in matching compound noun descriptions against split-up variants and return the corresponding ICD code. The proposed solution is based mainly on the usage of the NLP python package.

## Pre-requirements

* Python >= 3.6
* nltk == 3.6.5
* python-Levenshtein == 0.12.2
* Flask == 2.0.1

To install the required python packages run the following command:

``` pip install -r requirements.txt ```
## Run Unit tests
In order to test the solution run the script 'unit_tests.py' using the following command:
``` python unit_tests.py```

in this case we run 4 three testing cases, which are 
* Input: 'Infektion der Harnblase'	; expected output: 'N30.9'
* Input: 'Harnblaseninfektion'		; expected output: 'N30.9'
* Input: 'Schenkelhalsfraktur'		; expected output: 'S72.00'
* Input: 'Fraktur des Schenkelhalses'	; expected output: 'S72.00'

The output looks like:
![alt text](https://github.com/FeryelZoghlamii/NLP-CHALLENGE---COMPOUND-NOUNS/blob/master/unit_tests.PNG?raw=true)

Which means that the test runs without crashing and without failures :)

## Run The Solution through web API
1. Open a command prompt window and run the script 'predict_icd.py' with the command:

``` python predict_icd.py```

the output looks like:

![alt text](https://github.com/FeryelZoghlamii/NLP-CHALLENGE---COMPOUND-NOUNS/blob/master/server_url.PNG?raw=true)

2. Open a browser and navigate to the url: "http://127.0.0.1:5000/"

One web page is open which looks like:

![alt text](https://github.com/FeryelZoghlamii/NLP-CHALLENGE---COMPOUND-NOUNS/blob/master/web_page.PNG?raw=true)

3. Under Description in the text field enter the description (e.g 'Riss der Arterie')

4. Press the botton 'GET'. This will lead you to another web page with the corresponding ICD code (e.g. 'I77.2').



## Error in loading NLP package!
**If you face a problem in loading nltk modules, please run the script 'downloads.py' only once.**