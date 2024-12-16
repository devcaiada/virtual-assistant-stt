import pyttsx3
import speech_recognition as sr
import webbrowser
import requests

def text_to_speech(text):
    """Converte texto em fala"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    """Converte fala em texto"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text_to_speech("Estou ouvindo...")
        print("Diga algo: ")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {command}")
            return command.lower()
        except sr.UnknownValueError:
            text_to_speech("Desculpe, não entendi.")
            return None
        except sr.RequestError as e:
            text_to_speech("Erro ao conectar ao serviço de reconhecimento de fala.")
            print(f"Erro: {e}")
            return None

def search_wikipedia(query):
    """Realiza uma busca no Wikipedia"""
    url = f"https://pt.wikipedia.org/wiki/{query.replace(' ', '_')}"
    webbrowser.open(url)
    text_to_speech(f"Aqui está o resultado para {query} no Wikipedia.")

def open_youtube():
    """Abre o YouTube"""
    webbrowser.open("https://www.youtube.com")
    text_to_speech("Abrindo o YouTube.")

def find_nearest_pharmacy():
    """Localiza a farmácia mais próxima (exemplo utilizando Google Maps)"""
    url = "https://www.google.com/maps/search/farmácia+próxima/"
    webbrowser.open(url)
    text_to_speech("Aqui está a farmácia mais próxima.")

def process_command(command):
    """Processa o comando de voz e aciona as funções correspondentes"""
    if "wikipedia" in command:
        text_to_speech("Qual termo deseja buscar no Wikipedia?")
        term = speech_to_text()
        if term:
            search_wikipedia(term)
    elif "youtube" in command:
        open_youtube()
    elif "farmácia" in command:
        find_nearest_pharmacy()
    else:
        text_to_speech("Comando não reconhecido. Tente novamente.")

def main():
    text_to_speech("Olá, sou seu assistente virtual. Como posso ajudar?")
    while True:
        command = speech_to_text()
        if command:
            if "sair" in command:
                text_to_speech("Encerrando o assistente. Até logo!")
                break
            process_command(command)

if __name__ == "__main__":
    main()
