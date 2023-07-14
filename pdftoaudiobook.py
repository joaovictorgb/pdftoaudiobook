import pdfplumber
import pyttsx3
import os

def extract_text_from_pdf(pdf_path):
    # Abrir o arquivo PDF
    with pdfplumber.open(pdf_path) as pdf:
        progress = 0
        text = ""  # Variável para armazenar o texto acumulado
        for page in pdf.pages:
            # Extrair o texto da página
            text += page.extract_text()

            # Mostrar a barra de progresso
            progress += 1
            print(f"Extraindo texto da página {progress} de {len(pdf.pages)} páginas.")

    # Fechar o arquivo PDF
    pdf.close()
    
    return text

def convert_text_to_speech(text, audio_file, voice="Brazilian Male"):
    # Inicializar a engine de síntese de voz
    speaker = pyttsx3.init()
    speaker.setProperty("voice", voice)
    speaker.setProperty("quality", 1)

    # Salvar a narração no arquivo de áudio
    speaker.save_to_file(text, audio_file)
    speaker.runAndWait()

if __name__ == "__main__":
    # Definir o caminho do PDF exemplo
    pdf_path = "C:/Users/joaov/Downloads/livro/OPMaudiobook.pdf"

    # Criar um arquivo de áudio
    audio_file = os.path.join(os.path.dirname(pdf_path), "meu_livro.mp3")

    # Extrair texto do PDF
    text = extract_text_from_pdf(pdf_path)

    # Converter texto em narração
    convert_text_to_speech(text, audio_file, voice="Brazilian Male")
