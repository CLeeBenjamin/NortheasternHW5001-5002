from hanoi_viz import initialize_towers
from hanoi_viz import move_disk

TOWERS = ["Musa", "Caesar", "Zulu"]

def number_of_disks():

    
    while True: 
        try:
             disks = int(input("Pick a number of disks. (1-8)\n"))       
             if (disks < 1) or (disks > 8):
                 print("Try again. Pick an integer from 1-8.")
             else:
                 return disks

        except ValueError:
            print("Try again. Pick an integer from 1-8.")



def move_tower(num, source, target, middle):

    king_towers = initialize_towers(num, TOWERS[0], TOWERS[1],TOWERS[2])

    
    if num == 1:
            move_disk(source, target, king_towers)

##    else:
##            move_tower(num - 1, source, middle, target)
##            move_disk(source, target, king_towers)
##            move_tower(num - 1, middle, target, source)

def main():
    
     num_disks = number_of_disks()
     move_tower(num_disks,TOWERS[0], TOWERS[1], TOWERS[2])

      
main()



