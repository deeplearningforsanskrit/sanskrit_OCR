swars = """
अ
आ
इ
ई
उ
ऊ
ऋ
ए
ऐ
ऑ
ओ
औ
अं
अः"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

vyanjans = """क
ख
ग
घ
ङ
च
छ
ज
झ
ञ
ट
ठ
ड
ढ
ण
त
थ
द
ध
न
प
फ
ब
भ
म
य
र
ल
व
श
ष
स
ह
ळ
ष"""





vowels = """ा
ि
ी
ु
ू
े
ै
ो
ौ
ं
ः
्
ॉ
ृ
ॄ
ँ
ॅ"""

"""१
२
३
४
५
६
७
८
९
०"""

expressions = """।
॥
"""

udatt_anudatt = f"""{chr(int("0951", 16))}
{chr(int("0952", 16))}
"""

jivan = ""
swars = swars.split("\n")
udatt_anudatt = udatt_anudatt.split("\n")
chars = vyanjans.split("\n")
vowels = vowels.split("\n")

import random
from tqdm import tqdm 
for j in tqdm(range(200)):
    word = random.choice(swars)


    for i in range(5000):
        word+= random.choice(chars) +  random.choice(vowels)

        if i%93==0:
            word+=" \n"

        

        if i%15==0:
            word+= " "
        elif i%5==0 and word[-1]!="\n":
            word+= udatt_anudatt[0]
        elif i%3==0 and word[-1] !='\n':
            word+= udatt_anudatt[1]



    img = Image.fromarray(np.ones((1024, 1024), dtype=np.uint8)*255)
#
    draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)

    font = ImageFont.truetype(r"/home/abhijitd/Downloads/Adishila/Adishila.ttf", 16)

    draw.text((0, 0), word, color = 0,font=font)
    img.save(f'data/sample-out_{j}.jpg')

    with open(f"data/sample_text_{j}.txt", "a+") as f:
        f.write(word)
