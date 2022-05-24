# greek-namedays 📆

JSON files containing both fixed and moving Greek namedays.

# Files explanation
- ```fixed_namedays.json```: Contains fixed namedays of the entire year
- ```moving_namedays.json```: Contains moving namedays with their celebration method 
- ```monthly (DIR)```: Contains fixed namedays separated by their celebration month e.g. ```monthly/01.json``` contains the namedays for January only

# How to scrap manually

1. (Optional) Create a virtual environment ```python3 -m venv <env-name>``` and activate it ```source ./<env-name>/bin/activate```
2. Install all the dependencies from requirements.txt ```pip3 install requirements.txt```
3. Run the scrapper.py ```python3 scrapper.py```

Congrats! You've created 12 JSON files containing the namedays of each month in a year.

###### Content scrapped from https://www.eortologio.xyz/
