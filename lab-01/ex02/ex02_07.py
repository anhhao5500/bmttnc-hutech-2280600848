print( "Input the text(please text 'done' when finished): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nletters have been converted to uppercase: ")
for line in lines:
    print(line.upper())