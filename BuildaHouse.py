##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
# Crating body of the house
square = drawpad.create_rectangle(230,240,500,490, fill='Red')

# Creating the roof
line1 = drawpad.create_line(365,100,230,240)
line2 = drawpad.create_line(365,100,500,240)

# Door Creation
rectangle = drawpad.create_rectangle(330,380,400,490, fill='brown')
oval = drawpad.create_oval(335,430,345,440, fill='yellow')

# Creating the windows
square = drawpad.create_rectangle(250,260,320,330, fill='light blue')
square = drawpad.create_rectangle(410,260,480,330, fill='light blue')

#Chimney Creation
line3 = drawpad.create_line(420,110,420,157)
line4 = drawpad.create_line(420,110,460,110)
line5 = drawpad.create_line(460,110,460,200)

# Lawn
rectangle = drawpad.create_rectangle(0,490,800,600, fill='green')

root.mainloop()



