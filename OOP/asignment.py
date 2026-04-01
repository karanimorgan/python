class Students:
    def __init__(this, name, reg_no, age, course):
        this.name = name
        this.reg_no = reg_no
        this.age = age
        this.course = course

Joy = Students("Joy", 135, 25, "Human Resource" )
Alex = Students("Alex", 136, 23, "Cullinary Art")
Samuel = Students("Samuel", 145, 24, "Criminology")
Mike = Students("Mike", 143, 25, "Human Resorce")
Daniel = Students("Daniel", 155, 23, "Wildlife conservancy")
Lorna = Students("Lorna", 165, 20, "Chemical Engineering")

print(f"{Joy.name} is a student regestration number {Joy.reg_no} aged-{Joy.age} taking a {Joy.course} course")
print(f"{Alex.name} is a student regestration number {Alex.reg_no} aged-{Alex.age} taking a {Alex.course} course")
print(f"{Samuel.name} is a student regestration number {Samuel.reg_no} aged-{Samuel.age} taking a {Samuel.course} course")
print(f"{Mike.name} is a student regestration number {Mike.reg_no} aged-{Mike.age} taking a {Mike.course} course")
print(f"{Daniel.name} is a student regestration number {Daniel.reg_no} aged-{Daniel.age} taking a {Daniel.course} course")
print(f"{Lorna.name} is a student regestration number {Lorna.reg_no} aged-{Lorna.age} taking a {Lorna.course} course")