import tkinter as tk
import ttkbootstrap as ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
style = ttk.Style("lumen")

frame = ttk.Frame(padding=5)
frame.pack(padx=5, pady=5, fill=tk.X)

top_frame = ttk.Frame(frame)
bot_frame = ttk.Frame(frame)

top_frame.pack(fill=tk.X)
bot_frame.pack(fill=tk.X)

# for i, color in enumerate(['default', *style.colors]):
#     if i < 5:
#         f = ttk.Frame(top_frame)
#     else:
#         f = ttk.Frame(bot_frame)

#     ttk.Label(f, text=color, width=20).pack(side=tk.TOP)
#     a = ttk.Progressbar(f, bootstyle=color, orient=tk.HORIZONTAL)
#     a.pack(fill=tk.X)
#     a.start()
#     f.pack(side=tk.LEFT, padx=3, pady=10, fill=tk.X)

for i, color in enumerate(['default', *style.colors]):
    if i < 5:
        f = ttk.Frame(top_frame)
    else:
        f = ttk.Frame(bot_frame)

    ttk.Label(f, text=color, width=20).pack(side=tk.TOP)
    a = ttk.Progressbar(f, bootstyle=color+'striped', orient=tk.HORIZONTAL)
    a.pack(fill=tk.X)
    a.start()
    f.pack(side=tk.LEFT, padx=3, pady=10, fill=tk.X)

root.mainloop()
