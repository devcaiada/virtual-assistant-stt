# Assistente Virtual em Python

Este projeto implementa um assistente virtual utilizando Processamento de Linguagem Natural (PLN). O assistente pode realizar diversas tarefas como converter texto em fala, reconhecer comandos de voz e executar ações automatizadas, como abrir sites específicos e buscar informações online.

![virtual-assistant]()

## Funcionalidades

- **Conversão de Texto para Fala (Text-to-Speech - TTS):**

  - O assistente converte texto em áudio utilizando a biblioteca `pyttsx3`.

- **Conversão de Fala para Texto (Speech-to-Text - STT):**

  - Captura comandos de voz do usuário e os converte em texto utilizando a biblioteca `SpeechRecognition`.

- **Execução de Comandos Automatizados:**

  - Busca no Wikipedia.
  - Abertura do YouTube.
  - Localização da farmácia mais próxima via Google Maps.

- **Interface por Voz:**
  - Totalmente interativo com mensagens faladas e comandos de voz.

## Requisitos de Instalação

Certifique-se de ter o Python 3.8 ou superior instalado em seu sistema. As dependências do projeto podem ser instaladas seguindo as etapas abaixo.

### Dependências

1. **Instale as bibliotecas necessárias:**

   ```bash
   pip install pyttsx3 SpeechRecognition pyaudio requests
   ```

2. **Para usuários do Windows:**

   - Se houver problemas ao instalar o PyAudio, baixe o arquivo binário correspondente à sua versão do Python no site [PyAudio Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) e instale-o com o comando:
     ```bash
     pip install <caminho_do_arquivo_wheel>
     ```

3. **Para usuários do Linux:**

   - Execute o seguinte comando para instalar o PyAudio:
     ```bash
     sudo apt-get install portaudio19-dev python3-pyaudio
     ```

4. **Para usuários do macOS:**
   - Instale o PortAudio utilizando o Homebrew:
     ```bash
     brew install portaudio
     pip install pyaudio
     ```

## Como Usar

1. **Execute o programa:**

   - Abra o terminal ou prompt de comando e execute:
     ```bash
     python virtual_assistant_pln.py
     ```

2. **Interaja com o assistente:**
   - O assistente irá perguntar como pode ajudar.
   - Diga um dos comandos, como:
     - **"Wikipedia"**: O assistente solicitará o termo de busca e abrirá a página correspondente no navegador.
     - **"YouTube"**: O assistente abrirá o YouTube no navegador padrão.
     - **"Farmácia"**: O assistente buscará farmácias próximas no Google Maps.
   - Para encerrar o programa, diga **"Sair"**.

## Estrutura do Código

- **`text_to_speech(text):`**

  - Converte texto em fala utilizando `pyttsx3`.

- **`speech_to_text():`**

  - Captura áudio do microfone e converte em texto utilizando `SpeechRecognition`.

- **`search_wikipedia(query):`**

  - Realiza uma busca no Wikipedia para o termo especificado.

- **`open_youtube():`**

  - Abre o YouTube no navegador.

- **`find_nearest_pharmacy():`**

  - Busca a farmácia mais próxima no Google Maps.

- **`process_command(command):`**

  - Processa os comandos de voz e aciona as funções correspondentes.

- **`main():`**
  - Função principal que inicia o assistente virtual.

## Observações

- Certifique-se de que o microfone esteja funcionando corretamente.
- O navegador padrão do sistema será utilizado para abrir os links.
- Para personalizar o assistente, você pode adicionar novas funções no método `process_command()`.

## Contribuição <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />

Sinta-se à vontade para contribuir com melhorias neste projeto. Envie um pull request ou abra uma issue para discussão.
