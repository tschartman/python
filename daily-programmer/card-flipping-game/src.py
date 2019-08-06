
def flip(number):
    order, next_card_higher = [], False
    for index, num in enumerate(number):
        order.append(index) if next_card_higher else order.insert(0, index)
        next_card_higher ^= num == "1"
    return order if next_card_higher else "No solution"

print(flip("010111111111100100101000100110111000101111001001011011000011000"))