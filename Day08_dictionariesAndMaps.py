# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    n = int(input().strip())
    contacts = dict()

    for i in range(n):
        x,y = input().strip().split()
        contacts[x] = y

    q=input().strip()
    while(q):
        if q in contacts.keys():
            print(q, "=", contacts[q],sep="")
        else:
            print("Not found")
        try:
            q=input().strip()
        except:
            break

if ( __name__ == "__main__" ):
    main()