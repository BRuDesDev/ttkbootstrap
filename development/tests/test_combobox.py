import tkinter as tk
import ttkbootstrap as ttk


DARK = 'superhero'
LIGHT = 'flatly'

def create_combobox_test(bootstyle, style, test_name):
    frame = ttk.Frame(padding=10)

    # title
    title = ttk.Label(
        master=frame, 
        text=test_name, 
        anchor=tk.CENTER
    )
    title.pack(padx=5, pady=2, fill=tk.BOTH)
    ttk.Separator(frame).pack(padx=5, pady=5, fill=tk.X)

    # default
    cbo = ttk.Combobox(
        master=frame, 
        values=['default', 'other'], 
        bootstyle=bootstyle
    )
    cbo.pack(padx=5, pady=5, fill=tk.BOTH)
    cbo.current(0)

    # color
    for color in style.theme.colors:
        cbo = ttk.Combobox(
            master=frame, 
            values=[color, 'other'], 
            bootstyle=(color, bootstyle)
        )
        cbo.pack(padx=5, pady=5, fill=tk.BOTH)
        cbo.current(0)

    # disabled
    cbo = ttk.Combobox(
        master=frame, 
        values=[bootstyle,'other'], 
        bootstyle=bootstyle, 
        state=tk.DISABLED
    )
    cbo.pack(padx=5, pady=5, fill=tk.BOTH)
    cbo.current(0)

    return frame


if __name__ == '__main__':
    # create visual widget style tests
    root = tk.Tk()
    style = ttk.Style()

    test1 = create_combobox_test('TCombobox', style, 'Combobox')
    test1.pack(side=tk.LEFT, fill=tk.BOTH)

    root.mainloop()