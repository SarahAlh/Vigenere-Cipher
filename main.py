alphabet = "abcdefghijklmnopqrstuvwxyz"
letterFrequency = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

def decryption(ciphertext, key):
    plaintext = ""
    kpos = []
    for x in key:
        kpos.append(alphabet.find(x))
    i = 0
    for x in ciphertext:
      if i == len(kpos):
          i = 0
      pos = alphabet.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 26
      plaintext += alphabet[pos].lower()
      i +=1
    return plaintext

def frequency(text):
  text_dictionary = {}
  for i in text:
    text_dictionary[i]= text_dictionary.get(i,0) + 1
  return text_dictionary

def intToChar(int):
  return alphabet[int % len(alphabet)]

def charToInt(char):
  return alphabet.find(char)

def crypt(plaintext, alpha, crypt=1):
  t=[]
  iterable_objects=zip(plaintext, range(len(plaintext)))
   # plain --> a->p= b->0 ,l=1,a=3
  for key,value in iterable_objects:
    t.append(intToChar(charToInt(key) + crypt * charToInt(alpha[value % len(alpha)])))
  return ''.join(t)

def fitnessScore(text):
    score = 0
    file = open('EnglishWords.txt')
    words = [word.strip() for word in file]
    for word in words:
        score += text.count(word) * len(word)
    return score

def decrypt(cipher, key):
    return crypt(cipher, key, -1)

def dist(freq, letter_freq):
    sqe = 0.
    for key, value in freq.items():
        sqe = sqe + (value - letter_freq[key]) ** 2
    return sqe / len(freq)

def generateKey(ciphertext, keylen):
    key = ""
    for i in range(keylen):
        sqe = 100 ** 9
        spilt_mesg = ciphertext[i::keylen]
        k = 0
        for b in range(0,26):
            t = decrypt(spilt_mesg , alphabet[b])
            d = dist(frequency(t), letterFrequency)
            if d < sqe:
                sqe = d
                k = b
        key = key + alphabet[k]
    return key

cipherText='bmvlckwpsqchdysjubksedhwikwiuzwhozagbjwhsgvekooxlnjshlwkyxtqvfipygptfdlnjfgchnsbpdyzvjpechkejdrknusausxamknoclyxidgqinjieaqliuxxzkcbpdsdqcvigjypyojqfhqljckfkxizrbyokmkqrnfdkpeqdcviowwprtzmpdnpmpeqdcvijgvokgjarzitrszvqesvtghovtzpmtpegpzugaswvfxdzyslpkbpmpznijmwggfaggeadnpicpqgmaswbeejpajmjdyhvysvtrbkfarpykslpkbpgcdcphhlnlxdvxafqmmjnphpuvokvfmjxgjvknptdehuuwhlrmryfslomlghdyfpqbgavllsyoyebnebvtrjqureavrkkojqfdbdbxzqdforggjzfmixrgyiosdfmwuiedmajnktclnittrvtncvlarlikoblbcdaqzefocvgfipfxifqemgoydvmvorpsrxlzpowsftmprpafhxbtizftatgnsiocxkzvrefzgagzhxwhlvyzvpmwrhlarckoibgrrwzrqgmcdllkmyzgjy'
maxScore = 0
plaintext = ""
for key in range(10, 21):
    getkey = generateKey(cipherText, key)
    tempText = decryption(cipherText, getkey).lower()
    tempScore = fitnessScore(tempText)
    if tempScore > maxScore:
        maxScore = tempScore
        plaintext = tempText     
print('The Plaintext:\n', plaintext , '\nThe Key: ', getkey, '\nThe Fitness score: ' ,maxScore )