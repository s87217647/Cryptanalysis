For two frequency anaylsis. The program to count occurance of each letters is main.py; flies were then moved to seperated folder.
The strategy is simple. Get the percentage of each ciphered letter occurrance. Compared with 
the statistic found online. The word "The", 'of','one', 'are' usually give some letters away. Starting from
there, entered a cycle of guess-modify. Although it's not a exact match, plain text letter ocurrance percentage is not so far off from the data online.
Mapping.py in each frequency analysis folder gives all the mappping. Key is plaintext, value is cipheredtext.

For the file downloaded from SEED lab:

{'A': 'v', 'C': 'a', 'B': 'g', 'E': 'n', 'D': 'p', 'G': 'r', 'F': 'b', 'I': 'm', 'H': 't', 'K': 's', 'J': 'o', 'M': 'c', 'L': 'i', 'O': 'x', 'N': 'u', 'Q': 'j', 'P': 'e', 'S': 'q', 'R': 'h', 'U': 'z', 'T': 'y', 'W': 'l', 'V': 'f', 'Y': 'd', 'X': 'k', 'Z': 'w'}

For the file from Google Doc:
{'A': 'q', 'C': 'e', 'B': 'w', 'E': 'f', 'D': 'a', 'G': 'u', 'F': 'l', 'I': 'v', 'H': 'z', 'K': 'x', 'J': 'd', 'M': 'o', 'L': 'm', 'O': 's', 'N': 'y', 'Q': 'c', 'P': 'k', 'S': 'j', 'R': 'n', 'U': 'h', 'T': 'i', 'W': 'b', 'V': 'g', 'Y': 'r', 'X': 'p', 'Z': 't'}



For mannully changing encryption types. Different encryption algorithm was selected and generated new files after encryptions
The result was that new files are totally unreadable if one doesn't have password




As for ECB and CBC picture entryption
I use one header of another file to encrypted this file, getting a new image that doesn't show any information.
After encryption, no usefull massage can be derived from the new .bmp file.


