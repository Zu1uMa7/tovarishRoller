import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy

def roll_dice(dice_type):
    return random.randint(1, dice_type)

def roll_button_clicked():
    all_results=[]
    total_results = []
    for j in range(int(num_rolls.get())):
        results = []
        for i in range(int(num_dice.get())):
            roll_result = roll_dice(int(dice_type.get()[1:]))
            results.append(roll_result)
            all_results.append(roll_result)
    
        if sum_dice.get():
            total_result = sum(results)
            total_results.append(total_result)

    if sum_dice.get():
        if (int(num_rolls.get())>1):
            result_text.set("Media: {:0.3f}, Varianza: {:0.3f}".format(sum(total_results)/len(total_results), numpy.var(total_results)))
            plot_results(total_results)
        else:
            result_text.set("Result: {}  <-{}".format(total_result,results))
    else:
        if (int(num_dice.get())*int(num_rolls.get())>1):
            result_text.set("Media: {:0.3f}, Varianza: {:0.3f}".format(sum(all_results)/len(all_results), numpy.var(all_results)))
            plot_results(all_results)
        else:
           result_text.set("Result: {}".format(roll_result))

def plot_results(results):
    if(sum_dice.get() and int(num_dice.get())!=0):
        dice_max=int(dice_type.get()[1:])*int(num_dice.get())
    else:
        dice_max=int(dice_type.get()[1:])
    plt.clf()
    plt.hist(results, align='left', rwidth=0.3, bins=range(0,dice_max+2))
    plt.xlabel('Risultati')
    plt.ylabel('Frequenza')
    plt.title('Lanci di dado')
    if dice_max<50:
        plt.xticks(numpy.arange(0, dice_max+2))
    plt.show()

root = tk.Tk()
root.title("Tovarish Dice Roller")
root.geometry("480x150")

# UI elements
dice_type = ttk.Combobox(root, values=['d2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd30', 'd100'], width=5)
dice_type.current(0)
num_dice= tk.Entry(root, width=3)
num_dice.insert(0, '1')
num_rolls = tk.Entry(root, width=6)
num_rolls.insert(0, '1')
sum_dice = tk.BooleanVar()
sum_check = tk.Checkbutton(root, text='Somma i risultati', variable=sum_dice)
roll_button = tk.Button(root, text='Lancia i dadi', command=roll_button_clicked)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)

# layout
dice_type.grid(row=0, column=1, padx=5, pady=5)
num_dice.grid(row=0, column=0, padx=5, pady=5)
num_rolls.grid(row=0, column=2, padx=5, pady=5)
sum_check.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
roll_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=3, column=3, columnspan=3, padx=5, pady=5)


root.mainloop()