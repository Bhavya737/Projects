import pandas as pd

book={ 'Book Name':['Data Structures','Java','Python','DBMS','C & C++','Software Engineering','Software Testing','File structures','Maths','English'],
        'Book Author':['Padma Reddy','Joshua Bloch','Alex Martelli','Abraham Silberschatz','Padma Reddy','Ian Sommerville','Cem Kaner','Michael J. Folk','DSC','Gloria Albert']
}
df=pd.DataFrame(book)
print(df)
s=input(("Enter the book name to be searched"))
print(df[df['Book Name'].str.contains(s)])
