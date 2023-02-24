class Category:
    def __init__(self, name):
        self.name = name

    def priority(self, name):
        match name:
            case 'Bills':
                return 'A'
            case 'Work':
                return 'A'
            case 'Gym':
                return 'B'
            case 'Shopping':
                return 'B'
            case 'Plans':
                return 'C'
            case 'Fun':
                return 'C'

    def features(self, name):
        match name:
            case 'Bills':
                deadline = input("Deadline: ")

                #  amount = input("Amount: ")
                return deadline  # +"&"+amount
            case 'Work':
                return input("Deadline: ")
            case 'Gym':
                return 'B'
            case 'Shopping':
                return 'B'
            case 'Plans':
                return 'C'
            case 'Fun':
                return 'C'


    # GETTERS N SETTERS
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
