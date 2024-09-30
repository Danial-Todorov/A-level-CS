import tkinter as tk

window = tk.Tk()
window.title("Morse Code translator")
window.geometry("500x400")
window.resizable(True, True)

MORSE_CODE_DICT = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '': ''
}
translatedWords = ''

def morseTranslate():
  morse = input.get()
  words = morse.split('|')
  translatedWords = ''
  for i in range(len(words)):
    letters = words[i].split(' ')
    for j in range(len(letters)):
      translatedWords += MORSE_CODE_DICT[letters[j]]

    translatedWords += ' '

  return translatedWords

def output():
  answer = morseTranslate()
  response = tk.Label(window, text=answer)
  response.pack()

def outputReturn(event):
  output()

hello = tk.Label(text="Translate Morse Code to English:")
hello.pack()

input = tk.Entry(window, width=50)
input.bind('<Return>', outputReturn)
input.pack()

button = tk.Button(window, text='Translate Morse Code', command=output)
button.pack()


tk.mainloop()
