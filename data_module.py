import pandas as pd

def load_data():
        
    data = {
        "Name": ["Anna", "Bob", "Charlie", "Diana", "Eric"],
        "Age": [20, 34, 23, None, 33],
        "Gender": ["f", "m", "m", "f", "m"],
        "Job": ["Programmer", "Writer", "Cook", "Programmer", "Teacher"],
    }

    df = pd.DataFrame(data)
    return df


