import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Visual novel") 
window.geometry("400x400") 

story = "You're walking down the street and see a cute cat"

def petCat():
  global story
  canvas.itemconfig(container, image=cat2)
  story = "He thanks you for the pet and grants you 3 wishes"
  storyLabel["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()

def wishes():
  global story
  canvas.itemconfig(container, image=cat3)
  story = "You can't wish for more wishes!"
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()
  button2.pack()

def anotherCat():
  global story
  canvas.itemconfig(container, image=cats)
  story = "So many lovely cats!"
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()

def keepWalking():
  global story
  canvas.itemconfig(container, image=cat3)
  story = "You find another cat"
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  button2.pack_forget()
  restartButton.pack_forget()
  button.pack()
  button5.pack()

def restart():
  global story
  canvas.itemconfig(container, image=cat1)
  story = "You're walking down the street and see a v cute cat"
  storyLabel["text"] = story
  restartButton.pack_forget()
  button.pack()
  button2.pack()

def ignoreCat():
  global story
  canvas.itemconfig(container, image=sadcat)
  story = "You made the cat sad :("
  storyLabel["text"] = story
  button.pack_forget()
  button5.pack_forget()
  restartButton.pack()
  
cat1 = tk.PhotoImage(file=".tutorial/cat.png")
cat1 = cat1.subsample(4)
cat2 = tk.PhotoImage(file=".tutorial/cat2.png")
cat2 = cat2.subsample(4)
cat3 = tk.PhotoImage(file=".tutorial/cat3.png")
cat3 = cat3.subsample(4)
cats = tk.PhotoImage(file=".tutorial/cats.png")
cats = cats.subsample(4)
sadcat = tk.PhotoImage(file=".tutorial/sadcat.png")
sadcat = sadcat.subsample(4)

canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()
container = canvas.create_image(150,150, image=cat1)
storyLabel = tk.Label(text=story)
storyLabel.pack()
button = tk.Button(text = "Pet the cat", command = petCat)
button.pack()
button2 = tk.Button(text="Keep walking", command=keepWalking)
button2.pack()
button3 = tk.Button(text="Wish for more wishes", command = wishes)
button4 = tk.Button(text="Wish for more cats", command=anotherCat)
restartButton = restartButton = tk.Button(text="Start again", command=restart)
button5 = tk.Button(text="Ignore this cat too", command=ignoreCat)

