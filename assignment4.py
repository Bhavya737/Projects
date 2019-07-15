import pandas as pd

data = {'Name':['Joey','Jason','Manish','Krishna','Sridevi','Sherlock','Stacy','Jon Snow','Sheldon','Alice'],
        'USN':['2KE16IS008','2KE16IS070','2KE16IS015','2KE16IS031','2KE16CS010','2KE16IS020','2KE16EE002','2KE16EC045','2KE16ME065','2KE16CV043'],
        'SEM':[7,6,7,7,6,7,7,7,6,6],
        'Marks':[95,90,95,90,85,70,65,83,100,56],
        'Region':['Kumta','Kumta','Kumta','Hubli','Bangalore','Sirsi','USA','USA','USA','USA']
       }
s= pd.DataFrame(data)
print(s)

print("Describe")
print(s.describe())

print("Maximum Mark")
print(s[s['Marks']==s['Marks'].max()])

print("Names in uppercase")
print(s['Name'].str.upper())


print("Group by Sem")
print(s.groupby(['Sem']).groups)

print("Group by Region")
print(s.groupby(['Region']).groups)

print(s.rename(index={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}))

