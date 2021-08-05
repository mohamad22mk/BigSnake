# python => 3.8.3

import sys
import time
import random
import pygame 

from pygame.locals import *


__version__ = "1.6.3"

pygame.init()

# Day 1 : 12:00 ---
# Day 2 : 13:00 -----> [33 H]
# Day 3 : 08:00 ---


# - - - info code - - - 
file = {
    # Pic
    "TNT"              : pygame.image.load("Pic\\TNT.png"),
    "fire"             : pygame.image.load("Pic\\Fire.png"),
    "heart"            : pygame.image.load("Pic\\Heart.png"),
    "space"            : pygame.image.load("Pic\\Space.png"),
    "apple"            : pygame.image.load("Pic\\Apple32.png"),
    "pepper"           : pygame.image.load("Pic\\pepper.png"),
    "mini_icon"        : pygame.image.load("Pic\\Icon.png"),
    "Half_Heart"       : pygame.image.load("Pic\\Half_Heart.png"),
    "Empty_heart"      : pygame.image.load("Pic\\Empty_Heart.png"),
    "Explosion_Fire"   : pygame.image.load("Pic\\Explosion_Fire.png"),
    "Left_Meteorite"   : pygame.image.load("Pic\\Left_Meteorite.png"),
    "Right_Meteorite"  : pygame.image.load("Pic\\Right_Meteorite.png"),
    "Middle_Meteorite" : pygame.image.load("Pic\\Middle_Meteorite.png"),
    
    # Sound
    "Eat"                 : pygame.mixer.Sound("Sound\\Eat.ogg"),
    "Level_Up"            : pygame.mixer.Sound("Sound\\Level_Up.ogg"),
    "game_over"           : pygame.mixer.Sound("Sound\\Game_Over.ogg"),
    "main_music"          : pygame.mixer.Sound("Sound\\main_music.ogg"),
    "Meteor_Fall"         : pygame.mixer.Sound("Sound\\Meteor_Fall.mp3"),
    "Explosion_TNT"       : pygame.mixer.Sound("Sound\\TNT.wav"),
    "Eat_Big_Apple"       : pygame.mixer.Sound("Sound\\Eat_Big_Apple.ogg"),
    "Explosion_Meteorite" : pygame.mixer.Sound("Sound\\Explosion_Meteorite.mp3"),
    
    # Font
    "font"  : ("Font\\Plaguard-ZVnjx.otf"),
    "font2" : ("Font\\SportypoReguler-OVGwe.ttf"),
}

color = {
    "red"    : (255, 0, 0),
    "blue"   : (0, 0, 255),
    "green"  : (0, 255, 0),
    "yellow" : (255, 255, 0),
    "purple" : (153, 51, 255)
}

window = {
    "width"      : 800,
    "height"     : 600,
    "caption"    : "Big Snake :)",
    "back_grand" : file["space"]
}

game = {
    "fps"   : 13,
    "score" : 0,
    "level" : 1,
    
    "score_for_level_up" : [1000, 2500, 3100],
}

snake = {
    "x"       : (window["width"] // 2),
    "y"       : (window["height"] // 2),
    "speed_x" : 0,
    "speed_y" : 0,
    "size"    : 20,
    "color"   : color["yellow"],
    "length"  : 0,
    "health"  : 3,
}

permit = {
    "TNT"       : 0,
    "pepper"    : 0, 
    "big_apple" : 0,
    "meteorite" : False
}

meteorite = {
    "middle" : {
        "x" : (window["width"] // 2 - 50),
    },
    
    "left" : {
        "x" : 0,
    },
    
    "right" : {
        "x" : (window["width"] - 200),
    },
    
    "y"             : -100,
    "speed"         : 30,
    "damage"        : 1,
    "interrupt_run" : 5, #Second
    "size"          : int(random.choice(["100", "128", "150"])),
    
    "Explosion" : {
        "size" : 200,
    },
}

item = {
    "apple" : {
        "x" : random.randrange(0, (window["width"]  - 20), 20),
        "y" : random.randrange(0, (window["height"] - 20), 20),
    },
    
    "big_apple" : {
        "x" : random.randrange(0, (window["width"]  - 20), 20),
        "y" : random.randrange(0, (window["height"] - 20), 20),
        
        "size" : 40,
    },
    
    "pepper" : {
        "x" : random.randrange(0, (window["width"]  - 20), 20),
        "y" : random.randrange(0, (window["height"] - 20), 20),
        
        "size" : 40,
    },
    
    "TNT" : {
        "x1" : random.randrange(0, (window["width"]  - 20), 20),
        "y1" : random.randrange(0, (window["height"] - 20), 20),
        
        "x2" : random.randrange(0, (window["width"]  - 20), 20),
        "y2" : random.randrange(0, (window["height"] - 20), 20),
        
        "x3" : random.randrange(0, (window["width"]  - 20), 20),
        "y3" : random.randrange(0, (window["height"] - 20), 20),
        
        "x4" : random.randrange(0, (window["width"]  - 20), 20),
        "y4" : random.randrange(0, (window["height"] - 20), 20),
        
        "x5" : random.randrange(0, (window["width"]  - 20), 20),
        "y5" : random.randrange(0, (window["height"] - 20), 20),
        
        "size" : 40,
        "damage" : 0.5,
    },
    
    "Explosion_Fire" : {
        "size" : 200,
    },
}

end_meteorite = {
    "x" : 820,
    "y" : 620,
}


# - - - game - - -
win = pygame.display.set_mode((window["width"], window["height"]))
pygame.display.set_caption(window["caption"])
pygame.display.set_icon(pygame.transform.scale(file["mini_icon"], (80, 80)))

snake_list = []
aim_meteorite = (None)
start_time_meteorite = time.time()
file["main_music"].play(-1)



def Eat_meteorite():
    #pygame.draw.rect(win, color["red"], ((meteorite["right"]["x"]), meteorite["y"], 128, 128), 1)
    def play_Eat_meteorite(x, y):
        global aim_meteorite
        global start_time_meteorite
        
        print_Variables()
        win.blit(pygame.transform.scale(file["Explosion_Fire"], (meteorite["Explosion"]["size"], meteorite["Explosion"]["size"])), (x, y))
        
        aim_meteorite = (None)
        meteorite["y"] = (-100)
        start_time_meteorite = time.time()
        
        snake["health"] -= (meteorite["damage"])
        
        file["Explosion_Meteorite"].play()
        pygame.display.update()
        time.sleep(1)
    
    
    if(aim_meteorite == "middle"):
        if    (snake["x"] <= (meteorite["middle"]["x"] + 50) <= (snake["x"] + 50)):
            if(snake["y"] <= (meteorite["y"] + 150)          <= (snake["y"] + 150)):
                
                play_Eat_meteorite(meteorite["middle"]["x"], meteorite["y"])
                meteorite["middle"]["x"] = (window["width"] // 2 - 50)
    
    
    if(aim_meteorite == "left"):
        if    (snake["x"] <= (meteorite["left"]["x"] + 100) <= (snake["x"] + 100)):
            if(snake["y"] <= (meteorite["y"] + 100)         <= (snake["y"] + 100)):
                
                play_Eat_meteorite(meteorite["left"]["x"], meteorite["y"])
                meteorite["left"]["x"] = (0)
    
    
    if(aim_meteorite == "right"):
        if    (snake["x"] <= (meteorite["right"]["x"] + 100) <= (snake["x"] + 100)):
            if(snake["y"] <= (meteorite["y"] + 100)          <= (snake["y"] + 100)):
                
                play_Eat_meteorite(meteorite["right"]["x"], meteorite["y"])
                meteorite["right"]["x"] = (window["width"] - 200)


def Collision_meteorite_to_line_end():
    global start_time_meteorite
    global aim_meteorite
    
    if(meteorite["y"] == end_meteorite["y"]):
        
        start_time_meteorite = time.time()
        
        meteorite["middle"]["x"] = (window["width"] // 2)
        meteorite["left"]["x"] = (0)
        meteorite["right"]["x"] = (window["width"] - 200)
        meteorite["y"] = -100
        
        aim_meteorite = (None)
        file["Meteor_Fall"].stop()


def print_meteorite():
    global aim_meteorite
    
    if((int(time.time() - start_time_meteorite) >= meteorite["interrupt_run"]) and (permit["meteorite"] == True)):
        
        if(aim_meteorite == None):
            random_meteorite = random.choice(["left", "middle", "right"])
            file["Meteor_Fall"].play()
        
        else: random_meteorite = aim_meteorite
        
        
        if(random_meteorite == "middle"):
            aim_meteorite = ("middle")
            
            win.blit(file["Middle_Meteorite"], (meteorite["middle"]["x"], meteorite["y"]))
            
            meteorite["y"] += (meteorite["speed"])
        
        if(random_meteorite == "left"):
            aim_meteorite = ("left")
            
            img = (pygame.transform.scale(file["Left_Meteorite"], (meteorite["size"], meteorite["size"]))) 
            win.blit(img, (meteorite["left"]["x"], meteorite["y"]))
            
            meteorite["left"]["x"] += (meteorite["speed"])
            meteorite["y"] += (meteorite["speed"])
        
        if(random_meteorite == "right"):
            aim_meteorite = ("right")
            
            img = (pygame.transform.scale(file["Right_Meteorite"], (meteorite["size"], meteorite["size"]))) 
            win.blit(img, (meteorite["right"]["x"], meteorite["y"]))
            
            meteorite["right"]["x"] -= (meteorite["speed"])
            meteorite["y"] += (meteorite["speed"])
    
    
    pygame.display.update()


def clean_number(number):
    number = str(number)
    
    var = []
    cute1 = int(-3)
    cute2 = int(-6)
    
    for j in range(1): var.append((number[-3::]))
    
    for i in number:
        var.append(number[cute2:cute1])
        
        cute1 += (-3)
        cute2 += (-3)
    
    var = var[::-1]
    while("" in var): var.remove("")
    return(",".join(var))


def Eat_TNT():
    def play_Eat_TNT(x, y):
        print_Variables()
        win.blit(pygame.transform.scale(file["Explosion_Fire"], (item["Explosion_Fire"]["size"], item["Explosion_Fire"]["size"])), ((x - 70), (y - 70)))
        
        snake["health"] -= (item["TNT"]["damage"])
        
        file["Explosion_TNT"].play()
        pygame.display.update()
        time.sleep(1)
    
    
    if    (snake["x"] <= (item["TNT"]["x1"] + 20) <= (snake["x"] + 20)):
        if(snake["y"] <= (item["TNT"]["y1"] + 20) <= (snake["y"] + 20)):
            
            if((game["level"] >= 1) and (permit["TNT"] >= 3)):
                play_Eat_TNT((item["TNT"]["x1"]), (item["TNT"]["y1"]))
                
                item["TNT"]["x1"] = random.randrange(0, (window["width"]  - 20), 20)
                item["TNT"]["y1"] = random.randrange(0, (window["height"] - 20), 20)
    
    
    if    (snake["x"] <= (item["TNT"]["x2"] + 20) <= (snake["x"] + 20)):
        if(snake["y"] <= (item["TNT"]["y2"] + 20) <= (snake["y"] + 20)):
            
            if((game["level"] >= 2) and (permit["TNT"] >= 3)):
                play_Eat_TNT((item["TNT"]["x2"]), (item["TNT"]["y2"]))
                
                
                item["TNT"]["x2"] = random.randrange(0, (window["width"]  - 20), 20)
                item["TNT"]["y2"] = random.randrange(0, (window["height"] - 20), 20)
    
    
    if    (snake["x"] <= (item["TNT"]["x3"] + 20) <= (snake["x"] + 20)):
        if(snake["y"] <= (item["TNT"]["y3"] + 20) <= (snake["y"] + 20)):
            
            if((game["level"] >= 2) and (permit["TNT"] >= 3)):
                play_Eat_TNT((item["TNT"]["x3"]), (item["TNT"]["y3"]))
                
                
                item["TNT"]["x3"] = random.randrange(0, (window["width"]  - 20), 20)
                item["TNT"]["y3"] = random.randrange(0, (window["height"] - 20), 20)
    
    
    if    (snake["x"] <= (item["TNT"]["x4"] + 20) <= (snake["x"] + 20)):
        if(snake["y"] <= (item["TNT"]["y4"] + 20) <= (snake["y"] + 20)):
            
            if((game["level"] >= 3) and (permit["TNT"] >= 3)):
                play_Eat_TNT((item["TNT"]["x4"]), (item["TNT"]["y4"]))
                
                
                item["TNT"]["x4"] = random.randrange(0, (window["width"]  - 20), 20)
                item["TNT"]["y4"] = random.randrange(0, (window["height"] - 20), 20)
    
    
    if    (snake["x"] <= (item["TNT"]["x5"] + 20) <= (snake["x"] + 20)):
        if(snake["y"] <= (item["TNT"]["y5"] + 20) <= (snake["y"] + 20)):
            
            if((game["level"] >= 3) and (permit["TNT"] >= 3)):
                play_Eat_TNT((item["TNT"]["x5"]), (item["TNT"]["y5"]))
                
                
                item["TNT"]["x5"] = random.randrange(0, (window["width"]  - 20), 20)
                item["TNT"]["y5"] = random.randrange(0, (window["height"] - 20), 20)


def print_TNT():
    if((game["level"] >= 1) and (permit["TNT"] >= 3)):
        win.blit(pygame.transform.scale(file["TNT"], (item["TNT"]["size"], item["TNT"]["size"])), (item["TNT"]["x1"], item["TNT"]["y1"]))
    
    if((game["level"] >= 2) and (permit["TNT"] >= 3)):
        win.blit(pygame.transform.scale(file["TNT"], (item["TNT"]["size"], item["TNT"]["size"])), (item["TNT"]["x2"], item["TNT"]["y2"]))
        win.blit(pygame.transform.scale(file["TNT"], (item["TNT"]["size"], item["TNT"]["size"])), (item["TNT"]["x3"], item["TNT"]["y3"]))
    
    if((game["level"] >= 3) and (permit["TNT"] >= 3)):
        win.blit(pygame.transform.scale(file["TNT"], (item["TNT"]["size"], item["TNT"]["size"])), (item["TNT"]["x4"], item["TNT"]["y4"]))
        win.blit(pygame.transform.scale(file["TNT"], (item["TNT"]["size"], item["TNT"]["size"])), (item["TNT"]["x5"], item["TNT"]["y5"]))


def print_and_Eat_pepper():
    if(permit["pepper"] >= 5):
        win.blit(pygame.transform.scale(file["pepper"], (item["pepper"]["size"], item["pepper"]["size"])), (item["pepper"]["x"], item["pepper"]["y"]))
        
        if    (snake["x"] <= (item["pepper"]["x"] + 20) <= (snake["x"] + 20)):
            if(snake["y"] <= (item["pepper"]["y"] + 20) <= (snake["y"] + 20)):
                snake["length"] += (1)
                game["score"] += (200)
                permit["TNT"] += (1)
                
                
                permit["pepper"] = (0)
                game["fps"] += (2)
                
                
                file["Eat"].play()


def Eat_Big_Apple():
    if    (snake["x"] <= (item["big_apple"]["x"] + 20) <= (snake["x"] + 20)):
        if(snake["y"] <= (item["big_apple"]["y"] + 20) <= (snake["y"] + 20)):
            snake["length"] += (1)
            game["score"] += (300)
            permit["TNT"] += (1)
            
            permit["big_apple"] = (0)
            
            file["Eat_Big_Apple"].play()


def Eat_apple():
    win.blit(pygame.transform.scale(file["apple"], (snake["size"], snake["size"])), (item["apple"]["x"], item["apple"]["y"]))
    
    if((snake["x"] == item["apple"]["x"]) and (snake["y"] == item["apple"]["y"])):
        item["apple"]["x"] = random.randrange(0, (window["width"]  - 20), 20)
        item["apple"]["y"] = random.randrange(0, (window["height"] - 20), 20)
        
        snake["length"] += (1)
        game["score"] += (100)
        permit["TNT"] += (1)
        
        
        permit["big_apple"] += (1)
        permit["pepper"] += (1)
        
        file["Eat"].play()


def snake_function(snake_lst, snake_x, snake_y):
    snake_head = [snake_x, snake_y]
    snake_lst.append(snake_head)
    
    for lst in snake_lst:
        pygame.draw.rect(win, snake["color"], (lst[0], lst[1], snake["size"], snake["size"]))


def print_Variables():
    # Back Grand
    win.blit(pygame.transform.scale(window["back_grand"], (window["width"], window["height"])), (0, 0))
    
    
    # Print Texts
    win.blit(pygame.font.Font(file["font2"], 20).render("by mkg", True, color["purple"]), (5, 570))
    win.blit(pygame.font.Font(file["font" ], 40).render(f"Level : {game['level']}", True, color["purple"]), (10, 10))
    win.blit(pygame.font.Font(file["font" ], 30).render(f"Score : {clean_number(game['score'])}", True, color["blue"]), (10, 50))
    win.blit(pygame.font.Font(None, 25).render(f"FPS : {game['fps']}", True, color["blue"]), (window["width"] - 75, window["height"] - 20))
    
    # Line End Meteorite
    pygame.draw.rect(win, color["red"], (-10, -10, end_meteorite["x"], end_meteorite["y"]), 1)
    
    
    # Print Health
    if(True):
        win.blit(pygame.transform.scale(file["Empty_heart"], (50, 50)), (740, 5))
    
    if(snake["health"] >= 0.5):
        win.blit(pygame.transform.scale(file["Half_Heart"], (50, 50)), (740, 5))
    
    if(snake["health"] >= 1):
        win.blit(pygame.transform.scale(file["heart"], (50, 50)), (740, 5))
    
    
    if(True):
        win.blit(pygame.transform.scale(file["Empty_heart"], (50, 50)), (680, 5))
    
    if(snake["health"] >= 1.5):
        win.blit(pygame.transform.scale(file["Half_Heart"], (50, 50)), (680, 5))
    
    if(snake["health"] >= 2):
        win.blit(pygame.transform.scale(file["heart"], (50, 50)), (680, 5))
    
    
    if(True):
        win.blit(pygame.transform.scale(file["Empty_heart"], (50, 50)), (620, 5))
    
    if(snake["health"] >= 2.5):
        win.blit(pygame.transform.scale(file["Half_Heart"], (50, 50)), (620, 5))
    
    if(snake["health"] >= 3):
        win.blit(pygame.transform.scale(file["heart"], (50, 50)), (620, 5))


def Pause_Game(Condition):
    file["main_music"].stop()
    file["Meteor_Fall"].stop()
    
    win.blit(pygame.transform.scale(window["back_grand"], (window["width"], window["height"])), (0, 0))
    win.blit(pygame.font.Font(file["font"], 100).render("pause", True, color["red"]), ((window["width"] // 2 - 150), (window["height"] // 2 - 90)))
    
    pygame.display.update()
    
    while(Condition):
        for evt in pygame.event.get():
            if(evt.type == QUIT):
                sys.exit()
            
            if(evt.type == KEYDOWN):
                if(evt.key == K_SPACE):
                    file["main_music"].play(-1)
                    Condition = False
    
    pygame.display.update()


def Rest_All_Game():
    # Rest All Game
    game["fps"]   = (13)
    game["score"] = (0)
    game["level"] = (1)
    
    snake["x"]       = (window["width"] // 2)
    snake["y"]       = (window["height"] // 2)
    snake["speed_x"] = (0)
    snake["speed_y"] = (0)
    snake["length"]  = (0)
    snake["health"]  = (3)
    
    permit["TNT"]       = (0)
    permit["pepper"]    = (0)
    permit["big_apple"] = (0)
    
    start_time_meteorite = time.time()
    
    snake_list.clear()


def Game_Over(Condition):
    if(snake["health"] <= 0):
        file["main_music"].stop()
        file["Meteor_Fall"].stop()
        file["game_over"].play()
        
        
        win.blit(pygame.transform.scale(window["back_grand"], (window["width"], window["height"])), (0, 0))
        win.blit(pygame.font.Font(file["font"], 100).render("DEFEAT", True, color["red"]), ((window["width"] // 2 - 170), (window["height"] // 2 - 100)))
        
        win.blit(pygame.font.Font(None, 30).render("Press Enter to Continue", True, color["green"]), ((window["width"] // 2 - 110), (window["height"] // 2 + 260)))
        
        win.blit(pygame.font.Font(file["font"], 40).render(f"Level : {game['level']}",               True, color["purple"]), ((window["width"] // 2 - 80), (window["height"] // 2 - 0)))
        win.blit(pygame.font.Font(file["font"], 35).render(f"Score : {clean_number(game['score'])}", True, color["blue"]),   ((window["width"] // 2 - 120), (window["height"] // 2 - -40)))
        
        pygame.display.update()
        
        while(Condition):
            for evt in pygame.event.get():
                if(evt.type == QUIT):
                    sys.exit()
                
                if(evt.type == KEYDOWN):
                    if((evt.key == K_KP_ENTER) or (evt.key == K_RETURN)):
                        file["game_over"].stop()
                        file["main_music"].play(-1)
                        Rest_All_Game()
                        Condition = False
        
        win.blit(pygame.transform.scale(window["back_grand"], (window["width"], window["height"])), (0, 0))
        pygame.display.update()


def Level_Up():
    if((game["score"] >= game["score_for_level_up"][0]) and (game["level"] != 2) and (game["level"] != 3) and (game["level"] != 4)):
        game["level"] = 2
        file["Level_Up"].play()
    
    if((game["score"] >= game["score_for_level_up"][1]) and (game["level"] != 3) and (game["level"] != 4)):
        game["level"] = 3
        file["Level_Up"].play()
    
    if((game["score"] >= game["score_for_level_up"][2]) and (game["level"] != 4)):
        game["level"] = 4
        file["Level_Up"].play()


def Not_Out_Screen():
    if(snake["x"] < 0):
        snake["x"] = (window["width"] - 20)
    
    if(snake["x"] > (window["width"] - 20)):
        snake["x"] = 0
    
    if(snake["y"] < 0):
        snake["y"] = (window["height"] - 20)
    
    if(snake["y"] > (window["height"] - 20)):
        snake["y"] = 0



while(True):
    #print(int(time.time() - start_time_meteorite))
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
        
        if(event.type == KEYDOWN):
            if((event.key == K_RIGHT) or (event.key == K_d)):
                # شرط اول برای اینه که مار سرعت بیشتر نگیره
                # شرط دومم برا اینه که مار به جهت مخالفی که داره حرکت میکنه بر نگرده
                if((snake["speed_x"] != 20) and (snake["speed_x"] != -20)):
                    snake["speed_x"] += 20
                    snake["speed_y"] = 0
                
                if(permit["meteorite"] == False):
                    start_time_meteorite = time.time()
                
                permit["meteorite"] = True
            
            if((event.key == K_LEFT) or (event.key == K_a)):
                if((snake["speed_x"] != -20) and (snake["speed_x"] != 20)):
                    snake["speed_x"] -= 20
                    snake["speed_y"] = 0
                
                if(permit["meteorite"] == False):
                    start_time_meteorite = time.time()
                
                permit["meteorite"] = True
            
            if((event.key == K_UP) or (event.key == K_w)):
                if((snake["speed_y"] != -20) and (snake["speed_y"] != 20)):
                    snake["speed_y"] -= 20
                    snake["speed_x"] = 0
                
                if(permit["meteorite"] == False):
                    start_time_meteorite = time.time()
                
                permit["meteorite"] = True
            
            if((event.key == K_DOWN) or (event.key == K_s)):
                if((snake["speed_y"] != 20) and (snake["speed_y"] != -20)):
                    snake["speed_y"] += 20
                    snake["speed_x"] = 0
                
                if(permit["meteorite"] == False):
                    start_time_meteorite = time.time()
                
                permit["meteorite"] = True
            
            
            if(event.key == K_SPACE):
                Pause_Game(True)
    
    
    snake["x"] += (snake["speed_x"])
    snake["y"] += (snake["speed_y"])
    
    
    # اگر جون پلیر 0 بود بازی تموم شه
    Game_Over(True)
    
    # نماد ها انرژی و امتیاز را روی صفه چاپ میکند
    print_Variables()
    
    # اگر امتیاز به حد اندازه ی مورد نیاز برسد به لول بعد میروید
    Level_Up()
    
    # اگر مار به چپ صفه بخوره از راست در میاد به بالا بخوره از پایین و بر عکس
    Not_Out_Screen()
    
    #اگر مار تی ان تی بخوره اجرا میشه
    Eat_TNT()
    
    # چاپ بمب
    print_TNT()
    
    # اگر شهاب سنگ به اخر صفه خورد پاک بشه و ادامه نده
    Collision_meteorite_to_line_end()
    
    
    # چاپ فلفل
    # اگر مار فلفل رو خورد اجرا بشه
    print_and_Eat_pepper()
    
    
    # چاپ سیب بزرگ
    if(permit["big_apple"] >= 3):
        win.blit(pygame.transform.scale(file["apple"], (item["big_apple"]["size"], item["big_apple"]["size"])), (item["big_apple"]["x"], item["big_apple"]["y"]))
        Eat_Big_Apple()
    
    # چاپ سیب
    Eat_apple()
    
    
    if(len(snake_list) > snake["length"]):
        snake_list.pop(0)
    
    snake_function(snake_list, snake["x"], snake["y"])
    
    
    # چاپ مار
    pygame.draw.rect(win, snake["color"], (snake["x"], snake["y"], snake["size"], snake["size"]))    
    
    # اگر به شهاب سنگ بر خورد کردیم اجرا بشه
    Eat_meteorite()
    
    # چاپ شهاب سنگ
    print_meteorite()
    
    
    pygame.time.Clock().tick(game["fps"])
    pygame.display.update()

# The End
