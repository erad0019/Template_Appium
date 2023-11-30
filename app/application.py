
from features.pages_object.InitialSteps_Page import InitialStepsPage

class Application:
    def __init__(self, driver):
        self.InitialStepsPage = InitialStepsPage(driver)
