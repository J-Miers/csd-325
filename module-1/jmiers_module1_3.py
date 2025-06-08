"""
Jessie Miers
CSD325
6/8/25

This program uses a non-recursive loop use a numerical input from a 
user to display the "99 bottles of beer on the wall" song until it reaches 0
and then displays a message to get more beer. 
"""
#Function asks user for count and offers error checking
def get_beer_count():
    while True:
        try:
            count = int(input("Enter number of bottles:\t"))
            if count <=0:
                print("Please insert non-negative numbers only!")
            else:
                break
        except ValueError:
            print("Please enter only positive numbers.")

    return count

#Function uses count from get_beer_count and displays the song
def song(count):


    #Creates a loop using the provided count and display the song lyrics until count reaches 1 then provides a grammatical change to the wording.  
    for i in range(count, 0, -1):
        print(f"{i} bottle{'s'if i !=1 else''} of beer on the wall, {i} bottle{'s'if i !=1 else''} of beer.")
        print(f"Take one down and pass it around, {i-1} bottle(s) of beer on the wall.\n")

    
#Main function calls other functions and Calls for user to buy more beer at the end of the loop.    
def main():
    count = get_beer_count()
    song(count)
   
    print("\nTime to buy more bottles of beer.")
    
    
if __name__ == "__main__":
    main()