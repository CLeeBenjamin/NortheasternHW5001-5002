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


def move_tower(num, source, target, middle, towers):

    if num == 1:
            move_disk(source, target, towers)

    else:
            move_tower(num - 1, source, middle, target, towers)
            move_disk(source, target, towers)
            move_tower(num - 1, middle, target, source, towers)



def main():
    
     num_disks = number_of_disks()
     kings = initialize_towers(num_disks, TOWERS[0], TOWERS[1], TOWERS[2])
     move_tower(num_disks,TOWERS[0], TOWERS[1], TOWERS[2], kings)

      
main()



