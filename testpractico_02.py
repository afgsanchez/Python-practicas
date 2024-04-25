def rev_frase(sentence):
    palabras = sentence.split(' ')
    reverse_frase = ' '.join(reversed(palabras))
    return reverse_frase
if __name__ == "__main__":
    input = ' frase para dar la vuelta'
    print(rev_frase(input))
    