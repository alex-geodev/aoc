def read_input(filepath: str)->str:
    with open(filepath) as f:
        data = f.read()
        return data
