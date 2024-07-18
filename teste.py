import pyautogui
import time
from urllib.parse import quote
import pyperclip

# Lista de números de telefone
phone_numbers = [
    "5517997176013",
    "5517996189716",
    "5511984065166",
    "5512981259709",
    "557199054861",
    "553399149070",
    "555381199359",
    "558188407399",
    "5511974055440",
    "5511914817190",
    "5511917236771",
    "5511918554125",
    "5511932812812",
    "551193491055",
    "5511939005147",
    "5511940376689",
    "5511945439252",
    "5511950473133",
    "5511953930382",
    "5511962140164",
    "5511965069584",
    "5511966723911",
    "5511966769999",
    "5511979512749",
    "5511983991799",
    "5511987160074",
    "5511994031883",
    "5514981834056",
    "5514991960401",
    "5514997091949",
    "5514997417983",
    "5514997432941",
    "5514998976775",
    "5515998319526",
    "5516997123055",
    "5517935006565",
    "5517981992106",
    "5517991698368",
    "5517997342546",
    "5517997772539",
    "5518981335473",
    "5519971066786",
    "5519971090908",
    "5519982190640",
    "5519988539394",
    "5519992619330",
    "5519993691404",
    "551999573630",
    "5519998486106",
    "5521968472826",
    "5521971494594",
    "5521988980638",
    "5521989568763",
    "5521994213373",
    "5521995864778",
    "5522992034424",
    "5527988171526",
    "5527998504276",
    "553183734884",
    "553187310060",
    "553189622472",
    "553194362327",
    "553288127607",
    "553492457428",
    "553584764664",
    "553588894248",
    "553599385799",
    "553788149915",
    "553888067403",
    "554196338087",
    "554197367073",
    "554384469992",
    "554399041651",
    "554484088372",
    "554498038270",
    "554598356814",
    "554788515140",
    "554788730360",
    "554788883421",
    "554791029208",
    "554792083379",
    "554898083108",
    "554999333230",
    "555180313506",
    "555391933295",
    "555496464882",
    "555596277845",
    "556181818765",
    "556182781722",
    "556195586673",
    "556198501689",
    "556493198397",
    "556592250834",
    "556593536500",
    "556684123984",
    "556684258531",
    "556699822866",
    "556792424994",
    "556793221468",
    "556798033048",
    "557388584282",
    "557388628515",
    "557399325825",
    "557583447820",
    "557583552468",
    "557598018368",
    "558182175847",
    "558184673053",
    "558184822082",
    "558186010494",
    "558186844477",
    "558187691927",
    "558188131771",
    "558188408704",
    "558189219999",
    "558191416767",
    "558193346473",
    "558194086041",
    "558195936963",
    "558196055452",
    "558197224890",
    "558199284331",
    "558288697414",
    "558386554041",
    "558388031050",
    "558391257215",
    "558486029083",
    "558494019887",
    "558496297911",
    "558496513210",
    "558582347615",
    "558589251249",
    "558591349726",
    "558591629603",
    "558592606938",
    "558596489692",
    "558598679220",
    "558681296831",
    "558688645278",
    "558695972053",
    "558699672059",
    "558781634456",
    "558791296868",
    "558791509273",
    "559584257191",
    "559984358153",
    "56958064108",
    "593963165733",
    "59898515556",
    "994405391294"
]



def main():
    message = "Olá! Tudo bem? Eu vendo streaming baratas como Netflix, HBO MAX, Globo Play, Disney entre outras. Não quer dar uma olhadinha? Meu site é https://streamingdw.shop. Se quiser ver mais, meu TikTok é @codigo.criativo"
    encoded_message = quote(message)

    for phone_number in phone_numbers:
        # URL do WhatsApp com o número de telefone e mensagem codificada
        url = f"https://wa.me/{phone_number}?text={encoded_message}"

        # Copia o URL para a área de transferência
        pyperclip.copy(url)

        time.sleep(5)  # Aguarda 5 segundos antes de iniciar o próximo loop

        # Pressiona Ctrl + L para selecionar a barra de endereço do navegador
        pyautogui.hotkey('ctrl', 'l')
        # Aguarda um segundo para garantir que a barra foi selecionada
        time.sleep(1)

        # Cola o URL
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Aguarda um segundo para garantir que o URL foi colado

        # Pressiona Enter para acessar o URL
        pyautogui.press('enter')

        # Aguarda um tempo antes de ir para o próximo número
        time.sleep(5)  # Ajuste o tempo conforme necessário

        # Tenta localizar a imagem na tela
        image_location = pyautogui.locateCenterOnScreen('./img/iniciar.png')
        if image_location:
            # Clica na posição da imagem
            pyautogui.click(image_location)
        else:
            print("Imagem não encontrada na tela.")
        
        time.sleep(2)
        # Tenta localizar a imagem na tela
        image_location = pyautogui.locateCenterOnScreen('./img/usar.png')
        if image_location:
            # Clica na posição da imagem
            pyautogui.click(image_location)
        else:
            print("Imagem não encontrada na tela.")
        time.sleep(15)

        image_location = pyautogui.locateCenterOnScreen('./img/enviar.png')
        if image_location:
            # Clica na posição da imagem
            pyautogui.click(image_location)
        else:
            print("Imagem não encontrada na tela.")

if __name__ == "__main__":
    main()
