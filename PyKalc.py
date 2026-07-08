import customtkinter as ctk
import sys
import os

if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "icon.ico")
else:
    icon_path = "icon.ico"

# Set the app to dark theme
ctk.set_appearance_mode("dark")

class PyKalc(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PyKalc")
        self.geometry("350x550")
        self.resizable(False, False)
        self.iconbitmap(icon_path)

        # Config on how the grid works
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        # Build UI
        self.create_display()
        self.create_buttons()

        self.expression = ""

    # The top display (where the numbers appear!)
    def create_display(self):
        self.display = ctk.CTkEntry(
            self,
            height = 120,
            font=("Arial", 32, "bold"),
            justify = "right",
            fg_color = "#1E1E1E",
            text_color = "white",
            placeholder_text = "0"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=(20, 10), sticky="ew")

    # Quick press animation (Squishy squish effect? kind of?!?)
    def animation_press(self, button):
        original_height = button.cget("height")

        button.configure(height=original_height - 10)
        self.after(80, lambda: button.configure(height=original_height))

    # All of the button creation
    def create_buttons(self):
        # Button style config
        button_style = {
            "height": 70,
            "font": ("Arial", 20),
            "corner_radius": 12,
            "border_spacing": 0
        }

        # Buttons (text, row, column, colour)
        buttons = [
            ("C", 1, 0, "#FF3B5C"), ("⌫", 1, 2, "#2D2D2D"), ("/", 1, 3, "#FF9500"),
            ("7", 2, 0, "#2D2D2D"), ("8", 2, 1, "#2D2D2D"), ("9", 2, 2, "#2D2D2D"), ("*", 2, 3, "#FF9500"),
            ("4", 3, 0, "#2D2D2D"), ("5", 3, 1, "#2D2D2D"), ("6", 3, 2, "#2D2D2D"), ("-", 3, 3, "#FF9500"),
            ("1", 4, 0, "#2D2D2D"), ("2", 4, 1, "#2D2D2D"), ("3", 4, 2, "#2D2D2D"), ("+", 4, 3, "#FF9500"),
            ("0", 5, 0, "#2D2D2D"), (".", 5, 2, "#2D2D2D"), ("=", 5, 3, "#FF9500")
        ]

        for text, row, col, color in buttons:
            btn = ctk.CTkButton(
                self,
                text = text,
                fg_color = color,
                hover_color = "#3D3D3D" if color == "#2D2D2D" else "#FFB143",
                text_color = "white",
                **button_style,

                command = lambda t=text, b=None: self.button_pressed(t, b)
            )

            # Place the button on grid
            if text == "0":
                btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="ew")
            elif text == "C":
                btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="ew")
            else:
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

            # Button connection to the func with animation
            btn.configure(command=lambda t=text, b=btn: self.button_pressed(t, b))

    # BUTTON PRESS!!
    def button_pressed(self, value, button=None):
        if button:
            self.animation_press(button) # Play the squishy anim

        if value == "C":
            self.display.delete(0, "end")
            self.expression = ""
        elif value == "=":
            try:
                result = eval(self.expression)
            except:
                self.expression = ""
                self.display.delete(0, "end")
                self.display.insert(0, self.expression)
            else:
                self.expression = result
                self.expression = str(self.expression)
                self.display.delete(0, "end")
                self.display.insert(0, self.expression)
        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.display.delete(0, "end")
            self.display.insert(0, self.expression)
        else:
            self.expression += value
            self.display.delete(0, "end")
            self.display.insert(0, self.expression)

# Create & RUN!!
app = PyKalc()
app.mainloop()
