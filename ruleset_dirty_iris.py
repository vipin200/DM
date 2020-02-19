def check_species(df):
    ch = df["Species"].isin(['setosa' , 'versicolor' , 'virginica'])
    return ch
def check_positive(data):
    return ((data.iloc[:,:-1] > 0).apply(lambda x: x[0] and x[1] and x[2] and x[3], axis = 1))

def ch_petal_length_twice(df):
    ch = df['Petal.Length'] >= (2 * df['Petal.Width'])
    return ch

def ch_sepal_length_30(df):
    ch = df['Sepal.Length'] <= 30
    return ch

def  sepal_longer_petal(df):
    ch = df['Sepal.Length'] > df['Petal.Length']
    return ch