# you are given the total liter of water used by a house and output the total water bill.
# the water bill is calculated as follows.
# for 1st 100 litres : Rs 15 per litre
# for next 100 liters: Rs 14 per litre,
# after 200 litre: Rs 12 per litre




total_liters = int(input("Enter the total liters of water used by the house: "))


if total_liters <= 100:
    water_bill = total_liters * 15
elif total_liters <= 200:
    water_bill = (100 * 15) + ((total_liters - 100) * 14)
else:
    water_bill = (100 * 15) + (100 * 14) + ((total_liters - 200) * 12)


print("The Water bill is Rs: ", water_bill)

