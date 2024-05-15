



# kuidas k2ivitada koodi teisest failist vastavalt soovile
students = ['anita', 'kersti', 'leone', 'victoria','triing']


# koledalt vormitud kood (PEP8????)
for i,student in enumerate(students,1):
  print("{} - {}".format(i,student.capitalize()))  
who = input("Sisesta number kelle koodi k2ivitame:")
i = int(who)-1
print("Käivitan {}.py koodi:\n\n\n".format(students[i]))
__import__(students[i])
print("programmi l6pp")
print("-"*25)

# Tänased (15.05.2024) teemad:
# 1. muutjad, massiivid, vaatame ligemalt
# 2. funktsioonid
# 3. 6pime koos (kuidas siin k6igi koode käivitada)
# 3.1 __import__
# 3.2 .replit confi fail
# 4. Syveneme natuke Algoritmi: Jahipidamise mäng
# 4.1 probleemi definitsioon
# 4.2 lahendus
# 4.3 competitive coding
# 5. tuples, dictionaries, generators
# 6. OOP - mis see on ja miks seda vaja on, mida see lahendab
# 8. ?
