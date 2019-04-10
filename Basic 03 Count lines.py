f = open("files/everything-is-awesome.txt", "r")
count = 0
for line in f:
    count += 1
print("count: " + str(count))