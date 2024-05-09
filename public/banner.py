from pyfiglet import Figlet
from transfer_data import Transaction

banners_with_figlet = ('ogre', 'puffy', 'rectangles', 'red_phoenix', 'rounded', 'santa_clara', 'script', 'serifcap', 'slant', 'slscript', 'small', 'small_slant', 'soft', 'speed', 'spliff', 'standard', 'straight', 'varsity', 'train', 'tinker-toy', 'sweet', 'poison', 'swamp_land', 'swan')

#* Función para imprimir distintos banners con el módulo figlet, recibe algunos parametros para aumentar la personalización
def figlet_banner(text:str = 'PROM2023-2024', color:str = "\033[93m", banner_index:int = 0, bold:bool = True, font_width:int = 140, align:str = 'center'):
    if bold:
        negrita = "\033[1m"
    else:
        negrita = ''
    
    custom_fig = Figlet(font=banners_with_figlet[banner_index], width=font_width, justify=align)
    print(f"{color}{negrita}{custom_fig.renderText(text)}{Transaction().normal_color}")
    return f"{color}{negrita}{custom_fig.renderText(text)}{Transaction().normal_color}"


# if __name__ == "__main__":
#     print(figlet_banner())