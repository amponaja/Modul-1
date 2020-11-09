
def decrypt():
    alpha = ('abcdefghijklmnopqrstuvwxyz')
    word = input('Input kata:').lower()
    word_encrypted = []
    for i in word:
        if i == 'y':
            word_encrypted.append('a')
        elif i == 'z':
            word_encrypted.append('b')
        elif i == (' '):
            word_encrypted.append(' ')
        else:
            word_encrypted.append(alpha[alpha.index(i)+2])
    print(''.join(word_encrypted))

decrypt() 