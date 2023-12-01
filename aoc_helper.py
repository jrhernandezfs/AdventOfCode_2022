# Function for opening input
def open_input(filename) :
    with open(filename, 'r') as f:
        lines = f.readlines()
        measurements = [entry.strip() for entry in lines]
        return measurements
