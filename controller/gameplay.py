from model.gameplay.dice import Dice
import model.gameplay.service as service
import numpy as np
import matplotlib.pyplot as plt

class GameplayController:
    def __init__(self, view):
        self.view = view

    def _generate_plot(self, success_dice_size, diff_dice_size, modifiers_range=10, case='>'):
        v = np.vectorize(service.compute_probs)

        x,y = np.mgrid[0:modifiers_range+1, 0:modifiers_range+1]
        x = [[Dice(success_dice_size, j) for j in i] for i in x]
        y = [[Dice(diff_dice_size, j) for j in i] for i in y]

        z = v(x, y, case)
        return z

    def calculate(self, event):
        success_dice_size = int(self.view.main_frame.left_frame.success_dice_entry.get())
        success_mod = int(self.view.main_frame.left_frame.success_mod_entry.get())
        diff_dice_size = int(self.view.main_frame.left_frame.diff_dice_entry.get())
        diff_mod = int(self.view.main_frame.left_frame.diff_mod_entry.get())
        case = self.view.main_frame.left_frame.case_combo.get()

        success_dice = Dice(success_dice_size, success_mod)
        diff_dice = Dice(diff_dice_size, diff_mod)

        total_cases = service.compute_total_cases(success_dice, diff_dice)
        fav_cases = service.compute_fav_cases(success_dice, diff_dice, case)
        probs = service.compute_probs(success_dice, diff_dice, case)
        
        self.view.main_frame.center_frame.reset()
        self.view.main_frame.center_frame.total_cases_label['text'] = self.view.main_frame.center_frame.total_cases_label['text'] + str(total_cases)
        self.view.main_frame.center_frame.fav_cases_label['text'] = self.view.main_frame.center_frame.fav_cases_label['text'] + str(fav_cases)
        self.view.main_frame.center_frame.probs_label['text'] = self.view.main_frame.center_frame.probs_label['text'] + str(probs)

        z = self._generate_plot(success_dice_size, diff_dice_size, case=case)
        self.view.main_frame.center_frame.redraw(z, success_dice=success_dice, diff_dice=diff_dice, case=case)

    def savefig(self, event):
        savepath = self.view.main_frame.center_frame.savefig_entry.get()
        fig = self.view.main_frame.center_frame.fig
        fig.savefig(savepath)
