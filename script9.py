i=0
with open('awk_pattern_match.txt', 'a') as file:
    while i <= 100:
        file.write(str(i)+"\n")
        i = i + 1
    print("End")