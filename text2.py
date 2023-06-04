from tkinter import *
win=Tk()

win.geometry("900x900")

text1 =Text(win, height=30, width=60)
photo = PhotoImage(file='apple1.png')
text1.insert(END, '\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)


text2 = Text(win, height=30, width=60)
scroll = Scrollbar(win, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold', font=('Arial', 12, 'bold'))
text2.tag_configure('bold_italic', font=('Verdana', 20, 'bold','italic'),foreground="red")
text2.tag_configure('matter',
                    foreground='black',
                    font=('Helvetica', 12),wrap=WORD)

text2.insert(END,'\n PROVERB FOR THE DAY', 'bold')
text2.insert(END,'\n An apple a day keeps the doctor away \n', 'bold_italic')
proverb1 = """
An apple a day keeps the doctor away - is a common English-language proverb that appeared in the 19th century, advocating for the consumption of apples, and by extension, "if one eats healthy foods, one will remain in good health and will not need to see the doctor often.
"""
text2.insert(END, proverb1, 'matter')

text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

win.mainloop()
