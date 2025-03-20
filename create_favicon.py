from PIL import Image, ImageDraw, ImageFont
import os

# Créer une image 32x32 pixels (taille standard pour favicon)
img = Image.new('RGB', (32, 32), color='#2c3e50')
d = ImageDraw.Draw(img)

# Dessiner les initiales
d.text((16, 16), "SB", fill='white', anchor="mm", font=None)

# Créer le dossier assets/img s'il n'existe pas
os.makedirs('assets/img', exist_ok=True)

# Sauvegarder l'image
img.save('assets/img/favicon.png')
