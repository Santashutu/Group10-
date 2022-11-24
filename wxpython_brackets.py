import wx

# import the newly created GUI file
import demo
app = wx.App()
window = wx.Frame(None, title = "Brackets Code", size = (300,200))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = "To exit, press #", pos = (100,50))
class CalcFrame(demo.MyFrame1):
   def __init__(self,parent):
      demo.MyFrame1.__init__(self,parent)

print(f'// To exit, press "#"')
b_list = []
o_list = []
brackets_dict = {
    '[': ']', '<': '>','{': '}','(': ')'
}
#Loop to enter code
i = 1
while True:
    code = input(f'{i}:\t')

    # Loops for individual characters
    for char in code:
        if '{' == char or '(' == char or '[' == char or '<' == char:

            if len(b_list) > 0:
                if b_list[-1] == '<' and char != '>':
                    o_list.append(char)

            b_list.append(char)

        elif '}' == char or ')' == char or ']' == char or '>' == char:
            if len(b_list) > 0:
                if brackets_dict[b_list[-1]] == char:
                    b_list.pop()
                else:
                    o_list.append(char)
            else:
                o_list.append(char)

    # Break the Code
    if code == '#':
        break

    i += 1

if len(b_list) == 0 and len(o_list) == 0:
    print("Good! Well Nested")

elif len(b_list) > 0 or len(o_list) > 0:
    print("Oops! Work on your Nesting")

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
