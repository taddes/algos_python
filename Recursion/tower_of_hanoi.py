"""
Three rods and a number of disks of different sizes which can slide on any rod.
Puzzle begins with the disks in a neat stack in ascending order of size on the leftmost
rod. The smallest disk is at the top, making a conical shape.

Rules:
Only one disk can be moved at a time
Each move consists of taking the upper disk from one stack and placing it on another.
No disk may be placed on top of a smaller disk.

Minimum No. of moves required to solved is 2^n - 1 O(2^n) - Exponential time complexity

Recurring sub-problem: at some point, one will have managed to shift n - 1 plates (for 3 plates, this is 2)
to the middle auxiliary rod, at which point the largest disk has to be moved to the final
rod. The largest disk is the only one left, so it can be placed on the final rod.
"""

def hanoi(disk, source='A', middle='B', destination='C'):
    # base case - 0 is always the smallest plate
    # We manipulat the smallest plate in the base case (index 0)
    if disk == 1:
        # Move disk from source to dest
        print(f'Disk {disk} moved from {source} to {destination}')
        return
    hanoi(disk-1, source, destination, middle)
    print(f'Disk {disk} moved from {source} to {destination}')
    hanoi(disk-1, middle, source, destination)

hanoi(3, 'a', 'b', 'c')