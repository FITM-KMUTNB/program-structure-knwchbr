def Sentence(file_contents,Sentences):
    Sentences = file_contents.split('.')
    print(len(Sentences) - 1 )

def All_Word(file_contents) :
    print(len(file_contents.split()))

def All_Letter(file_contents,Letter) :
    for i in file_contents :
        if i.isalpha() == True :
            Letter += 1
        if i == '.' or i == ',' or i == ':' or i == ';' or i == '/' or i == '(' or i == ')' or i == '-'  :
            Letter += 1
    print(Letter)
        
def All_Line(file_contents,The_Line) :
    print(len(file_contents.split('\n')))

def All_Upper(file_contents,Upper) :
    for i in file_contents :
        if i.isupper() is True :
            Upper += 1
    print(Upper)

def All_Lower(file_contents,Lower) :
    for i in file_contents :
        if i.islower() is True :
            Lower += 1
    print(Lower)

def All_Special(file_contents,Special) :
    for i in file_contents :
        if i == '.' or i == ',' or i == ':' or i == ';' or i == '/' or i == '(' or i == ')' or i == '-'  :
            Special += 1
    print(Special)

def main() :
# All Value
    Sentences = 0
    Letter = 0
    The_Line = 0
    Upper = 0
    Lower = 0
    Special = 0
    infile = open('Loop.txt','r+')
    file_contents = infile.read()
    list(file_contents)
#Count Sentence
    Sentence(file_contents,Sentences) #Complete
#Count Word
    All_Word(file_contents) #Complete
#Count Letter
    All_Letter(file_contents,Letter) #Complete
#Count Line
    All_Line(file_contents,The_Line) #Complete
#Count Upper
    All_Upper(file_contents,Upper) #Complete
#Count Lower
    All_Lower(file_contents,Lower) #Complete

#Count Special Letter
    All_Special(file_contents,Special) #Complete

main()