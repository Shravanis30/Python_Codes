# Program to find best of two test average marks out of three test marks accepted from the user

def best_two_average(t1, t2, t3):
    marks = [t1, t2, t3]
    marks.sort(reverse = True)
    
    best_two_sum = marks[0] + marks[1]
    Average = best_two_sum / 2
    return Average

test1 = int(input("Enter the marks of test 1 : "))
test2 = int(input("Enter the marks of test 2 : "))
test3 = int(input("Enter the marks of test 3 : "))

Average = best_two_average(test1, test2, test3)

print(f"Average of the best two test is : {Average:.2f}")
