
# The Magical Creature Habitat
def feed_creatures(creatures):
    for creature in creatures:
        food_needed = creature["food_required"]
        
        # Adjust food needed based on creature type
        if creature["type"] == "dragon":
            food_needed *= 1.2  # 20% more food
        elif creature["type"] == "unicorn":
            food_needed *= 0.5  # Half the food
        elif creature["type"] == "phoenix":
            food_needed *= 2     # Twice the food
        
        # Print the food needed for each creature
        print(f"{creature['name']} the {creature['type']} needs {food_needed} units of food.")
        
        # Alert for special attention
        if food_needed >= 50:
            print(f"Special attention needed for {creature['name']}!")

def simple_function():
    pass