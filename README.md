# pdftoaudiobook
# Conversor de PDF para Áudio

Este é um programa simples em Python que extrai o texto de um arquivo PDF e converte-o em narração de áudio.

## Instalação

1. Certifique-se de ter o Python 3 instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org).

2. Clone este repositório para o seu computador ou faça o download do arquivo ZIP e extraia-o.

3. Abra um terminal/prompt de comando e navegue até o diretório do projeto.

4. Execute o seguinte comando para instalar as dependências necessárias:


Isso irá instalar as bibliotecas `pdfplumber` e `pyttsx3`.

## Como usar

1. Coloque o arquivo PDF que deseja converter em um diretório acessível.

2. Abra o arquivo `convert_pdf_to_audio.py` em um editor de texto.

3. No início do arquivo, defina o caminho do PDF que deseja converter, alterando a variável `pdf_path`.

4. Execute o seguinte comando no terminal/prompt de comando:


O programa irá extrair o texto do PDF e gerar um arquivo de áudio no mesmo diretório do PDF.

5. Após a execução, você poderá encontrar o arquivo de áudio com o nome `meu_livro.mp3` (ou o nome que você especificou) no mesmo diretório do PDF.

## Personalização

- Você pode alterar a voz usada para a narração modificando o parâmetro `voice` na função `convert_text_to_speech()` no arquivo `convert_pdf_to_audio.py`. Consulte a documentação do `pyttsx3` para obter a lista de vozes disponíveis.

- Sinta-se à vontade para personalizar o programa de acordo com suas necessidades. Você pode adicionar mais funcionalidades, como reconhecimento de idioma, pausas na narração, entre outros.

## Dependências

- Python 3
- pdfplumber
- pyttsx3

## Licença

Este programa está licenciado sob a [MIT License](LICENSE).
