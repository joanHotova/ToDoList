from Category import Category


class GymCategory(Category):

    def __init__(self, name, timecap, cals):
        super().__init__(name)
        self.timecap = timecap
        self.cals=cals

 # GETTERS N SETTERS
    def get_timecap(self):
        return self.timecap
    def set_timecap(self, timecap):
        self.timecap = timecap

    def get_cals(self):
        return self.cals
    def set_cals(self, cals):
        self.cals = cals
