import random
import time 
from colorama import init, Fore, Back, Style
init(autoreset=True)

amount = 0
sc_vl = 1
explored = 0
health = 100
mana = 100
hp = 0
mp = 0
G = 0
MonD = 0
MonsNames = ["Wolf","Goblit","Wizzard","Warrior","Bear","Ghoul","Guardion","Archer","Dragon","Hydra","Minotaur","Medusa","Cerberus","Chimera"]

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
            G_to_Give = random.randint(1,Max_vl+int(sc_vl/Mul_vl))
            print(Fore.YELLOW + f"\r{'+' if stat == 'G' else '-'}{G_to_Give}",end="")
            time.sleep(timeA)
        if stat == "G":
            G += G_to_Give
        elif stat == "-G":
            G -= G_to_Give      
        print(Fore.YELLOW + Style.BRIGHT + f"\r{'+' if stat == 'G' else '-'}{G_to_Give} G ")
    
    elif stat == "MP":
        for i in range(Range):
            M_to_Give = random.randint(1,Max_vl)
            print(Fore.LIGHTBLUE_EX + f"\r+{M_to_Give}",end="")
            time.sleep(timeA)
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\r+{M_to_Give} M Potion ")
        mp += M_to_Give 
    
    elif stat == "HP":
        for i in range(Range):
            H_to_Give = random.randint(1,Max_vl)
            print(Fore.LIGHTRED_EX + f"\r+{H_to_Give}",end="")
            time.sleep(timeA)    
        print(Fore.LIGHTRED_EX + Style.BRIGHT + f"\r+{H_to_Give} H Potion ")
        hp += H_to_Give 

    elif stat in ("+HEALTH", "-HEALTH"):
        health_red = 0
        for i in range(Range):
            Health_to_Give = random.randint(1,Max_vl+int(sc_vl/Mul_vl))
            print(Fore.RED + f"\r{'+' if stat =='+HEALTH' else '-'}{Health_to_Give}", end="")
            time.sleep(timeA)
        if stat == "+HEALTH":
            health += Health_to_Give   
            if health > (100 + sc_vl):
                health_red = health - (100+sc_vl)
                health_cap()
            print(Fore.RED + Style.BRIGHT + f"\r+{Health_to_Give - health_red} Health ")
        elif stat == "-HEALTH":
            health -= Health_to_Give   
            print(Fore.RED + Style.BRIGHT + f"\r-{Health_to_Give} Health ")    

    elif stat in ("+MANA","-MANA"):
        mana_red = 0
        for i in range(Range):
            Mana_to_Give = random.randint(1,Max_vl+int(sc_vl/Mul_vl))
            print(Fore.BLUE +f"\r+{Mana_to_Give}",end="")
            time.sleep(timeA)
        if stat == "+MANA":
            mana += Mana_to_Give   
            if mana > (100 + sc_vl):
                mana_red = mana - (100+sc_vl)
                mana_cap()
            print(Fore.BLUE + Style.BRIGHT + f"\r+{Mana_to_Give - mana_red} Mana ") 
        elif stat == "-MANA":
            mana -= Mana_to_Give
            print(Fore.BLUE + Style.BRIGHT + f"\r-{Mana_to_Give} Mana ")    
    
def Rnd_Number_Guess(Gses):
    global G, health, mana, sc_vl
    RnG = random.randint(1,50+sc_vl)
    print("________________")
    print(Fore.GREEN + Back.WHITE + f"Guess the number 1-{50+sc_vl} for a reward in {Gses+int(sc_vl/500)} tries")
    while True:
        for gueses in range(Gses+int(sc_vl/100)):
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
            Number_anim(30,0.04,"G",10,10)
            break
        if guess != RnG:
            T_f = random.randint(1,10 + int(sc_vl/2))
            health -= T_f
            print(Fore.WHITE + Back.RED + f"you Lost correct number was {RnG}")
            Number_anim(30,0.04,"-HEALTH",10,5)   
            break               
        
def Store():
    global mp, hp, G, amount
    price = 5+int(sc_vl/50)
    while True:
        print(Fore.WHITE + Back.LIGHTBLACK_EX + "_______STORE_______")
        print(Fore.YELLOW + f"You have {G} G")
        print(f"Items: BuyH {price}.G / BuyM {price}.G / exit :")
        choice = input("Action: ").lower()
            
        if choice == "exit":
            print("Exited")
            break
        elif choice == "buym" :
            amount_input()
            if G >= (amount * price):
                G -= price * amount
                mp += amount
                print(Fore.WHITE + Back.CYAN +f"Obtained {amount} M Potion")
                print(Fore.YELLOW +f"-{amount*price} G") 
            else: 
                print("Not enough G")    
        elif choice == "buyh" :
            amount_input()
            if G >= (amount * price):
                G -= price*amount
                hp += amount
                print(Fore.WHITE + Back.CYAN +f"Obtained {amount} H Potion")
                print(Fore.YELLOW +f"-{amount*price} G")
            else:
                print(Fore.WHITE + Back.RED +"not enough G")
        else:
            print(Fore.WHITE + Back.RED +"invalid")
            
def Show_stats():
    print(Fore.BLACK + Back.WHITE + f"health:{health} mana:{mana} H.Potions:{hp} M.potions:{mp} G:{G}")

def Use_Hp():
    global health, hp, sc_vl, amount 
    hlv = 0
    h_cp = 0
    amount_input()
    if hp >= amount and health < (100 + sc_vl):
        for i in range(amount):
            hp -= 1
            T_f = random.randint(10,20 + sc_vl)
            health += T_f
            hlv += T_f
            if health > (100 + sc_vl):
                h_cp = health - (100 + sc_vl)
                health_cap()
                break
        print(f"+{hlv - h_cp } health")
    else:
        print("Can't use")

def Use_Mp():
    global mana, mp, sc_vl, amount
    mlv = 0
    m_cp = 0
    amount_input()
    if mp >= amount and mana < (100 + sc_vl):
        for i in range(amount):
            mp -= 1
            T_f = random.randint(10,20 + sc_vl)
            mana += T_f
            mlv += T_f
            print(f"\r +{mlv}")
            time.sleep(0.1)
            if mana > (100 + sc_vl):
                m_cp = mana - (100 + sc_vl)
                mana_cap()
                print(f"\r +{mlv - m_cp} mana")
                break
        print(f"\r +{mlv - m_cp} mana")
    else:
        print("Can't use")
            
def  Monster_F(name, Hcap, MaxD, Agro, atribute):
    global health, mana, G, MonD, sc_vl, mp, hp
    Mhp = random.randint(Hcap+int(sc_vl/5),100+sc_vl)
    while True:
        if health <= 0:
            break
        print(Fore.WHITE + Back.LIGHTWHITE_EX + "_______BATTLE_______")
        Show_stats()
        MRd = random.randint(1,10)
        print(f"{atribute}:{name}: hp:{Mhp}")
        Act = input("Actions: fight / flee / UseH / UseM :").lower()
        if Act == "flee":
            Rdm = random.randint(1,100)
            if Rdm < 60:
                print(Fore.WHITE + Back.RED +"unsuccsesfull")
                Number_anim(30,0.04,"-HEALTH",10,5)
            else:
                print(Fore.WHITE + Back.CYAN +"escaped:")
                break
        elif Act == "fight" and mana > 0:
            MRd = random.randint(1,10)
            Rdm = random.randint(1, 100)
            if Rdm <= 15:
                for i in range(2000):
                    Rdm = random.randint(20+int(sc_vl/10),50+sc_vl)
                    print(Fore.RED + Back.BLACK +f"\r-{Rdm}",end="")
                    time.sleep(0.001)
                print(Fore.RED + Back.BLACK + f"\r-CRIT- {name} -{Rdm} hp -CRIT-")
                Mhp -= Rdm
            else:    
                for i in range(30):
                    Rdm = random.randint(1+int(sc_vl/10),20+sc_vl)
                    print(Fore.LIGHTRED_EX+f"\r-{Rdm}",end="")
                    time.sleep(0.04)
                print(Fore.LIGHTRED_EX+f"\r{name} -{Rdm} hp")
                Mhp -= Rdm
                for i in range(30):
                    Rdm = random.randint(1,5+int(sc_vl/2))
                    print(Fore.LIGHTBLUE_EX+f"\r-{Rdm}",end="")
                    time.sleep(0.04)    
                mana -= Rdm
                print(Fore.LIGHTBLUE_EX+f"\r-{Rdm} mana cost")
            if MRd < Agro and Mhp > 0:
                for i in range(30):
                    Mdmg = random.randint(1,MaxD+int(sc_vl/5))
                    print(Fore.RED+f"\r-{Mdmg}",end="")
                    time.sleep(0.04)  
                print(Fore.RED+f"\r{name} attacked -{Mdmg} health")
                health -= Mdmg
        elif Act == "useh":
            Use_Hp()
        elif Act == "usem":
            Use_Mp()
        else:
            print(Fore.WHITE + Back.RED +"Invalid")
        
        if Act == "fight" and mana <= 0:
            print(Fore.WHITE + Back.RED +"Not enough mana!")    

        if atribute == "LFS" and Mhp > 0:
            print(Fore.RED +f"Lifestole health")
            Number_anim(30,0.04,"-HEALTH",10,10)
            Rdm = random.randint(0,5+int(sc_vl/10))
            Mhp += Rdm
            print(Fore.RED +f"{name} regenerated +{Rdm} stolen health")
        if atribute == "GREEDY":
            print(Fore.YELLOW +"ThE GoBliN LikEs GoulD")
        if atribute == "MGC" and Mhp > 0:
            print(Fore.BLUE + Back.CYAN +f"captured mana")
            Number_anim(30,0.04,"-MANA",10,10)
        if atribute == "BRN" and Mhp > 0:
            print(Fore.YELLOW + Back.RED + f"-Burned-")
            Number_anim(30,0.04,"-HEALTH",10,10)
        if name == "Dragon" and Mhp > 0:
            print(Fore.YELLOW + Back.RED + f"-Burned-")
            Number_anim(30,0.04,"-HEALTH",10,10)    

        if Mhp <= 0:
            print(Fore.WHITE + Back.CYAN +"you won ")
            Number_anim(30 ,0.04, "G",10,10)
            if name == "Merchant":
                print(Fore.LIGHTMAGENTA_EX+f"you found some potions in his bag") 
                Number_anim(30,0.04,"MP",2,1)
                Number_anim(30,0.04,"HP",2,1)
            elif name == "Goblin":
                print(Fore.LIGHTYELLOW_EX+"you found some gold he stole from you")
                Number_anim(30,0.04,"G",10, 10)
            elif name == "LifeStealer":
                print(Fore.LIGHTRED_EX+"You captured some stolen health")
                Number_anim(30,0.04,"+HEALTH",10,5)
            elif name == "Angry wizzard":
                print(Fore.LIGHTBLACK_EX+"You captured held mana")
                Number_anim(30,0.04,"+MANA",10,5)
            MonD += 1
            break
                        
while health > 0:
    for Runs in range (99999999):
        print("________________")
        Show_stats()
        Command = input("Actions: UseH / UseM / expl / store: ").lower()
        
        if Command == "useh" or Command == "h":
            Use_Hp()
        elif Command == "cl":
            import os
            os.system('cls')
            continue
        elif Command == "info":
            print("-")
            Show_stats()
            print(f"Max health - {100 + sc_vl}, Max mana - {100 + sc_vl}, explored - {explored} times,")
            print(f"Monsters killed {MonD} scale value {sc_vl}" )
            print("-")
            continue
        elif Command == "store":
            Store()
        elif Command == "usem":
            Use_Mp()
        elif Command == "expl":    
            rng = random.randint(1,13)
            #rng = 3
            Result_name = ["You found","A wizzard gave you","You forgot you had","A merchant gave you","You stole from the shop","You stole from a traveler"]
    
            if rng == 1:
                RD_EV_effect = random.choice(Result_name)
                print(Fore.LIGHTCYAN_EX+f"{RD_EV_effect}")
                Number_anim(30,0.04,"HP",2,9999999999999999)
                if RD_EV_effect == "You stole from the shop":
                    Monster_F("Merchant", 10, random.randint(5,50+sc_vl),random.randint(4,10),"ANGRY")
                elif RD_EV_effect == "You stole from a traveler":
                    Monster_F("Traveler", 10,random.randint(1,10+sc_vl),random.randint(3,7),"BRN")    
            if rng == 2:
                RD_EV_effect = random.choice(Result_name)
                print(Fore.LIGHTCYAN_EX+f"{RD_EV_effect}")
                Number_anim(30,0.04,"MP",2,9999999999999999)
                if RD_EV_effect == "You stole from the shop":
                    Monster_F("Merchant", 10, random.randint(5,50+sc_vl),random.randint(4,10),"ANGRY")
                elif RD_EV_effect == "You stole from a traveler":
                    Monster_F("Traveler", 10,random.randint(1,10+sc_vl),random.randint(3,7),"BRN")    
            if rng == 3:
                Random_Event = ["A stranger slashed you","A stray arrow hit you","You fell","A wizzard lifestole","You felt ill",]
                RD_EV_effect = random.choice(Random_Event)
                print(Fore.LIGHTRED_EX+f"{RD_EV_effect}")
                Number_anim(30,0.04,"-HEALTH",10,1)
                if RD_EV_effect == "A wizzard lifestole":
                    Monster_F("LifeStealer",50,random.randint(5,50+sc_vl),random.randint(4,10),Fore.LIGHTRED_EX+"LFS")    
            if  rng == 4:
                if mana > 0:
                    print(f"Angry wizard manastole ")
                    Number_anim(30,0.04,"-MANA",10,1)
                    Rdm = random.randint(1,10)
                    if Rdm < 8:
                        Monster_F("Angry wizzard",50,random.randint(30,50+sc_vl),random.randint(4,10),Fore.LIGHTBLUE_EX+"MGC")
                else:
                    print(f"A wizard restored")
                    Number_anim(30,0.04,"+MANA",10,1)       
            if rng == 5:
                Monster_F(random.choice(MonsNames), 10, random.randint(5,50+sc_vl),random.randint(4,5),Fore.BLUE+"STR")
            if rng == 6:
                RD_EV_effect = random.choice(Result_name)
                print(Fore.LIGHTYELLOW_EX+f"{RD_EV_effect}")
                Number_anim(30,0.04,"G",10,10)
                if RD_EV_effect == "You stole from the shop":
                    Monster_F("Merchant", 10, random.randint(5,50+sc_vl),random.randint(4,10),Fore.LIGHTRED_EX+"ANGRY")
                elif RD_EV_effect == "You stole from a traveler":
                    Monster_F(Fore.LIGHTRED_EX+ Back.LIGHTYELLOW_EX +"Traveler", 10,random.randint(1,10+sc_vl),random.randint(3,7),Fore.LIGHTRED_EX+ Back.LIGHTYELLOW_EX + "BRN")
            if rng == 7:
                print(Fore.LIGHTRED_EX+f"Healer healed you for")
                Number_anim(30,0.04,"+HEALTH",10,1)
            if rng == 8:
                print(Fore.LIGHTBLUE_EX+f"Happy wizard restored")
                Number_anim(30,0.04,"+MANA",10,1)
            if rng == 9:
                Rnd_Number_Guess(random.randint(4,10))
            if rng == 10:
                Monster_F(random.choice(MonsNames), 50, random.randint(5,30+sc_vl), random.randint(5,10),Fore.MAGENTA+ "NRM")
            if rng == 11:
                if G >= 1:
                    print(Fore.LIGHTYELLOW_EX+f"A goblin stole")
                    Number_anim(30,0.04,"-G",10,10)
                    if G < 0:
                        G = 0  
                        Monster_F("Goblin", 10, random.randint(5,30+sc_vl), random.randint(5,10),Back.LIGHTYELLOW_EX + Fore.YELLOW +"GREEDY")  
                elif G == 0:
                    print(Fore.LIGHTYELLOW_EX+f"A goblin felt bad for you broke boy")
                    Number_anim(10,0.02,"+G",1,99999999999999)
            if rng == 12:
                Monster_F(random.choice(MonsNames), 10, random.randint(10,30+sc_vl), random.randint(9,10),Fore.MAGENTA+ "ACR")
            if rng == 13:
               print(Fore.LIGHTYELLOW_EX+"You found nothing +0 of everything")
               Number_anim(10,0.02,"+HEALTH",1,99999999999999)
               Number_anim(10,0.02,"-HEALTH",1,99999999999999)
               Number_anim(10,0.02,"+MANA",1,9999999999999)
               Number_anim(10,0.02,"-MANA",1,9999999999999)
               Number_anim(10,0.02,"G",1,999999999999999)
               Number_anim(10,0.02,"-G",1,999999999999999)
               time.sleep(0.2)
               print(Fore.BLUE + "+1 M potion")
               time.sleep(0.2)
               print(Fore.BLUE + "-1 M potion")
               time.sleep(0.2)
               print(Fore.RED+"+1 H potion")
               time.sleep(0.2)
               print(Fore.RED+"-1 H potion")
            
            if health <= 0:
                break
            explored += 1
            sc_vl += 1
                
                
        else:
            print("nothing happened")
        
        if health <= 0:
            break
            
    if health <= 0:
        break
        
if health <= 0:
    print("________________")
    print(Fore.BLACK + Back.RED +"Your'e dead")
    Show_stats()
    print(f"explored {explored} times ,Monsters defeated {MonD}")
