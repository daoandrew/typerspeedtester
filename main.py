from tkinter import *
import random
import math

# ----------CONTSTANTS--------#
TEXTS = [
    ''' 
She asked the question even though she didn't really want to hear the answer. It was a no-win situation since she already knew. If he told the truth, she'd get confirmation of her worst fears. If he lied, she'd know that he wasn't who she thought he was which would be almost as bad. Yet she asked the question anyway and waited for his answer.
Breastfeeding is good for babies and moms. Infants that are breastfed get antibodies from their mothers against common illnesses. Breastfed babies have less chance of being obese as an adult. Breastfeeding a baby lets the infant-mother pair bond in a very unique way. Mother’s who breastfeed lower their chances of developing breast cancer. Usually, mothers who breastfeed lose their pregnancy weight more quickly and easily. The benefits of breastfeeding are numerous.
Rhonda prided herself on always taking the path less traveled. She'd decided to do this at an early age and had continued to do so throughout her entire life. It was a point of pride and she would explain to anyone who would listen that doing so was something that she'd made great efforts to always do. She'd never questioned this decision until her five-year-old niece asked her, "So, is this why your life has been so difficult?" and Rhonda didn't have an answer for her.
Samantha wanted to be famous. The problem was that she had never considered all the downsides to actually being famous. Had she taken the time to objectively consider these downsides, she would have never agreed to publically sing that first song.
Green vines attached to the trunk of the tree had wound themselves toward the top of the canopy. Ants used the vine as their private highway, avoiding all the creases and crags of the bark, to freely move at top speed from top to bottom or bottom to top depending on their current chore. At least this was the way it was supposed to be. Something had damaged the vine overnight halfway up the tree leaving a gap in the once pristine ant highway.''',
    '''
    Sleeping in his car was never the plan but sometimes things don't work out as planned. This had been his life for the last three months and he was just beginning to get used to it. He didn't actually enjoy it, but he had accepted it and come to terms with it. Or at least he thought he had. All that changed when he put the key into the ignition, turned it and the engine didn't make a sound.
It was the first day of the rest of her life. This wasn't the day she was actually born, but she knew that nothing would be the same from this day forward. Although this was a bit scary to her, it was also extremely freeing. Her past was no longer a burden or something that she needed to be concerned about and defend. She threw off the covers keeping her warm in bed, placed her feet over the side of the bed, slipped on her slipper, and took the first step of the first day of her new life.
It was difficult for him to admit he was wrong. He had been so certain that he was correct and the deeply held belief could never be shaken. Yet the proof that he had been incorrect stood right before his eyes. "See daddy, I told you that they are real!" his daughter excitedly proclaimed.
I haven't bailed on writing. Look, I'm generating a random paragraph at this very moment in an attempt to get my writing back on track. I am making an effort. I will start writing consistently again!
It had been a rough day. Things hadn't gone as planned and that meant Hannah got yelled at by her boss. It didn't even matter that it wasn't her fault. When things went wrong at work, Hannah got the blame no matter the actual circumstances. It wasn't fair, but there was little she could do without risking her job, and she wasn't in a position to do that with the plans she had.
    ''',
    '''
    Many people say that life isn't like a bed of roses. I beg to differ. I think that life is quite like a bed of roses. Just like life, a bed of roses looks pretty on the outside, but when you're in it, you find that it is nothing but thorns and pain. I myself have been pricked quite badly.
She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work?
Sometimes it's the first moment of the day that catches you off guard. That's what Wendy was thinking. She opened her window to see fire engines screeching down the street. While this wasn't something completely unheard of, it also wasn't normal. It was a sure sign of what was going to happen that day. She could feel it in her bones and it wasn't the way she wanted the day to begin.
The house was located at the top of the hill at the end of a winding road. It wasn't obvious that the house was there, but everyone in town knew that it existed. They were just all too afraid to ever go and see it in person.
He heard the crack echo in the late afternoon about a mile away. His heart started racing and he bolted into a full sprint. "It wasn't a gunshot, it wasn't a gunshot," he repeated under his breathlessness as he continued to sprint.
    '''
]

FONT_NAME = "Courier"
WORK_MIN = 1


# -----------WORD COUNT-----------#

def word_count(prompt_txt, inp_txt):
    count = 0
    list_words = prompt_txt.split()
    input_words = inp_txt.split()
    for i in range(len(input_words)):
        if input_words[i] == list_words[i]:
            count += 1
    return f"Your type speed is {count} WPM"


# -----------TIMER LOGIC-----------#

def start_timer():
    work_sec = WORK_MIN * 60
    count_down(work_sec)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_text.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        wpm.config(text=word_count(prompt_txt=text, inp_txt=inptxt.get("1.0",END)))

def reset_timer():
    window.after_cancel(timer)
    timer_text.config(text="00:00")
    


# -------UI------#
# For window of Tkinter and size
window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50)

# To label the app
title_label = Label(text="Speed Typer")
title_label.grid(column=0, row=0)

# to show text prompt
text = random.choice(TEXTS)
prompt = Message(text=text)
prompt.grid(column=0, row=2)

# Timer
timer_text = Label(text="00:00", font=(FONT_NAME, 12, "bold"))
timer_text.grid(column=1, row=0, columnspan=1)

# WPM
wpm = Label(text="")
wpm.grid(column=2, row=0)

# Start timer and reset buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=1)

# to show the input box
inptxt = Text(window, height=30, width=60, highlightthickness=0)
inptxt.grid(column=1, row=2, columnspan=2)

window.mainloop()
