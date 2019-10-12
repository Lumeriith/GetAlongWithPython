import tkinter as tk
import math, random

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
    
    def is_outside(self):
        pos = self.get_position()
        return pos[0] > canvas.winfo_width() or pos[0] < 0 or pos[1] > canvas.winfo_height() or pos[1] < 0


    def delete(self):
        self.canvas.delete(self.item)


class GameText(object):
    def __init__(self, text, x, y, color='black', size='40'):
        global canvas
        global objects
        self.canvas = canvas
        if type(color) == tuple:
            self.item = self.canvas.create_text(x, y, text=str(text), font=('Helvetica', size), fill='#%02x%02x%02x' % color)
        else:
            self.item = self.canvas.create_text(x, y, text=str(text), font=('Helvetica', size), fill=color)
        objects.append(self)

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

    def set_text(self, text):
        self.canvas.itemconfig(self.item, text=text)
        
    def is_outside(self):
        pos = self.get_position()
        return pos[0] > canvas.winfo_width() or pos[0] < 0 or pos[1] > canvas.winfo_height() or pos[1] < 0


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
        self.canvas.bind("<1>", lambda event: self.canvas.focus_set())

    def get_distance(self, a, b):
        coords_a = self.canvas.coords(a.item)
        coords_b = self.canvas.coords(b.item)
        return math.sqrt((coords_a[0] - coords_b[0]) ** 2 + (coords_a[1] - coords_b[1]) ** 2)

    def get_direction(self, from_, to):
        coords_from = self.canvas.coords(from_.item)
        coords_to = self.canvas.coords(to.item)
        vector = coords_to[0] - coords_from[0], coords_to[1] - coords_from[1]
        magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        return vector[0] / magnitude, vector[1] / magnitude

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

    def link(self, key, function):
        self.canvas.bind(key, lambda _: function())
        
    def get_random_edge(self):
        choice = random.randrange(0, 4)
        if choice == 0:
            x = 0
            y = random.randrange(0, self.canvas.winfo_height())
        elif choice == 1:
            x = self.canvas.winfo_width()
            y = random.randrange(0, self.canvas.winfo_height())
        elif choice == 2:
            x = random.randrange(0, self.canvas.winfo_width())
            y = 0
        else:
            x = random.randrange(0, self.canvas.winfo_width())
            y = self.canvas.winfo_height()
        return [x, y]