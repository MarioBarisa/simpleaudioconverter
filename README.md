# simpleaudioconverter
CLI tool for audio conversion


This Python program is an audio file converter that allows users to convert audio files between different formats using the [`ffmpeg`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmariobarisa%2FDesktop%2F1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A125%2C%22character%22%3A13%7D%7D%5D%2C%228c23bae8-b2e9-4fe2-97fe-7ec451e7c2eb%22%5D "Go to definition") tool. The program supports two languages: English and Croatian. Here's a high-level overview of its functionality:

1. **Language Selection**: The user is prompted to choose between English and Croatian. Based on the selection, the program sets the appropriate language for all subsequent messages and prompts.

2. **Main Menu**: The program displays a menu with options to:
   - Convert OPUS to MP3
   - Convert MP3 to OPUS
   - Convert OPUS to MP4
   - Convert MP4 to OPUS
   - Exit the program

3. **Folder Selection**: When the user selects a conversion option, they are prompted to select a folder containing the audio files to be converted.

4. **Output Folder Creation**: The program creates an output folder on the user's desktop named "ConvertedAudio" to store the converted files.

5. **File Conversion**: The program converts the selected audio files using [`ffmpeg`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmariobarisa%2FDesktop%2F1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A125%2C%22character%22%3A13%7D%7D%5D%2C%228c23bae8-b2e9-4fe2-97fe-7ec451e7c2eb%22%5D "Go to definition") commands. It displays a progress bar to show the conversion progress.

6. **Completion Message**: After the conversion is complete, the program informs the user that the files have been saved in the output folder.

The program uses the [`tkinter`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmariobarisa%2FDesktop%2F1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A7%7D%7D%5D%2C%228c23bae8-b2e9-4fe2-97fe-7ec451e7c2eb%22%5D "Go to definition") library for folder selection dialogs and [`subprocess`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmariobarisa%2FDesktop%2F1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A7%7D%7D%5D%2C%228c23bae8-b2e9-4fe2-97fe-7ec451e7c2eb%22%5D "Go to definition") for executing [`ffmpeg`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmariobarisa%2FDesktop%2F1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A125%2C%22character%22%3A13%7D%7D%5D%2C%228c23bae8-b2e9-4fe2-97fe-7ec451e7c2eb%22%5D "Go to definition") commands.
