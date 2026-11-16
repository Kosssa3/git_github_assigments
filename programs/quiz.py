score = 0;

print("Ile to 4 * 3?")
a = int(input())
if a == 12:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Stolicą województwa Wielkopolskiego jest?")
b = input()
if b == "Poznań":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Score: %d of 2" % score)
if score == 2:
    print("What am I suppose to congratulate you for knowing basics?")
elif score != 2:
    print("Look maybe MAYBE you don't know how to use the polish letters but, that just proves you don't know the basics so GO BACK AND LEARN THEM!.")
