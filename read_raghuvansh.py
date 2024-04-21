IMAGE_SIZE=(512,1024)
import numpy as np 
from PIL import Image 

img = Image.fromarray(np.ones(IMAGE_SIZE, dtype=np.uint8)*255,)

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


X_SPACING = 4 
Y_SPACING = 6
font = ImageFont.truetype(r"C:\Users\Abhijit_asus\github_stuff\minuszero\Adishila\Adishila\Adishila.ttf", 16)

draw = ImageDraw.Draw(img)

START_LOCATION = [10,20]
fp = r"C:\Users\Abhijit_asus\github_stuff\minuszero\Raghuvamsa-with-commentary.txt"
fp = r"C:\Users\Abhijit_asus\github_stuff\sanskrit_ocr\small_txt.txt"
with open(fp, 'r', encoding="utf8   ") as f:
    #for i in f.readline():
    #    print(i )
    #    break
    content = f.readlines()

print(content)
text = "".join(content)
print(text)


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import pathlib 
path = pathlib.Path(r"C:\Users\Abhijit_asus\github_stuff\minuszero\Adishila\Adishila")
for font_dir in path.iterdir():
    img = Image.fromarray(np.ones((512,1024), dtype=np.uint8)*255)

    draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)

    font = ImageFont.truetype(font_dir, 32)

    draw.text((0, 0), text, color = 0,font=font)
    img.save(f'sample-out-{font_dir.stem}.jpg')

text=r"""

		प्रथमः सर्गः।
मातापितृभ्यां जगतो नमो वामार्धजानये ।
सद्यो दक्षिणदृक्पातसंकुचद्वामदृष्टये ।।
अन्तरायतिमिरोपशान्तये शान्तपावनमचिन्त्यवैभवम् ।
तं नरं वपुषि कुञ्जरं मुखे मन्महे किमपि तुन्दिलं महः ।।

"""

img = Image.fromarray(np.ones((512,1024), dtype=np.uint8)*255)

draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)

font = ImageFont.truetype(r"C:\Users\Abhijit_asus\github_stuff\sanskrit_ocr\Lohit-Devanagari.ttf", 16)

draw.text((0, 0), text, color = 0,font=font)
img.save(f'sample-out-LOHIT.jpg')
