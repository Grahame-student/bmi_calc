class BmiCalc:
    def __init__(self, height, weight):
        """
        simple BMI calculator
        height is in cm
        weight is in kg
        """
        self.height = 0
        self.weight = 0

        self.set_height(height)
        self.set_weight(weight)

    def set_height(self, new_height):
        # convert from cm to m
        self.height = new_height / 100

    def set_weight(self, new_weight):
        self.weight = new_weight

    def get_bmi(self):
        if self.height == 0:
            return "0"
        else:
            return f"{self.weight / (self.height * self.height)}"
