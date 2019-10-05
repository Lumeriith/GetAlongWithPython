import tkinter as tk

objects = []
class GameImage(object):
    def __init__(self, file, x, y):
        global canvas
        global objects
        self.canvas = canvas

        self.image = tk.PhotoImage(file=file)
        self.item = canvas.create_image((x, y), image=self.image)
        objects.append(self)
    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


class GameText(object):
    def __init__(self, text, x, y, color='black', size='40'):
        global canvas
        global objects
        self.canvas = canvas
        if type(color) == tuple:
            self.item = self.canvas.create_text(x, y, text=text, font=('Helvetica', size), fill='#%02x%02x%02x' % color)
        else:
            self.item = self.canvas.create_text(x, y, text=text, font=('Helvetica', size), fill=color)
        objects.append(self)
    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


class GameWindow(tk.Frame):
    def __init__(self, name, width, height, color):
        global master, canvas
        self.root = tk.Tk()
        self.root.title(name)
        super(GameWindow, self).__init__(self.root)

        master = self.root
        self.width = width
        self.height = height
        if type(color) == tuple:
            self.canvas = tk.Canvas(self, bg='#%02x%02x%02x' % color, width=self.width, height=self.height)

        else:
            self.canvas = tk.Canvas(self, bg=color, width=self.width, height=self.height,)
        canvas = self.canvas
        self.canvas.pack()
        self.pack()
        self.root.bind('<Motion>', self.motion)
        self.mouse_x = 0
        self.mouse_y = 0

    def motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def start_loop(self, function, time):
        self.loop_function = function
        self.loop_time = time

        self.do_loop()
        self.mainloop()

    def do_loop(self):
        self.loop_function()
        self.after(int(self.loop_time * 1000), self.do_loop)