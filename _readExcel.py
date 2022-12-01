# import pandas as pd

# df = pd.read_excel('0_FINAL450.xlsx', sheet_name='Sheet1')
# print(df)
template = '''

#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define endl '\\n'

int main(){
    ll t,n;
    cin>>t;
    while(t--){
        cin>>n;
        
    }
    return 0;
}


'''


import openpyxl
import os


def getNthLink(n:int):
    nextFile = 0
    nextName = ''
    for file in os.listdir(os.getcwd()):
        # print(file)
        if(file.endswith('.cpp') or file.endswith('.py')):
            try:
                nextFile = max(nextFile, int(file.split('_')[0]))
            except:
                pass
            
    nextName = str(n)+'_'+ ws.cell(row=5 + n, column=2).value + ".cpp"
    
    if(input("Do you want to overwrite the file? (y/n)") == 'y'):
        with open(nextName.replace(" ",""), 'w') as f:
            f.write(template)
            
    return ws.cell(row=6 + nextFile, column=2).hyperlink.target

def getNextLink():
    nextFile = 0
    nextName = ''
    for file in os.listdir(os.getcwd()):
        # print(file)
        if(file.endswith('.cpp') or file.endswith('.py')):
            try:
                nextFile = max(nextFile, int(file.split('_')[0]))
            except:
                pass
    nextName = str(nextFile + 1)+'_'+ ws.cell(row=6 + nextFile, column=2).value + ".cpp"
    
    if(input("Do you want to overwrite the file? (y/n)") == 'y'):
        with open(nextName.replace(" ",""), 'w') as f:
            f.write(template)
            
    return ws.cell(row=6 + nextFile, column=2).hyperlink.target

wb = openpyxl.load_workbook('0_FINAL450.xlsx')
ws = wb['Sheet1']


if(input("Do you want the next link? (y/n)") == 'y'):
    print(getNextLink())
    
elif(input("Do you want a specific link? (y/n)") == 'y'):
    print(getNthLink(int(input("Enter the number of the question: "))))




# This will fail if there is no hyperlink to target