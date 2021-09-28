# War-Card-Game
Halanna Yuh

You can access the cloud deployment here: http://3.88.196.126/

Running the web application locally:
1. Open a terminal and git clone this repository. 'git clone https://github.com/hayuh/War-Card-Game.git'
2. Install all requirements by running 'pip install -r requirements.txt'
3. Create tables in database by running 'python manage.py migrate'
4. Run the web application with 'python manage.py runserver'
5. You should see some text on your terminal. Among the text, you should see "Starting development server at 'http://127.0.0.1:<port>/'.
    Click on the link to see the web application running locally.

If you encounter errors such as "Couldn't import Django" when running any of the commands, you may need to create a virtual environment.
You can do this by:
1. Run "python -m venv <your virtual environment name>"
2. Run "<your virtual environment name>/Scripts/activate" (activate.bat on Windows, activate in MAC/Linux).
3. In the virtual environment, run 'pip install -r requirements.txt'
4. Try running the 'python manage.py' commands again.
You can exit the virtual environment by running 'deactivate.'

You can also run "python war.py" to see the main backend application.

Notes
Here are some things I may attempt if given more time:
1. Implement a version of the game involving human interaction. This will involve some JavaScript to take in user input and additional  models for users to store their usernames and lifetime wins information. 
2. Refine the UI. Because Django template language does not work well with numbers, it was difficult to implement stylistic
elements to represent the cards in the players' deck on the HTML page.