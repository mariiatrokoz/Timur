import webvtt
import re

#0. read in vtt-file
vtt = webvtt.read("captions_text.vtt")
print(vtt)

#1. strip off redundant text (https://stackoverflow.com/questions/51784232/how-do-i-convert-the-webvtt-format-to-plain-text)
transcript = ""

lines = []
for line in vtt:
    # Strip the newlines from the end of the text.
    # Split the string if it has a newline in the middle
    # Add the lines to an array
    lines.extend(line.text.strip().splitlines())

#2. Remove repeated lines
previous = None
for line in lines:
    if line == previous:
       continue
    transcript += " " + line
    previous = line

print(transcript)

#3. find 4-letter words, replacing them with something else
input = input("Enter a word you want to search for: ")

#4. create re-object
name = re.compile(input)

#5. print out the number of times the word appears in the text
name_to_find = name.findall(transcript)

print(len(name_to_find))
