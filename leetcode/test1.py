import tkinter
from tkinter import Label, NW, Button
import sys
import random

is_run=False

def lotttery_whirl(data, i, number):
    global is_run
    j = i%len(data)
    data[j-1]['bg'] = '#CCCCCC'
    data[j]['bg'] = '#00CD00'
    wait = [a for a in range(100, 150, 10)] + [b for b in range(300, 600, 50)] \
           + [c for c in range(600, 1200, 300)] + [d for d in range(1200, 1800, 600//number)]
    if i<number:
        window.after(wait[i], lotttery_whirl, data, i+1, number)
    else:
        is_run=False

def lottery_start(data):
    global is_run
    if is_run:
        return
    is_run = True
    for x in range(len(data)-1):
        data[x]['bg'] = '#CCCCCC'
    number = random.randint(0, 20)
    lotttery_whirl(data, 0, number)

def create_label(name, x, y):
    label = Label(window, text=name, width=13, height=3, bg='#CCCCCC', font='宋体 -18 bold')
    label.place(anchor=NW, x=x, y=y)
    return label

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('500x290+250+150')
    window.title('      装盘抽奖器')

    bg_label = Label(window, width=80, height=24, bg='#ECf5FF')
    bg_label.place(anchor=NW, x=0, y=0)

    label_names = ['大衣', '植村秀口红BR784', '阿玛尼口红', '小米运动手环', '投影仪', '水晶球', '欧舒丹香氛礼盒', '米酒', 'coach包包', '金项链', '衣服']
    random.shuffle(label_names)
    label_names = label_names[:8]
    xs = [20, 180, 340, 340, 340, 180, 20, 20]
    ys = [20, 20, 20, 110, 200, 200, 200, 110]
    data = list()
    for name, x, y in zip(label_names, xs, ys ):
        data.append(create_label(name, x, y))
    button_core = Button(window, text='开  始', command=lambda: lottery_start(data), width=130, height=53, bg='#00CD00',
                        font='宋体 -18 bold', bitmap='gray50', compound=tkinter.CENTER)
    button_core.place(anchor=NW, x=180, y=110)




    window.mainloop()