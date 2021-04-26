flowerpot = int(input('How many flowerpots? '))
flower_seeds = int(input('How many packs of flower seeds? '))

soil = int(input('How many bags of soil? '))

flowerpot_price = 4.00
flower_seed_price = 1.00
soil_price = 5.00

tax_price = 0.06

cost_of_items = (flowerpot * flowerpot_price) + (flower_seeds * flower_seed_price) + (soil * soil_price)

print(cost_of_items)