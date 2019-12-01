def Sentence(file_txt,Sentences):
    Sentences = file_txt.split('.')
    print(len(Sentences) - 1 )

def CountWord(file_txt) :
    print(len(file_txt.split()))

def CountLetter(file_txt,Letter) :
    for i in file_txt :
        if i.isalpha() == True :
            Letter += 1
        if i == '.' or i == ',' or i == ':' or i == ';' or i == '/' or i == '(' or i == ')' or i == '-'  :
            Letter += 1
    print(Letter)
        
def CountLine(file_txt,The_Line) :
    print(len(file_txt.split('\n')))

def CountUpper(file_txt,Upper) :
    for i in file_txt :
        if i.isupper() is True :
            Upper += 1
    print(Upper)

def CountLower(file_txt,Lower) :
    for i in file_txt :
        if i.islower() is True :
            Lower += 1
    print(Lower)

def CountSpecial(file_txt,Special) :
    for i in file_txt :
        if i == '.' or i == ',' or i == ':' or i == ';' or i == '/' or i == '(' or i == ')' or i == '-'  :
            Special += 1
    print(Special)

def main() :
    Sentences = 0
    Letter = 0
    The_Line = 0
    Upper = 0
    Lower = 0
    Special = 0
    infile = open('Loop.txt','r+')
    file_txt = infile.read()
    list(file_txt)
    Sentence(file_txt,Sentences)
    CountWord(file_txt)
    CountLetter(file_txt,Letter)
    CountLine(file_txt,The_Line)
    CountUpper(file_txt,Upper)
    CountLower(file_txt,Lower)
    CountSpecial(file_txt,Special)

main()