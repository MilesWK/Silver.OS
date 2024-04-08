"""
SILVER OS

Created by: MilesWK

DESCRIPTION: SILVER OS is a program that simulates a command prompt for a
computer, but with way more commands.

NOTE: You may NOT use any of the code contained in Silver-OS.py or
silverosgames.py without explicit permission from the developer. 


"""

try:
  version = "3.4"    # First number change: multiple features added. Second number changes: Small feature added, number changes to 10 or 0, bug fixes
  print('Importing Assets...')
  print("  importing os...")
  import os
  print('  importing sys...')
  import sys
  print("  from time importing sleep and strftime...")
  from time import sleep,strftime
  print('  importing colors...')
  # Termcolor and colorama are both modules from pip. If the user does not have them downloaded, this program should automatically download it.
  Installations = 0
  try:
    from termcolor import colored
  except:
    try:
      print("Termcolor import failed. Attempt at installing Termcolor from pip.")
      os.system("pip install termcolor")
      Installations += 1
      from termcolor import colored
    except Exception as E: 
      print("Termcolor import failed. Please contact the developer for support")
      raise E
  try:
    from colorama import init
  except:
    try:
      print("Colorama import failed. Attempt at installing Colorama from pip.")
      os.system("pip install colorama")
      Installations += 1
      from colorama import init
    except Exception as E:
      print("Colorama import failed. Please contact the developer for support")
      raise E
  print('  importing random...')
  import random
  from Assets.silverosgames import *
  print(f"Imports completed with {Installations} installation(s)")
  print("Getting Games")

  """

  Contine with Silver OS

  """



  print("Getting Variables")
  messages = []
  account = False
  clear_always = False

  #colorcodes retrieved from "Colorify" by OverdriveReplit

  bold = '\033[1m'
  green = '\033[92m'
  yellow = '\033[38;2;255;255;0m'
  green = '\033[38;2;00;160;00m'
  blue= '\033[38;2;0;40;255m'
  purple = '\033[38;2;130;0;250m'
  brown = '\033[38;2;135;62;35m' 
  red = '\033[0;31m'
  orange = '\033[38;2;255;90;0m'
  normal = '\033[0m'+'\033[38;2;255;255;255m'
  italic = '\x1B[3m'
  hello_phrases = ["Hi! You found an easter egg!","Hello! How are you? This is an easter egg!","Hi! Glad your here :D. Easter egg you have found.", "Did you need something, or did you want to see this easter egg?"]
  current_date = strftime("%m-%d")
  current_date_informational = strftime("%B %d, %Y")

  print("Getting user")
  try:
      user = os.environ["REPL_OWNER"]
  except:
      user = None
  if not user:
    account = False
  else:
    account = True
    
  spacer = "\n\n"
  #the dates for the holidays credit to CoreOS by TriTech
  holidays = {"12-24":"Christmas Eve","12-25": "Christmas","10-30": "Hallow's Eve","10-31":  "Halloween","10-31": "New Year's Eve","01-01": "New Year's Day", "02-14": "Valentine's Day"}
  #This is me:
  holidaymessage = {"Christmas Eve":"'Twas the night before Christmas, and all through the house, not a creature was sturring. Not even a mouse! You exited for christmas tomarrow?","Christmas":"WHOOP! WHOOP! CHRISTMAS IS HERE! SO HAPPY!","Hallow's Eve":"What is that shadow? Is that a creepy thing? Or just a cat. Yeah it is just the cat! Halloween is tomarrow!","Halloween":"BOO! Did I scare you? Happy Halloween!","New Year's Eve":"Tomarrow the calender turns and a fresh start will be given!","New Year's Day":"A new year! WHOOP WHOOP!","Valentine's Day":"Happy Valentine's Day! I hope you have a good day!"}

  print("Getting Logo")

  logo = f"""
  {red+bold}########## {green+ bold}########## {blue+bold} #         {yellow + bold} #           # {purple+ bold} ########## {orange+ bold} ########
  {red+bold}#          {green+ bold}    #      {blue+bold} #         {yellow + bold}  #         #  {purple+ bold} #          {orange+ bold} #       #  
  {red+bold}#          {green+ bold}    #      {blue+bold} #         {yellow + bold}   #       #   {purple+ bold} #          {orange+ bold} #       #  
  {red+bold}########## {green+ bold}    #      {blue+bold} #         {yellow + bold}    #     #    {purple+ bold} ########## {orange+ bold} ########
  {red+bold}         # {green+ bold}    #      {blue+bold} #         {yellow + bold}     #   #     {purple+ bold} #          {orange+ bold} #       #  
  {red+bold}         # {green+ bold}    #      {blue+bold} #         {yellow + bold}      # #      {purple+ bold} #          {orange+ bold} #        #  
  {red+bold}########## {green+ bold}########## {blue+bold} ######### {yellow + bold}       #       {purple+ bold} ########## {orange+ bold} #         #  
  """

  print("Getting Functions")
  def terminal(text):
    print(f"{green+ bold}{text}") 
    
  def startup():
    loading = 0
    for x in range(1,21):
      loading += 1
      print(spacer)
      clear()
      print(f"""{logo}\n{blue+bold}OS by MilesWK {red+bold}\n\nloading: {yellow + bold}{"#"*loading}{" " * int((20-loading))} {loading*5}%""")
      sleep(0.1)

  def clear():
    os.system("cls")
  clear()

  startup()  # function defined at line 266-233

  sleep(1)
  clear()
  try:
    holiday = holidays[current_date]
    messages.append(holidaymessage[holiday])
    
  except:
    pass

  accountMessage = ""
  command = ""
  account = False

  messages.append('Silver OS is curently in development. Some features might not work or there might be major bugs in the code. ')
  if account is False:
    messages.append(f"{red}{bold}Your account is not configured. This means no data will be stored{normal}")
  else:
    accountMessage = ""

  #Makes the right amount of dashes above and below the date
    
  while command != "Close":
    
    if len(messages) != 0:
      print(f'{normal}You have {len(messages)} messages! Run {blue}"MESSAGES"{normal} to read these messages')
    dateblock = "-"*(len(current_date_informational)+1)
    print(f"{red}SILVER OS{blue} (Version {version}.):\n\n{normal}{dateblock}\n{blue}{current_date_informational}{normal}\n{dateblock}\n")

    print(f"{bold}{accountMessage}{normal}{blue}Run {bold}{red}'HELP'{normal}{blue} or{bold}{red} 'LIST'{normal} {blue}to get a list of commands")
    command = input(f"\n\n{green}{user}:{str(sys.platform)}:~/SilverOS$ {normal}")
    command = command.lower()
    if clear_always is not False:
      clear()
    print("  ")
    
    if command == "close" or command == "exit":
      print(f"{red}closing")
      
    elif command == "help" or command == "list":
      print(f"""{blue}Here is a list of commands:
      {normal}
      Help - Gives a list of commands
      List - Gives a list of commands
      Close/Exit - Closes the program
      Clear - Clears the terminal
      Messages - Reads all your messages.
      Clears - Toggle the clearing for each time a command is entered. Current mode: {clear_always}
      Games - Lists all the avaliable games""")
      
    elif command == "clear":
      clear()
      
    elif command == "messages":
      if len(messages) == 0:
        print('You have no messages!')
      else:
        for currentmessage in range(0,len(messages)):
          print(currentmessage+1,": ",messages[currentmessage])
        print("  ")
        input(f"{red}Press ENTER to delete these messages ")
        messages.clear()
        print("  ")
        
    elif command == "clears":
      if clear_always is False:
        clear_always = True
      else:
        clear_always = False
      clear()
      print(f"{bold}Clearing after command now set to {clear_always}.")

    # Wordle Game Command
    
    elif command == "wordle":
      wordlegame() # See silverosgames.py for this game

    # Dice Roll Game
    
    elif command == "dice-roll":
      roll_die() # See silverosgames.py for this game

    # List games
      
    elif command == "games":
      print(f"""
  {bold+blue}Games!{normal}
  Wordle: A Game based on the New York Times game "Wordle"
  dice-roll: Role some dice and get a random number between 1-6!
  """)

    # Easter egg "hi" (shhhh)
      
    elif command == "hi" or command == "hello":
      print(random.choice(hello_phrases))


    else:
      if command != "":
        print(f"{red}{bold}Command {command} not found.")
    print(f"{normal}{bold}-------------------------------------------")

# If something goes wrong, this will catch it:

except Exception as error:
  input(f" :( - Oh no! We ran into this issue: \"{error}\". This is an error in the code. Let the developer know! Press Enter to close this window")
  
