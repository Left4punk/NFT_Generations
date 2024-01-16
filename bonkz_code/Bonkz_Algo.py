from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import random
from PIL import Image
import shutil
import time

st = time.time()

number_of_ones = 93
collection_number = 15001
position_list = random.sample(range(1, collection_number), number_of_ones)
position_list.sort()
whole_json = []


##storing 1/1 paths to generate them
one_NFTs = [f for f in listdir("Bonk/- 1-1s") if isfile(join("Bonk/- 1-1s", f))]
random.shuffle(one_NFTs)


# def Get_Layers() for all pngs
BackGrounds = [f for f in listdir("Bonk/0.Background") if isfile(join("Bonk/0.Background", f))]
Aura_Back = [f for f in listdir("Bonk/1.Aura/Back") if isfile(join("Bonk/1.Aura/Back", f))]
Aura_Front = [f for f in listdir("Bonk/1.Aura/Front") if isfile(join("Bonk/1.Aura/Front", f))]
Hand_Charcoal = [f for f in listdir("Bonk/2.Hand/Hand charcoal") if isfile(join("Bonk/2.Hand/Hand charcoal", f))]
Hand_Shib = [f for f in listdir("Bonk/2.Hand/Hand shib") if isfile(join("Bonk/2.Hand/Hand shib", f))]
Hand_Solana = [f for f in listdir("Bonk/2.Hand/Hand solana") if isfile(join("Bonk/2.Hand/Hand solana", f))]
Base = [f for f in listdir("Bonk/3.Base") if isfile(join("Bonk/3.Base", f))]
Expression = [f for f in listdir("Bonk/4.Expression") if isfile(join("Bonk/4.Expression", f))]
Clothing = [f for f in listdir("Bonk/5.Clothing") if isfile(join("Bonk/5.Clothing", f))]
HeadWear = [f for f in listdir("Bonk/6.Head") if isfile(join("Bonk/6.Head", f))]
FaceWear = [f for f in listdir("Bonk/7.Face") if isfile(join("Bonk/7.Face", f))]



# ##Rarities
BackGrounds_Rarity = [13,12,10,10,12,12,4,9,5,13]
Aura_Back_Rarity = [1,1,97,1]
Hand_Charcoal_Rarity=[1.5,3.5,2,2,1.5,1.75,2,0.5,1.25,0.75,0.75,1.5,1.25,2,2,1,0.75,2.5,2.5,50.75,2,2,1.5,1,1,2.5,2,2.25,2,2]
Hand_Shib_Rarity=[1.5,3.5,2,2,1.5,1.75,2,0.5,1.25,0.75,0.75,1.5,1.25,2,2,1,0.75,2.5,2.5,50.75,2,2,1.5,1,1,2.5,2,2.25,2,2]

Hand_Solana_Rarity=[1.5,3.5,2,2,1.5,1.75,2,0.5,1.25,0.75,0.75,1.5,1.25,2,2,1,0.75,2.5,2.5,50.75,2,2,1.5,1,1,2.5,2,2.25,2,2]
Base_Rarity = [7,92,1]
Expression_Rarity = [10,2,5,1.5,4,4,1,12,1,14,7,4,10.5,5,15,4]
Clothing_Rarity = [3,2,4,1.5,2.5,1.5,1.5,2,2,1,0.5,4,2.5,4,2.5,1,1.5,5,1.5,1,3,1,0.5,3,3,3,3,3,2,1.5,2,3,4,4,3,4,3,2.5,2,2.5,2.5]
Head_Rarity = [1.5,2,3,3,3,2,2,0.75,3,3,0.5,2,1,2.5,2.5,3,1.5,0.5,1.5,48.25,0.5,0.5,2.5,1.5,0.5,2,0.5,2,3.5]
Face_Rarity = [3.5,3,2,2.5,72.75,0.5,3,3.5,1.25,2,3,3]
### importing rarity table #####
df = pd.DataFrame(columns = ["Background","Aura","Base","Hand","Expression","Clothing","Headwear","Facewear"])


##trait generation
for i in range(1,collection_number):
    ##indexing random 1/1s on the whole generation
    if (len(position_list)!=0 and i == position_list[0]):
        
        NFT_Name = one_NFTs[0]
        NFT_Format = NFT_Name.split('.')[1]
        if (NFT_Format == 'png' or NFT_Format == 'jpg_medium' or NFT_Format == 'jpg' or NFT_Format == 'jpeg' or NFT_Format == 'jpg_large' or NFT_Format == 'PNG'):
            One_On_One_NFT_Image = 'Bonk/- 1-1s/'+one_NFTs[0]
        
            NFT_One_On_One = Image.open(One_On_One_NFT_Image).convert("RGBA")

            NFT_One_On_One.save (f'Bonkz_Collection/{i}.png')
            
        elif (NFT_Format == 'gif'):
            shutil.copy('Bonk/- 1-1s/'+one_NFTs[0], f'Bonkz_Collection/{i}'+'.'+NFT_Format)
            
        metadata = {'name':f'BONKz #{i}',
                    'symbol':'BONKz',
                    'description':'BONKz',
                    'seller_fee_basis_points': 200,
                    'image':f'{i}.'+NFT_Format,
                    'attributes':[
                        {
                            'trait_type':'Background',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Aura',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Hand',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Base',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Expression',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Clothing',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Head',
                            'value':'1/1'
                        },
                        {
                            'trait_type':'Facewear',
                            'value':'1/1'
                        },
                        {   'trait_type':'1/1',
                             'value': NFT_Name.split('.')[0]
                            }],
                    'properties':{
                        'files':[
                            {
                                'uri':f'{i}.'+NFT_Format,
                                'type':'image/'+NFT_Format}
                            ],
                        'category':'image',
                        'creators':[
                            {
                                'address':'GkYZr19qj2pLEzWy1kghbvaTTWLen2TGcJm1f8K63PtP',
                                'share':100
                            }
                        ]
                        }
                    
                    
     
        }
        json_out = open(f'Bonkz_Collection/{i}.json','w')
        json.dump(metadata, json_out, indent=4)
        json_out.close()
        whole_json.append(metadata)
        position_list.pop(0)
        one_NFTs.pop(0)
        print (f'Bonk_#{i} - 1/1')
        continue
    
    
    ##ensure that we take all after any if
    Expression = [f for f in listdir("Bonk/4.Expression") if isfile(join("Bonk/4.Expression", f))]
    FaceWear = [f for f in listdir("Bonk/7.Face") if isfile(join("Bonk/7.Face", f))]
    HeadWear = [f for f in listdir("Bonk/6.Head") if isfile(join("Bonk/6.Head", f))]
    
    
    NFT_BackGround = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Aura = random.choices(Aura_Back,weights=(Aura_Back_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]

    # print (NFT_Base)
    if NFT_Base == 'shib.png':
        NFT_Hand = random.choices(Hand_Shib,weights=(Hand_Shib_Rarity))[0]
    elif NFT_Base == 'solana.png':
        NFT_Hand = random.choices(Hand_Solana,weights=(Hand_Solana_Rarity))[0]
    elif NFT_Base == 'charcoal.png':
        NFT_Hand = random.choices(Hand_Charcoal,weights=(Hand_Charcoal_Rarity))[0]

    NFT_Expression = random.choices(Expression,weights=(Expression_Rarity))[0]
    NFT_Clothing = random.choices(Clothing,weights=(Clothing_Rarity))[0]
    NFT_HeadWear = random.choices(HeadWear,weights=(Head_Rarity))[0]
    NFT_FaceWear = random.choices(FaceWear,weights=(Face_Rarity))[0]
    
    ## conditions
    
    ##background
    if NFT_BackGround.split('.')[0] == 'binary':
        NFT_Aura = 'none.png'
    ##hand    
    if (NFT_Hand.split('.')[0] == 'champagne' or
        NFT_Hand.split('.')[0] == 'cigar' or
        NFT_Hand.split('.')[0] == 'coffee' or
        NFT_Hand.split('.')[0] == 'inflateable' or
        NFT_Hand.split('.')[0] == 'iphone' or
        NFT_Hand.split('.')[0] == 'mug' or
        NFT_Hand.split('.')[0] == 'pokeball' or
        NFT_Hand.split('.')[0] == 'spatula' or
        NFT_Hand.split('.')[0] == 'tea' or
        NFT_Hand.split('.')[0] == 'wand' or
        NFT_Hand.split('.')[0] == 'whiskey' or
        NFT_Hand.split('.')[0] == 'wine'):
        NFT_Expression = random.choices(['eyes.png','mask.png','mindblown.png','pain.png','red eye.png','shock.png','smile.png','smug.png','straight.png','suspicious.png','tongue.png'],(10,5,2,4,1.5,12,14,7,10.5,5,15))[0]
    
    elif NFT_Hand.split('.')[0] == 'joint':
        NFT_Expression = random.choices(['eyes.png','mindblown.png','pain.png','red eye.png','shock.png','smile.png','smug.png','straight.png','suspicious.png','tongue.png'],(10,5,4,1,12,14,7,10.5,5,15))[0]

    elif NFT_Hand.split('.')[0] == 'balloon':
        NFT_HeadWear = random.choices([ 'admiral.png','backwards cap black.png','backwards cap white.png','beanie.png','bowler.png','cap.png','fedora.png','fisherman beanie.png','flame.png','flower.png','halo.png','hat.png','headband.png','headphones.png','horns.png','indian headdress.png','mc bonk.png','regal.png','samauri.png','sherif.png','solana cap.png','sombrero.png','spongebob.png','super saiyan.png','sweatband.png','trucker.png','none.png'],weights=(2,3,3,3,2,2,3,3,0.5,2,1,2.5,2.5,3,1.5,0.5,1.5,0.5,0.5,2.5,1.5,0.5,2,0.5,2,3.5,46))[0]
   
    elif (NFT_Hand.split('.')[0] == 'cell phone' or NFT_Hand.split('.')[0] == 'phone'):
        NFT_HeadWear = random.choices(['!!!.png','admiral.png','backwards cap black.png','backwards cap white.png','beanie.png','bowler.png','cap.png','fedora.png','fisherman beanie.png','flame.png','flower.png','halo.png','hat.png','headband.png','horns.png','indian headdress.png','mc bonk.png','regal.png','samauri.png','sherif.png','solana cap.png','sombrero.png','spongebob.png','super saiyan.png','sweatband.png','trucker.png','none.png','crown.png'],weights=(1.5,2,3,3,3,2,2,3,3,0.5,2,1,2.5,2.5,1.5,0.5,1.5,0.5,0.5,2.5,1.5,0.5,2,0.5,2,3.5,46,0.5))[0]
        NFT_Expression = random.choices(['eyes.png','mindblown.png','mask.png','red eye.png','onyx.png','pain.png','shock.png','shoop da woop.png','smile.png','smug.png','straight.png','suspicious.png','tongue.png'],weights=(10,7,2,1,2,7,12,1,12,7,8,7,12))[0]
    
    elif (NFT_Hand.split('.')[0] == 'wand'):
        NFT_Expression = random.choices(['eyes.png,mindblown.png','mask.png','red eye.png','onyx.png','pain.png','shock.png','smile.png','smug.png','straight.png','suspicious.png','tongue.png'],weights=(10,5,2,1,1.5,4,12,14,7,10.5,5,15))[0]
    elif (NFT_Hand.split('.')[0] == 'infinity gauntlet' or NFT_Hand.split('.')[0] == 'newspaper'):
        NFT_Expression = random.choices(['eyes.png','mindblown.png','mask.png','red eye.png','onyx.png','pain.png','shock.png','shoop da woop.png','smile.png','smug.png','stick.png','straight.png','suspicious.png','tongue.png','treat.png'],weights=(10,7,2,1,2,7,12,1,12,7,4,8,7,12,4))[0]
    
    # print (NFT_BackGround+','+NFT_Aura+','+NFT_Base+','+NFT_Expression+','+NFT_Clothing+','+NFT_HeadWear+','+NFT_FaceWear)
    
    ##expression
    if NFT_Expression.split('.')[0] == 'onyx':
        NFT_FaceWear = 'none.png'
        NFT_HeadWear = random.choices(['!!!.png','admiral.png','backwards cap black.png','backwards cap white.png','beanie.png','bowler.png','cap.png','crown.png','fedora.png','fisherman beanie.png','flame.png','flower.png','halo.png','hat.png','headband.png','headphones.png','horns.png','indian headdress.png','mc bonk.png','regal.png','sherif.png','solana cap.png','sombrero.png','spongebob.png','super saiyan.png','sweatband.png','trucker.png','none.png'],(2,2,3,3,3,2,2,0.75,3,3,0.5,2,1,2.5,2.5,3,1.5,0.5,1.5,0.5,2.5,1.5,0.5,2,0.5,2,3.5,48.25))[0]
    elif NFT_Expression.split('.')[0] == 'mask':
        NFT_HeadWear = random.choices(['!!!.png','admiral.png','backwards cap black.png','backwards cap white.png','beanie.png','bowler.png','cap.png','crown.png','fedora.png','fisherman beanie.png','flame.png','flower.png','halo.png','hat.png','headband.png','headphones.png','horns.png','indian headdress.png','mc bonk.png','regal.png','sherif.png','solana cap.png','sombrero.png','spongebob.png','super saiyan.png','sweatband.png','trucker.png','none.png'],(2,2,3,3,3,2,2,0.75,3,3,0.5,2,1,2.5,2.5,3,1.5,0.5,1.5,0.5,2.5,1.5,0.5,2,0.5,2,3.5,48.25))[0] 
    ##head
    if (NFT_HeadWear.split('.')[0] == 'fisherman beanie' or NFT_HeadWear.split('.')[0] == 'trucker'):
        NFT_FaceWear = 'none.png'
    
    elif NFT_HeadWear.split('.')[0] == 'flower':
        NFT_FaceWear = random.choices(['round sunglasses.png','thug life.png','none.png'],(3.5,3,72.2))[0]
    
    elif NFT_HeadWear.split('.')[0] == 'hat':
        NFT_FaceWear = random.choices(['clubmaster.png','goggles.png','gold sunglasses.png','pixel shades.png','monocle.png','round sunglasses.png','ski goggles.png','thug life.png','none.png'],(3,3,2,3,3,3,3,2,69.5))[0]
    
    elif NFT_HeadWear.split('.')[0] == 'headphones':
        NFT_FaceWear = random.choices(['round sunglasses.png','thug life.png','none.png'],(3.5,3,72.25))[0]
    
    elif NFT_HeadWear.split('.')[0] == 'indian headdress':
        NFT_FaceWear = random.choices(['thug life.png','none.png'],(3,72.25))[0]
    
    elif (NFT_HeadWear.split('.')[0] == 'samauri' or NFT_HeadWear.split('.')[0] == 'super saiyan' or NFT_HeadWear.split('.')[0] == 'sombrero'):
        NFT_FaceWear = 'none.png'
    
    
    ##import images
    Image_BackGround = 'Bonk/0.Background/'+NFT_BackGround
    Image_Aura_Back = 'Bonk/1.Aura/Back/'+NFT_Aura
    Image_Aura_Front = 'Bonk/1.Aura/Front/'+NFT_Aura

  
    if NFT_Base == 'shib.png':
        Image_Hand = 'Bonk/2.Hand/Hand shib/'+NFT_Hand
    elif NFT_Base == 'solana.png':
        Image_Hand = 'Bonk/2.Hand/Hand solana/'+NFT_Hand
    elif NFT_Base == 'charcoal.png':
        Image_Hand = 'Bonk/2.Hand/Hand charcoal/'+NFT_Hand

    Image_Base = 'Bonk/3.Base/'+NFT_Base
    Image_Expression = 'Bonk/4.Expression/'+NFT_Expression
    Image_Clothing = 'Bonk/5.Clothing/'+NFT_Clothing
    Image_HeadWear = 'Bonk/6.Head/'+NFT_HeadWear
    Image_FaceWear = 'Bonk/7.Face/'+NFT_FaceWear
  
    
    ##image generation
    BackGround_Image = Image.open(Image_BackGround).convert("RGBA")
    Aura_Back_Image = Image.open(Image_Aura_Back).convert("RGBA")


    int1 = Image.alpha_composite(BackGround_Image, Aura_Back_Image)
    

    
    ##adding condition for base in front of hand
    ## if hand = the following then layering is background aura base expression clothing hand 
    if (NFT_Hand == 'champagne.png' or NFT_Hand == 'coffee.png' or NFT_Hand == 'tea.png'  or NFT_Hand == 'infinity gauntlet.png'  or NFT_Hand == 'inflateable.png' 
    or NFT_Hand == 'iphone.png'  or NFT_Hand == 'newspaper.png'  or NFT_Hand == 'spatula.png' or NFT_Hand == 'mug.png'  or NFT_Hand == 'wand.png' 
    or NFT_Hand == 'wine.png'):
        
        Base_Image = Image.open(Image_Base).convert("RGBA")

        int2 = Image.alpha_composite(int1, Base_Image)

        ##adding condition for expression = mask, if mask then clothing goes first
        if (NFT_Expression != 'mask.png'):    
            Expression_Image = Image.open(Image_Expression).convert("RGBA")
            int3 = Image.alpha_composite(int2, Expression_Image)

            Clothing_Image = Image.open(Image_Clothing).convert("RGBA")
            int4 = Image.alpha_composite(int3, Clothing_Image)
        else:
            Clothing_Image = Image.open(Image_Clothing).convert("RGBA")
            int3 = Image.alpha_composite(int2, Clothing_Image)

            Expression_Image = Image.open(Image_Expression).convert("RGBA")
            int4 = Image.alpha_composite(int3, Expression_Image)
    
        
        Hand_Image = Image.open(Image_Hand).convert("RGBA")
        int5 = Image.alpha_composite(int4, Hand_Image)

    else:
        Hand_Image = Image.open(Image_Hand).convert("RGBA")

        int2 = Image.alpha_composite(int1, Hand_Image)

        Base_Image = Image.open(Image_Base).convert("RGBA")
    
        int3 = Image.alpha_composite(int2, Base_Image)

        ##adding condition for expression = mask, if mask then clothing goes first
        if (NFT_Expression != 'mask.png'):    
            Expression_Image = Image.open(Image_Expression).convert("RGBA")
            int4 = Image.alpha_composite(int3, Expression_Image)

            Clothing_Image = Image.open(Image_Clothing).convert("RGBA")
            int5 = Image.alpha_composite(int4, Clothing_Image)
        else:
            Clothing_Image = Image.open(Image_Clothing).convert("RGBA")
            int4 = Image.alpha_composite(int3, Clothing_Image)

            Expression_Image = Image.open(Image_Expression).convert("RGBA")
            int5 = Image.alpha_composite(int4, Expression_Image)
    
    HeadWear_Image = Image.open(Image_HeadWear).convert("RGBA")

    int6 = Image.alpha_composite(int5, HeadWear_Image)

    FaceWear_Image = Image.open(Image_FaceWear).convert("RGBA")

    int7 = Image.alpha_composite(int6, FaceWear_Image)

    Aura_Front_Image = Image.open(Image_Aura_Front).convert("RGBA")
        
    final = Image.alpha_composite(int7, Aura_Front_Image)

    final.save (f'Bonkz_Collection/{i}.png')

    metadata = {'name':f'BONKz #{i}',
                'symbol':'BONKz',
                'description':'BONKz',
                'seller_fee_basis_points': 200,
                'image':f'{i}.png',
                'attributes':[
                    {
                        'trait_type':'Background',
                        'value':NFT_BackGround.split('.')[0].title()
                    },
                    {
                        'trait_type':'Aura',
                        'value':NFT_Aura.split('.')[0].title()
                    },
                    {
                        'trait_type':'Hand',
                        'value':NFT_Hand.split('.')[0].title()
                    },
                    {
                        'trait_type':'Base',
                        'value':NFT_Base.split('.')[0].title()
                    },
                    {
                        'trait_type':'Expression',
                        'value':NFT_Expression.split('.')[0].title()
                    },
                    {
                        'trait_type':'Clothing',
                        'value':NFT_Clothing.split('.')[0].title()
                    },
                    {
                        'trait_type':'Head',
                        'value':NFT_HeadWear.split('.')[0].title()
                    },
                    {
                        'trait_type':'Facewear',
                        'value':NFT_FaceWear.split('.')[0].title()
                    },
                    {   'trait_type':'1/1',
                         'value': 'None'
                        }],
                'properties':{
                    'files':[
                        {
                            'uri':f'{i}.png',
                            'type':'image/png'}
                        ],
                    'category':'image',
                    'creators':[
                        {
                            'address':'GkYZr19qj2pLEzWy1kghbvaTTWLen2TGcJm1f8K63PtP',
                            'share':100
                        }
                    ]
                    }
                
                
 
    } 
    append_df = pd.DataFrame({'Background':NFT_BackGround.split('.')[0],
                            'Aura':NFT_Aura.split('.')[0],
                            'Base':NFT_Base.split('.')[0],
                            'Hand':NFT_Hand.split('.')[0],
                            'Expression':NFT_Expression.split('.')[0],
                            'Clothing':NFT_Clothing.split('.')[0],
                            'Headwear':NFT_HeadWear.split('.')[0],
                            'Facewear':NFT_FaceWear.split('.')[0]}, index = [i])

    df = pd.concat([append_df,df])
    
    json_out = open(f'Bonkz_Collection/{i}.json','w')
    json.dump(metadata, json_out, indent=4)
    json_out.close()
    whole_json.append(metadata)
    
    print (f'Bonk_#{i}')


df.to_excel ('Bonkz_Collection/Traits/Total_Traits.xlsx', sheet_name='Sheet1')

Background_Rarities = ((df['Background'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'))
Aura_Back_Rarities = (df['Aura'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
Base_Rarities = (df['Base'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
Hand_Rarities = (df['Hand'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
Expression_Rarities = (df['Expression'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
Clothing_Rarities = (df['Clothing'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
Headwear_Rarities = (df['Headwear'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')
Facewear_Rarities = (df['Facewear'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%')



with open('Bonkz_Collection/Traits/Trait_Rarities.txt','w') as rarities_out:
    # rarities_out.write('BackGround Rarity: \n')
    # for i in len(Background_Rarities):
    #     rarities_out.write(Background_Rarities[i])
    # else:
    #     rarities_out.write('\n')
    
    rarities_out.write('Background Rarity \n'+
        Background_Rarities.to_string(header=None)+'\n'+
        'Aura Rarity \n'+
        Aura_Back_Rarities.to_string(header=None)+'\n'+
        'Base Rarity \n'+
        Base_Rarities.to_string(header=None)+'\n'+
        'Hand Rarity \n'+
        Hand_Rarities.to_string(header=None)+'\n'+
        'Expression Rarity \n'+
        Expression_Rarities.to_string(header=None)+'\n'+
        'Clothing Rarity \n'+
        Clothing_Rarities.to_string(header=None)+'\n'+
        'Headwear Rarity \n'+
        Headwear_Rarities.to_string(header=None)+'\n'+
        'Facewear Rarity \n'+
        Facewear_Rarities.to_string(header=None))

##printing proper metadata
generated_files = [f for f in listdir("Bonkz_Collection/") if isfile(join('Bonkz_Collection/', f))]
json_files =[]
for file in generated_files:
    if (file.split('.')[1] == 'json'):
        json_files.append(int(file.split('.')[0]))

json_files.sort()


with open('Bonkz_Collection/Traits/Metadata.txt', 'w') as outfile:
    for filename in json_files:
        with open('Bonkz_Collection/'+str(filename)+'.json') as infile:
            for line in infile:
                outfile.write(str(line))
            else:
                outfile.write(','+'\n')
                
    
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')