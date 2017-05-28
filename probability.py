p_coin = .5
p_card = .4375

total = 0
probabilities = []
p_total = 0

for index in range(1,14):
    value = float(index)
    p_this = p_card*0.07692307692
    print(p_this)
    print(float((6 - abs(7 - value))))
    p_this = p_this + p_coin*float((6 - abs(7 - value))/36)
    probabilities.append(p_this)
    total = total + index*p_this
    p_total = p_total + p_this
    
print(probabilities)
print(total)
print(p_total)