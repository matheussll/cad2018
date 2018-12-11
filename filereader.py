lines = open('dij_entries.txt').read().split('\n')
entries = [line.split(" ") for line in lines]
for entrie in entries:
    if (len(entrie) > 2):
        entrie[2] = int(entrie[2])
# parsedEntries = [entrie[2] = 10 for entrie in entries]
print(entries)
