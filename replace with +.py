test_str = 'Python is the best for geeks '

print("The original string is : " +str(test_str))

sub_str = 'best'

res = test_str.replace(sub_str, "") +str(sub_str)

print("The string after word removal : " + str(res))