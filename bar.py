import tkinter as tk


class Bar:
    def __init__(self, window):
        self.window = window
        self.bar_canvas = None
        self.bar_text = None
        self.bar = None

    def update_bar(self, time, snipe_time):
        if (snipe_time - 1 < time) and (snipe_time > time):
            self.bar_canvas.itemconfig(self.bar, fill='green')
        else:
            self.bar_canvas.itemconfig(self.bar, fill='orange')
        fill = 1 + (round((time - snipe_time) * 1000) % 1000) / 2.5
        self.bar_canvas.coords(self.bar, 1, 1, fill, 41)

    def setup_window(self):
        self.bar_canvas = tk.Canvas(self.window, width=400, height=40, background="grey")

        # Colored loading bar
        self.bar = self.bar_canvas.create_rectangle(1, 1, 201, 41, fill="orange", width=0)
        self.bar_text = self.bar_canvas.create_text((200, 20), font="calibri 20 bold", width=300)

        return self.bar_canvas
