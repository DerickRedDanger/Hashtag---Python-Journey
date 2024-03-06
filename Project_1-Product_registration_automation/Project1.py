"""
Before writting the program, start by describing the step by step that you would do if you had to do it manually.
Then use it as a guideline to guide you on what you should make your program do.
"""

import pyautogui as pyauto
import time
import pandas as pd

# pyautogui.write -> Writes a text
# pyautogui.press -> press 1 tecla key
# pyautogui.click -> click in a X/Y position in the window
# pyautogui.hotkey -> press a combination of keys (like ctrl+c)


# Step by step
# step 1: Enter the company's system
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Used to add a pause between each pyauto command, after some tests, it felt unescessary here.
# But might be useful in other cases to avoid bug when something unpredictable like a delay happens.
# pyauto.PAUSE = 0.2

# Variable to find how long it took for this code to run
star_time = time.time()

# open the browser (edge in this case)
pyauto.press("win") # press windows Key
pyauto.write("microsoft edge")
pyauto.press("enter")

# The above will be executed quickly, but the Computer may need a second or two to open the browser
# So we set it to wait a second
time.sleep(1)

# once our browser is open, enter the link
pyauto.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyauto.press("enter")

# As before, depending of the internet, it may take a bit for the page to load.
time.sleep(2)

# step 2: Login
# manually open the edgy and insert a email and password
pyauto.press("tab")
pyauto.write("random_test_email@gmail.com")
pyauto.press("tab")
pyauto.write("random_password")
pyauto.press("enter")
time.sleep(2)

# step 3: import the products database
table = pd.read_csv("./products.csv")
print(table)

# variable to check how many lines were written in the page
n=0
# Step 4: Registering the products
for line, row in table.iterrows():
    n+=1
    pyauto.press("tab")
    pyauto.write(row["codigo"])

    pyauto.press("tab")
    pyauto.write(row["marca"])

    pyauto.press("tab")
    pyauto.write(row["tipo"])

    pyauto.press("tab")
    # write only works with Strings, catergory is int, so it needs to be transformed into a str
    category = str(row["categoria"])
    pyauto.write(category)

    
    pyauto.press("tab")
    unit_price = str(row["preco_unitario"])
    pyauto.write(unit_price)

    pyauto.press("tab")
    cost = str(row["custo"])
    pyauto.write(cost)

    pyauto.press("tab")
    obs = str(row["obs"])
    if obs:
        pyauto.write(obs)

    pyauto.press("tab")
    pyauto.press("enter")

    # after pressin enter, the window will update, but will remain at the same position.
    # To move back to the top, we can just click on a empty part of the site and press tab
    # So we execute the find_position.py, point the cursos to a empty part of the site, wait 5 seconds
    # then copy it's location and use it for the click function
    pyauto.click(x=607, y=708)
    # Since this for started with a tab, we don't need to add another here. 
    print(n)

# Variable to help find how long it took for this code to run
end_time= time.time()


print (f"It took {end_time-star_time} seconds for this code to run")