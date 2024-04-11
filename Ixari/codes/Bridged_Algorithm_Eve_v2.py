from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import random
from PIL import Image
from random import randint
from pathlib import Path

def Get_Working_Base():
    
    base_name = input('Base Character: ')
    
    return base_name

def merge_hair_body (Image_Hair, Image_Head):
     
     Hair_Image = Image.open(Image_Hair).convert("RGBA")

     Head_Image = Image.open(Image_Head).convert("RGBA")

     result = Image.alpha_composite(Hair_Image,Head_Image)

     return result

def get_body_image (Image_Base):
    
    Head_Image = Image.open(Image_Base).convert("RGBA")

    return Head_Image

def Get_Layers (base_name):
    
    BackGrounds = [f for f in listdir(f"{input_path}/0.background") if isfile(join(f"{input_path}/0.background", f))]
    Back = [f for f in listdir(f"{input_path}/1.back") if isfile(join(f"{input_path}/1.back", f))]
    Base = [f for f in listdir(f"{input_path}/2.base") if isfile(join(f"{input_path}/2.base", f))]
    Torso = [f for f in listdir(f"{input_path}/3.torso") if isfile(join(f"{input_path}/3.torso", f))]
    Eyes = [f for f in listdir(f"{input_path}/5.eyes") if isfile(join(f"{input_path}/5.eyes", f))]
    Mouth = [f for f in listdir(f"{input_path}/4.mouth") if isfile(join(f"{input_path}/4.mouth", f))]
    Head = [f for f in listdir(f"{input_path}/6.head") if isfile(join(f"{input_path}/6.head", f))]
    Helmet = [f for f in listdir(f"{input_path}/7.helmet") if isfile(join(f"{input_path}/7.helmet", f))]
    Symbol = [f for f in listdir(f"{input_path}/8.symbols") if isfile(join(f"{input_path}/8.symbols", f))]
    
    return BackGrounds, Back, Base, Torso, Eyes, Mouth, Head, Helmet, Symbol


def Get_Rarities (base_name):
    
    BackGrounds_Rarity = [3.5,0.5,6,6,6,2,0.5,6,2,3,6,2,0.5,3.5,3.5,3.5,6,3.5,3.5,3,3,2,6,3.5,3,6,6]
    Back_Rarity = [0.4,1,1,0.8,0.8,0.6,1,0.4,1,1,0.8,0.6,1.2,0.6,88.8]
    Base_Rarity = [0,14,29,29,28]
    Torso_Rarity=[0.25,2,3,3,2,2,3,0.5,0.5,0.5,0.5,0.5,2,0.5,1,1,1,0.5,1,1,1,2,2,0.5,2,2,1,0.25,3,2,3,0.25,1,2,3,2,0.5,2,1,1,2,3,3,5,0.5,1,1,1,1,0.25,1,1,2,0.25,0.5,0.5,1,1,1,1,0.75,1,1,1,0.5,1,1,2,0.5,1,3,3]  
    Head_Rarity = [2,0.25,2,2,3,0.5,0.25,0.2,0.25,0.2,0.25,0.2,0.25,3,0.5,0.5,3,0.5,2,2,2,2,2,64.15,0.25,0.5,2,0.25]
    Eyes_Rarity=[2,1.5,2,2,3,2,56.5,1.5,1.5,3,2,2,3,2,2,3,3,2,2,2,2]
    Mouth_Rarity = [2,3,3,3,3,2,2,3,72,2,3,1,1]
    Helmet_Rarity = [0.5,0.25,1,0.25,0.5,0.5,1.5,0.5,2.5,81.5,2,3,2,2,2]
    Symbol_Rarity = [1,1,95,1,1,1]
    
    return BackGrounds_Rarity, Back_Rarity, Base_Rarity, Torso_Rarity, Head_Rarity, Eyes_Rarity, Mouth_Rarity, Helmet_Rarity, Symbol_Rarity

def NFT_First_Iteration (BackGrounds,BackGrounds_Rarity,Back,Back_Rarity,Base,Base_Rarity,Torso,Torso_Rarity,Head,Head_Rarity,Eyes, Eyes_Rarity,Mouth,Mouth_Rarity,Helmet,Helmet_Rarity, Symbol, Symbol_Rarity):
  

    NFT_BackGround = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Back = random.choices(Back,weights=(Back_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_Eyes = random.choices(Eyes,weights=(Eyes_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_Helmet = random.choices(Helmet,weights=(Helmet_Rarity))[0]
    NFT_Symbol= random.choices(Symbol,weights=Symbol_Rarity)[0]
    
    
    return NFT_BackGround, NFT_Back, NFT_Base, NFT_Torso, NFT_Head, NFT_Eyes, NFT_Mouth, NFT_Helmet, NFT_Symbol


def Mouth_Conflicts (NFT_Mouth, NFT_Head_OG,NFT_Eyes_OG):
    
        ##Mouth conflicts
    if (NFT_Mouth == 'Aegis.png' or NFT_Mouth == 'Lockjaw.png' or NFT_Mouth == 'Scenter.png' or NFT_Mouth == 'Snarl II.png' or NFT_Mouth == 'Snarl I.png'):
        NFT_Head = random.choices(['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png','Nirvana.png','none.png'],weights=(5,5,5,5,5,5,5,5))[0] 
        NFT_Eyes = random.choices(['none.png','Scratch.png','Iris.png','Temper.png'],weights=(11,11,11,11))[0]
        excluded_traits = ['Brainrot.png','Vizor.png','Hydra.png','Scylla.png','Wraith.png']
    
    elif (NFT_Mouth == 'Augury I.png' or NFT_Mouth == 'Augury II.png'):
        NFT_Head = random.choices(['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png',
        'Nirvana.png','none.png'],weights=(5,5,5,5,5,5,5,5))[0] 
        NFT_Eyes = random.choices(['none.png','Scratch.png','Iris.png','Temper.png'],weights=(11,11,11,11))[0]
        excluded_traits = ['Brainrot.png','Vizor.png','Hydra.png','Scylla.png','Wraith.png']

    elif (NFT_Mouth == 'Bandana I.png' or NFT_Mouth == 'Bandana II.png' or NFT_Mouth == 'Lounge.png'):
        NFT_Head = random.choices(['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Hydra.png','Narcissus.png','Nightmare.png',
        'Nirvana.png','none.png','Oxen.png','Scylla.png'],weights=(5,5,5,5,5,5,5,5,5,5,5))[0] #'Non La.png'
        NFT_Eyes = NFT_Eyes_OG
        excluded_traits = ['Tracker.png','Wraith.png']

    elif (NFT_Mouth == 'Stitcher.png'):
        NFT_Head = random.choices(['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Hydra.png','Narcissus.png','Nightmare.png',
        'Nirvana.png','none.png','Scylla.png','Tracker.png'],weights=(5,5,5,5,5,5,5,5,5,5,5))[0]
        NFT_Eyes = NFT_Eyes_OG
        excluded_traits = ['Hydra.png','Scylla.png','Wraith.png']

    elif (NFT_Mouth == 'Carnal.png'):
        NFT_Head = random.choices(['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png',
        'Nirvana.png','none.png'],weights=(5,5,5,5,5,5,5,5))[0]
        NFT_Eyes = NFT_Eyes_OG
        excluded_traits = ['Brainrot.png','Tracker.png','Vizor.png','Hydra.png','Scylla.png','Wraith.png']

    elif (NFT_Mouth == 'Seal.png'):
        NFT_Head = random.choices(['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png',
        'Nirvana.png','none.png'],weights=(5,5,5,5,5,5,5,5))[0]
        NFT_Eyes = NFT_Eyes_OG
        excluded_traits = ['Hydra.png','Scylla.png','Wraith.png','Vizor.png']

    else:    
        NFT_Head = NFT_Head_OG
        NFT_Eyes = NFT_Eyes_OG
        excluded_traits = []
        
    return NFT_Head, NFT_Eyes, excluded_traits

def Eyes_Conflicts (NFT_Eyes,NFT_Head_OG,excluded_traits,base_name):
    
    if (NFT_Eyes in excluded_traits):
        
        NFT_Eyes = 'None.png'
        NFT_Head = NFT_Head_OG

    elif (NFT_Eyes == 'Vizor.png'):
        

        available_heads = ['Dark Cap.png','Diadem.png','Nirvana.png','none.png']
        available_rarity = [5,5,5,5] 
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                # print (elem)
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0] 
        NFT_Eyes = NFT_Eyes
    elif (NFT_Eyes == 'Circlet.png'):
        
        available_heads = ['Coronet.png','Diadem.png','Hydra.png','Narcissus.png','Nightmare.png','none.png','Scylla.png']
        available_rarity = [5,5,5,5,5,5,5]
        
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                # print (elem)
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0] 
        NFT_Eyes = NFT_Eyes
    elif (NFT_Eyes == 'Psych.png' or NFT_Eyes == 'Obsidian.png'):
       
        available_heads = ['Dark Cap.png','Coronet.png','Diadem.png','Nightmare.png','Nirvana.png','none.png']
        available_rarity = [5,5,5,5,5,5]
        
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                print (elem)
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0]
        NFT_Eyes = NFT_Eyes
    elif (NFT_Eyes == 'Pearce.png'):
        
        if (base_name == 'Eve'):
            available_heads = ['Dark Cap.png','Diadem.png','Gunner.png','Nirvana.png','none.png']
            available_rarity = [5,5,5,5,5]
        else:
            available_heads = ['Dark Cap.png','Diadem.png','Gunner.png','Nightmare.png','Nirvana.png','none.png']
            available_rarity = [5,5,5,5,5,5]
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                # print (elem)       
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0]
        NFT_Eyes = NFT_Eyes
        
    
    elif (NFT_Eyes == 'Seethe.png' or NFT_Eyes == 'Temper.png'):
        
        available_heads = ['Coronet.png','Diadem.png','Gunner.png','Hydra.png','Narcissus.png','Nightmare.png','Nirvana.png','none.png','Scylla.png']
        available_rarity = [5,5,5,5,5,5,5,5,5]
        
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                # print (elem)          
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0] 
        NFT_Eyes = NFT_Eyes
        
    elif (NFT_Eyes == 'Bloodshot.png' or NFT_Eyes == 'Iris.png' or NFT_Eyes == 'Leaf.png' or NFT_Eyes == 'Lens.png'
          or NFT_Eyes == 'Patch.png' or NFT_Eyes == 'Trance Dark.png' or NFT_Eyes == 'Trance Light.png' or NFT_Eyes == 'Rebel.png'):
        
        available_heads = ['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png','Nirvana.png','none.png']
        available_rarity = [5,5,5,5,5,5,5,5]
        
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                # print (elem)          
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0]      
        NFT_Eyes = NFT_Eyes
    elif (NFT_Eyes == 'Scratch.png' or NFT_Eyes == 'Shade.png' or NFT_Eyes == 'Stripe.png'):
        
        available_heads = ['Dark Cap.png','Coronet.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png','Nirvana.png','none.png']
        available_rarity = [5,5,5,5,5,5,5,5]
        
        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
                # print (elem)          
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0]  
        NFT_Eyes = NFT_Eyes
    elif (NFT_Eyes == 'Hovergraph.png'):
        
        available_heads = ['Dark Cap.png','Diadem.png','Gunner.png','Narcissus.png','Nightmare.png','Nirvana.png','none.png']
        available_rarity = [5,5,5,5,5,5,5]

        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
 
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0]
        NFT_Eyes = NFT_Eyes
    elif (NFT_Eyes == 'Oculux.png'):
        
        available_heads = ['Dark Cap.png','Coronet.png','Crucify.png','Diadem.png','Gunner.png','Hydra.png','Narcissus.png','Nightmare.png','Nirvana.png','none.png','Scylla.png','Wraith.png']
        available_rarity = [5,5,5,5,5,5,5,5,5,5,5,5]

        for elem in excluded_traits:
            if elem in available_heads:
                remove = available_heads.index(elem)
                available_heads.pop(remove)
                available_rarity.pop(remove)
 
        NFT_Head = random.choices(available_heads,weights=(available_rarity))[0]
        NFT_Eyes = NFT_Eyes
    else:
        NFT_Head = NFT_Head_OG
        NFT_Eyes = NFT_Eyes
    
    
    return NFT_Head, NFT_Eyes

def torso_conflicts (base_name,Torso,Torso_Rarity):

    if (base_name == 'Titus'):
        excluded_torsos = ['Black Shirt.png','Black Suit.png','Clavicle.png','Commander Dark.png','Commander Light.png','Epaulette.png', 'Grey Pullover.png','Khaki Pullover.png','Pinstripe Suit.png','Polar.png']
    elif (base_name == 'Lucifer'):
        excluded_torsos = ['Royal Mantle Ruby.png','Royal Mantle Citrine.png']
        
    for elem in excluded_torsos:

        if elem in excluded_torsos:
            remove = excluded_torsos.index(elem)
            Torso.pop(remove)
            Torso_Rarity.pop(remove)

    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    return NFT_Torso
    
def control_ADN(ADN_list,NFT_BackGround,NFT_Back,NFT_Base,NFT_Torso,NFT_Eyes,NFT_Mouth,NFT_Head,NFT_Helmet, NFT_Symbol):
    
    ADN_NFT = NFT_BackGround + '&' + NFT_Back+'&' + NFT_Base+ '&' + NFT_Torso+ '&' + NFT_Eyes+ '&' + NFT_Mouth + '&' + NFT_Head + '&' + NFT_Helmet  + '&' + NFT_Symbol
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control

def get_Images (base_name,NFT_BackGround,NFT_Back, NFT_Base, NFT_Torso, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Helmet,NFT_Symbol):
    
    Bald_Eves_Head = ['Brainrot.png', 'Coronet.png', 'Crest.png', 'Crucify.png', 'Dark Cap.png', 'Diadem.png', 'Flame.png', 'Gunner.png', 'Highland.png','Hydra.png', 'Light Cap.png','Maleficent.png', 'Narcissus.png', 'Nirvana.png', 'Network Holo I.png', 'Nightmare.png'
        'Nirvana.png','Non La.png', 'Oxen.png', 'Scylla.png', 'Tracker.png', 'Wraith.png' ] ##'ScyllaX.png','WraithX.png','HydraX.png'
    
    Bald_Eves_Eyes = ['Circlet.png']
    
    Bald_Eves_Helmet = ['Carve.png', 'Gamer.png', 'Countdown.png', 'Giggle.png', 'Goat.png', 'Grin I.png', 'Hush.png', 'Ibex.png', 'Oryx.png','Raptor I.png', 'Raptor II.png', 'Visor.png', 'Witness.png']

    Bald_Eves_Mouth = ['Aegis.png', 'Bandana I.png', 'Bandana II.png', 'Carnal.png', 'Lockjaw.png', 'Scenter.png', 'Seal.png','Snarl I.png', 'Snarl II.png','Stitcher.png']

    Image_BackGround = f'{input_path}/0.background/'+NFT_BackGround
    Image_Back = f'{input_path}/1.back/'+NFT_Back
    Image_Base = f'{input_path}/2.base/'+NFT_Base
    Image_Torso = f'{input_path}/3.torso/'+NFT_Torso
    Image_Symbol = f'{input_path}/8.symbols/'+NFT_Symbol
    
    if (NFT_Mouth in Bald_Eves_Mouth and (NFT_Base == 'Eve Bald.png' or NFT_Base == 'Short Eve.png')):
        Image_Mouth = f'{input_path}/4.mouth_bald/'+NFT_Mouth
    else:
        Image_Mouth = f'{input_path}/4.mouth/'+NFT_Mouth

    if ((NFT_Head in Bald_Eves_Head or NFT_Head == 'Non La.png') and NFT_Base == 'Eve Bald.png'):
        Image_Head = f'{input_path}/6.head_bald/'+NFT_Head
    
    else:
        Image_Head = f'{input_path}/6.head/'+NFT_Head

    if (NFT_Eyes in Bald_Eves_Eyes and NFT_Base == 'Eve Bald.png'):
        Image_Eyes = f'{input_path}/5.eyes_bald/'+NFT_Eyes
    else:
        Image_Eyes = f'{input_path}/5.eyes/'+NFT_Eyes

    if ((NFT_Helmet in Bald_Eves_Helmet) and NFT_Base == 'Eve Bald.png'):
        Image_Helmet = f'{input_path}/7.helmet_bald/'+NFT_Helmet
        
    else:
        Image_Helmet = f'{input_path}/7.helmet/'+NFT_Helmet

    
    if (NFT_Base == 'Short Eve.png' and NFT_Head == 'Crest.png'):
        Image_Head = f'{input_path}/6.head/none.png'
    else:
        Image_Head = Image_Head
    
    if (NFT_Base == 'Eve.png'):
        
        if (NFT_Head == 'Dark Cap.png' or NFT_Head == 'Light Cap.png' or NFT_Head == 'Brainrot.png' or NFT_Head == 'Gunner.png' or NFT_Head == 'Maleficent.png' or NFT_Head == 'Oxen.png'):
            Image_Hair = f'{input_path}/2.1.hair/Cap Hair.png'
            Image_Base = f'{input_path}/2.base/Bald Eve.png'
            Image_Base = merge_hair_body(Image_Base,Image_Hair)

        elif ((NFT_Head == 'Diadem.png' or NFT_Head == 'Crucify.png')):
            Image_Hair = f'{input_path}/2.1.hair/Coronet Hair.png'
            Image_Base = f'{input_path}/2.base/Bald Eve.png'
            print (Image_Hair)
            Image_Base = merge_hair_body(Image_Base,Image_Hair)

        elif (NFT_Head == 'Coronet.png'):
            Image_Hair = f'{input_path}/2.1.hair/Coronet Hair.png'
            Image_Base = f'{input_path}/2.base/Bald Eve.png'
            print (Image_Hair)
            Image_Base = merge_hair_body(Image_Base,Image_Hair)
        else:
            Image_Base = get_body_image(Image_Base)

    elif (NFT_Base == 'Eve Blonde.png'):
        
        if(NFT_Head == 'Dark Cap.png' or NFT_Head == 'Light Cap.png' or NFT_Head == 'Brainrot.png' or NFT_Head == 'Gunner.png' or NFT_Head == 'Maleficent.png' or NFT_Head == 'Oxen.png'):
            Image_Hair = f'{input_path}/2.1.hair/Blonde Cap Hair.png'
            Image_Base = f'{input_path}/2.base/Bald Eve.png'
            Image_Base = merge_hair_body(Image_Base,Image_Hair)

        elif (NFT_Head == 'Diadem.png' or NFT_Head == 'Crucify.png'):
            Image_Hair = f'{input_path}/2.1.hair/Blonde Coronet Hair.png'
            Image_Base = f'{input_path}/2.base/Bald Eve.png'
            print (Image_Hair)
            Image_Base = merge_hair_body(Image_Base,Image_Hair)

        elif (NFT_Head == 'Coronet.png'):
            Image_Hair = f'{input_path}/2.1.hair/Blonde Coronet Hair.png'
            Image_Base = f'{input_path}/2.base/Bald Eve.png'
            print (Image_Hair)
            Image_Base = merge_hair_body(Image_Base,Image_Hair)
        else:
            Image_Base = get_body_image(Image_Base)

    elif (NFT_Base == 'Short Eve.png'):
        
        if (NFT_Head == 'Dark Cap.png' or NFT_Head == 'Light Cap.png' or NFT_Head == 'Brainrot.png' or NFT_Head == 'Gunner.png' or NFT_Head == 'Maleficent.png' or NFT_Head == 'Oxen.png'):
            Image_Hair = f'{input_path}Bridged_Traits_Eve/2.1.hair/Short Cap Hair.png'
            Image_Base = f'{input_path}Bridged_Traits_Eve/2.base/Bald Eve.png'
            Image_Base = merge_hair_body(Image_Base,Image_Hair)

        elif ((NFT_Head == 'Diadem.png' or NFT_Head == 'Crucify.png')):
            Image_Hair = f'{input_path}Bridged_Traits_Eve/2.1.hair/Short Coronet Hair.png'
            Image_Base = f'{input_path}Bridged_Traits_Eve/2.base/Bald Eve.png'
            print (Image_Hair)
            Image_Base = merge_hair_body(Image_Base,Image_Hair)

        elif (NFT_Head == 'Coronet.png'):
            Image_Hair = f'{input_path}Bridged_Traits_Eve/2.1.hair/Short Crown Hair.png'
            Image_Base = f'{input_path}Bridged_Traits_Eve/2.base/Bald Eve.png'
            print (Image_Hair)
            Image_Base = merge_hair_body(Image_Base,Image_Hair) 
        else:
            Image_Base = get_body_image(Image_Base)
    else:
        Image_Base = get_body_image(Image_Base)

    
    return Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet, Image_Symbol


def get_NFT_main (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):
    
     BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
     Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

     int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

     Back_Image = Image.open(Image_Back).convert("RGBA")

     int1 = Image.alpha_composite(int0, Back_Image)
    
     Base_Image = Image_Base

     int2 = Image.alpha_composite(int1, Base_Image)

     Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
     int3 = Image.alpha_composite(int2, Torso_Image)

     Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
     int4 = Image.alpha_composite(int3, Mouth_Image)
    
        
     Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
     int5 = Image.alpha_composite(int4, Eyes_Image)

     Head_Image = Image.open(Image_Head).convert("RGBA")
    
     int6 = Image.alpha_composite(int5, Head_Image)
    
     Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
     final = Image.alpha_composite(int6, Helmet_Image)

     return final


def get_NFT_circlet (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):
    
    BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
    Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

    int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

    Back_Image = Image.open(Image_Back).convert("RGBA")

    int1 = Image.alpha_composite(int0, Back_Image)
    
    Base_Image = Image_Base

    int2 = Image.alpha_composite(int1, Base_Image)

    Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
    int3 = Image.alpha_composite(int2, Torso_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Mouth_Image)
    
    Head_Image = Image.open(Image_Head).convert("RGBA")
     
    int5 = Image.alpha_composite(int4, Head_Image) 
    
    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
    int6 = Image.alpha_composite(int5, Eyes_Image)

    
    Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
    final = Image.alpha_composite(int6, Helmet_Image)

    return final

def get_NFT_eyes (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):
    
    BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
    Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

    int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

    Back_Image = Image.open(Image_Back).convert("RGBA")

    int1 = Image.alpha_composite(int0, Back_Image)
    
    Base_Image = Image_Base

    int2 = Image.alpha_composite(int1, Base_Image)


    Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
    int3 = Image.alpha_composite(int2, Torso_Image)

    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
        
    int4 = Image.alpha_composite(int3, Eyes_Image)

    Head_Image = Image.open(Image_Head).convert("RGBA")
     
    int5 = Image.alpha_composite(int4, Head_Image) 
    
    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int6 = Image.alpha_composite(int5, Mouth_Image)
    
    Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
    final = Image.alpha_composite(int6, Helmet_Image)

    return final

def get_NFT_mouth_over (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):
    
    BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
    Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

    int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

    Back_Image = Image.open(Image_Back).convert("RGBA")

    int1 = Image.alpha_composite(int0, Back_Image)
    
    Base_Image = Image_Base

    int2 = Image.alpha_composite(int1, Base_Image)

    Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
    int3 = Image.alpha_composite(int2, Torso_Image)

    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Eyes_Image)
    
    Head_Image = Image.open(Image_Head).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, Head_Image)
    
    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int6 = Image.alpha_composite(int5, Mouth_Image)

    Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
    final = Image.alpha_composite(int6, Helmet_Image)

    return final

def get_NFT_eyes_over_head (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):
    
    BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
    Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

    int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

    Back_Image = Image.open(Image_Back).convert("RGBA")

    int1 = Image.alpha_composite(int0, Back_Image)
    
    Base_Image = Image_Base

    int2 = Image.alpha_composite(int1, Base_Image)

    Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
    int3 = Image.alpha_composite(int2, Torso_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Mouth_Image)
    
    Head_Image = Image.open(Image_Head).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, Head_Image)
        
    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
    int6 = Image.alpha_composite(int5, Eyes_Image)

    Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
    final = Image.alpha_composite(int6, Helmet_Image)

    return final


def get_NFT_dusa (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):
     
     BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
     Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

     int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

     Back_Image = Image.open(Image_Back).convert("RGBA")

     int1 = Image.alpha_composite(int0, Back_Image)
    

     Base_Image = Image_Base

     int2 = Image.alpha_composite(int1, Base_Image)

     Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
     int3 = Image.alpha_composite(int2, Mouth_Image)
    
        
     Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
     int4 = Image.alpha_composite(int3, Eyes_Image)

    
     Head_Image = Image.open(Image_Head).convert("RGBA")
    
     int5 = Image.alpha_composite(int4, Head_Image)

     Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
     int6 = Image.alpha_composite(int5, Torso_Image)
    
     Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
     final = Image.alpha_composite(int6, Helmet_Image)

     return final


def get_NFT_main_special (Image_BackGround, Image_Back, Image_Base, Image_Hair, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol):

    BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    
    Symbol_Image = Image.open(Image_Symbol).convert("RGBA")

    int0 = Image.alpha_composite(BackGround_Image, Symbol_Image)

    Back_Image = Image.open(Image_Back).convert("RGBA")

    int1 = Image.alpha_composite(int0, Back_Image)
    
    Base_Image = Image_Base

    int2 = Image.alpha_composite(int1, Base_Image)

    Torso_Image = Image.open(Image_Torso).convert("RGBA")
    
    int3 = Image.alpha_composite(int2, Torso_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Mouth_Image)

    Hair_Image = Image.open(Image_Hair).convert("RGBA")   

    int5 = Image.alpha_composite(int4, Hair_Image)
    
    Head_Image = Image.open(Image_Head).convert("RGBA") 
    
    int6 = Image.alpha_composite(int5, Head_Image)
        
    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
    int7 = Image.alpha_composite(int6, Eyes_Image)

    Helmet_Image = Image.open(Image_Helmet).convert("RGBA")
    
    final = Image.alpha_composite(int7, Helmet_Image)

    return final


if __name__ == '__main__':
    
    base_name = Get_Working_Base()
    
    current_dir = Path(__file__).parent

    base_dir = current_dir.parent

    input_path = base_dir/rf'traits/Bridged_Traits_{base_name}'
    output_path = base_dir / base_name 
    
    output_path.mkdir(parents=True, exist_ok=True)

    BackGrounds, Back, Base, Torso, Eyes, Mouth, Head, Helmet, Symbol = Get_Layers (base_name)

    BackGrounds_Rarity, Back_Rarity, Base_Rarity, Torso_Rarity, Head_Rarity, Eyes_Rarity, Mouth_Rarity, Helmet_Rarity, Symbol_Rarity = Get_Rarities(base_name)

    ## control
    ADN_list = []
    ## control
    
    i = 1
    while (i<1001):
        
        
        NFT_BackGround, NFT_Back, NFT_Base, NFT_Torso, NFT_Head, NFT_Eyes, NFT_Mouth, NFT_Helmet, NFT_Symbol = NFT_First_Iteration (BackGrounds,BackGrounds_Rarity,Back,Back_Rarity,Base,Base_Rarity,Torso,Torso_Rarity,Head,Head_Rarity,Eyes, Eyes_Rarity,Mouth,Mouth_Rarity,Helmet,Helmet_Rarity, Symbol, Symbol_Rarity)

    #conflicts
        
        if (NFT_Head == 'Sombrero.png'):
            NFT_Eyes = 'none.png'
        
        ##Mouth Conflicts

        NFT_Head, NFT_Eyes, excluded_traits = Mouth_Conflicts (NFT_Mouth, NFT_Head,NFT_Eyes) 
        
        # ##Eyes conflicts
        NFT_Head, NFT_Eyes = Eyes_Conflicts (NFT_Eyes,NFT_Head,excluded_traits,base_name)
        
        ## torso conflicts
        if ((NFT_Mouth == 'Bandana I.png' or NFT_Mouth == 'Bandana II.png') and (base_name == 'Lucifer' or base_name == 'Titus')):
            
            Torso_Pop = Torso
            Torso_Rarity_Pop = Torso_Rarity
            NFT_Torso = torso_conflicts (base_name,Torso_Pop,Torso_Rarity_Pop)
                        
            BackGrounds, Back, Base, Torso, Eyes, Mouth, Head, Helmet, Symbol = Get_Layers (base_name)
            BackGrounds_Rarity, Back_Rarity, Base_Rarity, Torso_Rarity, Head_Rarity, Eyes_Rarity, Mouth_Rarity, Helmet_Rarity, Symbol_Rarity = Get_Rarities(base_name)

        ## hair conflocts
        if (NFT_Helmet.split('.')[0] != 'None'):
            NFT_Head = 'none.png'
            NFT_Eyes = 'none.png'
            NFT_Mouth = 'none.png'    

        ##others
        if (NFT_Helmet.split('.')[0] != 'None'):
            NFT_Head = 'none.png'
            NFT_Eyes = 'none.png'
            NFT_Mouth = 'none.png'

        elif (NFT_Head == 'HydraX.png' or NFT_Head == 'Hydra.png' or
            NFT_Head == 'ScyllaX.png' or NFT_Head == 'Gunner.png'):
            NFT_Eyes = 'none.png'
       
        
        if (NFT_Head == 'Oxen.png' and (NFT_Mouth != 'Bandana I.png' or NFT_Mouth != 'Bandana II.png')):
            NFT_Mouth = 'none.png'

        ## control
        ADN_List, control = control_ADN(ADN_list,NFT_BackGround,NFT_Back,NFT_Base,NFT_Torso,NFT_Eyes,NFT_Mouth,NFT_Head,NFT_Helmet, NFT_Symbol)    
        ## control

        ##import images
        try:
            Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet, Image_Symbol = get_Images (base_name,NFT_BackGround,NFT_Back, NFT_Base, NFT_Torso, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Helmet,NFT_Symbol)
        except:
            continue
        
        ##image layering
            
        if ((NFT_Mouth == 'Bandana I.png' or 'Bandana II.png')  and
            (NFT_Head == 'Hydra.png' or NFT_Head == 'Scylla.png' or NFT_Head == 'ScyllaX.png' or NFT_Head == 'HydraX.png' or NFT_Head == 'Brainrot.png' or NFT_Eyes == 'Vizor.png' or NFT_Eyes == 'Crest.png' or NFT_Eyes == 'Psych.png' or NFT_Eyes == 'Graze.png')):
            
            final = get_NFT_mouth_over (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)
            
        elif (NFT_Mouth != 'Seal.png' and (NFT_Head == 'ScyllaX.png' or NFT_Head == 'HydraX.png')):
              
            final = get_NFT_mouth_over (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)
            
        elif (NFT_Eyes == 'Seethe.png' or NFT_Eyes == 'Temper.png' or NFT_Eyes == 'Scratch.png' or NFT_Eyes == 'Stripe.png'
            or ((NFT_Mouth == 'Bandana I.png' or NFT_Mouth == 'Bandana II.png' or NFT_Mouth == 'Seal.png') and (NFT_Eyes == 'Seethe.png' or NFT_Eyes == 'Temper.png' or NFT_Eyes == 'Scratch.png'))):
                
            final = get_NFT_eyes (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)

        elif (NFT_Mouth == 'Lockjaw.png' or NFT_Mouth == 'Bandana I.png' or NFT_Mouth == 'Bandana II.png' or NFT_Mouth == 'Lounge.png'):
                
            final = get_NFT_mouth_over (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)
                
        elif (NFT_Eyes == 'Circlet.png'):
                
            final = get_NFT_circlet (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)
            
        elif (NFT_Eyes == 'Hovergraph.png'):
            
            final = get_NFT_eyes_over_head (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)

        elif (NFT_Head == 'Dusa Black.png' or NFT_Head == 'Dusa Black Guard.png' or NFT_Head == 'Dusa Gold.png' or NFT_Head == 'Dusa Gold Guard.png' or NFT_Head == 'Dusa Silver.png' or NFT_Head == 'Dusa Silver Guard.png'):

            final = get_NFT_dusa (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)

        else:
            
            final = get_NFT_main (Image_BackGround, Image_Back, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_Head, Image_Helmet,Image_Symbol)    

        final.save (f'{output_path}/{base_name} #{i}.png')

        print (f'{base_name} #{i}')
        
        i+=1
       