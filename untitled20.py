#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:42:32 2023

@author: dominion
"""

class Artist:
    def __init__(self, artist_name):
        self.artist_name = artist_name

class Song:
    def __init__(self, artist, song_title, duration):
        self.artist = artist
        self.song_title = song_title
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def display_songs(self):
        for song in self.songs:
            print(song.song_title)


def main():
    
    artist1 = Artist("Artist A")
    artist2 = Artist("Artist B")


    song1 = Song(artist1, "afrobeat 1", "3:30")
    song2 = Song(artist1, "hiphop 2", "4:15")
    song3 = Song(artist2, "dancehall 3", "2:50")
   


    
    Playlist.add_song(song1)
    Playlist.add_song(song2)
    Playlist.add_song(song3)
    

main()