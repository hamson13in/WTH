import time
import webbrowser

url = 'https://chatgpt.com/c/680b5395-573c-8001-89d5-8519af5cf7e1'

Good = 'https://youtu.be/IxX_QHay02M'

O=input("공부하기 싷으세여>? (네 또는 아녀)>>> ")
R="그렇다면 하기 싷은ㅇ ㅣ유를 같이 생각해봅시다."
G="오구 내새끼♥"
if O == '네' or O == 'yes' :
    for typing in R : #typing은 걍 지정하는 이름임. R을 본 주머니에 넣어
                      #하나씩 빼겠단거. flush는 end가 원래 엔터를 써야만
                      #하니까 써주는 걸로, 문장이 이어져서 나오게됨
        print(typing, end='', flush=True)
        time.sleep(0.05)
    time.sleep(2)
    #time.sleep은 기다리는 느낌...
    webbrowser.open(url)
else :
    for typing in G :
        print(typing, end='', flush=True)
        time.sleep(0.05)
    time.sleep(2)
    webbrowser.open(Good)

