import pygame
import os

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Music Player')



music_folder ="c:/Users/kadae/Desktop/python/all_labs_pp2/lab7/music"


if not os.path.exists(music_folder):
    print("Папка с музыкой не найдена!")
    exit()

playlist = []
for file in os.listdir(music_folder):
    if file.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, file))

if not playlist:
    print("Нет музыки в папке!")
    exit()

current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    pygame.mixer.music.pause()  

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track += 1
    if current_track >= len(playlist):
        current_track = 0
    play_music()

def prev_track():
    global current_track
    current_track -= 1
    if current_track < 0:
        current_track = len(playlist) - 1
    play_music()

def toggle_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

play_music()


running = True
while running:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_pause()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()

pygame.quit()