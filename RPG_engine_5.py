import random
import time 
import math
import json
from colorama import init, Fore, Back, Style
init(autoreset=True, convert=True)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
amount = 0
sc_vl = 1
explored = 0
health = 100
mana = 100
hp = 0
mp = 0
G = 0
MonD = 0
BossD = 0
Karma = "NEUTRAL" 
Karma_vl = 0
dif_vl = 1
MonsNames = ["Wolf","Goblit","Wizzard","Warrior","Bear","Ghoul","Guardion","Archer","Dragon","Hydra","Minotaur","Medusa","Cerberus","Chimera"]
cur_diff = ""
inventory = []
max_inv = 5
spells = ["Spell[A]"]
max_spells = 2

good_text_choice = ["Thank you for your great deed.","Your kindness does not go unnoticed.","Youve made a difference, however small.","Your mercy is noted.","May Goodness follows your path.","Your actions have weight—choose wisely.",
                    "Someone benefited from your choice.","You feel the balance tip slightly in your favor.","Even small acts echo in the world.","Youve done well, for now.","Your compassion is a light in the dark.",
                    "Youve honored the better part of yourself.","Hah! You think that changes anything?","Do you really expect thanks? Pathetic.","I wouldve killed you if I were smarter.","Keep your pity. I dont need it.",
                    "Thats all? Weakling","Ill remember this… and mock you for it.","You just made yourself weaker.","Your generosity is a joke.","Do you even know what youre doing?","I dont owe you anything",
                    "Your mercy is noise in an indifferent void.","Gratitude is a lie we tell ourselves.","You think your actions matter? They do not.","I feel nothing but the weight of existence.","Even your good deeds are swallowed by meaninglessness",
                    "Your morality is irrelevant here.","Do you expect the world to answer your kindness?"]
bad_text_choice = ["Do you regret this?","What have you done...","Are you proud of yourself?","You feel the weight of your choices.","Is this who you want to be?","Would you do it again?","You wonder if it could have been different.",
                   "Have you caused more harm than good?","do you question your own motives.","Would the world be better without your hand in it?","Do You feel the cold truth of your choices.","What does it say about you?",
                   "You wonder if kindness was ever an option.","You feel small in the face of your own deeds.","Was there another way?","You sense the consequences, faint but real.","Did you push too far?","You think about those you affected.",
                   "Something about this doesnt feel right.","You wonder what could have been spared.","Could you have shown mercy?","Well… that escalated quickly.","Oops. There goes your reputation.","The universe sighs. Loudly.",
                   "You did that. Dont pretend you didnt.","You cant take that back… and why would you want to?","Well, someones having a bad day.","Some things cant be fixed. You are one of them.","Youve outdone yourself in poor judgment.",
                   "Your choices are a masterclass in failure.","Well done. Chaos loves you.","Your incompetence is impressive."]
def save_file():
    game_save_var = {
        "health" : health,"mana" : mana,"G": G,"mp":mp,"hp":hp,"cur_dif":cur_diff,"sc_vl":sc_vl,"dif_vl":dif_vl,"MonD":MonD,"explored":explored,"Karma":Karma,"Karma_vl":Karma_vl,"BossD":BossD,
        "spells":spells,"inventory": inventory, "max_inv": max_inv,"max_spells":max_spells,
    }
    
    with open('game_save_var.json','w') as f:
        json.dump(game_save_var,f)
        print("s______________________")

def file_load():
    global health,mana,G,mp,hp,cur_diff,dif_vl,sc_vl,MonD,cur_text,explored,Karma,Karma_vl,BossD,max_inv,inventory,spells,max_spells

    try:
        with open('game_save_var.json', "r") as f:
            game_load_var = json.load(f)
        cur_text = "-GAME LOADED-"
        health = game_load_var["health"]
        mana = game_load_var["mana"]
        G = game_load_var["G"]
        mp = game_load_var["mp"]
        hp = game_load_var["hp"]
        cur_diff = game_load_var["cur_dif"]
        sc_vl = game_load_var["sc_vl"]
        dif_vl = game_load_var["dif_vl"]
        MonD = game_load_var["MonD"]
        explored = game_load_var["explored"]
        Karma = game_load_var["Karma"]
        Karma_vl = game_load_var["Karma_vl"]
        BossD = game_load_var["BossD"]
        max_inv = game_load_var["max_inv"]
        inventory = game_load_var["inventory"]
        spells = game_load_var["spells"]
        max_spells = game_load_var["max_spells"]


    except FileNotFoundError:
       cur_text = "ERROR FILE NOT FOUND "   

def Start_Menu(): 
    global cur_diff,Game_States, dif_vl, cur_sc,cur_text
    import os
    MenuTXT = {
        "Menu start":"RPG ENGINE 4.1",
        "menu start2": {
            "Menu options1":"----Start----",
            "Menu options2":"Difficulty - ",
            "Menu option3":"scaling - ",
            
            "difficulty_list":"difficulty commands { \n"
            "dif normal \n"
            "dif hard \n"
            "dif INSANE \n"
            "dif masochist \n"
            "dif ######\n"
            "}"

            ,"class_list":"class commands"
            "class TheGambler"
            "class ect"
        }
    }   
   
    Game_States = {
        "cur_dif":"normal"
         ,"Class":""
        ,"cur_sc":"lin"
        }
        
    Game_dif_options = {
        "dif_choice":{
        "normal":"normal"
        ,"hard":"hard",
        "insane":"INSANE",
        "masochist":"masochist"
        }
        ,"dif_value":{
            "normal":1,
            "hard":2,
            "insane":3,
            "masochist":4
        }
    }

    cur_text = "##########"
    while True:

        if cur_diff == "normal":
            dif_vl = 1
        elif cur_diff == "hard":
            dif_vl = 1.5
        elif cur_diff == "INSANE":
            dif_vl = 2
        elif cur_diff == "masochist":
            dif_vl = 2.5
        elif cur_diff == "TheGambler":
            dif_vl = random.random(1,2)   
        
        cur_sc = Game_States["cur_sc"]
        print("__________")
        print(Fore.GREEN + f"{cur_text}")
        print(f"{MenuTXT['Menu start']}\n{MenuTXT['menu start2']['Menu options1']}\n{MenuTXT['menu start2']['Menu options2']}{cur_diff}\n{MenuTXT['menu start2']['Menu option3']}{Game_States['cur_sc']}")
        Act = input("ENTER COMMAND: / start / dif (difficulty name) / info dif / load: ").lower().replace(" ","#").split("#")
        cur_text = Act
        
        if Act[0] == "start" and len(Act) == 1:
            os.system('cls')
            break
        elif Act[0] == "load" and len(Act) == 1:
            file_load()
        elif Act[0] == "difvl" and len(Act) == 1:
            if Act[1] == "difvl":
                dif_vl = amount
        elif Act[0] == "sc" and len(Act) == 2:
            if Act[1] == "lin":
                Game_States["cur_sc"] = "lin"
            elif Act[1] == "expo": 
                Game_States["cur_sc"] = "expo"    
        
        elif Act[0] == "dif" and len(Act) == 2:
            cur_diff = Game_dif_options["dif_choice"].get(Act[1],"")
            if cur_diff == "":
                cur_text = "INVALID"
            os.system('cls')
            continue
        elif Act[0] == "info" and len(Act) == 2:
            if Act[1] == "dif":
                cur_text = MenuTXT["menu start2"]["difficulty_list"]
        else:
            os.system('cls')
            continue

        os.system('cls')

def Glitch_Anim(color,delay):
    glitch_effect = ["* ✖ ✶ ✷ ✶ * ✷ ✖ ","✶ * ✷ ✖ * ✖ ✶ ✷ ","✖ * ✶ * ✶ * ✷ ✖","✷ ✶ * ✖ ✖ * ✶ * "]
    for i in range (delay):
        if color == "GREEN":
            print(Fore.GREEN +f"\r{random.choice(glitch_effect)}",end="")
        elif color == "RED":
            print(Fore.RED +f"\r{random.choice(glitch_effect)}",end="")
        time.sleep(0.02)
    print(Fore.MAGENTA+"\r---")    

def Flare(times,anim,randomn):
    animations = {
        "wave":["_____","-____","_-___","__-__","___-_","____-","___-_","__-__","_-___","-____"],
        "hash":["#-/--","-#//-","--#|-","--\#-","-??-#","--\#-","--#|-","-#//-","#-/--"],
        "bubble":["#####()#####","#####(#)####","#####(##)###","####(##)####","###(####)###","##(######)##","#(########)#","#(#########)","(##########)"],
        "holy":["══════════","╬═════════","═╬════════","══╬═══════","═══╬══════","════╬═════","═════╬════","══════╬═══","═══════╬══","════════╬═","═════════╬"],
        "circle":["  ○  ","  ●  ","  ◯  ","  ◎  ","  ◉  ","  ◌  ","  ◍  ","  ◑  " ,"  ◒  " ,"  ◓  " ,"  ◔  " ,"  ◕  " ,"  ◖  " ,"  ◗  "],
        "crypt":["≈≥∫∈∂∉÷√∩×∏∞≠∑±∆∪≤∇","∪∑∂≠∩≥√∈∞×∆÷±∇∫≈≤∉∏","∂∩×∞∈∪≈÷∫≥∏∑≠∇∆≤±√∉","∉±≈∫×≥∂∆÷∑∞∩∏≤√∇≠∈∪","∏√∂∩≈∪∞∇±≥∈≠×÷≤∫∆∑∉","×∑≠≥∈±√∞∂∉÷≤∆∫≈∩∪∏∇","∂≥∉√≈∫∞∩≠×∑±∇÷∪∈≤∆∏","∞≈÷∫∉±≥×∏∈∪∆∑√≠∂∇∩≤","≠∉∑∆∪≥∞×∩√±≈∏∈∂∫÷≤∇","∇∞≤≠∪∩÷∈≈∂±∆∫√≥×∑∉∏"],
        "poly":["▄ ▀ ▌ ▐ ■ ▪ ▫ ▲ ▼ ◄ ► ◆ ◊","◄ ▐ ▫ ▼ ▪ ▲ ▌ ► ◆ ■ ▀ ▄ ◊","◆ ▪ ▀ ▌ ▫ ► ◊ ▲ ◄ ■ ▐ ▼ ▄","◊ ▲ ▪ ▀ ▌ ▐ ◆ ▼ ▄ ► ▫ ■ ◄","▼ ▌ ◄ ▐ ▫ ■ ◊ ▪ ▲ ▄ ▀ ► ◆","► ▀ ▲ ▫ ▄ ◄ ◆ ▐ ▪ ▼ ▌ ■ ◊","■ ▲ ◊ ▼ ◆ ▄ ▪ ▀ ▐ ▫ ► ▌ ◄","▐ ► ▫ ◄ ▲ ▌ ▪ ▀ ◊ ◆ ▄ ▼ ■","▲ ◆ ▀ ◄ ▫ ▼ ▄ ▐ ► ▌ ▪ ◊ ■","▫ ▀ ◆ ▲ ▌ ◊ ▄ ▼ ▐ ▪ ► ■ ◄"],
        "arrow":["← ↑ → ↓ ↔ ↕ ↖ ↗ ↘ ↙ ⇐ ⇑ ⇒ ⇓ ⇔ ⇕","↖ ← ↑ ↗ ↔ → ↘ ↓ ↕ ↙ ⇐ ⇑ ⇒ ⇓ ⇔ ⇕","↑ ↗ → ↘ ↕ ↓ ↙ ← ↔ ↑ ⇑ ⇒ ⇓ ⇐ ⇕ ⇔","↗ → ↘ ↓ ↙ ← ↑ ↖ ↔ ↕ ⇒ ⇓ ⇐ ⇑ ⇕ ⇔","→ ↘ ↓ ↙ ← ↖ ↑ ↗ ↔ ↕ ⇓ ⇐ ⇑ ⇒ ⇔ ⇕","↘ ↓ ↙ ← ↖ ↑ ↗ → ↕ ↔ ⇐ ⇑ ⇓ ⇒ ⇕ ⇔","↓ ↙ ← ↖ ↑ ↗ → ↘ ↔ ↕ ⇑ ⇐ ⇒ ⇓ ⇔ ⇕","↙ ← ↖ ↑ ↗ → ↘ ↓ ↕ ↔ ⇑ ⇒ ⇐ ⇓ ⇕ ⇔","← ↖ ↑ ↗ → ↘ ↓ ↙ ↔ ↕ ⇒ ⇐ ⇑ ⇔ ⇓ ⇕","↖ ↑ ↗ → ↘ ↓ ↙ ← ↕ ↔ ⇐ ⇓ ⇑ ⇒ ⇕ ⇔"],
        "oblock":["▄ ░ ▒ ▓ ▀","░ ▒ ▓ ▀ ▄","▒ ▓ ▀ ▄ ░","▓ ▀ ▄ ░ ▒"],
        "bwawe":["░ ▒ ▓ ░ ▒","▒ ▓ ░ ▒ ▓","▓ ░ ▒ ▓ ░","░ ▒ ▓ ░ ▒","▒ ▓ ░ ▒ ▓","▓ ░ ▒ ▓ ░"],
        "zigzag":["/ ?? | / ","?? | / ?? |","| / ?? | /","/ ?? | / ??"],
        "star":["★ ✦ ✧ ✪ ✫","✦ ✧ ✪ ✫ ★","✧ ✪ ✫ ★ ✦","✪ ✫ ★ ✦ ✧","✫ ★ ✦ ✧ ✪"]

    }
    Flare_list = ["wave","hash","bubble","holy","circle","crypt","poly","arrow","oblock","bwawe","zigzag","star"]
    aval_colors = [lambda:Fore.RED,lambda:Fore.GREEN,lambda:Fore.MAGENTA,lambda:Fore.YELLOW,lambda:Fore.BLUE,lambda:Fore.CYAN]
    radm_C = random.sample(aval_colors,k=1)[0]()
    if randomn == False:
        for i in range (times):
            for lay in animations[anim]:
                print(f"\r{radm_C}{lay}",end="")
                time.sleep(0.07)
        print("\r                                                                          ",end="")
        print("\r",end="")
    else:
        for i in range (times):
            for i in range(len(animations[anim])):
                print(f"\r{radm_C}{random.choices(animations[anim],k=1)[0]}",end="")
                time.sleep(0.07)
        print("\r                                                                          ",end="")
        print("\r",end="")
def amount_input():
    global amount 
    while True:
        try:
            amount = int(input("enter amount: "))
            break
        except ValueError:
            print("Not a number")
            continue    

def health_cap():
    global health, sc_vl
    if health > 100+sc_vl:
            reduct = health - (100 + sc_vl)
            health -= reduct

def mana_cap():
    global mana, sc_vl
    if mana > 100+sc_vl:
            reduct = mana - (100 + sc_vl)
            mana -= reduct   
 
def Number_anim(Range,timeA,stat,Max_vl,Mul_vl):
    global G, health, mana, mp, hp, sc_vl, RD_EV_effect
    
    if stat in ("-G","G"):
        for i in range(Range):
            G_to_Give = random.randint(1+int((sc_vl*dif_vl)/(25+(sc_vl/1100))),Max_vl+int((sc_vl*dif_vl)/(16+(sc_vl/900))))
            print(Fore.YELLOW + f"\r{'+' if stat == 'G' else '-'}{G_to_Give}",end="")
            time.sleep(timeA)
        if stat == "G":
            G += G_to_Give
            print(Fore.YELLOW + Style.BRIGHT + f"\r{'+' if stat == 'G' else '-'}{G_to_Give} G ")
        elif stat == "-G":
            G -= G_to_Give - int(sc_vl/20)
            if G < 0:
                G = 0
            print(Fore.YELLOW + Style.BRIGHT + f"\r{'+' if stat == 'G' else '-'}{G_to_Give - int(sc_vl/20) } G ")
    
    elif stat == "MP":
        for i in range(Range):
            M_to_Give = random.randint(1,Max_vl)
            print(Fore.LIGHTBLUE_EX + f"\r+{M_to_Give}",end="")
            time.sleep(timeA)
        
        if cur_diff in ("hard","INSANE","masochist"):
            Rdm = random.randint(0,1)
            mp += M_to_Give - Rdm
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\r+{M_to_Give - Rdm} M Potion ")
        else:
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\r+{M_to_Give} M Potion ")
            mp += M_to_Give 
    
    elif stat == "HP":
        for i in range(Range):
            H_to_Give = random.randint(1,Max_vl)
            print(Fore.LIGHTRED_EX + f"\r+{H_to_Give}",end="")
            time.sleep(timeA)    
        if cur_diff in ("hard","INSANE","masochist"):
            Rdm = random.randint(0,1)
            hp += H_to_Give - Rdm
            print(Fore.LIGHTRED_EX + Style.BRIGHT + f"\r+{H_to_Give - Rdm} H Potion ")
        else:
            hp += H_to_Give
            print(Fore.LIGHTRED_EX + Style.BRIGHT + f"\r+{H_to_Give } H Potion ")

    elif stat in ("+HEALTH", "-HEALTH"):
        health_red = 0
        for i in range(Range):
            Health_to_Give = random.randint(1+int((sc_vl*dif_vl)/(10+(sc_vl/1100))),Max_vl+int((sc_vl*dif_vl)/(3+(sc_vl/900))))
            print(Fore.RED + f"\r{'+' if stat =='+HEALTH' else '-'}{Health_to_Give}", end="")
            time.sleep(timeA)
        if stat == "+HEALTH": 
            health += int(Health_to_Give / Mul_vl)
            if health > (100 + sc_vl):
                health_red = health - (100+sc_vl)
                health_cap()
            print(Fore.RED + Style.BRIGHT + f"\r+{int(Health_to_Give / Mul_vl) - health_red} Health ")
        elif stat == "-HEALTH":
            health -= int(Health_to_Give / Mul_vl)
            print(Fore.RED + Style.BRIGHT + f"\r-{int(Health_to_Give / Mul_vl)} Health ")    

    elif stat in ("+MANA","-MANA"):
        mana_red = 0
        for i in range(Range):
            Mana_to_Give = random.randint(1+int((sc_vl*dif_vl)/(5+(sc_vl/1100))),Max_vl+int((sc_vl*dif_vl)/(2.5+(sc_vl/900))))
            print(Fore.BLUE +f"\r+{Mana_to_Give}",end="")
            time.sleep(timeA)
        if stat == "+MANA":
            mana += int(Mana_to_Give / Mul_vl)
            if mana > (100 + sc_vl):
                mana_red = mana - (100+sc_vl)
                mana_cap()
            print(Fore.BLUE + Style.BRIGHT + f"\r+{int(Mana_to_Give / Mul_vl) - mana_red} Mana ") 
        elif stat == "-MANA":
            mana -= int(Mana_to_Give / Mul_vl)
            print(Fore.BLUE + Style.BRIGHT + f"\r-{int(Mana_to_Give / Mul_vl)} Mana ")    
    
def Rnd_Number_Guess(Gses):
    global G, health, mana, sc_vl
    print("________________")
    if cur_diff in ("hard","INSANE","masochist"):
        RnG = random.randint(1,50+(sc_vl*dif_vl))
        print(Fore.GREEN + Back.WHITE + f"Guess the number 1-{int(1,50+sc_vl*dif_vl)} for a reward in {Gses+int(sc_vl/50)} tries")
    else:
        RnG = random.randint(1,50+sc_vl)
        print(Fore.GREEN + Back.WHITE + f"Guess the number 1-{50+sc_vl} for a reward in {Gses+int(sc_vl/50)} tries")

    while True:
        for gueses in range(Gses+int(sc_vl/50)):
            try:
                guess = int(input("Number: "))
            except ValueError:
                print("invalid")  
                guess = 0  
            if guess > RnG:
                print("guess Too High")
            if guess < RnG:
                print("guess Too Low")
            if guess == RnG:
                break        
        if guess == RnG:
            print(Fore.WHITE + Back.CYAN + f"You won in {gueses + 1} tries ")
            Number_anim(30,0.02,"G",20,10)
            break
        if guess != RnG:
            T_f = random.randint(1,10 + int(sc_vl/2))
            health -= T_f
            print(Fore.WHITE + Back.RED + f"you Lost correct number was {RnG}")
            Number_anim(30,0.02,"-HEALTH",10,5)   
            break               

def difficulty_comparison(PlaceA,PlaceB):
    if cur_diff in ("hard","INSANE","masochist"):
        return PlaceA()
    else:
        return PlaceB()

def Store():
    global mp, hp, G, amount, sc_vl
    price = difficulty_comparison(lambda: 5+int(sc_vl/(24-int(dif_vl*3))),lambda: 5+int(sc_vl/30) )
    if Karma in "GOOD":
        price -= 1+ int(sc_vl/50)
    elif Karma in "BAD":
        price += 1+ int(sc_vl/25)    
    while True:
        print(Fore.WHITE + Back.LIGHTBLACK_EX + "_______STORE_______")
        print(Fore.YELLOW + f"You have {G} G")
        print(f"Items: BuyH {price}.G / BuyM {price}.G / Buylootp {int(price*2)}.G exit :")
        choice = input("Action: ").lower()
            
        if choice == "exit":
            print(Fore.WHITE + Back.CYAN +"Exited")
            break
        elif choice == "buym" :
            amount_input()
            if G >= (amount * price):
                G -= price * amount
                mp += amount
                print(Fore.BLUE +f"▶ ▶ ▶ Obtained {amount} M Potion")
                print(Fore.YELLOW +f"◀ ◀ ◀ -{amount*price} G") 
            else: 
                print(Fore.WHITE + Back.RED +"Not enough G")    
        elif choice == "buyh" :
            amount_input()
            if G >= (amount * price):
                G -= price*amount
                hp += amount
                print(Fore.RED +f"▶ ▶ ▶ Obtained {amount} H Potion")
                print(Fore.YELLOW +f"◀ ◀ ◀ -{amount*price} G")
            else:
                print(Fore.WHITE + Back.RED +"not enough G")
        elif choice == "buylootp":
            amount_input()
            G_sum = 0
            item_sum = 0
            if G >= (amount * price):
                for i in range(amount):
                    if len(inventory) < max_inv:
                        inventory.append("lootp")
                        G -= int(price*2)
                        G_sum += int(price*2)
                        item_sum += 1
                    else:
                        print("Max inventory")
                        break
                print(Fore.RED +f"▶ ▶ ▶ Obtained {item_sum} Loot Pouch")
                print(Fore.YELLOW +f"◀ ◀ ◀ -{G_sum} G")
            else:
                print(Fore.WHITE + Back.RED +"not enough G")
        
        else:
            print(Fore.WHITE + Back.RED +"invalid")
            
            
def Show_stats():
    glitch_effect = ["* ✖ ✶ ✷ ✶ * ✷ ✖ ","✶ * ✷ ✖ * ✖ ✶ ✷ ","✖ * ✶ * ✶ * ✷ ✖","✷ ✶ * ✖ ✖ * ✶ * "]
    if random.randint(0,100) > 1:
        print(Fore.BLACK + Back.WHITE + f"health:{health} mana:{mana} H.Potions:{hp} M.potions:{mp} G:{G}")
    else:
        for i in range(100):
            print(Fore.CYAN + Back.YELLOW + Style.BRIGHT + f" \r{random.choice(glitch_effect)}", end="")
            time.sleep(0.01)
        print(Fore.CYAN + Back.YELLOW + Style.BRIGHT + "\r* ✖ ✶ ✷ ✶ * ✷ ✖* ✖ ✶ ✷ ✶ * ✷ ✖*-something went wrong")

def Use_Hp():
    global health, hp, sc_vl, amount 
    hlv = 0
    h_cp = 0
    amount_input()
    if hp >= amount and health < (100 + sc_vl):
        for i in range(amount):
            hp -= 1
            T_f = random.randint(10+int((sc_vl*dif_vl)/(8+(sc_vl/1100))),30+int((sc_vl*dif_vl)/(4+(sc_vl/900))))
            health += T_f
            hlv += T_f
            if health > (100 + sc_vl):
                h_cp = health - (100 + sc_vl)
                health_cap()
                break
        print(Fore.RED +f"+{hlv - h_cp } health")
    else:
        print(Fore.WHITE + Back.RED +"Can't use")

def Use_Mp():
    global mana, mp, sc_vl, amount
    mlv = 0
    m_cp = 0
    amount_input()
    if mp >= amount and mana < (100 + sc_vl):
        for i in range(amount):
            mp -= 1
            T_f = random.randint(10+int((sc_vl*dif_vl)/(8+(sc_vl/1100))),30+int((sc_vl*dif_vl)/(4+(sc_vl/900))))
            mana += T_f
            mlv += T_f
            time.sleep(0.1)
            if mana > (100 + sc_vl):
                m_cp = mana - (100 + sc_vl)
                mana_cap()
                break
        print(Fore.BLUE +f"+{mlv - m_cp} mana")
    else:
        print(Fore.WHITE + Back.RED +"Can't use")

def karma_choice(choice):
    global Karma
    if choice: # TRUE
        if Karma == "NEUTRAL":
            Karma = "GOOD"
        elif Karma in ("BAD"):
            Karma = "NEUTRAL"
    else: #Take karma
        if Karma == "GOOD":
            Karma = "NEUTRAL"
        elif Karma == "NEUTRAL":
            Karma = "BAD"

streak = 0
def fair_random():
    global streak
    cont_streak = 2
    random_chance = 0.5
    streak_addision = 1
    streak_elimination = 0
    streak_random_chance_reduction = 0.1
    
    if streak >= cont_streak:
        random_chance = streak_random_chance_reduction
    if random.random() <= random_chance:
        streak += streak_addision
        return True
    else:
        streak = streak_elimination
        return False

def Item_use(Item_name):
    global mana, inventory, health, G, sc_vl, dif_vl, Karma, Karma_vl
    Every_item_ever = {
        "mpouch":["+MANA"],
        "lmpouch":["+MANA"],
        "cmpouch":["+MANA","-MANA"],
        "chpouch":["+HEALTH","-HEALTH"],
        "hpouch":["+HEALTH"],
        "lhpouch":["+HEALTH"],
        "maxs":["+HEALTH","+MANA"],
        "lootbox":["+HEALTH","+MANA","G","MP","HP"],
        "amuletog":["G","-G"],
        "horb":"horb",
        "morb":"morb",
        "rpot":["+HEALTH","-MANA"],
        "dpot":["+HEALTH","+MANA"]
        
    }
    Flare_list = random.choice(["wave","hash","bubble","holy","circle","crypt","poly","arrow","oblock","bwawe","zigzag","star"])
    stat = Every_item_ever.get(Item_name)
    aval_colors = [lambda:Fore.RED,lambda:Fore.GREEN,lambda:Fore.MAGENTA,lambda:Fore.YELLOW,lambda:Fore.BLUE,lambda:Fore.CYAN]
    if Item_name in inventory:
        inventory.remove(Item_name)
        print(Fore.BLUE+f"[{Item_name}] was used")
        Flare(5,Flare_list,False)
    else:
        print(Fore.RED+Back.WHITE+"INVALID") 
        Item_name = "sdfgahsdfhasdhsdfgdhsdfhdf"       
    if Item_name in ("lhpouch","cmpouch","chpouch","mpouch","lmpouch","hpouch"):
        if fair_random():
            print(Fore.YELLOW+"Big Restore")
            if Item_name in ("mpouch","hpouch"):
                Number_anim(40,0.02,stat[0],30,0.7) 
            elif Item_name in ("lmpouch","cmpouch","chpouch","lhpouch"):
                Number_anim(40,0.02,stat[0],30,0.3) 
        else:
            if Item_name in ("mpouch","lmpouch","hpouch","lhpouch"):
                print(Fore.MAGENTA+"Sad restore")
            else:
                print(Fore.RED+Back.LIGHTRED_EX+" Curse ")
            if Item_name in ("mpouch","hpouch"):
                Number_anim(40,0.02,stat[0],10,5)
            elif Item_name in ("cmpouch","chpouch"):
                Number_anim(40,0.02,stat[1],30,0.5)
            else:
                Number_anim(40,0.02,stat[0],20,1)
    elif Item_name == "maxs":
        Number_anim(100,0.02,stat[random.randint(0,1)],999,0.1)
    elif Item_name == "lootbox":
        for i in range (60):
            radm_C = random.sample(aval_colors,k=1)[0]()
            pick = random.sample(stat,k=1)[0]
            print(f"\r{radm_C}{pick}",end="")
            time.sleep(0.09)
        print(radm_C+f"\rReward {pick}")
        max_values = {
            "+MANA":50,
            "+HEALTH":50,
            "G":10,
            "MP":3,
            "HP":3
        }
        if pick in ("+MANA","+HEALTH","G"):
            Number_anim(60,0.02,pick,max_values[pick],1)
        else:
            Number_anim(60,0.02,pick,max_values[pick],1)
    elif Item_name == "amuletog":
        rand_numb = random.randint(1,10+int((sc_vl*dif_vl)/(16+(sc_vl/900))))
        print("How much gold do you want to get dont get too greedy")
        amount_input()
        if amount <= rand_numb:
            print(Fore.YELLOW+"you got rewarded")
            G += amount
            print(Fore.YELLOW+f"+{amount}")
        else:
            print("You Got too greedy")
            G_to_take = int(rand_numb/2)
            G -= G_to_take
            print(Fore.YELLOW+f"-{G_to_take}")
    elif Item_name in ("horb","morb"):
        if Item_name == "morb":
            Number_anim(40,0.02,"+MANA",int(health/1.5),1)
        else:
            Number_anim(40,0.02,"+HEALTH",int(mana/1.5),1)
    elif Item_name == "chest":
        chest_event() 
    elif Item_name == "rpot":
        print(Fore.YELLOW+"Rage potion active")  
        if mana >= 10:
            Number_anim(40,0.02,stat[0],mana,1)
            Number_anim(40,0.02,stat[1],mana,2)
        else:
            Number_anim(40,0.02,stat[0],50,1)
            Number_anim(40,0.02,stat[1],100,2)
    elif Item_name in ("mpotog","hpotog"):
        if Item_name in ("mpotog"):
            Number_anim(49,0.02,"+MANA",(G*5)+1,1)
        else:
            Number_anim(49,0.02,"+HEALTH",(G*5)+1,1)
    elif Item_name == "elootbox":
        inventory_add("special")
    elif Item_name == "lgold":
        Number_anim(40,0.02,"-G",int(G/2.5)+1,1)
        if random.randint(1,10) < 5:
            Number_anim(40,0.02,"+MANA",(G*5),1)
        else:
            Number_anim(40,0.02,"+HEALTH",(G+10),1)
    elif Item_name == "blpouch":
        mana_g = health
        health_g = mana
        mana = mana_g
        health = health_g
        print(Fore.YELLOW+" /\ SWAPPED /\ ")
        Show_stats()
    elif Item_name == "hwater":
        good_vl = 2
        evil_vl = 2
        if Karma_vl < 0:
            evil_vl = int(Karma_vl/-1)+1
        else:
            good_vl = Karma_vl+1
        for i in range(15):
            print(Fore.YELLOW+f"\r╬ HOLY ╬",end="")
            time.sleep(0.09)
            print(Fore.LIGHTRED_EX+"\r◊ EVIL ◊",end="")
            time.sleep(0.09)
        if Karma == "BAD":
            print(Fore.LIGHTRED_EX+"\r◊ EVIL ◊")
            Number_anim(40,0.02,"-HEALTH",evil_vl,1)
            karma_choice(True)
            print(Fore.LIGHTRED_EX+f"Bitter Medicine, Karma - {Karma}")
            Karma_vl += 5
        elif Karma == "GOOD":
            print(Fore.YELLOW+f"\r╬ HOLY ╬")
            Number_anim(40,0.02,"+HEALTH",(good_vl*7),1)
        else:
            print(Fore.MAGENTA+f"\rIt has no effect on you , you are neither good or bad")
            Number_anim(40,0.02,"G",2,10)
            Karma_vl += 1
    elif Item_name == "dpot":
        if Karma_vl < 0:
            evil_vl = int(Karma_vl/-1)
        else:
            evil_vl = 2
        Number_anim(40,0.02,stat[random.randint(0,1)],10+int(evil_vl*2),1)
        karma_choice(False)
        Karma_vl -= 5
    elif Item_name == "invslot":
        print("+ 1 Inventory slot")
        max_inv += 1
    elif Item_name == "lootp":
        inventory_add("pouch")

def Inventory():
    global max_inv,inventory
    def inv_disp():
        if len(inventory) >= 1:
            (inventory).sort()
            print (Back.MAGENTA+Fore.WHITE+f"Inventory -",end=" ")
            break_l = 0
            for items in inventory:
                print(Back.MAGENTA+Fore.WHITE+f" {items} ",end=" ")
                break_l +=1
                if break_l >= 10:
                    print("\n")
                    break_l = 0
            print("",end="\n")    
        else:
            print(Back.MAGENTA+Fore.WHITE+"Inventory - empty |")    
    def inv_kill():
        while True:
            print("________")
            inv_disp()
            Act = input(Fore.BLACK+Back.WHITE+"\rCommads / (item) / exit: ").lower()
            if "exit" in Act:
                break
            elif Act in inventory and len(inventory) >= 1:
                inventory.remove(Act)
                print(f"{Act} was removed")
                break
            else:
                print(Fore.RED+Back.WHITE+"INVALID")
        
    item_list = {
            "mpouch":"-\n[Mana Pouch] : restores either no mana or a lot in a pinch \n-",
            "hpouch":"-\n[Health Pouch] : restores either no health or a lot in a pinch \n-",
            "lmpouch":"-\n[Large Mana Pouch] restores either no mana or a lot more than avarage \n-",
            "lhpouch":"-\n[Large Health Pouch] restores either no health or a lot more than avarage \n-",
            "maxs":"-\n[Max Stat] restores health/mana to its max at random \n-",
            "cmpouch":"-\n[Cursed Mana Pouch] either restores mana or drains it \n-",
            "chpouch":"-\n[Cursed Health Pouch] either restores health or drains it \n-",
            "lootbox":"-\n[Loot Box] use for a random reward \n-",
            "amuletog":"-\n[Amulet Of Greed] Dont get greedy\n-",
            "morb":"-\n[Mana Orb] regenerates mana based on youre current health \n-",
            "horb":"-\n[Health Orb] heals you based on youre current mana \n-",
            "chest":"-\n[Chest] its a chest \n-",
            "rpot":"-\n[Rage Potion] has a chance to give a lot of health but takes a lot of mana either way \n-",
            "invslot":"-\n[Inventory Slot] adds one inventory slot \n-",
            "mpotog":"-\n[Mana potion of greed] Restores Mana based on youre current gold \n-",
            "hpotog":"-\n[Health potion of greed] Restores Health based on youre current gold \n-",
            "elootbox":"-\n[Exotic Loot Box] randomly gives you inventory items \n-",
            "lgold":"-\n[Liquid Gold] uses gold to regenerate randomly mana or health the more gold you have the more you can potetially rgenerate \n-",
            "blpouch":"-\n[Blood Pouch] swapts health with mana \n-",
            "hwater":"-\n[Holy Water] Makes you a better person, burns if Evil, heals if holy \n-",
            "dpot":"-\n[Demon Potion] The more negative karma you have the stronger the potion gets. The potion lowers youre karma, regenerates either mana or health at random \n-",
            "lootp":"-\n[Loot pouch] Like a loot box but its a loot pouch has a chance to drop good loot \n-",

        
        }
    main_loop_cmds = {
        "inv":inv_disp,
        "throw":inv_kill,
        }
    while True :
        Show_stats
        cmd = input(Fore.MAGENTA+"Enter commands: exit (e) / inv / throw / info (item name) / use (item name):  ").lower().replace(" ","#").split("#")
        result = main_loop_cmds.get(cmd[0],"")  
        if cmd[0] in ("e","exit"):
            break
        elif cmd[0] == "use" and len(cmd) == 2:
            if cmd[1] in inventory:
                Item_use(cmd[1])
            else:
                print(Fore.RED+Back.WHITE+"INVALID")    
        elif cmd[0] == "info" and len(cmd) == 2:
            inf = item_list.get(cmd[1]," ")
            if inf != " ":
                print(Fore.BLACK+Back.WHITE+f"{inf}")
            else:
                print(Fore.RED+Back.WHITE+"INVALID")
        elif result == "":
            print(Fore.RED+Back.WHITE+"Invalid")
            continue 
        else:
            result()

def inventory_add(L_table):
    def rand_pick(weight,item):
        return random.choices(item,weights=weight,k=1)[0]
    
    weight = { "all":[5,5,5,5,4,4,4,4,4,4,3,3,3,3,3,2,1,1,1],
                "boss":[20,25,15,15,10,10,5],
                "special":[5,5,5,5,5,5,5,5],
                "normal":[20,25,15,15,10,10,5],
                "pouch":[100,100,30,30,10,10,10,10,1]
        }
    aval_colors = [lambda:Fore.RED,lambda:Fore.GREEN,lambda:Fore.MAGENTA,lambda:Fore.YELLOW,lambda:Fore.BLUE,lambda:Fore.CYAN]
    aval_item = { 
        "boss":["horb","maxs","rpot","morb","amuletog","chest","lootbox"],
        "normal":["mpouch","cmpouch","chpouch","morb","hpouch","horb","lootbox"],
        "special":["chest","lootbox","amuletog","rpot","dpot","hwater","lmpouch","lhpouch"],
        "test":["chest","amuletog","rpot","maxs","maxs","maxs","maxs"],
        "all":["hpouch","mpouch","chpouch","cmpouch","morb","mpotog","hpotog","horb","lmpouch","lhpouch","amuletog","rpot","dpot","blpouch","lgold","hwater","chest","lootbox","elootbox"],
        "pouch":["hpouch","mpouch","morb","horb","lhpouch","lmpouch","hpotog","mpotog","rpot"]
                }
    for i in range(65):   #TEMP per - 65              
        radm_C = random.sample(aval_colors,k=1)[0]()
        itemz = random.sample(aval_item[L_table],k=1)[0]
        print(f"\r|{radm_C} {itemz}|",end = "")
        time.sleep(0.09)
        print(f"\r                             ",end ="")
    item_t_add = rand_pick(weight[L_table],aval_item[L_table])
    print(radm_C+f"\ryou got - {item_t_add} - ")
    if len(inventory) < max_inv:
        inventory.append(item_t_add)
    else:
        while True :
            print(radm_C+f"do you want to retrieve ? - {item_t_add} - ")
            if len(inventory) == max_inv:
                print(Fore.RED+Back.WHITE+"inventory full")
            Act = input("Commands: inv / exit / retrieve (rtw) : ").lower()
            if Act == "exit":
                break
            elif Act in ("inv"):
                Inventory()
            elif Act == "rtw":
                if len(inventory) < max_inv:
                    inventory.append(item_t_add)
                    break
                else:
                    print(Fore.RED+Back.WHITE+"inventory full")
            else:
                print(Fore.RED+Back.WHITE+"INVALID")        
                    
 
def  Monster_F(name, Hmin, MaxD, Agro, atribute):                             #BATTLE ENGINE
    global health, mana, G, MonD, sc_vl, mp, hp, dif_vl, Mhp, Const_mhp, M_Pots,Const_mhp ,Turn_Blocked,M_Turn_Blocked, E_Boss, boss_RNG, Karma, Karma_vl, enemy_missed, BossD 
    enemy_missed = 0
    enemy_agressive = False

    if atribute in ("PSN","DOUBLE PSN","LFS","GREEDY","BRN","Dragon") and random.randint(1,200) == 5:
        E_Boss = True
    elif atribute == ("BOSS"):
        E_Boss = True
    elif random.randint(1,300) == 47:
        E_Boss = True
    else:
        E_Boss = False    

    Mhp = difficulty_comparison(lambda:random.randint(Hmin+int((sc_vl*dif_vl)/3),70+int((sc_vl*dif_vl)/1.1)),lambda:random.randint(Hmin+int(sc_vl),70+int(sc_vl)))
    if E_Boss == True:
        Mhp *= 3
    Const_mhp = Mhp
    M_Pots = difficulty_comparison(lambda:random.randint(0,3+int(dif_vl)),lambda:random.randint(0,3))
    turns = 0
    
    def enemy_stats():
        print("- MONSTER - ")
        print(f"max_mhp - {Const_mhp}, mhp - {Mhp}, boss - {E_Boss}, turns - {turns}, agressive - {enemy_agressive}, E_potions - {M_Pots}")
        print(f"NRM_M_D - MIN-{1+int((sc_vl*dif_vl)/(5.5+(sc_vl/1100)))} MAX-{MaxD+int((sc_vl*dif_vl)/(3+(sc_vl/900)))}, NRM_BOSS_M_D - MIN-{1+int(((sc_vl*dif_vl)/(31+(sc_vl/1100))))} MAX-{1+MaxD+int(((sc_vl*dif_vl)/(30+(sc_vl/900))))},")
        print(f"CRIT_M_D - MIN-{10+int(((sc_vl*dif_vl)/(2.5+(sc_vl/1100))))} MAX-{10+MaxD+int(((sc_vl*dif_vl)/(2+(sc_vl/900))))}, CRIT_BOSS_D - MIN-{10+int(((sc_vl*dif_vl)/(31+(sc_vl/1100))))} MAX-{11+MaxD+int(((sc_vl*dif_vl)/(30+(sc_vl/900))))}")
        print("- PLAYER - ")
        print(f"Max health - {100 + sc_vl}, Max mana - {100 + sc_vl}, explored - {explored} times,")
        print(f"Monsters killed - {MonD} sc_vl {sc_vl}" )
        print(f"difficulty - {cur_diff}, scaling - {cur_sc}, difficulty value - {dif_vl}, K-{Karma}|{Karma_vl}")
        print(f"NRM_dmg - MIN-{1+int((sc_vl*dif_vl)/(5+(sc_vl/1100)))} MAX-{20+int((sc_vl*dif_vl)/(3+(sc_vl/900)))}, CRIT_dmg - MIN-{20+int((sc_vl*dif_vl)/(3+(sc_vl/1100)))} MAX-{50+int((sc_vl*dif_vl)/(1.2+(sc_vl/900)))}")
        print(f"Potion_give - MIN-{10+int((sc_vl*dif_vl)/(8+(sc_vl/1100)))} MAX-{30+int((sc_vl*dif_vl)/(4+(sc_vl/900)))}, Mana_regen_vl - {5+int(int(sc_vl/dif_vl)/8)}")
        print(f"MANA_C - MIN-{1+int((sc_vl*dif_vl)/(12+(sc_vl/1100)))} MAX-{20+int((sc_vl*dif_vl)/(3.5+(sc_vl/900)))}")
        print("-")

    def status_effect():                                                               #STATUS EFFECT
        global Mhp, health, mana
        if atribute in ("PSN", "DOUBLE PSN") and Mhp > 0:
            if atribute == "PSN":
                print(Fore.GREEN + Back.MAGENTA + "✦ Poisoned ✦")
                Number_anim(30,0.02,"-HEALTH",10,2)
            else:
                print(Fore.GREEN + Back.MAGENTA + "✦ DOUBLE Poison ✦")
                Number_anim(30,0.02,"-HEALTH",10,2)
                Number_anim(30,0.02,"-HEALTH",10,2)
        if atribute == "LFS" and Mhp > 0 and fair_random():
            print(Fore.RED +f"◀ ◀ ◀ ╬ Lifestole health ╬")
            Number_anim(30,0.02,"-HEALTH",10,2)
            Rdm = difficulty_comparison(lambda:random.randint(0+int((sc_vl*dif_vl)/(15+(sc_vl/1100))),20+int((sc_vl*dif_vl)/(10+(sc_vl/900)))),lambda:random.randint(0+int((sc_vl*dif_vl)/(15+(sc_vl/1100))),5+int((sc_vl*dif_vl)/(10+(sc_vl/900)))))
            print(Fore.RED +f"◀ ◀ ◀ ╬ {name} regenerated +{Rdm} stolen health ╬")
            Mhp += Rdm
        if atribute == "GREEDY" and fair_random() :
            print(Fore.YELLOW + Back.WHITE+"ThE GoBliN LikEs GoulD")
        if atribute == "MGC" and Mhp > 0 and fair_random():
            print(Fore.WHITE + Back.BLUE +f"◀ ◀ ◀ captured mana")
            Number_anim(30,0.02,"-MANA",10,2)
        if atribute == "BRN" and Mhp > 0 and fair_random():
            print(Fore.YELLOW + Back.RED + f"◀ ◀ ◀  Burned-")
            Number_anim(30,0.02,"-HEALTH",10,2)
        if name == "Dragon" and Mhp > 0 :
            print(Fore.YELLOW + Back.RED + f"◀ ◀ ◀ Burned-")
            Number_anim(30,0.02,"-HEALTH",10,2)    
    
    def enemy_ATC(MaxD,Agro):                                                              #ENEMY ATTACK
        global health,sc_vl,cur_diff,dif_vl,Mhp, enemy_missed
        if (random.randint(1,10)  <= Agro or E_Boss == True or enemy_agressive == True) and Mhp > 0:
            if random.randint(0,15) == 1:
                for i in range(2000):
                    if E_Boss == False:
                        enemy_missed = 0
                        Mdmg = random.randint(10+int(((sc_vl*dif_vl)/(2.5+(sc_vl/1100)))),10+MaxD+int(((sc_vl*dif_vl)/(2+(sc_vl/900)))))
                    else:
                        enemy_missed = 0
                        Mdmg = random.randint(10+int(((sc_vl*dif_vl)/(31+(sc_vl/1100)))),11+MaxD+int(((sc_vl*dif_vl)/(30+(sc_vl/900)))))                    
                    print(Fore.RED+f"\r-{Mdmg}",end="")
                    time.sleep(0.002)  
                print(Fore.RED + Back.BLACK + f"\r▶ ▶ ▶ -CRIT- {name} attacked -{Mdmg} health -CRIT-")
                health -= Mdmg
            else:
                for i in range(30):
                    if E_Boss == True:
                        enemy_missed = 0
                        Mdmg = random.randint(1+int(((sc_vl*dif_vl)/(31+(sc_vl/1100)))),1+MaxD+int(((sc_vl*dif_vl)/(30+(sc_vl/900)))))
                    else:
                        enemy_missed = 0
                        Mdmg = random.randint(1+int((sc_vl*dif_vl)/(5.5+(sc_vl/1100))),MaxD+int((sc_vl*dif_vl)/(3+(sc_vl/900))))
                    print(Fore.RED+f"\r-{Mdmg}",end="")
                    time.sleep(0.02)  
                print(Fore.RED+f"\r▶ ▶ ▶ {name} attacked -{Mdmg} health")
                health -= Mdmg
        else:
            enemy_missed += 1
            print(Back.YELLOW+Fore.RED+" MISSED ")        

    def palyer_atck():                                                   #PLAYER ATACK
        global Mhp, mana, hp,spells, max_spells
        def spell_format():
            global spells,max_spells
            if len(spells) < max_spells:
                while len(spells) < max_spells:
                    spells.append("[empty]")
            return spells
        def damage_calc_spells():
            global spells,mana
            spell_dict = {
                "Spell[B]":"b",
                "Spell[A]":"a"
            }
            cur_spells = []
            for spels in spells:
                spell_to_add = spell_dict.get(spels)
                cur_spells.append(spell_to_add)
            spellos = {
                "a":[random.randint(1+int((sc_vl*dif_vl)/(5+(sc_vl/1100))),20+int((sc_vl*dif_vl)/(3+(sc_vl/900)))),random.randint(5+int((sc_vl*dif_vl)/(25+(sc_vl/1100))),20+int((sc_vl*dif_vl)/(9+(sc_vl/1100)))),"Spell[A]","normal"],
                "b":[random.randint(int(mana/2),int(mana)),random.randint(int(mana/1.1111111111),int(mana)),"Spell[B]","normal"]
            }
            while True:
                print(Fore.BLACK+Back.WHITE+f"spells - {spell_format()} -")
                Act = input("Chose a spell / (spell letter): ").lower()
                if mana > 0 and Act in cur_spells:
                    returns = spellos.get(Act)
                    return returns[0],returns[1],returns[2],returns[3],True
                else:
                    returns = [0,0,0,0]
                    return returns[0],returns[1],returns[2],returns[3],False
        spell_to_M = damage_calc_spells()
        if spell_to_M[4] == True:
            if random.randint(1,100) < 6:
                for i in range(3000):
                    Rdm = random.randint(20+int((sc_vl*dif_vl)/(3+(sc_vl/1100))),50+int((sc_vl*dif_vl)/(1.2+(sc_vl/900))))
                    print(Fore.RED+f"\r-{Rdm}",end="")
                    time.sleep(0.001)    
                Mhp -= int(spell_to_M[0]*2.5)
                print(Fore.RED + Back.BLACK + f"\rused {spell_to_M[2]} ◀CRIT▶ {name} -{int(spell_to_M[0]*2.5)} hp ◀CRIT▶")
            else:
                for i in range(30):
                    Rdm = random.randint(20+int((sc_vl*dif_vl)/(3+(sc_vl/1100))),50+int((sc_vl*dif_vl)/(1.2+(sc_vl/900))))
                    print(Fore.LIGHTRED_EX+f"\r-{Rdm}",end="")
                    time.sleep(0.02) 
                Mhp -= spell_to_M[0]
                print(Fore.LIGHTRED_EX + Back.BLACK + f"\rused {spell_to_M[2]} {name} -{spell_to_M[0]} hp ")
            for i in range(30):
                Rdm = random.randint(1+int((sc_vl*dif_vl)/(12+(sc_vl/1100))),20+int((sc_vl*dif_vl)/(3.5+(sc_vl/900))))
                print(Fore.LIGHTBLUE_EX+f"\r-{Rdm}",end="")
                time.sleep(0.02)    
            Rdm = spell_to_M[1]
            print(Fore.LIGHTBLUE_EX+f"\r-{Rdm} mana cost",end="\n")
            mana -= Rdm
            return spell_to_M[3]
        else:
            print(Fore.RED+Back.WHITE+"INVALID")
            return False
    
    def M_dead():                                                                                #MONSTER DEAD
        print(Fore.WHITE + Back.CYAN +f"{'LACKY MADAFAKA' if turns == 0 else 'you won'}")
        Number_anim(30 ,0.02, "G",15,10)
            
        if M_Pots >= 1:
            if fair_random():
                print(Fore.LIGHTMAGENTA_EX+f"You found some H Potions {name} had ")
                Number_anim(30,0.02,"HP",2,9999999999999)
            elif fair_random():
                print(Fore.LIGHTMAGENTA_EX+f"You found some M Potions {name} had ")
                Number_anim(30,0.02,"MP",2,9999999999999)
        if name == "Merchant":
            if fair_random(): 
                print(Fore.LIGHTMAGENTA_EX+f"you found some potions in his bag") 
                Number_anim(30,0.02,"MP",2,99999999999999999)
                Number_anim(30,0.02,"HP",2,99999999999999999)
        elif name == "Goblin":
            if fair_random(): 
                print(Fore.LIGHTYELLOW_EX+"you found some gold he stole from you")
                Number_anim(30,0.02,"G",1, 35)
        elif name == "LifeStealer":
            if fair_random(): 
                print(Fore.LIGHTRED_EX+"You captured some stolen health")
                Number_anim(30,0.02,"+HEALTH",10,5)
        elif name == "Angry wizzard":
            if fair_random(): 
                print(Fore.LIGHTBLUE_EX+"You captured held mana")
                Number_anim(30,0.02,"+MANA",10,5)
        elif E_Boss == True:
            if fair_random():
                Number_anim(30 ,0.02, "G",20,2)
            elif fair_random():
                Number_anim(30 ,0.02, "G",20,2)
            if "Spell[B]" not in spells:
                spells.remove("[empty]")
                spells.append("Spell[B]")
            if fair_random(): 
                Number_anim(30,0.02,"MP",2,99999999999999999)
            elif fair_random():
                Number_anim(30,0.02,"HP",2,99999999999999999)
    
    def Mana_regen():
        global mana, health, sc_vl, dif_vl, amount
        H_sum = 0
        M_sum = 0
        mana_give = 5+int(sc_vl/25)
        health_take = 1+int(sc_vl/75)
        print(f"conversion rate {health_take} health to {mana_give} mana")
        while True:
            amount_input()
            if  health >= (amount) and mana <= 0:
                for i in range(amount):
                    health -= health_take
                    H_sum += health_take
                    mana += mana_give
                    M_sum += health_take 
                    if mana > 0:
                        break
                print(Fore.BLUE+f"you regenerated {M_sum} mana, you lost {H_sum} health")
                break
            else:
                print(Fore.RED+Back.WHITE+"Invalid")
                Act =  input("exit ? y/n")
                if Act == "y":
                    break
                else:
                    continue  

    def M_Used_Potion():                                       #MONSTER POTION USE 
        global Mhp,M_Pots,Const_mhp, E_Boss
        if (M_Pots >= 1 or E_Boss == True) and (fair_random() or E_Boss == True) and (Mhp < (Const_mhp/2) or E_Boss == True):
            print(Fore.RED +f"▶ ▶ ▶ {name} used a health potion")
            Pot_Health_ammount = difficulty_comparison(lambda:random.randint(1+int(sc_vl/10),10+int(sc_vl/10)),lambda: random.randint(5+int(sc_vl/15),15+int(sc_vl/10)))
            glitch_effect = ["* ✖ ✶ ✷ ✶ * ✷ ✖ ","✶ * ✷ ✖ * ✖ ✶ ✷ ","✖ * ✶ * ✶ * ✷ ✖","✷ ✶ * ✖ ✖ * ✶ * "]
            for i in range (110):
                print(f"\r{random.choice(glitch_effect)}",end="")
                time.sleep(0.02)
            print(Fore.LIGHTRED_EX +f"\r▶ ▶ ▶ {name} healed for +{Pot_Health_ammount} health")
            M_Pots -= 1
            Mhp += Pot_Health_ammount
    
    Turn_Blocked = False
    M_Turn_Blocked = False
    boss_RNG = 1 
    boss_attacked_row = 0
    boss_healed_row = 0
    while E_Boss == True:
        if health <= 0:
            if Karma == "GOOD":
                Glitch_Anim("GREEN",100)
                print(Fore.GREEN+f"you are a good person {name} spared you ")
                health = int((100+health)/2)
                break
            elif Karma == "BAD":
                Glitch_Anim("RED",100)
                print(Fore.RED+"You have done terrible things")
                break
            else:
                if random.randint(1,10) > 7:
                    Glitch_Anim("GREEN",100)
                    print(Fore.GREEN+f"{name} spared you ")
                    print(Fore.GREEN+"try to be kind")
                    health = int((100+health)/2)
                    break
                else:
                    Glitch_Anim("GREEN",100)
                    break
        if Mhp <= 0:
            BossD += 1
            while True:
                print(Fore.BLACK+Back.WHITE+"-----CHOICE-----")
                Act = input("Command: Spare / KILL ").lower()
                if Act == "spare":
                    print(f"{name} was spared ")
                    print(Fore.CYAN+f"{random.choice(good_text_choice)}")
                    Karma_vl += 10
                    if "Spell[B]" not in spells:
                        spells.remove("[empty]")
                        spells.append("Spell[B]")
                    if random.randint(1,10) < 5:
                        Number_anim(40,0.02,"G",10,2)
                    else:
                        inventory_add("boss")
                    karma_choice(True)
                    break
                elif Act  == "kill":
                    print(f"{name} was killed")
                    Karma_vl -= 10
                    karma_choice(False)
                    print(Fore.RED+f"{random.choice(bad_text_choice)}")
                    M_dead()
                    break
                else:
                    print("you must chose")
            break
        
        print(Fore.GREEN + Back.LIGHTWHITE_EX + "✦✦✦_______BOSS_______✦✦✦")             #BOSS FIGHT
        Show_stats()  
        if Mhp >= int(Const_mhp/1):
            print(Fore.WHITE+f"{atribute}:{name}: hp:{Mhp}")
        elif Mhp > int(Const_mhp/1.1):
            boss_RNG = 2
            print(Fore.WHITE+f"{atribute}:{name}: hp:{Mhp}")
        elif Mhp > int(Const_mhp/1.4):
            boss_RNG = 2
            print(Fore.WHITE+f"{atribute}:{name}: hp:{Mhp}")
        elif Mhp > int(Const_mhp/1.7):
            boss_RNG = 3
            print(Fore.MAGENTA+f"{atribute}:{name}: hp:{Mhp}")   
        elif Mhp > int(Const_mhp/2):
            boss_RNG = 4
            print(Fore.MAGENTA+f"{atribute}:{name}: hp:{Mhp}")   
        elif Mhp > int(Const_mhp/2.4):
            boss_RNG = 5
            print(Fore.BLUE+f"{atribute}:{name}: hp:{Mhp}")   
        elif Mhp > int(Const_mhp/2.8):
            boss_RNG = 6
            print(Fore.BLUE+f"{atribute}:{name}: hp:{Mhp}") 
        elif Mhp > int(Const_mhp/3):
            boss_RNG = 7
            print(Fore.LIGHTRED_EX+f"{atribute}:{name}: hp:{Mhp}")
        elif Mhp > int(Const_mhp/3.4):
            boss_RNG = 8
            print(Fore.LIGHTRED_EX+f"{atribute}:{name}: hp:{Mhp}")
        elif Mhp > int(Const_mhp/4):
            boss_RNG = 9
            print(Fore.RED+f"{atribute}:{name}: hp:{Mhp}")
        else:
            boss_RNG = 1
            print(Fore.RED+f"{atribute}:{name}: hp:{Mhp}")
        Act = input("Actions: fight / parry / UseH / UseM / RegenMana(rgm) / inv : ").lower()
        if Act == "info":
            enemy_stats()
            continue
        elif Act == "inv":
            Inventory()
            continue
        elif Act in ("fight","f") and mana > 0:
            if M_Turn_Blocked == False:
                if palyer_atck() == False:
                    continue
                if (random.randint(1,10) < boss_RNG or boss_attacked_row >= 2 ) and boss_healed_row < 2 :
                    M_Used_Potion()
                    boss_healed_row += 1
                    boss_attacked_row = 0
                else:        
                    enemy_ATC(MaxD,Agro)
                    boss_healed_row = 0
                    boss_attacked_row += 1
            elif M_Turn_Blocked == True:
                print(Fore.GREEN+f"{name} turn was Blocked")
                if palyer_atck() == False:
                    continue
                else:
                    M_Turn_Blocked = False     
        elif Act in ("parry","p"):
            print(Fore.CYAN+Back.WHITE+"-parried-")
            Glitch_Anim("GREEN",40)
            print(Fore.GREEN +f"\r▶ ▶ ▶ ◀ ◀ ◀")
            if (random.randint(1,10) < boss_RNG or boss_attacked_row >= 2 ) and boss_healed_row < 2 :
                print(Fore.RED+" UNSUCSECFULL -YOU LOSE A TURN-")
                M_Used_Potion()
                boss_healed_row += 1
                boss_attacked_row = 0
                Turn_Blocked = True
            else:
                print(Fore.MAGENTA+f"- {name} ATTACK BLOCKED-")
                boss_healed_row = 0
                boss_attacked_row += 1
                print("You get a free turn")
                M_Turn_Blocked = True
                continue
        elif Act in ("useh","h","usem","m","regenmana","rgm"):
                if M_Turn_Blocked == True:
                    print(Fore.BLUE+Back.WHITE+"Monster Turn Blocked")     
                if Act in ("useh","h"):
                    if M_Turn_Blocked == False:
                        Use_Hp()
                        if (random.randint(1,10) < boss_RNG or boss_attacked_row >= 2 ) and boss_healed_row < 2 :
                            M_Used_Potion()
                            boss_healed_row += 1
                            boss_attacked_row = 0
                        else:        
                            enemy_ATC(MaxD,Agro)
                            boss_healed_row = 0
                            boss_attacked_row += 1
                    else:
                        Use_Hp()
                        M_Turn_Blocked = False
                elif Act in ("usem","m"):
                    if M_Turn_Blocked == False:
                        Use_Mp()
                        if (random.randint(1,10) < boss_RNG or boss_attacked_row >= 2 ) and boss_healed_row < 2 :
                            M_Used_Potion()
                            boss_healed_row += 1
                            boss_attacked_row = 0
                        else:        
                            enemy_ATC(MaxD,Agro)
                            boss_healed_row = 0
                            boss_attacked_row += 1
                    else:
                        Use_Mp()
                        M_Turn_Blocked = False
                elif Act in ("regenmana","rgm"):
                    if mana > 0:
                        print(Fore.BLUE+Back.CYAN+"Cant regen Mana must be <= 0")
                        continue
                    else:
                        Mana_regen()
                        continue
        else:
            print(Fore.RED+Back.WHITE+"INVALID")
        
        if Turn_Blocked == True and M_Turn_Blocked == False:
            print(Fore.RED+ Back.WHITE+"- failed parry - youre turn is blocked-")
            Turn_Blocked = False
            if (random.randint(1,10) < boss_RNG or boss_attacked_row >= 2 ) and boss_healed_row < 2 :
                M_Used_Potion()
                boss_healed_row += 1
                boss_attacked_row = 0
            else:        
                enemy_ATC(MaxD,Agro)
                boss_healed_row = 0
                boss_attacked_row += 1
        if M_Turn_Blocked == False and Mhp > 0:
            status_effect()
            continue
    aval_colors = [lambda:Fore.RED,lambda:Fore.GREEN,lambda:Fore.MAGENTA,lambda:Fore.YELLOW,lambda:Fore.BLUE,lambda:Fore.CYAN]  
    radm_C = random.sample(aval_colors,k=1)[0]()   
    while E_Boss == False:                                                          #NORMAL FIGHT
        if health <= 0:
            break
        print(Fore.WHITE + Back.LIGHTWHITE_EX + "_______BATTLE_______")
        Show_stats()  
        if enemy_missed == 2:
            enemy_agressive = True
        print(f"{Fore.RED+'Aggressive 'if enemy_agressive==True else ''}{radm_C}{atribute}:{name}: hp:{Mhp}")
        Act = input("Actions: fight / flee / UseH / UseM / inv : ").lower()
        if Act in ("flee","fl"):
            Rdm = random.randint(1,100)
            if Rdm < 40:
                print(Fore.WHITE + Back.RED +"unsuccsesfull")
                Number_anim(30,0.02,"-HEALTH",10,5)
            else:
                print(Fore.WHITE + Back.CYAN +"escaped:")
                break
        elif Act == "inv":
            Inventory()
            continue
        elif Act == "info":
                enemy_stats()
                continue
        elif Act in ("fight","f") and mana > 0:
            Rdm = random.randint(1, 100)
            if palyer_atck() != False:
                enemy_ATC(MaxD,Agro)
            else:
                continue
            M_Used_Potion()
        
        elif Act in("useh","h"):
            if cur_diff in ("hard","INSANE","masochist"):
                Use_Hp()
                enemy_ATC(MaxD,Agro)
            else:
                Use_Hp()    
        elif Act in ("usem","m"):
            if cur_diff in ("hard","INSANE","masochist"):
                Use_Mp()
                enemy_ATC(MaxD,Agro)
            else:
                Use_Mp()     
        else:
            print(Fore.WHITE + Back.RED +"Invalid")
            continue
        if Act == "fight" and mana <= 0:
            print(Fore.WHITE + Back.BLUE +"Not enough mana!")   
        status_effect()
        if Mhp <= 0:
            if random.randint(1,10) < 5:
                while True:
                    print("-----CHOICE-----")
                    Act = input("Command: Spare / KILL ").lower()
                    if Act == "spare":
                        print(f"{name} was spared ")
                        print(Fore.CYAN+f"{random.choice(good_text_choice)}")
                        Karma_vl += 2
                        karma_choice(True)
                        break
                    elif Act  == "kill":
                        print(f"{name} was killed")
                        Karma_vl -= 2
                        print(Fore.RED+f"{random.choice(bad_text_choice)}")
                        karma_choice(False)
                        M_dead()
                        break
                MonD += 1
                break
            else:
                M_dead()
                MonD += 1
                break
        if random.randint(1,10) < 2 and Mhp <= int(Const_mhp/3):
            print(Fore.RED + Back.WHITE + f"{name} escaped to avoid death")
            print(Fore.RED + Back.WHITE + "you get nothing :( too bad so sad")
            break 
        turns += 1

def merchant():
        global inventory,max_inv, G, sc_vl, dif_vl
        aval_colors = [lambda:Fore.RED,lambda:Fore.GREEN,lambda:Fore.MAGENTA,lambda:Fore.YELLOW,lambda:Fore.BLUE,lambda:Fore.CYAN]
        possible_items = ["maxs","lhpouch","lmpouch","horb","morb","invslot","hwater","chest","lootbox","elootbox","blpouch","dpot","rpot","maxs"]
        prices = {
            "maxs": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "lhpouch": random.randint(5,5+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "lmpouch": random.randint(5,5+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "horb": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "morb": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "invslot": random.randint(10,20+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "rpot": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "dpot": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "blpouch": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "hwater": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "chest": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "lootbox": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
            "elootbox": random.randint(5,10+int((sc_vl*dif_vl)/(16+(sc_vl/900)))),
        } 
        current_items = random.sample(possible_items,3)
        shop_items = {item: prices[item] for item in current_items} 
        while True:
            print(f"_TRAVELING_MERCHANT_") 
            for item, price in shop_items.items():
                radm_C = random.sample(aval_colors,k=1)[0]()
                Glitch_Anim("GREEN",20)
                print(f"\r{radm_C}{item} - {price} G")
            Glitch_Anim("GREEN",20)
            Act = input("Commands: buy (item name) / exit / inv /: ").lower().replace(" ","#").split("#")
            if Act[0] in ("exit","e") and len(Act) == 1: 
                break
            elif Act[0] == "inv":
                Inventory()
            elif Act[0] == "buy" and len(Act) == 2:
                chosen = Act[1]
                if chosen not in current_items:
                    print("Item dosent exist")
                    continue 
                elif chosen in current_items and len(inventory) >= max_inv:
                    print("Max Inventory")
                    continue
                price = shop_items[chosen]
                if G >= price:
                    print(f"you bought {chosen}")
                    inventory.append(chosen)
                    G -= price 
                    current_items = []
                    print("-CLOSED-")
                    break
                else:
                    print("Broke bitch")
            else:
                print("invalid")  

Double_chest = False
def chest_event():
    global health, mana, hp, mp, sc_vl, Double_chest
    while True:
        print(Fore.YELLOW + "___CHEST___")
        Show_stats()
        if Double_chest == False:
            Act = input("Actions Open / Exit / Double it and give it to the next person (db): ").lower()
        else:
            print(Fore.YELLOW + "someone Doubled the chest, who could that be ?")
            Act = input("Actions Open / Exit: ").lower()
        
        if Act in ("double it and give it to the next person","db") and Double_chest == False:
            print(Fore.WHITE + Back.CYAN +"The next person will definetly be happy !")
            Double_chest = True
            break
        if Act == "open":
            if Double_chest == False:
                if fair_random():
                    Double_chest = False
                    print("You found in the chest!")
                    inventory_add("all")
                    break
                else:
                    Double_chest = False
                    Monster_F("Mimic",40,20,7,"PSN")
                    break
            else:
                if fair_random():
                    print("You found in the chest!")
                    Double_chest = False 
                    inventory_add("all")
                    inventory_add("all")
                    break
                else:
                    Monster_F("Mimic",40,20,7,"DOUBLE PSN")
                    Double_chest = False 
                    break
        if Act == "exit":        
            print(Fore.WHITE + Back.CYAN + "exited")
            Double_chest = False
            break
        else:
            print(Fore.WHITE + Back.RED + "Invalid")

temp = 30
event_choice_options = ["You see something odd ahead.","Something in the shadows is moving.","You spot motion out of the corner of your eye.","You smell something unfamiliar.","The air suddenly shifts.",
                        "Theres a strange warmth nearby.","You sense something watching.","You hear a distant scream. Or maybe its wind.","Something feels off.",
                        "You hear a faint rustle nearby.","A faint glow appears ahead.","You feel a strange energy nearby.","Something moves under the leaves.","You spot an object that wasnt there before.",
                        "You feel a void watching you.","A cold wind whispers of nothingness.","The path ahead seems to dissolve into darkness.","You sense eyes that dont care about you.",
                        "Something waits… indifferent to life or death.","Something shifts behind a rock.","You notice a small pile of objects half-buried in dirt.","You hear a soft jingling sound nearby.","A faint glow pulses from behind the rocks.",
                        "A mysterious container lies just off the path.","You notice a flicker of light beneath the leaves.","Something seems out of place among the trees.","You see an odd shape peeking from the undergrowth.","Something lies ahead, and it doesnt feel entirely safe.",
                        "A faint warmth radiates from something on the path.","Something lies ahead, and your instincts tingle.","A bundle of objects rests under a tree. Too still to ignore.","The air grows colder ahead, though the sun still shines.","A thin mist curls around the roots of the trees.",
                        "You see a suspiciously large potato.","You see a tiny flag waving for no reason. Cant unsee.","You spot a rock wearing a leaf like a hat.","You see a rock. Its definitely plotting something.","You notice a lonely tumbleweed.",
                        "that tree just winked at you.","You hear a soft giggle.","The path curves… or does it?","You notice a peasant yelling at a tree for being lazy.","A cart creaks ominously…","You see a rock balancing on another rock."]
Text_choice1 = ["And remember always be good!","Help others in need","Dont be Evil","Do you want to die as a hero or be remembered as a villan ?",
                                   "If you would be looking death in the eyes what would you do ?","Death is not good","Being alive is good","Dont let youre fears control you",
                                   "Green","Would you help because its right, or because its safe?","Even small actions ripple farther than you realize.","Who decides whats moral, anyway?",
                                   "If everyone does wrong, does it stay wrong?","A choice can change you more than it changes them.","Perhaps there is no good, only consequences we call right.",
                                   "Every act carries a shadow; no light exists without it.","Evil isnt born, its chosen—often without realizing it.","We are neither angels nor monsters, only stories we tell ourselves.",
                                   "Kindness and cruelty often share the same hand.","A single choice may echo farther than you think","What is justified for one may be sin for another.",
                                   "We weigh our hearts, not the world, when judging our deeds.","Morality is a mirror; we see ourselves in every choice.","Sometimes helping is the hardest path…",
                                   "Choose carefully, for even mercy has its price.","Would you be the same if you walked away?","Do your actions define you, or do you define them?",
                                   "If the world rewards cruelty, is that justice—or folly?","Can a good choice be wrong if it hurts someone else?","To save one may cost many but killing costs all.",
                                   "Strength without restraint can become weakness.","Sometimes mercy is cruelty in disguise.","Even selfish acts can shape a better world… or ruin it.","The line between right and wrong bends with perspective.",
                                   "They call it cruelty, but it feels… satisfying.","Step over them, and nothing stops you… except yourself.","Every forbidden act leaves a mark…","You could take it all… if you dare. But dare to what end?",
                                   "Even darkness has a weight. Can you carry it?","Why restrain yourself when the world doesnt?","Everyone fears the monster… but what if its inside you?","Do monsters act because they are evil, or because no one stops them?",
                                   "The thrill of wrongness is real…","Sometimes the world acts, and we only react.","Fate doesnt ask for permission—it just strikes."]
Random_Event3 = ["▶ ▶ ▶ A wizard gave you mana","✷ A sorcerer restores some of your spell energy ✷","▲ ▲ ▲ A friendly mage replenishes your magic ▲ ▲ ▲","▶ ▶ ▶ You absorb mana from a wandering wizard",
                                     "✷ A mystical hand returns lost mana ✷","◀ ◀ ◀ An old mage tops up your magical reserves","▲ ▲ ▲ Your spell juice is refilled by a traveling mage ▲ ▲ ▲","▶ ▶ ▶ A wizard tosses you a spark of mana",
                                     "▶ ▶ ▶ A wizard sneezes and accidentally gives you mana","✷ A distracted mage drops a mana crystal in your lap ✷","▲ ▲ ▲ A wizard trips and some of his mana spills into your hands ▲ ▲ ▲",
                                     "▶ ▶ ▶ You catch a mana bolt thrown by a careless mage","✷ A wizard waves his wand, and somehow your energy increases ✷","✷ You inhaled magic by accident ✷","▲ ▲ ▲ Mana leaked into you somehow ▲ ▲ ▲",
                                     "✖-You touched a glowing rock. Now you have mana.-","✷ You licked a spellbook and gained mana ✷","✷ You ate a candle. It was magical. ✷","▲ ▲ ▲ A wizard dropped his mana sandwich and you ate it ▲ ▲ ▲"]
Result_name = ["▶ ▶ ▶ You found","▶ ▶ ▶ A wizzard gave you","▶ ▶ ▶ You forgot you had","▶ ▶ ▶ A merchant gave you","◀ ◀ ◀ You stole from the shop","◀ ◀ ◀ You stole from a traveler","▶ ▶ ▶ A fairy gave you","▶ ▶ ▶ You discover",
                           "▶ ▶ ▶ You stumble upon","▶ ▶ ▶ You uncover","▶ ▶ ▶ Someone left you","▶ ▶ ▶ You notice something shining","▶ ▶ ▶ You spot something unusual","▶ ▶ ▶ You loot","◀ ◀ ◀ You swipe","◀ ◀ ◀ You snatch","◀ ◀ ◀ You take while no ones looking",
                           "◀ ◀ ◀ You take from the shelf","◀ ◀ ◀ You lift from a distracted merchant","◀ ◀ ◀ You lift something from a travelers bag","◀ ◀ ◀ You quietly take from the travelers pack","◀ ◀ ◀ You swipe a loose item off the traveler",
                           "◀ ◀ ◀ You steal while the traveler looks away","▶ ▶ ▶ A beggar gives you","You begged because you are such a poor person broke boy","▶ ▶ ▶ A priest gifts you","▶ ▶ ▶ You trip over","▶ ▶ ▶ You almost throw away","▶ ▶ ▶ You mistake it for trash",
                           "▶ ▶ ▶ You trip and land on something valuable","▶ ▶ ▶ You reach into your pocket and pull out…","▶ ▶ ▶ You cough and accidentally spit out an item","▶ ▶ ▶ You pat your pockets and something clanks loudly",
                           "▶ ▶ ▶ You kick a rock and something shiny rolls out","▶ ▶ ▶ You check under a rock and","▶ ▶ ▶ You blink and now somethings in your hand","▶ ▶ ▶ You stare at the ground until treasure appears"]
Random_Event = ["▼ A stranger slashed you ▼","✖-A stray arrow hit you-⫸ ","✷ You fell ✷","◀ ◀ ◀ A wizzard lifestole ╬","▶ ▶ ▶ You felt ill","▲ ▲ ▲ spikes▲ ▲ ▲ ▲","◀ ◀ ◀ You fell in a Pond","▼ ▼ ▼ Rocks fall ▼ ▼ ▼",
                                "▼ A wild dog bites ▼","◀ ◀ ◀ A stranger pushed you into danger","✷ You slipped on a mossy stone ✷","◀ ◀ ◀ You stumbled into a pit","▲ ▲ ▲ Lava splashes ▲ ▲ ▲","✷ You step on a hidden trap ✷",
                                "◀ ◀ ◀ A wizard drains your life ╬","▼ A phantom scratches ▼","✷ You stub your toe ✷","▲ ▲ ▲ You slammed your head on a low branch ▲ ▲ ▲","◀ ◀ ◀ A squirrel bit your finger ◀ ◀ ◀","▲ ▲ ▲ You slipped on a banana peel ▲ ▲ ▲",
                                "✷ A gust of wind knocked you over ✷","◀ ◀ ◀ You slipped in a puddle of… something ◀ ◀ ◀","✷ You lost balance trying to look cool ✷","▶ ▶ ▶ You kicked a rock and it kicked back ▶ ▶ ▶"]
Random_Event4 = ["▶ ▶ ▶ Healer healed you for","▶ ▶ ▶ A wizard slapped you and you felt healthier",
                                    "✷ A wizard poured soup on you. It healed you. ✷","You ate a magic shroom","you started going WILD","You drank some ALE","▶ ▶ ▶ A mage grants you a brief surge of health","▲ ▲ ▲ A crystal shard restores a portion of your vitality ▲ ▲ ▲",
                                    "▲ ▲ ▲ A passing breeze carries the last trace of healing magic ▲ ▲ ▲","▶ ▶ ▶ Something unseen grants you health","▲ ▲ ▲ You chugged 4 beers. -999 Coordination ▲ ▲ ▲","✷ You chewed a glowing leaf. It healed you for some reason ✷, you might be radioactive tho",
                                    "◀ ◀ ◀ You bit a random plant you Hoped it wasnt poison","▶ ▶ ▶ You inhaled sparkly dust.+0 IQ","You found soup on the floor. It healed you.–⫸","▲ ▲ ▲ You licked a crystal. Your wounds closed ▲ ▲ ▲",
                                    "◀ ◀ ◀ You drank something unlabelled.","▶ ▶ ▶ You found a berry. You didnt question it.","✷ You swallowed a healing orb like candy ✷","✷ You Have so much aura it healed you"]           
Random_Event2 = ["◀ ◀ ◀ Angry wizard manastole ","✷ A sorcerer siphons your energy ✷","▶ ▶ ▶ A mysterious mage absorbs your spell energy","◀ ◀ ◀ A draining aura touches you","✷ An enemy spell consumes your mana ✷",
                                     "◀ ◀ ◀ Mana slips through your fingers","◀ ◀ ◀ You sneezed and lost mana","▲ ▲ ▲ A pixie burped on you and stole your mana ▲ ▲ ▲","▶ ▶ ▶ You yawned too hard, mana gone ▶ ▶ ▶","◀ ◀ ◀ A magical squirrel nibbled your spell juice",
                                     "▲ ▲ ▲ You tried to meditate…","▶ ▶ ▶ You blinked and mana vanished","▲ ▲ ▲ A shadow wizard absorbs your magic ▲ ▲ ▲","▶ ▶ ▶ An enemy spellcaster steals your energy","◀ ◀ ◀ A mystical hand pulls your mana away"]
last_rng = 0
Start_Menu()
while health > 0:
    for Runs in range (99999999):
        save_file()
        #print("________________")
        Show_stats()
        Command = input("Actions: UseH / UseM / expl / inv / store: ").lower()
        print("_____________")
        
        if Command in ("useh","h"):
            Use_Hp()
        #elif Command == "zxt":
           # if random.randint(1,10) < 5:
            #    print("neine random")
            #    Flare(10,"star",False)
           # else:
              #  print("random")
               # Flare(10,"star",True)
        elif Command == "cl":
            import os
            os.system('cls')
            continue
        elif Command == "inv":
            Inventory()
        elif Command == "info":
            print("-")
            Show_stats()
            print(f"Max health - {100 + sc_vl}, Max mana - {100 + sc_vl}, explored - {explored} times,")
            print(f"Monsters killed - {MonD} sc_vl {sc_vl}, inv slots {max_inv}" )
            print(f"difficulty - {cur_diff}, scaling - {cur_sc}, difficulty value - {dif_vl}, K-{Karma}|{Karma_vl}")
            print(f"Potion_give - MIN-{10+int((sc_vl*dif_vl)/(8+(sc_vl/1100)))} MAX-{30+int((sc_vl*dif_vl)/(4+(sc_vl/900)))}")
            print("-")
            continue
        elif Command in ("rng set","rng free") :
            if Command == "rng set":
                setAmount = input("Rng set: ")
            
            
        elif Command in ("store","s"):
            Store()
        #elif Command == "add":
           # for i in range (5):
              # inventory_add("all")
        elif Command in ("usem","m"):
            Use_Mp()
        elif Command in ("expl","e"):    
            rng = random.randint(1,17)
            while rng == last_rng:
                rng = random.randint(1,17)
            #rng = 14
            if random.randint(1,10) < 2:
                temp_text = random.choice(event_choice_options)
                while True:
                    print("_____________")
                    print(Fore.YELLOW+f"{temp_text}")
                    Act = input(f"Actions: Run / Investigate (inv): ").lower()
                    if Act == "run":
                        break
                    elif Act == "inv":
                        break
                    else:
                        print(Fore.RED+Back.WHITE+"Invalid")
                if Act == "run":
                    continue        
            if rng == 1:
                RD_EV_effect = random.choice(Result_name)
                print(Fore.LIGHTCYAN_EX+f"{RD_EV_effect}")
                if random.randint(0,20) < 19:
                    Number_anim(30,0.02,"HP",2,9999999999999999)
                else:
                    inventory_add("all")
                if RD_EV_effect in ("◀ ◀ ◀ You stole from the shop","◀ ◀ ◀ You take from the shelf","◀ ◀ ◀ You lift from a distracted merchant","▶ ▶ ▶ You loot","◀ ◀ ◀ You swipe","◀ ◀ ◀ You snatch"):
                    Monster_F("Merchant", 20, random.randint(10,20),random.randint(4,10),"ANGRY")
                elif RD_EV_effect in ("◀ ◀ ◀ You stole from a traveler","◀ ◀ ◀ You lift something from a travelers bag","◀ ◀ ◀ You quietly take from the travelers pack","◀ ◀ ◀ You swipe a loose item off the traveler","◀ ◀ ◀ You steal while the traveler looks away"):
                    Monster_F("Traveler", 20,random.randint(10,20),random.randint(3,7),"BRN")    
            if rng == 2:
                RD_EV_effect = random.choice(Result_name)
                print(Fore.LIGHTCYAN_EX+f"{RD_EV_effect}")
                if random.randint(0,20) < 19:
                    Number_anim(30,0.02,"MP",2,9999999999999999)
                else:
                    inventory_add("all")
                if RD_EV_effect in ("◀ ◀ ◀ You stole from the shop","◀ ◀ ◀ You take from the shelf","◀ ◀ ◀ You lift from a distracted merchant","▶ ▶ ▶ You loot","◀ ◀ ◀ You swipe","◀ ◀ ◀ You snatch"):
                    Monster_F("Merchant", 20, random.randint(5,50),random.randint(4,10),"ANGRY")
                elif RD_EV_effect in ("◀ ◀ ◀ You stole from a traveler","◀ ◀ ◀ You lift something from a travelers bag","◀ ◀ ◀ You quietly take from the travelers pack","◀ ◀ ◀ You swipe a loose item off the traveler","◀ ◀ ◀ You steal while the traveler looks away"):
                    Monster_F("Traveler", 20,random.randint(1,10),random.randint(3,7),"BRN")    
            if rng == 3:
                RD_EV_effect = random.choice(Random_Event)
                print(Fore.LIGHTRED_EX+f"{RD_EV_effect}")
                Number_anim(30,0.02,"-HEALTH",10,1)
                if RD_EV_effect in ("◀ ◀ ◀ A wizzard lifestole ╬","◀ ◀ ◀ A wizard drains your life ╬"):
                    Monster_F("LifeStealer",30,random.randint(10,20),random.randint(4,10),"LFS")    
            if  rng == 4:
                if mana > 0:
                    RD_EV_efct = random.choice(Random_Event2)
                    print(Fore.LIGHTBLUE_EX+f"{RD_EV_efct}")
                    Number_anim(30,0.02,"-MANA",10,1)
                    Rdm = random.randint(1,10)
                    if Rdm < 5 or Karma == "BAD" and RD_EV_efct in ("◀ ◀ ◀ Angry wizard manastole ","▲ ▲ ▲ A shadow wizard absorbs your magic ▲ ▲ ▲","▶ ▶ ▶ An enemy spellcaster steals your energy","◀ ◀ ◀ A mystical hand pulls your mana away"):
                        Monster_F("Angry wizzard",30,random.randint(10,20),random.randint(4,10),"MGC")
                else:
                    print(Fore.LIGHTBLUE_EX+f"{random.choice(Random_Event3)}")
                    Number_anim(30,0.02,"+MANA",10,1)       
            if rng == 5:
                Monster_F(random.choice(MonsNames), 50, random.randint(20,30),random.randint(4,7),Fore.BLUE+"STR")
            if rng == 6:
                RD_EV_effect = random.choice(Result_name)
                print(Fore.LIGHTYELLOW_EX+f"{RD_EV_effect}")
                if random.randint(0,20) < 19:
                    Number_anim(30,0.02,"G",10,10)
                else:
                    inventory_add("all")
                if RD_EV_effect in ("◀ ◀ ◀ You stole from the shop","◀ ◀ ◀ You take from the shelf","◀ ◀ ◀ You lift from a distracted merchant","▶ ▶ ▶ You loot","◀ ◀ ◀ You swipe","◀ ◀ ◀ You snatch"):
                    Monster_F(F"Merchant", 20, random.randint(5,50),random.randint(4,10),Fore.LIGHTRED_EX+"ANGRY")
                elif RD_EV_effect in ("◀ ◀ ◀ You stole from a traveler","◀ ◀ ◀ You lift something from a travelers bag","◀ ◀ ◀ You quietly take from the travelers pack","◀ ◀ ◀ You swipe a loose item off the traveler","◀ ◀ ◀ You steal while the traveler looks away"):
                    Monster_F("Traveler", 20,random.randint(1,10),random.randint(3,7),"BRN")
            if rng == 7:
                print(Fore.LIGHTRED_EX+f"{random.choice(Random_Event4)}")
                Number_anim(30,0.02,"+HEALTH",10,1)
            if rng == 8:
                print(Fore.LIGHTBLUE_EX+f"{random.choice(Random_Event3)}")
                Number_anim(30,0.02,"+MANA",10,1)
            if rng == 9:
                chest_event()  
            if rng == 10:
                Monster_F(random.choice(MonsNames), 20, random.randint(10,20), random.randint(5,10),Fore.MAGENTA+ "NRM")
            if rng == 11:
                if G >= 1:
                    print(Fore.LIGHTYELLOW_EX+f"◀ ◀ ◀ A goblin stole")
                    Number_anim(30,0.02,"-G",10,10)
                    if random.randint(1,20) < 10:  
                        Monster_F("Goblin",20, random.randint(10,20),random.randint(5,10),"GREEDY")  
                elif G == 0:
                    print(Fore.LIGHTYELLOW_EX+f"▶ ▶ ▶ A goblin felt bad for you broke boy")
                    Number_anim(10,0.02,"G",1,99999999999999)
            if rng == 12:
                Monster_F(random.choice(MonsNames), 20, random.randint(10,15),10,Fore.MAGENTA+ "ACR")
            if rng == 13:
                price = 5+int(sc_vl/(24-int(dif_vl*3)))
                give_potion_amount = 1+int(sc_vl/50)
                gold_option_list = ["a homeless person begs you for gold","A traveler needs money","Ive got a job… for the right price ?","I need gold… now!"
                                    ,"Ive got debts I cant pay","You give me coin, Ill make it worth your while.",
                                    "Even a few coins would mean the world.","I hate asking for gold… but I have no choice.","Times are hard. Please, help me."]
                potion_option_list = [f"Just {give_potion_amount} potion… it could save my life!",f"I cant fight another step without {give_potion_amount} potions"
                                      ,f"Just {give_potion_amount} potions… thats all I ask Dont turn your back.","Do you really call yourself a hero if you let me die over a some potions ?"]
                if G >= price:
                    print(Fore.YELLOW+f"{random.choice(gold_option_list)}")
                    while True:
                        Act = input(f"choices: Give {price} gold(give) / STEAL {int(price/3)} gold (steal) /: ").lower()
                        if Act == "give":
                            print(Fore.CYAN+f"{random.choice(good_text_choice)}")
                            Karma_vl += 5
                            G -= price
                            karma_choice(True)
                            break
                        elif Act == "steal":
                            Karma_vl -= 5
                            print(Fore.RED+f"{random.choice(bad_text_choice)}")
                            G += int(price/3)
                            karma_choice(False)
                            break
                        else:
                            print("invalid")
                elif (hp or mp) >= give_potion_amount:
                    print(Fore.YELLOW+f"{random.choice(potion_option_list)}")
                    while True:
                        Act = input(f"choices: Give {give_potion_amount} potions (give) / STEAL {give_potion_amount} potions (steal) /: ").lower()
                        if Act == "give":
                            print(Fore.CYAN+f"{random.choice(good_text_choice)}")
                            Karma_vl += 2
                            if hp >= give_potion_amount:
                                hp -= give_potion_amount
                            else:
                                mp -= give_potion_amount
                            karma_choice(True)
                            break            
                        elif Act == "steal":
                            print(Fore.RED+f"{random.choice(bad_text_choice)}")
                            Karma_vl -= 2
                            if hp >= give_potion_amount:
                                hp += give_potion_amount
                            else:
                                mp += give_potion_amount
                            karma_choice(False)
                            break            
                        else:
                            print("invalid")
                else:
                    print(Fore.GREEN+f"ECHO : {random.choice(Text_choice1)}")
            if rng == 14:
                if Karma == "NEUTRAL":
                    print(Fore.GREEN+f"ECHO : {random.choice(Text_choice1)}")
                elif Karma == "GOOD":
                    print(Fore.GREEN+f"ECHO : {random.choice(Text_choice1)}")
                    if fair_random():
                        Number_anim(40,0.02,"G",5,2)
                elif Karma == "BAD":
                    print(Fore.RED+f"ECHO : {random.choice(bad_text_choice)}")
                    if random.randint(1,10)> 2:
                        Monster_F("Bounty Hunter",10,20,7,"KRM")                      
            if rng == 15:
                boss_names = ["Paladin","Necro","WorldBreaker","Oblivion","BoneCrusher","VOID","Arch","Kali","Mint","Ubuntu","Manjaro"]
                if sc_vl > temp:
                    temp += 50
                    if Karma in ("BAD"):
                        Monster_F(random.choice(boss_names),60,25,10,"BOSS")
                    elif Karma == "GOOD":
                        Monster_F(random.choice(boss_names),50,5,10,"BOSS")
                    else:
                        Monster_F(random.choice(boss_names),55,15,10,"BOSS")
                else:
                    print(Fore.YELLOW+"Something Strong is waiting for you...")    
            if rng == 16:
               print(Fore.LIGHTYELLOW_EX+"You found nothing +0 of everything")
               print(Fore.RED + "+1 health")
               time.sleep(0.2)
               print(Fore.RED + "-1 health")
               time.sleep(0.2)
               print(Fore.BLUE+"+1 mana")
               time.sleep(0.2)
               print(Fore.BLUE+"-1 mana")
               time.sleep(0.2)
               print(Fore.YELLOW+"+1 G")
               time.sleep(0.2)
               print(Fore.YELLOW+"-1 G")
               time.sleep(0.2)
               print(Fore.BLUE + "+1 M potion")
               time.sleep(0.2)
               print(Fore.BLUE + "-1 M potion")
               time.sleep(0.2)
               print(Fore.RED+"+1 H potion")
               time.sleep(0.2)
               print(Fore.RED+"-1 H potion")
            if rng == 17:
                merchant()
            
            last_rng = rng
            if health <= 0:
                break
            explored += 1
            if cur_sc == "expo":
                sc_vl += 1
                sc_vl *= int(math.log(sc_vl*sc_vl))
            else:
                sc_vl += 1
                
                
        else:
            print("nothing happened")
        
        if health <= 0:
            break
            
    if health <= 0:
        break
        
count = 0

def death_anim():
    glitch_effect = ["* ✖ ✶ ✷ ✶ * ✷ ✖ ","✶ * ✷ ✖ * ✖ ✶ ✷ ","✖ * ✶ * ✶ * ✷ ✖","✷ ✶ * ✖ ✖ * ✶ * "]
    glitch_effect2 = ["█ ░ ▒ ▓ ▒ ▓ █ ░ "," ▒ ▓ █ ░ █ ░ ▒ ▓","▒ █ ▓ ░  ▒ ▓ █ ░ "]
    for i in range(100): 
        print(Fore.LIGHTRED_EX + f" {random.choice(glitch_effect)}")
        print("\n")
        print(Fore.RED + f" {random.choice(glitch_effect2)}")
        print("\n")
        time.sleep(0.001)
score = int(sc_vl * MonD * dif_vl) + (mp * hp * G)
with open('game_save_var.json','w') as f:
        json.dump("lol you died ",f)
while True:
    if health <= 0:
        print(Back.RED + Fore.WHITE +"You are DEAD")
        print("-")
        Show_stats()
        print(f"Max health - {100 + sc_vl}, Max mana - {100 + sc_vl}, explored - {explored} times,")
        print(f"Monsters killed {MonD}, sc_vl-{sc_vl}, bosses defeated - {BossD}" )
        print(f"difficulty - {cur_diff}, scaling - {cur_sc}, K-{Karma}|{Karma_vl}")
        print(f"SCORE - {score*BossD}")
        print("-")
        input("Something went wrong ?: ")
