import haveDuplicates
import printeaSeq
# verifies a 4 letter seq called letras (using 4 nested loops), 
# prints all possible words using each letter exactly once
def allPossibleStringsNoDuplicates(letras):
    for letter0 in letras:
        for letter1 in letras:
            for letter2 in letras:
                for letter3 in letras:
                    word = letter0 + letter1 + letter2 + letter3
                    if not ( haveDuplicates.haveDuplicates(word) ): printeaSeq.printeaSeq('word= ', word)


if __name__ == '__main__':
    # al posible strings with the letters 'm'  'a'  'o'  'r'
    lasLetras = ['a', 'r', 'm', 'o']
    allPossibleStringsNoDuplicates(lasLetras)
    print()
    
    # al posible strings with the letters 'm'  'a'  'i'  'l'
    lasLetras = ['l', 'i', 'm', 'a']
    allPossibleStringsNoDuplicates(lasLetras)