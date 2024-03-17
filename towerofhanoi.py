def toh(disk,source,destination,auxilliary):
    if disk == 1:
        print(f"move from {source} to {destination}")
    else:
        toh(disk-1, source, auxilliary, destination)
        print(f"move from {source} to {destination}")
        toh(disk-1, auxilliary, destination, source)

def main():
    toh(4, 'A', 'C', 'B')

main()
