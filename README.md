# Tkconverter
 An object oriented version of a temperature converter

 # source https://www.pythontutorial.net/tkinter/tkraise/

 Special thanks to @MrLiu00 for the solution to fix the frame instances issue. The source tutorial mistankenly creates multiple frame instances on load, I mistakenly carried over this error in converting the tutorial to OOP. Although the tutorial and the OOP conversion "worked" they also broke the ability to properly use keybindings. The solutuion is to create the frame instances on frame switching.
