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

    
    # GETTERS N SETTERS
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
