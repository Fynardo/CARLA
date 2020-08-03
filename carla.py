from controller.main import MainController
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('{}x{}'.format(1024, 728))
    root.title("CAldeiro Research LAb, alpha 0.1")
    app = MainController(root)
    root.mainloop()
