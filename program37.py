total_heads = 35
total_legs = 94
for chickens in range(total_heads + 1):
    rabbits = total_heads - chickens
   
    if (chickens * 2 + rabbits * 4) == total_legs:
        print(f"Number of chickens: {chickens}")
        print(f"Number of rabbits: {rabbits}")
        break