import tkinter as tk

class CaptureBox(tk.Toplevel):
    def __init__(
        self,
        box_color: str = "blue",
        box_alpha: float = 0.3,
        box_x: int = 100,
        box_y: int = 100,
        box_width: int = 300,
        box_height: int = 200,
        text: str = ""
    ):
        super().__init__()
        self.capture_width, self.capture_height = box_width, box_height
        self.capture_x, self.capture_y = box_x, box_y
        self.geometry(f"{self.capture_width}x{self.capture_height}+{self.capture_x}+{self.capture_y}")
        self.overrideredirect(True)
        self.configure(bg=box_color)

        self.attributes("-alpha", box_alpha)
        self.attributes("-topmost", True)

        self.BORDER_WIDTH = 8
        self.MIN_SIZE = 20

        # Unified move/resize bindings
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<Motion>", self.update_cursor)

        self.text_label = tk.Label(self, text=text, bg=box_color, font=("Arial", 10, "bold"))
        self.text_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Bind events to label too as it blocks parent events
        self.text_label.bind("<ButtonPress-1>", self.on_press)
        self.text_label.bind("<B1-Motion>", self.on_drag)
        self.text_label.bind("<Motion>", self.update_cursor)

    def get_region(self, event):
        """Determine which region of the window the mouse is in."""
        if event.widget == self:
            x, y = event.x, event.y
        else:
            x = event.x_root - self.winfo_rootx()
            y = event.y_root - self.winfo_rooty()
            
        w = self.winfo_width()
        h = self.winfo_height()
        
        region = 0
        if y < self.BORDER_WIDTH: region |= 1 # N
        elif y > h - self.BORDER_WIDTH: region |= 2 # S
        if x < self.BORDER_WIDTH: region |= 4 # W
        elif x > w - self.BORDER_WIDTH: region |= 8 # E
        return region

    def update_cursor(self, event):
        """Update cursor based on mouse position."""
        region = self.get_region(event)
        if region == 0:
            cursor = "fleur" # Move cursor
        elif region in [1, 2]:
            cursor = "size_ns"
        elif region in [4, 8]:
            cursor = "size_we"
        elif region in [5, 10]:
            cursor = "size_nw_se"
        elif region in [6, 9]:
            cursor = "size_ne_sw"
        else:
            cursor = ""
        
        self.configure(cursor=cursor)
        self.text_label.configure(cursor=cursor)

    def on_press(self, event):
        """Store initial position and state for drag operations."""
        self.press_region = self.get_region(event)
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.orig_x = self.winfo_x()
        self.orig_y = self.winfo_y()
        self.orig_w = self.winfo_width()
        self.orig_h = self.winfo_height()

    def on_drag(self, event):
        """Handle moving and resizing."""
        dx = event.x_root - self.start_x
        dy = event.y_root - self.start_y
        
        new_x, new_y = self.orig_x, self.orig_y
        new_w, new_h = self.orig_w, self.orig_h

        if self.press_region == 0:
            # Move
            new_x += dx
            new_y += dy
        else:
            # Resize
            if self.press_region & 1: # N
                if self.orig_h - dy >= self.MIN_SIZE:
                    new_y = self.orig_y + dy
                    new_h = self.orig_h - dy
                else:
                    new_h = self.MIN_SIZE
                    new_y = self.orig_y + self.orig_h - self.MIN_SIZE
            elif self.press_region & 2: # S
                new_h = max(self.MIN_SIZE, self.orig_h + dy)
            
            if self.press_region & 4: # W
                if self.orig_w - dx >= self.MIN_SIZE:
                    new_x = self.orig_x + dx
                    new_w = self.orig_w - dx
                else:
                    new_w = self.MIN_SIZE
                    new_x = self.orig_x + self.orig_w - self.MIN_SIZE
            elif self.press_region & 8: # E
                new_w = max(self.MIN_SIZE, self.orig_w + dx)

        # Update both internal state and window geometry
        self.capture_x, self.capture_y = new_x, new_y
        self.capture_width, self.capture_height = new_w, new_h
        self.geometry(f"{new_w}x{new_h}+{new_x}+{new_y}")
