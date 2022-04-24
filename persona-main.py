from persona import persona

def main():
    victor = persona("victor", 45)
    victor.printea()




if __name__ == "__main__":
    #just to test __name__ value
    print("__name__ when running __main__ :: %s"  %  (__name__))
    
    main()