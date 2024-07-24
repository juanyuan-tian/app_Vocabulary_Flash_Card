from tkinter import *
import pandas
import random

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = ()
# data = pandas.read_csv("./data/french_words.csv")
# to_learn = data.to_dict(orient="records")

# check if words to learn exists
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    data = pandas.read_csv("./data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")

# $$$$$$$$$$$$$$$$$$$$$    next cards        $$$$$$$$$$$$$$$$$$$
def is_known():
    # 这些重复的其实也可以直接call func 👀👉👉👉👉😈😈👉👉👉👉😈😈👉👉👉👉😈😈
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # 点下个词就先取消倒计时
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)



    # with open("./data/words_to_learn.csv", "w"):

# random_pick = random.randint(0, len(new_data))
# new_fr_word = new_data[random_pick]["French"]
# 😭😭😭函数😭内外😭都有random，pick，保证一点开就随机找了个法语词汇😭😭
# 👀👉👉👉👉😈😈👉👉👉👉😈😈👉👉👉👉😈😈 就在函数内部，然后call这个函数 避免重复

# step4：现在认识不认识都共用一个next_card函数，如果不想重复新建一个，就要找到button键的区别，
# 知道是yes还是no,是yes的话删除数字,我肯定选择分开
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # 点下个词就先取消倒计时
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card) # 每个单词都会flip，👀👀👉👉👉把倒计时加回去

#     random_pick = random.randint(0, len(new_data))
#     new_fr_word = new_data[random_pick]["French"]
#     canvas.itemconfig(word, text=new_fr_word)
#     # canvas.itemconfig(title, text="French")
#     return random_pick

# $$$$$$$$$$$$$$$$$$$$$    flip cards        $$$$$$$$$$$$$$$$$$$
def flip_card():
    canvas.itemconfig(bg_image, image=card_back_img)
    canvas.itemconfig(word, text=current_card["English"], fill="red")
    canvas.itemconfig(title, text="English", fill="red")

# $$$$$$$$$$$$$$$$$$$$$    UI        $$$$$$$$$$$$$$$$$$$
window = Tk()
window.title("flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)  # after 用来倒计时
# canvas
canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
bg_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

# button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)
# 先换卡片，不要显示default的word title
next_card()



# window.after(3000)



window.mainloop()
