import os

from django.conf import settings
from PIL import Image


def resize_image(img, nova_largura=800):
    """ redimenciona a imagem para o tamanho desejado """

    imagem_caminho_completo = os.path.join(settings.MEDIA_ROOT, img.name)

    img_pil = Image.open(imagem_caminho_completo)

    original_largura, original_altura = img_pil.size

    nova_altura = round((nova_largura * original_altura) / original_largura)

    nova_imagem = img_pil.resize((nova_largura, nova_altura), Image.LANCZOS)

    nova_imagem.save(
        imagem_caminho_completo,
        optimize=True,
        quality=50
    )

    img_pil.close()
    nova_imagem.close()