from view.functions import FunctionsFrame
from view.gameplay import GameplayFrame
from view.main import MainFrame
from controller.gameplay import GameplayController
from controller.functions import FunctionsController
import model.functions.service as functions_service


class MainController:
    def __init__(self, root):
        self.root = root
        self.app = MainFrame(root, self)
        self.app.set_main_frame(GameplayFrame(self.app, GameplayController(self.app))) # Default Frame

    def selection_changed(self, event):
        f_name = self.app.selection_frame.utilities_combo.get()
        if f_name == 'Gameplay':
            self.app.main_frame.destroy()
            self.app.set_main_frame(GameplayFrame(self.app, GameplayController(self.app)))
            
        if f_name == 'Functions':
            self.app.main_frame.destroy()
            self.app.set_main_frame(FunctionsFrame(self.app, FunctionsController(self.app), functions_service.get_available_functions())) 