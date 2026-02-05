# CTI 110
# P1LAB1
# DURANTEA9352
# 2/5/2026
# Practice Python Program

name = "Steve"
print ("Hi, what's your first name? ")
first_name = input() 
last_name = input("what's your last name ")

print ("Nice to meet you", first_name, last_name)
print() #extra blank line
hobby = input("What type of 'stuff' do you like? ")
print("I'm a computer but I would probably like", hobby, "too")

# example of a loop
print("I can repeat myself!")
count = int(input("How many times should I repeat? "))
for time in range(count):
    print("I know a song that drives people crazy,")