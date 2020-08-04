from os import setgroups
from model.gameplay.dice import Dice
import model.randomwalk.service as service
import numpy as np
import matplotlib.pyplot as plt

class RandomwalkController:
    def __init__(self, view):
        self.view = view

    def calculate_walk(self, event):
        length = int(self.view.main_frame.left_frame.walk_length_entry.get())
        steps = eval(self.view.main_frame.left_frame.steps_entry.get())
        probs = eval(self.view.main_frame.left_frame.probs_entry.get())

        grid = self.view.main_frame.left_frame.grid_chk_var.get()
        x = np.arange(length)
        walk = service.simulate_walk(steps, length, probs)
        self.view.main_frame.center_frame.redraw(x, walk, grid)

        simulated_steps = service.simulate_steps(steps, length, probs)

        self.view.main_frame.center_frame.up_steps_label['text'] = 'Up steps: '+ str(sum(filter(lambda x: x == 1, simulated_steps)))
        self.view.main_frame.center_frame.plain_steps_label['text'] = 'Plain steps: '+ str(len(list(filter(lambda x: x == 0, simulated_steps))))
        self.view.main_frame.center_frame.down_steps_label['text'] = 'Down steps: '+ str(len(list(filter(lambda x: x == -1, simulated_steps))))


    def savefig(self, event):
        savepath = self.view.main_frame.center_frame.savefig_entry.get()
        fig = self.view.main_frame.center_frame.fig
        fig.savefig(savepath)
