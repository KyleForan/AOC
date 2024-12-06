data = open("Day05/input").read()
rules, updates = data.split("\n\n")


rules_list = [rule.split("|") for rule in rules.split("\n")]
rules = {}
for v, k in rules_list: 
    if k not in rules:
        rules[k] = [v]
    else: rules[k].append(v)


updates = [u.split(",") for u in updates.split("\n")]

unsafe = []

for update in updates:
    for i, num in enumerate(update):
        if num in rules and any([ x in update[i:] for x in rules[num]]) :
            unsafe.append(update)
            break

result = 0

for update in unsafe:
    new_rules = defaultdict(set)
    for i in update:
        if i not in rules: continue
        new_rules[i] = set(rules[i]) & set(update)

    
    new_update = map(int, sorted(new_rules, key=lambda k: len(new_rules[k]), reverse=True))
    new_update = list(new_update)

    result += (new_update[len(new_update)//2])

print(result)
