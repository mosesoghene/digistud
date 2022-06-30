for x in range(2, 13):
    for y in range(1, 13):
        print(f'{x} X {y} = {x * y}', file="timestable.txt")
    print('=============================', file="timestable.txt")

print("Done")