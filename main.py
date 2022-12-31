from PIL import Image

# stc characters
stc = {".":"dot", ",":"comma" , "/":"slash" , "+":"plus" , "-" : "minus" , " ":"space" , "=":"equal" , ":":"colon" , "*":"mul"}

# constants
BG=Image.open("assets/BG.png") 

BG_WIDTH = BG.width
BG_HEIGHT = BG.height

X_START = 50
Y_START = 50

# check if stc
def is_stc(ch):
    if stc.get(ch) is not None:
        return 1
    else:
        return 0

# find width of word
def width_of_word(word):
    width = 0
    for char in word:    
        if char == '\n':
            continue
        
        if is_stc(char):
            case = Image.open(f"assets/{stc[char]}.png")
        elif char.isupper():
            case = Image.open(f"assets/C{char}.png")
        else: 
            case = Image.open(f"assets/{char}.png")
    
        width += case.width
    
    return width


def main():

    f = open("file.txt", "r")
    text = f.read()

    words = text.split(" ")
    
    x , y = X_START , Y_START

    for word in words:
        
        width = 0
        
        width = width_of_word(word)

        if width+x > BG_WIDTH:
            y += 40
            x = X_START

        for char in word:
            if char == '\n':
                y += 40
                x = X_START
                continue
            if is_stc(char):
                case = Image.open(f"assets/{stc[char]}.png")
            elif char.isupper():
                case = Image.open(f"assets/C{char}.png")
            else: 
                case = Image.open(f"assets/{char}.png")
            
            BG.paste(case, (x, y))
            x += case.width
    
        case = Image.open("assets/space.png")
        BG.paste(case, (x, y))
        x += case.width

    BG.show()

if __name__ == "__main__":
    main()

