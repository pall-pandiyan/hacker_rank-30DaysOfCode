# Enter your code here. Read input from STDIN. Print output to STDOUT

def splitEvenAndOdd(string):
    n = len(string)
    oddString = ""
    evenString = ""
    
    for i in range(n):
        if ( i%2 == 0 ):
            oddString = oddString + string[i]
        else:
            evenString = evenString + string[i]
    
    return (oddString + " " + evenString)
        
def main():
    n = int(input().rstrip())
    for _ in range(n):
        s = input().rstrip()
        print(splitEvenAndOdd(s))

if __name__ == "__main__":
    main()