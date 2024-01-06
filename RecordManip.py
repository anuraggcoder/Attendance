import numpy as np
import pandas as pd



df = pd.read_csv('Employee.csv')
df = df.drop_duplicates(subset=['Name','Month','Year','Day'])
df.to_csv('Employee.csv', index=False)


def sortrecord(dataframe, sort_key):
    '''
    This function sorts the Data Frame 'In Place' when the user
    specifies on which column he wants to perform sorting
    operation
    '''
    if sort_key in ['Name','Year','Month','Day','Attendance']:
        dataframe.sort_values('Day', inplace=True)
    else:
        print('Wrong Key for sort provided')

def displayrecord(by_name=False, by_year=False, by_month=False):
    '''
    This function displays record of the Data Frame based on the
    option provided by the user. These options are: Name, Year and
    Month. If non is provided .
    '''
    '''
    When you’re working with pandas and you want to combine boolean
    masks, you should use '&' instead of 'and'. This is because you want
    to compare each element in the Series individually (element-wise),
    not the whole Series object at once.
    '''
    mask = (df['Name'] == by_name) & (df['Year'] == by_year) & (df['Month'] == by_month)
    df2 = pd.DataFrame()
    df2 = df[mask].copy()
    sortrecord(df2,'Day')
    return df2
    


    
if __name__=='__main__':
    displayrecord('Anurag', 2024, 'February')

