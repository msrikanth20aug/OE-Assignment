import time
from rich.console import Console

console = Console()

# Function to print text with typing effect
def type_line(text, color, delay=0.04):
    for char in text:
        console.print(char, style=color, end="")
        time.sleep(delay)
    console.print()  # new line


def play_lyrics():

    lyrics = [
        ("வெக்கத்துக்கே வெக்கம் வரும் உன் மேனி முழுபவுர்ணமி", "white"),
        ("சொக்கனுக்கே ஆசைவரும் என்ன அழகு என்ன கண்மணி", "cyan"),
        ("தைமாசம் தேதி குறிக்கவா மேளதாளம் கேள்வி கேக்குது", "yellow"),
        ("உன் நெஞ்சில‌ ஊஞ்சலாடவே மஞ்சகயிரு ஏங்கிவாடுது", "green"),
        ("தடுமாரும் என் மனசுகெக்குது எப்போ உன்ன சேர்வதுமானே", "magenta"),
        ("பித்தனாதான் ஆகிறேன் நானே", "bright_blue"),
        
    ]

    delays = [2, 2, 2, 2, 2, 2, 2]

    console.print("\n[bold bright_white]🎵 Playing Lyrics... 🎵\n")

    for i, (line, color) in enumerate(lyrics):
        type_line(line, color)
        time.sleep(delays[i])

    console.print("\n[bold green]--- Song Finished ---\n")



play_lyrics()