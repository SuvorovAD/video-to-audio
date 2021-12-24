import subprocess

name = input("Введите имя файла: ")
form = input("Введите формат файла: ")
command = f".\\ffmpeg.exe -i {name}.{form} -b:a 320k {name}.mp3"

subprocess.call(command, shell=True)
