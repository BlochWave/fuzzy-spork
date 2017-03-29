import time; start = time.time();
main = open("p022_names.txt","r").readlines();
position = 0;
total = 0;
for line in main:
    names = line.split(",")
    for name in sorted(names):
        name = name.strip('"');
        position += 1;
        value = 0;
        for character in name:
            value += ord(character) - 64;
            # print name, character, position, value, total
        total += position * value;
print total, time.time()-start;