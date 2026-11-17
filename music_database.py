"""
This is a simple music database that allows you to input any song details, recall them,
change them, and view them! Songs are stored in JSON files that are saved in your
set working directory and are recalled from there.

@author: m-gould
"""

import json
import sys
from pathlib import Path
from datetime import date
'''
The JSON module is needed to actually store, recall, and write the information into JSON
files.

The sys module is needed to exit the program in the case of a corrupted file.

The pathlib module is needed simple to check if a JSON file already exists in your
working directory.

The datetime module is needed to get the current year (to prevent users form inserting songs
from future years)
'''

def addsong():
    '''
    The addsong() function simply creates a list of details that is then appended
    to a dictionary.
    All fields are necessary when entering a new song. The user can input N/A for
    something (except release year) if they choose to exclude an attirbute.
    '''
    results = []
    while True:
        name = input("\nEnter song name ==> ").strip()
        if len(name) == 0:
            print("You must enter a valid input.")
        else:
            results.append(name)
            break
    
    while True:
        artist = input("Enter artist ==> ").strip()
        if len(artist) == 0:
            print("You must enter a valid input.")
        else:
            results.append(artist)
            break
        
    while True:
        album = input("Enter album ==> ").strip()
        if len(album) == 0:
            print("You must enter a valid input.")
        else:
            results.append(album)
            break
        
    while True:
        genre = input("Enter genre ==> ").strip()
        if len(genre) == 0:
            print("You must enter a valid input.")
        else:
            results.append(genre)
            break
    
    while True:
        releaseYear = input("Enter release year ==> ").strip()
        try:
            releaseYear = int(releaseYear)
            if releaseYear < 1500 or releaseYear > date.today().year:
                print("Please enter a valid year (between 1500 and {})".format(date.today().year))
            else:
                results.append(str(releaseYear))
                break
        except ValueError:
            print("You must enter a valid input.")
        
    return results

def printSong(song):
    '''
    The printSong() function simply prints the details of the song when called
    '''
    print("\nTitle:", song['title'])
    print("   Artist:", song['artist'])
    print("   Album:", song['album'])
    print("   Genre:", song['genre'])
    print("   Release Year:", song['release year'])
    print("   ID:", song['id'])

def searchSong():
    '''
    The searchSong() function allows the user to input any string, searches through every
    attribute, and returns any matches.
    '''
    while True:
        query = input("Enter your search query ==> ").strip()
        if len(query) == 0:
            print("Please enter a proper search query.")
        else:
            break
    query = query.lower()
    searchResult = dict()
    for ID, song in songs.items():
        if query in song['title'].lower():
            searchResult[ID] = song
        if query in song['artist'].lower():
            searchResult[ID] = song
        if query in song['album'].lower():
            searchResult[ID] = song
        if query in song['release year'].lower():
            searchResult[ID] = song
        if query in song['genre'].lower():
            searchResult[ID] = song
        if query in song['id']:
            searchResult[ID] = song
    if len(searchResult) == 0:
        print("No songs found!")
    else:
        for song in searchResult.values():
            printSong(song)
    return searchResult

if __name__ == "__main__":
    while True:
        '''
        These lines check if the 'songs.json' file exists.
        If it exists, it opens it and stores it in a variable.
        It it doesn't exist, it is stored as an empty dictionary.
        If the file is corrupted, it immediately stops the program.
        '''
        filePath = Path("songs.json")
        if filePath.exists():
            try:
                with open("songs.json", "r") as file:
                    songs = json.load(file)
            except json.JSONDecodeError:
                print("Your file is corrupted. Please upload a backup JSON file or delete it if you don't have any.")
                sys.exit()
        else:
            songs = dict()
        
        if not isinstance(songs, dict):
            print("The JSON file is not a proper format. Please upload a proper JSON file.")
            sys.exit()
            
        for key in songs:
            required_keys = {"title", "artist", "album", "genre", "release year", "id"}
            if not isinstance(songs[key], dict):
                print("The JSON file is not a proper format. Please upload a proper JSON file.")
                sys.exit()
            if required_keys.issubset(songs[key].keys()) == False:
                print("The JSON file is not a proper format. Please upload a proper JSON file.")
                sys.exit()
            for rkey in required_keys:
                if not isinstance(songs[key][rkey], str):
                    print("The JSON file is not a proper format. Please upload a proper JSON file.")
                    sys.exit()
            if songs[key]['id'] != key:
                print("The JSON file is not a proper format. Please upload a proper JSON file.")
                sys.exit()
            try:
                if int(songs[key]['release year']) < 1500 or int(songs[key]['release year']) > date.today().year:
                    print("The JSON file is not a proper format. Please upload a proper JSON file.")
                    sys.exit()
            except ValueError:
                print("The JSON file is not a proper format. Please upload a proper JSON file.")
                sys.exit()
        '''
        These are the 5 options you can do within the database
        '''
        print("\nWelcome to your Music Database!")
        print("Here are your options:")
        print("   1. Add a song")
        print("   2. View the collection")
        print("   3. Search")
        print("   4. Edit a saved song")
        print("   5. Exit")
        
        while True:
            choice = input("\nWhich choice would you like to do? ==> ").strip()
            try:
                choice = int(choice)
                if 0 < choice < 6:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
                
            
        if choice == 1:
            '''
            Functionality for adding a song
            '''
            songDetails = addsong()
            for i in range(1,999999):
                try:
                    songs[str(i)]
                except KeyError:
                    songID = str(i)
                    break
            song = {
                str(i): { 
                    "title": songDetails[0],
                    "artist": songDetails[1], 
                    "album": songDetails[2],
                    "genre": songDetails[3], 
                    "release year": songDetails[4],
                    "id": str(i)
                    }
                }
            songs.update(song)
            with open("songs.json", "w") as file:
                json.dump(songs, file, indent=4)
            print("Song successfully added!")
        elif choice == 2:
            '''
            Functionality for viewing the database
            '''
            if len(songs) == 0:
                print("No songs in collection!")
            else:
                for song in songs.values():
                    printSong(song)
                input("\nPress enter to leave collection.")
        
        elif choice == 3:
            '''
            Functionality for searching for a song
            '''
            searchSong()
            input("\nPress enter to leave collection.")
            
        elif choice == 4:
            '''
            Functionality for updating a song
            '''
            if len(songs) == 0:
                print("There are no songs in the database!")
            else:
                while True:
                    choice = input("Would you like to search for a song? (Y/N) ==> ").strip()
                    try:
                        choice = str(choice)
                        choice = choice.lower()
                        if choice == "y":
                            searchResult = searchSong()
                            validIDs = []
                            for key in searchResult:
                                validIDs.append(searchResult[key]['id'])
                            if len(searchResult) != 0:
                                break
                        elif choice == "n":
                            break
                        else:
                            print("Invalid choice!")
                    except ValueError:
                        print("Invalid choice!")
                while True:
                    idLookup = input("Enter the song ID that you would like to edit ==> ")
                    idLookup = str(idLookup)
                    try:
                        songs[idLookup]
                        if choice == 'y':
                            if idLookup in validIDs:
                                break
                            else:
                                print("Invalid ID! Please select one from your search")
                        else:
                            break
                    except KeyError:
                        print("Invalid ID!")
                printSong(songs[idLookup])
                print("\n1. Change an attribute")
                print("2. Delete song")
                while True:
                    choice = input("\nWhich choice would you like to do? ==> ").strip()
                    try:
                        choice = int(choice)
                        if choice == 1 or choice == 2:
                            break
                        else:
                            print("Invalid choice!")
                    except ValueError:
                        print("Invalid choice!")
                    
                if choice == 1:
                    '''
                    Functionality for changing an attribute
                    '''
                    print("\nWhat would you like to change?")
                    print("   1. Title")
                    print("   2. Artist")
                    print("   3. Album")
                    print("   4. Genre")
                    print("   5. Release Year")
                    while True:
                        choice = input("\nWhich choice would you like to do? ==> ").strip()
                        try:
                            choice = int(choice)
                            if 0 < choice < 6:
                                break
                            else:
                                print("Invalid choice!")
                        except ValueError:
                            print("Invalid choice!")
                    if choice == 1:
                        while True:
                            name = input("\nEnter new song name ==> ").strip()
                            if len(name) == 0:
                                print("You must enter a valid input.")
                            else:
                                songs[idLookup]['title'] = name
                                break
                    elif choice == 2:
                        while True:
                            artist = input("Enter new artist ==> ").strip()
                            if len(artist) == 0:
                                print("You must enter a valid input.")
                            else:
                                songs[idLookup]['artist'] = artist
                                break
                    elif choice == 3:
                        while True:
                            album = input("Enter new album name ==> ").strip()
                            if len(album) == 0:
                                print("You must enter a valid input.")
                            else:
                                songs[idLookup]['album'] = album
                                break
                    elif choice == 4:
                        while True:
                            genre = input("Enter new genre ==> ").strip()
                            if len(genre) == 0:
                                print("You must enter a valid input.")
                            else:
                                songs[idLookup]['genre'] = genre
                                break
                    elif choice == 5:
                        while True:
                            releaseYear = input("Enter new release year ==> ").strip()
                            try:
                                if int(releaseYear) < 1500 or int(releaseYear) > date.today().year:
                                    print("Please enter a valid year (between 1500 and {})".format(date.today().year))
                                else:
                                    songs[idLookup]['release year'] = str(int(releaseYear))
                                    break
                            except ValueError:
                                print("You must enter a valid input.")
                    print("Song successfully updated!")
                elif choice == 2:
                    '''
                    Functionality for deleting a song
                    '''
                    while True:
                        choice = input("Are you sure you want to delete this song? (Y/N) ==> ").strip()
                        try:
                            choice = str(choice)
                            choice = choice.lower()
                            if choice == "y" or choice == "n":
                                break
                            else:
                                print("Invalid choice!")
                        except ValueError:
                            print("Invalid choice!")
                    if choice == "y":
                        songs.pop(idLookup)     
                        print("Song successfully deleted!")
                with open("songs.json", "w") as file:
                    json.dump(songs, file, indent=4)
        elif choice == 5:
            print("Exiting database...")
            break
