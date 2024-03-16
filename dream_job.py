# **********************************************
# Program # 2                                  *
# Programmed by: CASTILLO, RALPH ANDREI T.     *
# Year & Section: BSCpE 1-2                    *
# **********************************************

import pyfiglet
from pyfiglet import Figlet # Module for fonts
import colorama
from colorama import Fore, Style # Module for color and style
colorama.init() # To initialize the module

name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")
figlet = Figlet(font='3d-ascii') # Font I used is 3d style (para maangas!)

result = (f"{dream_job} is an amazing job, {name}!") # I prefer using f-string more para mas madali maglagay ng variable sa output.
print(f"\n{Fore.CYAN}{Style.BRIGHT}{figlet.renderText(result)}") # Cyan color and Bright para mukhang neon