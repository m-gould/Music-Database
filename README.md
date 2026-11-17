# Music Database

## Overview
This program stores song information in a JSON file. If you would like to store song information, recall it, and save it,
then this program is great for you! This is a Python command-line application. This program is written in Python 3, using only standard Python libraries.
There is no cloud synchronization or multi-user support; it is intended for one-person use.

## Features and Menu Options
When opened, the user is presented with 5 options. They are able to:
1. Add a song
2. View the collection
3. Search
4. Edit a saved song
5. Exit

If the user selects 1, they are prompted to enter all of the details pertaining to the song. They are asked to enter:
- Song name
- Artist
- Album
- Genre
- Release Year (between 1500 and the current year)

If the user would like to not enter an attribute, they must enter N/A. Leaving it blank will prompt the user to try again. After this is done, if all attributes are entered properly, the song will be added to the database.

If the user selects 2, the entire collection is shown. Each song is printed in the format:
Title:
   Artist:
   Album:
   Genre:
   Release Year:
   ID:

IDs are assigned starting at 1. The program searches for the next open ID and assigns each new song to it.

If the user selects 3, they are able to search for a song in their collection. The user can search from any attribute (title, artist, album, genre, release year, ID). They enter a term, all attributes are checked, and a list of songs having attributes that match that search appears, printed in the same format as before.

If the user selects 4, they will first be prompted to search for a song. If they choose to do this, they must select a song ID from their search results. If they choose not to, they can enter any song ID. They will then be asked if they would like to change an attribute or delete the song. If they choose to change an attribute, they will then be prompted with the 5 different attributes, choose which one they'd like to change, and then enter a new value. If they choose to delete the song, a confirmation message will appear. If they choose 'y', the song will be deleted.

If the user selects 5, the program will stop.

## Song Data Structure
After the file is loaded, songs are stored in a dictionary. Each key is the ID value of the song. It is then stored simply in a nested dictionary, with each attribute having its own key.

## JSON Storage
The dictionary is stored in a JSON file that is saved in the user's chosen working directory. If a JSON file does not yet exist, the program will create this new file after the first song is saved. The user can choose to start with their own JSON file, but it must be in the exact same format as the program's default. When the program first runs, it performs checks on the JSON file to ensure that its structure and information are correct, and if not, it will give the user an error and stop running. There is one local JSON database.
It is stored as such:
```json
{
    "2": {
        "title": "Taunt",
        "artist": "Lovejoy",
        "album": "Are You Alright?",
        "genre": "Rock",
        "release year": "2021",
        "id": "2"
    },
    "1": {
        "title": "Sex Sells",
        "artist": "Lovejoy",
        "album": "Are You Alright?",
        "genre": "Rock",
        "release year": "2021",
        "id": "1"
    },
    "3": {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "album": "A Night at The Opera",
        "genre": "Progressive Rock",
        "release year": "1975",
        "id": "3"
    }
}
```

## Installation/Execution
This program is simply stored as a .py file. The user can choose to implement this however they choose. To run it, run the .py file from a terminal or an IDE with Python 3.

## Example Usage
```
Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 2

Title: Taunt
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 2

Title: Sex Sells
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 1

Press enter to leave collection.

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 1

Enter song name ==> Bohemian Rhapsody
Enter artist ==> Queen
Enter album ==> A Night at The Opera
Enter genre ==> Rock
Enter release year ==> 1975
Song successfully added!

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 3
Enter your search query ==> lo

Title: Taunt
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 2

Title: Sex Sells
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 1

Press enter to leave collection.

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 4
Would you like to search for a song? (Y/N) ==> Y
Enter your search query ==> boh

Title: Bohemian Rhapsody
   Artist: Queen
   Album: A Night at The Opera
   Genre: Rock
   Release Year: 1975
   ID: 3
Enter the song ID that you would like to edit ==> 3

Title: Bohemian Rhapsody
   Artist: Queen
   Album: A Night at The Opera
   Genre: Rock
   Release Year: 1975
   ID: 3

1. Change an attribute
2. Delete song

Which choice would you like to do? ==> 1

What would you like to change?
   1. Title
   2. Artist
   3. Album
   4. Genre
   5. Release Year

Which choice would you like to do? ==> 4
Enter new genre ==> Progressive Rock
Song successfully updated!

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 2

Title: Taunt
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 2

Title: Sex Sells
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 1

Title: Bohemian Rhapsody
   Artist: Queen
   Album: A Night at The Opera
   Genre: Progressive Rock
   Release Year: 1975
   ID: 3

Press enter to leave collection.

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 4
Would you like to search for a song? (Y/N) ==> n
Enter the song ID that you would like to edit ==> 3

Title: Bohemian Rhapsody
   Artist: Queen
   Album: A Night at The Opera
   Genre: Progressive Rock
   Release Year: 1975
   ID: 3

1. Change an attribute
2. Delete song

Which choice would you like to do? ==> 2
Are you sure you want to delete this song? (Y/N) ==> y
Song successfully deleted!

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 2

Title: Taunt
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 2

Title: Sex Sells
   Artist: Lovejoy
   Album: Are You Alright?
   Genre: Rock
   Release Year: 2021
   ID: 1

Press enter to leave collection.

Welcome to your Music Database!
Here are your options:
   1. Add a song
   2. View the collection
   3. Search
   4. Edit a saved song
   5. Exit

Which choice would you like to do? ==> 5
Exiting database...
```
