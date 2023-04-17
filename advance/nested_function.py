def university(max_marks,min_marks):
    if 35 <= min_marks/max_marks*100:
        passing_status = "Pass"
    else:
        passing_status = "Fail"
    return passing_status


def college(max_marks, min_marks):
    result_status = university(max_marks,min_marks)
    award_status = None
    if result_status == "Pass":
        award_status = 'Congratulations !\neligible for rewarding'

    elif result_status == "Fail":
        award_status = 'not eligible for reward'
    return award_status


max_marks = int(input("max marks: "))
min_marks = int(input("min marks: "))

result = college(max_marks, min_marks)
print(result)


