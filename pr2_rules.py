def check_species(dataset):
    return (dataset["Species"].isin(["setosa","versicolor","virginica"]))

def check_validity(dataset):
    return (dataset.iloc[:,:4] > 0)

def check_petal_length_width(dataset):
    return (dataset["Petal.Length"] >= 2*dataset["Petal.Width"])

def check_sepal_length(dataset):
    return (dataset["Sepal.Length"] <= 30)

def check_sepal_petal(dataset):
    return (dataset["Sepal.Length"] > dataset["Petal.Length"])