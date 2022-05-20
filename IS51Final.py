"""
PLAIN ENGLISH
set counter to 0
open file in read
capture variable (test scores) from list of grades (float)
input variable
calculate number of tests to be graded
append grade scores to avg list
calculate average grade for the class
determine percent of grades that are above average
(print) output grade information to user
END
"""

"""

initialize count to 0
initialize avg to 0
get list from txt.file (open in read(r))
input first grade 
add grade to total
plus one to counter
if counter is not = 0
determine average (total / count)
print sum of grades
print the average
print the percent above average 


"""

def calculate_percent_above_average(grades,avg):
    count = 0
    for grade in grades:
        if grade > avg:
            count += 1
    return(count * 100) / len(grades)

def main():
    f = open("Final.txt", 'r')
    grades =[]
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:",len (grades))
    avg = 0
    for grade in grades:
        avg +=grade
    avg /= len(grades)
    print("Average grade:",avg)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades,avg)))
    f.close()


main()
