cet = {'ninad','unnati','aniket','shreya','akif','pratham','alisha','jainam'}
jee = {'aakash','akif','shreya','nandini','nakul','aniket','esha','alisha'}
neet = {'alisha','yogita','ninad','unnati','gauri','vaishnavi','krkr','aakash'}

total = len(cet|jee|neet)
print(f"{total} students gave the exam")

print("List of all students")
print(cet|jee|neet)
print("\n")

#students who only appeared for cet
print("students who only appeared for cet")
print(cet-jee-neet)
print("\n")

#students who only appeared for jee
print("students who only appeared for cet")
print(jee-neet-cet)
print("\n")

#students who only appeared for neet
print("students who only appeared for cet")
print(neet-jee-cet)
print("\n")

#students who appeared for both cet and jee
print("students who appeared for both cet and jee")
print((cet|jee)-neet)
print("\n")

#students who appeared for both cet and neet
print("students who appeared for both cet and neet")
print((cet|neet)-jee)
print("\n")

#students who appeared for both jee and neet
print("students who appeared for both jee and neet")
print((jee|neet)-cet)
print("\n")
