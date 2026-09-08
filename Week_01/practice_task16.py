# 16. Given two sets of student names enrolled in two courses, find students enrolled in both, only Course A, and only Course B.
course_a={"Ali","Ahmed","Sara","John"}
course_b={"Sara","John","Maria","David"}
print("Both:",course_a&course_b)
print("Only Course A:",course_a-course_b)
print("Only Course B:",course_b-course_a)