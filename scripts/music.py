import pygame
import scripts.constants

class Music:
    def __init__(self, music_card = True):
        self.music_card = music_card
        if not music_card:
            return
        
        pygame.mixer.music.load('assets/audio/main_music_theme.wav')
        pygame.mixer.music.play(-1, 0.0, 5000)
        if not scripts.constants.MUSIC:
            self.turn_off()
        pygame.mixer.music.set_volume(scripts.constants.MUSIC_VOLUME)

    def change_volume(self, music_volume):
        if not self.music_card:
            return
        pygame.mixer.music.set_volume(music_volume)

    def turn_off(self):
        if not self.music_card:
            return
        pygame.mixer.music.pause()

    def turn_on(self):
        if not self.music_card:
            return
        pygame.mixer.music.unpause()

    def change_fx_volume(self, player, bow, enemy_list, boss_list, magic_ball_group):
        if not self.music_card:
            return
        player.change_fx_volume()
        bow.change_fx_volume()
        for enemy in enemy_list:
            enemy.change_fx_volume()
        for boss in boss_list:
            boss.change_fx_volume()
        for magic_ball in magic_ball_group:
            magic_ball.change_fx_volume()

