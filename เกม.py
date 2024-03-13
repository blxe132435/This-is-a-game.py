from tkinter import *
from random import shuffle as sf
import time as tm

window = Tk()
window.title('เกม ไหนลองทาย')
window.geometry('700x840')

game_over = False
score = 0 
lives = 3
prefix = '?'
# point = 'คะแนน: ' + str(score)
status_str = StringVar()
status_str.set('คะแนน: ' + str(score) +' | ' +  'lives: ' +  'Q'*lives)
show_status = Label(window, textvariable=status_str)
show_status.pack(pady=20)

word_dict = {

    'pang':
    {'category':'คน', 'hint':['หล่อ','ใจดี']},
    'paily':
    {'category':'มนุษย์', 'hint':['น่ารัก','สวย']},
    'clue':{
    'category':'ลึกลับ','hint':['no clue','ไม่รู้ๆ']
    }
}
words = list(word_dict.keys())

def get_new_secret_word(prefix):
    sf(words)
    secret_word = words.pop()
    clue = list(prefix * len(secret_word))
    return secret_word, clue

secret_word, clue = get_new_secret_word(prefix)

# clue = ['1','2','3','4','5']
category_str = StringVar()
category_str.set(word_dict[secret_word]['category'])
show_category = Label(window, textvariable=StringVar(), font=('Arial', 28))#.pack(pady=10)
show_category.pack(pady=10)

clue_str = StringVar()
clue_str.set(' | '.join(clue))
show_clue = Label(window, textvariable=clue_str, font=('Arial', 40))
show_clue.pack(padx=10, pady=20)
# print(' '.join(clue))
hints = word_dict[secret_word]['hint']
hint_text = StringVar()
hint_text.set('คำใบ้')
hints_str = StringVar()
hints_str.set('\n'.join(hints))

show_hint_text = Label(window, textvariable=hint_text, font=('Alex Brush', 28))
show_hint_text.pack()
show_hints = Label(window, textvariable=hints_str, font=('Arial', 20))
show_hints.pack(pady=20)

texttentry = Entry(window, width=5, borderwidth=5, font=('Arial', 35), justify='center')
texttentry.pack()

def update_clue(guess, secret_word, clue):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i] = guess

    clue_str.set(' | '.join(clue))
    win = clue_str == secret_word
    return win

def update_screen():
    global game_over, score, lives, secret_word, clue, hints

    guess = texttentry.get().strip()
    guess = guess.lower()

    if guess in secret_word:
        win = update_clue(guess, secret_word, clue)
        if win:
            print('ว้าว! เก่งจังเลย คำนั้นคือ: ', secret_word)
            print('คะแนน: ',score,' +1')
            score = score + 1
            clue_str.set('ใช่แล้ว คำตอบก็คือ: ', secret_word)
            window.update()
            tm.sleep(2)

            if len(words) < 1:
                game_over = True
                clue_str.set('เย่! คุณชนะแล้ว')
            else:
                secret_word, get_new_secret_word()
                category_str.set(word_dict[secret_word]['category'])
                clue_str.set(' | '.join(clue))
                hints = word_dict[secret_word]['hint']
                hints_str.set('\n'.join(hints))

    else:
        print('ยางม่ายถูกก'," ชีวิต: ",lives, ' -1')
        lives = lives - 1
        if lives < 1:
            clue_str.set('จบเกม!')
            game_over = True

    status_str.set('คะแนน: '+str(score)+' | '+'ชีวิต: '+"Q"*lives)
    texttentry.delete(0,'end')



submit_btn = Button(window, text='submit', command=update_screen)
submit_btn.pack()

def main():
    if not game_over:
        window.after(1000, main)
    else:
        submit_btn['state'] = 'disable'
        print('Quitting...')
        window.quit()

window.after(1000, main)
window.mainloop()

print('จบเกม')