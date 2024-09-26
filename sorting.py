def bubble(ls):
    for i in range(len(ls) - 1):  
        # sorts it faster by checking if already sorted early
        shortCut = True
        for j in range(len(ls) - i - 1):  
            a = ls[j]
            b = ls[j + 1] 
            if a > b:  
                ls[j] = b 
                ls[j + 1] = a
                shortCut = False
        if(shortCut):
            print("saved you ",len(ls)-i-1," recurtions")
            break
    return ls
  
def main():
    pigs = [1,2,4,3,2]
    print(bubble(pigs))

if __name__ == "__main__":
    main()
