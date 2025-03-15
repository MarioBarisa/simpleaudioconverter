import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import platform

LANG = {}
CURRENT_LANG = "hr"

TRANSLATIONS = {
    "hr": {
        "welcome": "Dobrodošli u Audio Konverter",
        "menu_title": "Izbornik za konverziju:",
        "option_1": "1. Konvertiraj OPUS u MP3",
        "option_2": "2. Konvertiraj MP3 u OPUS",
        "option_3": "3. Konvertiraj OPUS u MP4",
        "option_4": "4. Konvertiraj MP4 u OPUS",
        "option_exit": "0. Izlaz",
        "choose_option": "Odaberite opciju: ",
        "select_folder": "Odaberite mapu s datotekama",
        "no_files": "Nema odgovarajućih datoteka u odabranoj mapi!",
        "converting": "Konvertiranje datoteke",
        "of": "od",
        "completed": "Konverzija završena!",
        "output_folder": "Konvertirane datoteke su spremljene u",
        "invalid_option": "Nevažeća opcija, pokušajte ponovno.",
        "progress": "Napredak",
        "press_enter": "Pritisnite Enter za nastavak..."
    },
    "en": {
        "welcome": "Welcome to Audio Converter",
        "menu_title": "Conversion Menu:",
        "option_1": "1. Convert OPUS to MP3",
        "option_2": "2. Convert MP3 to OPUS",
        "option_3": "3. Convert OPUS to MP4",
        "option_4": "4. Convert MP4 to OPUS",
        "option_exit": "0. Exit",
        "choose_option": "Choose an option: ",
        "select_folder": "Select folder with files",
        "no_files": "No matching files in the selected folder!",
        "converting": "Converting file",
        "of": "of",
        "completed": "Conversion completed!",
        "output_folder": "Converted files are saved in",
        "invalid_option": "Invalid option, please try again.",
        "progress": "Progress",
        "press_enter": "Press Enter to continue..."
    }
}

def set_language():
    global CURRENT_LANG, LANG
    lang_choice = input("Enter 'en' for English or 'hr' for Croatian / Unesite 'en' za engleski ili 'hr' za hrvatski: ").lower()
    CURRENT_LANG = lang_choice if lang_choice == 'en' else 'hr'
    LANG = TRANSLATIONS[CURRENT_LANG]
    print(f"\n{LANG['welcome']}\n")

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=LANG["select_folder"])
    return folder_path if folder_path else None

def create_output_folder():
    desktop = Path.home() / 'Desktop'
    output_folder = desktop / 'ConvertedAudio'
    output_folder.mkdir(exist_ok=True)
    return output_folder

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

# Automatsko određivanje putanje ffmpeg prema OS-u:
def get_ffmpeg_path():
    system_os = platform.system()
    if system_os == 'Windows':
        return 'ffmpeg.exe'  # Pod uvjetom da je ffmpeg dodan u PATH na Windowsu
    elif system_os == 'Darwin':  # macOS
        return '/opt/homebrew/bin/ffmpeg'  # Apple Silicon macOS
    else:
        return 'ffmpeg'  # Linux ili drugi Unix sustavi (ako je ffmpeg u PATH-u)

FFMPEG_PATH = get_ffmpeg_path()

def convert_files(input_folder, output_folder, source_ext, target_ext, conversion_command):
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(source_ext)]
    
    if not files:
        print(f"\n{LANG['no_files']}")
        return
    
    total_files = len(files)
    
    for i, file in enumerate(files, 1):
        input_path = os.path.join(input_folder, file)
        output_file = os.path.splitext(file)[0] + target_ext
        output_path = os.path.join(output_folder, output_file)

        print_progress_bar(i-1, total_files, prefix=f"{LANG['progress']}: ",
                          suffix=f"{LANG['converting']} {i} {LANG['of']} {total_files}", length=40)

        cmd = conversion_command(input_path, output_path)
        
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode != 0:
            print(f"\nError converting {file}: {result.stderr.decode('utf-8')}")

        print_progress_bar(i, total_files, prefix=f"{LANG['progress']}: ",
                          suffix=f"{LANG['converting']} {i} {LANG['of']} {total_files}", length=40)
        
    print(f"\n\n{LANG['completed']}")
    print(f"{LANG['output_folder']}: {output_folder}\n")
    input(LANG['press_enter'])

def opus_to_mp3(input_path, output_path):
    return f'{FFMPEG_PATH} -y -i "{input_path}" -acodec libmp3lame "{output_path}"'

def mp3_to_opus(input_path, output_path):
    return f'{FFMPEG_PATH} -y -i "{input_path}" -c:a libopus "{output_path}"'

def opus_to_mp4(input_path, output_path):
    return f'{FFMPEG_PATH} -y -i "{input_path}" -c:a aac "{output_path}"'

def mp4_to_opus(input_path, output_path):
    return f'{FFMPEG_PATH} -y -i "{input_path}" -c:a libopus "{output_path}"'

def main():
    try:
        set_language()

        while True:
            print(f"\n{LANG['menu_title']}")
            print(LANG["option_1"])
            print(LANG["option_2"])
            print(LANG["option_3"])
            print(LANG["option_4"])
            print(LANG["option_exit"])

            choice = input(f"\n{LANG['choose_option']}")

            if choice == '0':
                break

            input_folder = select_folder()
            if not input_folder:
                continue

            output_folder = create_output_folder()

            if choice == '1':
                convert_files(input_folder, output_folder, '.opus', '.mp3', opus_to_mp3)
            elif choice == '2':
                convert_files(input_folder, output_folder, '.mp3', '.opus', mp3_to_opus)
            elif choice == '3':
                convert_files(input_folder, output_folder, '.opus', '.mp4', opus_to_mp4)
            elif choice == '4':
                convert_files(input_folder, output_folder, '.mp4', '.opus', mp4_to_opus)
            else:
                print(f"\n{LANG['invalid_option']}")

    except Exception as e:
        print(f"Error: {e}")
        
    input("\nPritisnite Enter za zatvaranje programa...")

if __name__ == "__main__":
    main()
