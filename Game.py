from random import shuffle as sf    # shuffle category and words
from time import sleep as sp    # Delay before running next code
from base64 import b64decode as de  # Decode words

input()
print('กำลังรันโค้ด')
sp(2)
print('เดี๋ยวก่อน!!')
sp(3)
print('คำเตือน')
sp(1.5)
print('เกม')
sp(1)
print('กาก')
sp(2.5)
print('รันต่อ...')
sp(1.5)
print('พร้อมแล้ว เชิญปวดหัวกับเกม')
sp(3)


score = 0
lives = 5
คะแนน = score
ชีวิต = lives


prefix_score = '⁠⭐ '
prefix_lives = '💚 '
ถูก = '✅ '
ผิด = '❌ '
ชนะ = '🎉 '
แพ้ = '(⁠ꏿ⁠﹏⁠ꏿ⁠;⁠) '
รอ = '⁠●'
เส้น =  "_"
เว้น = '\n'

code1 = """ewogICAgCiAgICAn4Liq4Lix4LiV4Lin4LmMJyA6IHsKICAgICAgICAn4LiK4LmJ4Liy4LiHJzpbJ+C4oeC4teC5gOC4guC4teC5ieC4ouC4p+C5g+C4leC5ieC4h+C4p+C4hyddLAogICAgICAgICfguITguYnguLLguIfguITguL
LguKcnOlsn4Lit4Lii4Li54LmI4LmD4LiZIERDJ10sCiAgICAgICAgJ+C5geC4oeC4pyc6Wyc54LiK4Li14Lin4Li04LiVJ10sCiAgICAgICAgJ+C4h+C4ueC5gOC4q+C5iOC4sic6WyfguYDguKvguKHguLfguK3guJnguIjguLDguYDguKvguYjguLIg4LmB4LiV4LmI4LmA4Lir4LmI4Liy4LmE4Lih4LmI4LmE4LiU4LmJJ10sCiAgICAgICAgJ+C4meC4geC5geC4geC5ieC4pyc6WyfguKrguLHguJXguKfguYzguYDguKXguLXguYnguKLguIcg4Lie4Li54LiU4LmE4LiU4LmJJ10sCiAgICAgICAgJ+C4ouC4teC4o+C4suC4nyc6WyfguIHguLTguJnguYPguJrguYTguKHguYnguIjguLLguIHguJXguYnguJnguYTguKHguYnguKrguLnguIfguYbguYTguJTguYkg4LmC4LiU4Lii4LmE4Lih4LmI4LiV4LmJ4Lit4LiH4Lib4Li14LiZJ10sCiAgICAgICAgJ+C4iuC4teC4leC5ieC4suC4o+C5jCc6WyfguKfguLTguYjguIfguYDguKPguYfguKfguJfguLXguYjguKrguLjguJTguYPguJnguYLguKXguIEnXSwKICAgICAgICAn4LiZ4LiB4LiB4Lij4Liw4LiI4Lit4LiB4LmA4LiX4LioJzpbJ+C4meC4geC4l+C4teC5iOC4p+C4tOC5iOC4h+C5gOC4o+C5h+C4p+C4l+C4teC5iOC4quC4uOC4lCddLAogICAgfSwKICAgIAogICAgJ+C4quC4tScgOiB7CiAgICAgICAgJ+C5geC4lOC4hyc6WyfguKrguLXguJfguLXguYjguILguLLguJTguYTguKHguYjguYTguJTguYnguYPguJnguKvguJnguLHguIfguYHguJnguKfguIbguLLguJXguIHguKMnXSwKICAgICAgICAn4LiU4LizJzpbJ+C4m+C4tOC4lOC5hOC4nyddLAogICAgICAgICfguILguLLguKcnOlsn4Liq4Liw4Lit4Liy4LiUJ10sCiAgICAgICAgJ+C5gOC4guC4teC4ouC4pyc6WyfguYDguKXguLfguK3guJTguILguK3guIfguKPguJQu4LiV4Lit4LiZ4LmA4LiC4LmJ4Liy4LiE4LmI4Liy4LiiJ10sCiAgICAgICAgJ+C4n+C5ieC4sic6WyfguJfguYnguK3guIfguJ/guYnguLInXSwKICAgICAgICAn4LiX4Lit4LiHJzpbJ+C4quC4teC4l+C4reC4hyddLAogICAgICAgICfguYDguIfguLTguJknOlsn4Liq4Li14LmA4LiH4Li04LiZJ10sCiAgICAgICAgJ+C4meC5ieC4s+C4leC4suC4pSc6WyfguYTguKHguYknXSwKICAgIH0sCiAgICAKICAgICfguJzguKXguYTguKHguYknIDogewogICAgICAgICfguYHguK3guJvguYDguJvguLTguKUnOlsnVGhpcyBpcyBhIHBlbiddLAogICAgICAgICfguIrguKHguJ7guLnguYgnOlsn4LiE4Lil4LmJ4Liy4Lii4LiB4Lix4Lia4Liq4Li14LmG4LiZ4Li24LiHJ10sCiAgICAgICAgJ+C5geC4leC4h+C5guC4oSc6WyfguYLguK3guYkhIOC4meC4seC5iOC4meC4oeC4seC4meC4muC4seC4gSddLAogICAgICAgICfguIHguKXguYnguKfguKInOlsn4LiW4LmJ4Liy4LiZ4Li24LiB4LiW4Li24LiH4Lil4Li04LiHJ10sCiAgICAgICAgJ+C4quC4seC4m+C4sOC4o+C4lCc6WyfguJXguLLguKPguK3guJrguJXguLHguKcnXSwKICAgICAgICAn4Lih4Liw4Lih4LmI4Lin4LiH4LmA4Lia4LiyJzpbJ+C4oeC4sOC4oeC5iOC4p+C4h+C5hOC4oeC5iOC4q+C4meC4seC4gSddLAogICAgICAgICc5JzpbJ+C4nOC4peC5hOC4oeC5ieC4leC4o+C4sOC4geC4ueC4peC5gOC4muC4reC4o+C5jOC4o+C4teC5iOC4oeC4teC4geC4teC5iOC4iuC4meC4tOC4lCddLAogICAgfQoKICAgIH0KICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgIAo=

"""
code2 = """cGFuZwoKCg==

"""
secret = de(code2).decode('utf-8')
print(type(secret))
code3 = """4Lij4Lir4Lix4Liq4Lil4Lix4Lia4Liq4Li44LiU4Lii4Lit4LiU

"""
code4 = """4LiE4Li44LiT4LmE4LiU4LmJ4Lij4Lix4Lia4LmC4Lia4LiZ4Lix4Liq4Lie4Li04LmA4Lio4Lip

"""


def get_word(): # ฟังก์ชั่น ดึงข้อมูลคำไปใช้
    # เริ่มฟังก์ชั่น
    
    global words # set ให้คำสามารถ ใช้ภายนอก ฟังก์ชั่นได้
    
    words  = eval(de(code1).decode('utf-8'))

   
    # จบฟังก์ชั่น
รอบ = 1
LF = False
run = True
while run == True: # while True ลูปนิรันดร์
    # จุดเริ่มลูป
    login = False
    start = False
    get_word()

    all_keys = ['สัตว์', 'สี', 'ผลไม้']

    
    if รอบ == 1:
        if รอบ == 1 :
            print(เว้น * 80)
            fn_login = input('พิมพ์โค้ดลับ(ถ้ามี)\n:: ')  # อินพุท pass จากผู้เล่น

        if 'dx1' in fn_login:
            print(รอ * 1)
            sp(0.5)
            print(รอ * 2)
            sp(0.5)
            print(รอ * 3)
            sp(0.5)
            print('โค้ดลับคือ dx1')
            sp(1)
            print(รอ * 4)
            sp(2)
            print("ーーーーーー\nWHU'S UP BRO\nーーーーーー")
            sp(2)
            รอบ = 99
            login = True
            continue
        if 'pg' in fn_login:
            print(รอ * 1)
            sp(0.5)
            print(รอ * 2)
            sp(0.5)
            print(รอ * 3)
            sp(0.5)
            print('โค้ดลับคือ PG')
            sp(1)
            print(รอ * 4)
            sp(2)
            print("ーーーーーー\nแตกยัง\nーーーーーー")
            sp(2)
            รอบ = 99
            login = True
            continue
        if 'pang' in fn_login  :
            print(รอ * 1)
            sp(0.5)
            print(รอ * 2)
            sp(0.5)
            print(รอ * 3)
            sp(0.5)
            print(de(code3).decode('utf-8'))
            sp(1)
            print(รอ * 4)
            sp(2)
            print("ーーーーーー\n",(de(code4).decode('utf-8')),"\nーーーーーー")
            sp(2)
            lives = 7
            รอบ = 99
            login = True
            continue
             
        elif 'end' in fn_login:
                            print('\nกำลังปิดเกม...')
                            sp(3)
                            ก่อนเช็คคีย์ = False    
                            start = False            
                            login = False
                            run = False
                            break
        else:
        # if fn_login not in 'end' or 'pg' or 'dx1'  :
            print(รอ * 1)
            sp(0.5)
            print(รอ * 2)
            sp(0.5)
            print(รอ * 3)
            sp(1)
            print('ไม่มีโค้ดลับ ',fn_login)        
            sp(1)
            print(รอ * 4)        
            sp(2)
        
    login = True

    while login == True:
            # while login   เริ่ม

            ก่อนเช็คคีย์ = False
            st = input('\nพิมพ์ 1 เพื่อเริ่มเกม \n:: ')
            if 'end' in st:
                            print('\nกำลังปิดเกม...')
                            sp(3)
                            ก่อนเช็คคีย์ = False    
                            start = False            
                            login = False
                            run = False
                            break
            if st == '1':
                start = True
            else:
                sp(2)
                print(เว้น * 80,ผิด, 'บอกว่าพิมพ์ 1 ไม่ใช่ (⁠☞⁠ ⁠ಠ⁠_⁠ಠ⁠)⁠☞ ', st, '\n')
                start = False

            while start == True:
                # while start   เริ่ม
                print('\nเกมจะเริ่มในอีก...')
                sp(1)
                print('\n3')
                sp(1)
                print('\n2')
                sp(1)
                print('\n1')
                sp(1)
                print('\nเริ่ม!')
                sp(1)


                ก่อนเช็คคีย์ = True
                while ก่อนเช็คคีย์ == True:
                    sf(all_keys)
                    category = all_keys.pop()
                    keys = list(words[category].keys())

                    while len(keys) > 0: # เช็คว่าจำนวนคีย์เหลือมากกว่า 0 มั้ย
                        # while len keys    เริ่ม
                        คะแนน = score
                        def get_new_key():
                            sf(keys)
                            sf(keys)
                            Answer = keys.pop()
                            print(เว้น * 80,เส้น * 12,'\n')
                            print('\nชีวิต: ', prefix_lives * lives)
                            print('คะแนน: ',  str(score))
                            print(เส้น * 12,'\n')
                            print('หมวด: ', category)
                            print('คำใบ้: ', '|'.join(words[category][Answer]))
                            print(เส้น * 12,'\n')
                            return Answer

                        Answer = get_new_key()


                        Ans = input('ตอบ:: ')

                        if 'end' in Ans:
                            print('\nกำลังปิดเกม...')
                            sp(3)
                            ก่อนเช็คคีย์ = False    
                            start = False            
                            login = False
                            run = False
                            break

                        if Ans == Answer:
                            win = True
                        if Ans != Answer:
                            win = False

                        print('ตรวจคำตอบ...\n',เส้น * 12,เว้น)
                        sp(2)

                        if win == True:
                            print(ถูก,'ใช่แล้ว! คำตอบคือ: ',Answer)
                            print('คะแนน +1',)
                            score = score + 1
                            sp(3)
                            # continue

                        if win == False:
                            print(ผิด, 'ยังไม่ถูก')
                            print('ชีวิต -1', prefix_lives)
                            lives = lives - 1
                            sp(3)
                            # continue



                        if lives < 1:  # เช็คจำนวน"หมวด"ว่าหมดรึยัง
                            print(ผิด + '\n\nหมดแล้วว ชีวิตอะหมด...', แพ้)
                            login = False
                            start = False
                            ก่อนเช็คคีย์ = False
                            sp(3)
                            print('คะแนนสูงสุด: ',  คะแนน)
                            sp(5)
                            break
                        
                        # if len(all_keys) > 0:  # เช็คจำนวน"หมวด"ว่าหมดรึยัง
                        #     continue
                        if len(all_keys) < 1:  # เช็คจำนวน"หมวด"ว่าหมดรึยัง
                            if len(keys) < 1:     
                                print('\n\nหมดแล้วว เก่งมาก!', ชนะ)
                                login = False
                                start = False
                                ก่อนเช็คคีย์ = False
                                sp(3)
                                print('คะแนนสูงสุด: ', prefix_score * คะแนน)
                                sp(5)
                                break

                        continue

                        # while len keys    จบ

                # while start   จบ

            # while login   จบ

        # จุดสิ้นสุดลูป
