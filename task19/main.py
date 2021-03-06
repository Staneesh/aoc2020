file = open("data5", "r")
rules, words = file.read().split("\n\n")

def find_rule(rule_number):
    for rule in rules.split('\n'):
        rule = rule.split(": ")
        if int(rule[0]) == rule_number:
            return rule[1]
    return -1

def word_matches_rule(word, rule_number):
    if word == "@" or word =="":
        return "@"

    rule = find_rule(rule_number)
    is_letter = rule.find("\"") != -1
    is_or = rule.find("|") != -1

    print(f"w = {word}, rulenum = {rule_number}, r = {rule}")
    
    if is_letter:
        leftmost_letter_in_word = word[0]
        quotation_index = rule.find("\"")
        letter_in_rule = rule[quotation_index + 1] 

        #print(f"its a letter, leftmost letter: {leftmost_letter_in_word}, letter rule: {letter_in_rule}")

        if leftmost_letter_in_word == letter_in_rule:
            #print("match!")
            word = word[1:]
        else:
            #print("mismatch!")
            word = "@" 

    elif is_or:
        #print("its an or")
        alternatives = rule.split(" | ")
        set1 = alternatives[0].split(" ")
        set2 = alternatives[1].split(" ")
        wordcpy = word
        for r in set1:
            partial = word_matches_rule(wordcpy, int(r))
            wordcpy = partial

            if wordcpy == "@":
                print("Trying second branch...")
                wordcpy = word
                for r in set2:
                    partial = word_matches_rule(wordcpy, int(r))
                    wordcpy = partial
                break   

    
        word = wordcpy
   
    else:
        #print("its normal")

        for rule_index in rule.split(" "):
            print(f"looking at rule index = {rule_index}")
            partial = word_matches_rule(word, int(rule_index))
            word = partial

    print(f"{rule_number} returning {word}")
    return word

result = 0
for word in words.split("\n"):
    if len(word) < 1:
        continue

    partial = word_matches_rule(word, 0)
    print(f"partial = {partial}")
    if partial =="":
        print(f"good for {word} -> {partial}")
        result += 1

print(f"result = {result}")

file.close()
