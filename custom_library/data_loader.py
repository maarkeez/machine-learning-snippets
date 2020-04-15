from csv import reader

# Load a CSV file
def load_csv(filename):

    dataset = list()
    with open(filename, "r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row:
               dataset.append(row)

    print("Loaded data")
    print("\t- File: {0}".format(filename))
    print("\t- Rows: {0}".format(len(dataset)))
    print("\t- Columns: {0}".format(len(dataset[0])))
    return dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()

    for i, value in enumerate(unique):
        lookup[value] = i

    for row in dataset:
        row[column] = lookup[row[column]]

    return lookup

def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])

    return minmax

def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            value = row[i]
            min = minmax[i][0]
            max = minmax[i][1]
            row[i] = (value - min) / (max - min)
    return dataset