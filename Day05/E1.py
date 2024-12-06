data = open("Day05/input").read()
rules, updates = data.split("\n\n")


rules_list = [rule.split("|") for rule in rules.split("\n")]
rules = {}
for v, k in rules_list: 
    if k not in rules:
        rules[k] = [v]
    else: rules[k].append(v)

print(rules)

updates = [u.split(",") for u in updates.split("\n")]


unsafe = []

for update in updates:
    for i, num in enumerate(update):
        if num in rules and any([ x in update[i:] for x in rules[num]]) :
            unsafe.append(update)
            break

correct = [ int(update[(len(update)//2)]) for update in updates if update not in unsafe ]

print(sum(correct))
