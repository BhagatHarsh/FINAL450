
import openpyxl
import os


template = """
//link: %s

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


"""

def convertCase(arr) : # https://www.geeksforgeeks.org/convert-given-array-of-strings-to-a-camel-case-format-sentence/
    ans = ""
    try:
        N = len(arr)
        for i in range(N) :
            if (len(ans) > 0) :
                ans += ' '
            ans += arr[i][0].upper()
            j = 1
            while j < len(arr[i]) :
                if (arr[i][j] == ' ') :
                    ans += ' '
                    ans += arr[i][j + 1].upper()
                    j += 1
                else :
                    ans += arr[i][j].lower()
                j += 1
    except:
        pass
    return ans


def getNthLink(n:int):
    nextFile = n
    nextName = ''
    nextName = convertCase((str(nextFile)+'_'+ ws.cell(row=5 + nextFile, column=2).value).split(" ")) + ".cpp"
    cellLink = ws.cell(row=5 + nextFile, column=2).hyperlink.target
    if(input("Do you want to overwrite the file? (y/n)") == 'y'):
        with open(nextName.replace(" ",""), 'w') as f:
            f.write(template%(str(cellLink)))
            
    return cellLink

def getNextLink():
    nextFile = 0
    nextName = ''
    for file in os.listdir(os.getcwd()):
        try:
            nextFile = max(nextFile, int(file.split('_')[0]))
        except:
            pass
    nextName = convertCase((str(nextFile + 1)+'_'+ ws.cell(row=6 + nextFile, column=2).value).split(" ")) + ".cpp"
    cellLink = ws.cell(row=6 + nextFile, column=2).hyperlink.target
    
    if(input("Do you want to overwrite the file? (y/n)") == 'y'):
        with open(nextName.replace(" ",""), 'w') as f:
            f.write(template%(str(cellLink)))
            
    return cellLink
wb = openpyxl.load_workbook('0_FINAL450.xlsx')
ws = wb['Sheet1']


if(input("Do you want the next link? (y/n)") == 'y'):
    print(getNextLink())
    
elif(input("Do you want a specific link? (y/n)") == 'y'):
    print(getNthLink(int(input("Enter the number of the question: "))))




# This will fail if there is no hyperlink to target