import keyboard
from dotenv import load_dotenv
from time import sleep
import signal
import json
import os

load_dotenv()

IP = os.getenv('IP')
PARAM = os.getenv('PARAM')

def handler(): # def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/N ")
    if res.lower() in ("y","yes","ye","ya","yeah","yis"):
        keyboard.press('f11')
        exit(1)
 
signal.signal(signal.SIGINT, handler)

ascii = json.load(open("json/ascii.json", encoding="utf-8"))
levels = json.load(open("json/levels.json", encoding="utf-8"))

def border(background, size):
     # FILL REST OF THE SCREEN WITH BLANK LINES 
    filled=len(background)
    nonfilled=size.lines - filled - 1 # -1 is reserved line for input field :)
    for i in range(nonfilled):
        background.append(" "*size.columns)

    up1=ascii["BORDER"][0]
    up2=ascii["BORDER"][1]
    side1=ascii["BORDER"][2]
    side2=ascii["BORDER"][3]
        
    margin_up=0
    margin_down=0

    # BORDER
    # BORDER UP AND DOWN
    background[0] = (up1*size.columns)[0:size.columns]
    background[1] = (up2*size.columns)[0:size.columns]
    background[len(background)-2]=(up2*size.columns)[0:size.columns]
    background[len(background)-1]=(up1*size.columns)[0:size.columns]

    # BORDER SIDES 
    
    for i in range(margin_up, len(background)-margin_down):
        background[i] = background[i][len(side1):len(background[i])-len(side1)]
        if up2=="-._.-=" and (i == 0 or i == len(background)-margin_down-1):
            if i == 0:
                up=".-=~=-."
                background[i] = up+background[i]+up
            if i == len(background)-margin_down-1:
                down="`-._.-'"
                background[i] = down+background[i]+down
            continue
        if i % 2 == 0:
            background[i] = side1+background[i]+side1
            continue
        background[i] = side2+background[i]+side2

    return background

main_menu = ["[PLAY]","[DIE]"]

level1_name="[SANITY]"
level2_name="[ANXIETY]"
level3_name="[AGITATION]"
level4_name="[DISORIENTATION]"
level5_name="[DELUSION]"
level6_name="[INSANE]"
level7_name="[MAD]"

dlc=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","[To Play This Level you Must Own a DLC]"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",]

levels_menu = ([level1_name,level2_name,level3_name,
                level4_name,level5_name,level6_name,
                level7_name,"[BACK]"])

level_menu = ["[PLAY]","[HINT]","[SOLUTION]","[SOURCE]","[BACK]"]

def print_menu(option="", margin=6, hint=False, solution=False, source=False, ctrlc=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    size = os.get_terminal_size() # (columns=172, lines=45)
    background=[]

    if(size.columns < len(ascii["INSANE EXPEDITION"][0])):
        print("The script may not be running from cmd or your screen size may be insufficient :D")
        exit()
        return
    
    if ctrlc==True:
            for a in range(int(size.lines/2) - 1):
                background.append(" ".center(size.columns, " "))
            background.append(" Ctrl-c was pressed. Do you really want to exit? y/N "
                              .center(size.columns, " "))
            for a in range(int(size.lines/2) - 1):
                background.append(" ".center(size.columns, " "))
    
            background = border(background=background, size=size)
            
            for b in background:
                print(b)
            return
    
    if option=="" or "play" in option or level1_name == option or level2_name == option or level3_name == option or level4_name == option or level5_name == option or level6_name == option or level7_name == option:
        
        if option=="" or "play" in option:
            for i in range (margin+1):
                background.append(" "*size.columns)
        else:
            for i in range (margin-1):
                background.append(" "*size.columns)

        if option=="":
            background[margin-2]="You will face horrors beyond your wildest imagination, for this is the".center(size.columns, " ")
   
        if "play" in option:
            background[margin-2]="As you descend deeper into madness, the difficulty of each level increases. Will you be able to make it through all the".center(size.columns, " ")

        # "Welcome to your worst nightmare, the Insane Expedition."
        # "This is not a journey for the weak-willed, for this is the Insane Expedition."
        # "Craziness and chaos await, for this is the Insane Expedition."
        #   "You will face horrors beyond your wildest imagination, for this is the Insane Expedition."
        # "Your sanity will be tested, for this is the Insane Expedition."
        # "Beyond the realms of reason, lies the Insane Expedition."
        # "Darkness and madness reign here, the Insane Expedition."
        #   "Leave your sanity behind, for this is the Insane Expedition."
        #   "The journey ahead is a path to madness, the Insane Expedition."

        if option=="":
            for a in ascii["INSANE EXPEDITION"]:
                background.append(a.center(size.columns, " "))

        if "play" in option:
            for a in ascii["LEVELS"]:
                background.append(a.center(size.columns, " "))

        if option=="" or "play" in option:
            for a in ascii["SKULL"]:
                background.append(a.center(size.columns, " "))
        
        elif "sanity" in option.lower():
            for a in ascii["SPACE"]:
                background.append(a.center(size.columns, " "))

        elif "anxiety" in option.lower():
            for a in ascii["GIRL"]:
                background.append(a.center(size.columns, " "))

        elif "agitation" in option.lower(): 
            for a in ascii["WEEPING_ANGEL"]:
                background.append(a.center(size.columns, " "))

        elif "DISORIENTATION".lower() in option.lower():
            for a in ascii["BACKROOMS"]:
                background.append(a.center(size.columns, " "))

        elif "DELUSION".lower() in option.lower():
            for a in ascii["DELUSION"]:
                background.append(a.center(size.columns, " "))

        elif "INSANE".lower() in option.lower():
            for a in ascii["HOODIE"]:
                background.append(a.center(size.columns, " "))

        elif "MAD".lower() in option.lower():
            for a in ascii["SPAZM_TEXT"]:
                background.append(a.center(size.columns, " "))

        # FILL REST OF THE SCREEN WITH BLANK LINES 
        filled=len(background)
        nonfilled=size.lines - filled - 1 # -1 is reserved line for input field :)
        for i in range(nonfilled):
            background.append(" "*size.columns)

        # PRINT MENU OPTIONS
        options=""
        spacing=" "*10 # MUST BE SUDE CISLO

        if option=="":
            menu=main_menu

        elif option==level1_name:
            menu=level_menu

        elif option==level2_name:
            menu=level_menu

        elif option==level3_name:
            menu=level_menu

        elif option==level4_name:
            menu=level_menu

        elif option==level5_name:
            menu=level_menu

        elif option==level6_name:
            menu=level_menu

        elif option==level7_name:
            menu=level_menu

        else:
            menu=levels_menu

        for i in range(len(menu)):
            if options=="":
                options+=menu[i]
                continue
            options+=spacing+menu[i]

        background[len(background)-1-round(nonfilled/2)]=options.center(size.columns, " ")

        if hint==True or solution==True or source==True:
            curr_level=""
            
            if option==level1_name:
                curr_level=option
                lore=  ("If you're not careful and you noclip out of reality in the wrong areas, you'll end up in the"+
                     "\nBackrooms, where it's nothing but the stink of old moist carpet, the madness of mono-yellow, the"+
                     "\nendless background noise of fluorescent lights at maximum hum-buzz, and approximately six hundred"+
                     "\nmillion square miles of randomly segmented empty rooms to be trapped in"+
                     "\nGod save you if you hear something wandering around nearby, because it sure as hell has heard you")
            
            if option==level2_name:
                curr_level=option
            
            if option==level3_name:
                curr_level=option
            
            if option==level4_name:
                curr_level=option
            
            if option==level5_name:
                curr_level=option
            
            if option==level6_name:
                curr_level=option
            
            if option==level7_name:
                curr_level=option

            thing=""
            if hint==True:
                thing=levels[curr_level]["HINT"]
            
            if source==True:
                thing=levels[curr_level]["SOURCE"]

            if solution==True:
                thing=levels[curr_level]["SOLUTION"]

            if solution==True or source==True or hint==True:
                background[len(background)-3-round(nonfilled/2)]=thing.center(size.columns, " ")

        text=""
        if option==level1_name:
            text=" [ Is This Even Real?? ] "
            # len(text)
            bcglen=len(background[len(background)-2-nonfilled])
            first_half=int((bcglen-len(text))/2)
            second_half=size.columns-first_half

            if size.columns%2==1:
                first_half=first_half-1

            if len(text)%2==0:
                background[len(background)-2-nonfilled]=background[len(background)-2-nonfilled][0:first_half]+text+background[len(background)-2-nonfilled][second_half:]
            else:
                background[len(background)-2-nonfilled]=background[len(background)-2-nonfilled][0:first_half]+text+background[len(background)-2-nonfilled][second_half-1:]

        if option==level2_name:
            text=" [ It's like my mind is playing tricks on me, making me think the worst is going to happen... ] "
            # len(text)
            bcglen=len(background[len(background)-2-nonfilled])
            first_half=int((bcglen-len(text))/2)
            second_half=size.columns-first_half

            if size.columns%2==1:
                first_half=first_half+1
            if len(text)%2==0:
                background[len(background)-2-nonfilled]=background[len(background)-2-nonfilled][0:first_half]+text+background[len(background)-2-nonfilled][second_half:]
            else:
                background[len(background)-2-nonfilled]=background[len(background)-2-nonfilled][0:first_half]+text+background[len(background)-2-nonfilled][second_half-1:]
            
            background[len(background)-3-round(nonfilled)]=("|"+" ".center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-1-round(nonfilled)]=("|"+"_".center(133, "_")+"|").center(size.columns, " ")
        
        if option==level3_name:
            text1=" The Weeping Angels are statues frozen in time, but when you turn your back on them, they come to life with lightning speed. Their "
            text2=" faces twist into terrifying grimaces as they move in for the kill, with sharp claws poised to grab hold of their unsuspecting prey. "
            text3=" Beware the Weeping Angels, for if they catch you, they'll send you back in time, leaving you stranded in a bygone era, unable to"
            text4=" return to your own time. Always watchful and waiting for their next victim, the Weeping Angels are one of the deadliest creatures."

            background[len(background)-6-round(nonfilled)]=("|"+"_".center(133, "_")+"|").center(size.columns, " ")
            background[len(background)-5-round(nonfilled)]=("|"+text1.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-4-round(nonfilled)]=("|"+text2.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-3-round(nonfilled)]=("|"+text3.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-2-round(nonfilled)]=("|"+text4.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-1-round(nonfilled)]=("|"+"_".center(133, "_")+"|").center(size.columns, " ")

        if option==level4_name:
            text1=" If you're not careful and you noclip out of reality in the wrong areas, you'll end up in the Backrooms, where it's nothing "
            text2=" but the stink of old moist carpet, the madness of mono-yellow, the endless background noise of fluorescent lights at maximum "
            text3=" hum-buzz, and approximately six hundred million square miles of randomly segmented empty rooms to be trapped in "
            text4=" God save you if you hear something wandering around nearby, because it sure as hell has heard you"
            textx="|                                                                                                                                     |"
            
            background[len(background)-5-round(nonfilled)]=("|"+text1.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-4-round(nonfilled)]=("|"+text2.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-3-round(nonfilled)]=("|"+text3.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-2-round(nonfilled)]=("|"+text4.center(133, " ")+"|").center(size.columns, " ")
            
        
        if option==level5_name:
            text=" [ HAVE YOU SEEN THIS MAN? ] "

            # background[len(background)-1-round(nonfilled)]=("|"+text.center(133, "@")+"|").center(size.columns, " ")
        
        if option==level6_name:
            text="[ Sanity is overrated, at this point I'd rather embrace the madness. ]"
            # text="[ I've crossed over into a world where nothing is what it seems, and at this point, I'm not sure if I want to come back. ]"
            
            background[len(background)-2-round(nonfilled)]=("|"+text.center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-3-round(nonfilled)]=("|"+" ".center(133, " ")+"|").center(size.columns, " ")
            background[len(background)-1-round(nonfilled)]=("|"+"_".center(133, "_")+"|").center(size.columns, " ")
        
        if option==level7_name:

            text1="I am silence that devours your mind"
            text2="I was then and i am now"
            text3="I embraced madness and it embraced me in return"
            text4="I am broken yet more complete than ever before"
            text5="I am the madness in your very soul"
            text6="I am madness lurking withnin you"
            text7="I am what you have made me"
            text8=""

            #  -36
            #  -23
            #  -47
            #  -46
            #  -34
            #  -32
            #  -26
            # I am mirror of consiousness -27
            # I am release from sanity -24
            # I am free of shackles of sanity -31

            # line=len(background)-30-nonfilled
            # bcg=background[line]
            # start=int((size.columns-len(ascii["SPAZM"][0]))/2)+3
            # text=text1
            # background[line]=bcg[0:start]+text+bcg[start+len(text):]

            # line=len(background)-30-nonfilled
            # bcg=background[line]
            # start=int((size.columns-len(ascii["SPAZM"][0]))/2)+133-len(text2)-1
            # text=text2
            # background[line]=bcg[0:start]+text+bcg[start+len(text):]

            # line=len(background)-26-nonfilled
            # bcg=background[line]
            # start=int((size.columns-len(ascii["SPAZM"][0]))/2)+
            # text=text3
            # background[line]=bcg[0:start]+text+bcg[start+len(text):]


        
    
    
    background = border(background=background, size=size)

    for b in background:
        print(b)
    
def play(level):


    os.system('cls' if os.name == 'nt' else 'clear')
    
    if level in level1_name.lower():
        os.system(f"ssh {level}@{IP} -t -i {level}.pem {PARAM} '/home/sanity/BufferOverflow'")
        # sleep(3)
    elif level in level2_name.lower():
        os.system(f"ssh {level}@{IP} -t {PARAM} python3 StrFormVuln.py")
        # sleep(5)
    elif level in level3_name.lower():
        os.system(f"ssh {level}@{IP} {PARAM}")

    elif level in level4_name.lower():
        os.system(f"ssh {level}@{IP} {PARAM}")

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("  [ To play this level you must own Insane DLC               ]")
        print("  [ If you do not own it, you can buy it at INSERT TEXT HERE ]")
        print("  [ or send 0.001 bitcoin to the following BTC address       ]")
        print("  [ bc1qdt6xxxrm7cfcgx7ex44tvm5e292xfwy0uvq7na               ]\n")

        res = input("  [ Press any key to continue... ] ")


def main(loop=True):
    keyboard.press('f11')
    level=""
    depth=0
    option_old=""
    option=""
    hint=False
    solution=False
    source=False
    while(loop):
        try:
            if depth==0:
                # page="levels"
                print_menu(option="")
            if depth==1:
                print_menu(option="play")
            if depth==2 and hint==False and solution==False and source==False:
                print_menu(option=level)
            option_old=option
            hint=False
            solution=False
            source=False
            option = input("[INPUT]> ")
        except Exception as e:
            
            print_menu(ctrlc=True)
            res = input("[INPUT]> ")
            if res.lower() in ("y","yes","ye","ya","yeah","yis"):
                os.system('cls' if os.name == 'nt' else 'clear')
                keyboard.press('f11')
                print(" ~ Your destiny is inescapable.")

                loop=False
                exit(1)
        #Check what choice was entered and act accordingly
        if "play" in option.lower():
            if depth==0:
                depth+=1
                print_menu(option="play")
            elif depth==2:
                #print(level) [SANITY]
                #sleep(3)
                play(level[1:len(level)-1].lower())
                continue
            else:
                print_menu(option="play")
                
            # play()
        elif "back" in option.lower() or "cd .." in option.lower():
            if depth==0:
                continue
            
            elif depth==1:
                depth-=1
                print_menu(option="")

            elif depth==2:
                depth-=1
                print_menu(option="play")
                level=""
            
        elif level1_name[1:len(level1_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level1_name.lower())
                continue
            depth+=1
            level=level1_name
            print_menu(option=level)
            # TODO

        elif level2_name[1:len(level2_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level2_name.lower())
                continue
            depth+=1
            level=level2_name
            print_menu(option=level)
            # TODO

        elif level3_name[1:len(level3_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level3_name.lower())
                continue
            depth+=1
            level=level3_name
            print_menu(option=level)
            # TODO

        elif level4_name[1:len(level4_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level4_name.lower())
                continue
            depth+=1
            level=level4_name
            print_menu(option=level)
            # TODO

        elif level5_name[1:len(level5_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level5_name.lower())
                continue
            depth+=1
            level=level5_name
            print_menu(option=level)
            # TODO

        elif level6_name[1:len(level6_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level6_name.lower())
                continue
            depth+=1
            level=level6_name
            print_menu(option=level)
            # TODO

        elif level7_name[1:len(level7_name)-1].lower() in option.lower():
            if depth != 1:
                print_menu(option=level7_name.lower())
                continue
            depth+=1
            level=level7_name
            print_menu(option=level)
            # TODO

        elif "hint" in option.lower():
            hint=True
            if depth != 2:
                pass

            if level == level1_name:
                print_menu(option=level, hint=True)

            elif level == level2_name:
                print_menu(option=level, hint=True)

            elif level == level3_name:
                print_menu(option=level, hint=True)

            elif level == level4_name:
                print_menu(option=level, hint=True)

            elif level == level5_name:
                print_menu(option=level, hint=True)

            elif level == level6_name:
                print_menu(option=level, hint=True)

            elif level == level7_name:
                print_menu(option=level, hint=True)
            else:
                print_menu(option=level)

        elif "source" in option.lower():
            source=True
            if depth != 2:
                pass
            if level == level1_name:
                print_menu(option=level, source=True)

            elif level == level2_name:
                print_menu(option=level, source=True)

            elif level == level3_name:
                print_menu(option=level, source=True)

            elif level == level4_name:
                print_menu(option=level, source=True)

            elif level == level5_name:
                print_menu(option=level, source=True)

            elif level == level6_name:
                print_menu(option=level, source=True)

            elif level == level7_name:
                print_menu(option=level, source=True)

            else:
                print_menu(option=level)

        elif "solution" in option.lower():
            solution=True
            if depth != 2:
                pass
            if level == level1_name:
                print_menu(option=level, solution=True)

            elif level == level2_name:
                print_menu(option=level, solution=True)

            elif level == level3_name:
                print_menu(option=level, solution=True)

            elif level == level4_name:
                print_menu(option=level, solution=True)

            elif level == level5_name:
                print_menu(option=level, solution=True)

            elif level == level6_name:
                print_menu(option=level, solution=True)

            elif level == level7_name:
                print_menu(option=level, solution=True)

            else:
                print_menu(option=level)

        elif "die" in option.lower():
            os.system('cls' if os.name == 'nt' else 'clear')
            keyboard.press('f11')
            print(" ~ Your destiny is inescapable.")
            exit()
        else:
            if depth==2:
                print_menu(option=level)
                continue
            option = option_old
            print_menu(option=option.lower())

        
if __name__ == "__main__":
    main()
    
    