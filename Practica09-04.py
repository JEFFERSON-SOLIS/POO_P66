#class MiPrimeraClase:
#    pass
#myFirts=MiPrimeraClase()
#class MiPrimeraClase1:
#    pass
#myFirts1=MiPrimeraClase()
#class MiPrimeraClase2:
#    pass
#myFirts2=MiPrimeraClase()
#class MiPrimeraClase3:
#    pass
#myFirts3=MiPrimeraClase()
#class MiPrimeraClase4:
#    pass
#myFirts4=MiPrimeraClase()
#class MiPrimeraClase5:
#    pass
#myFirts5=MiPrimeraClase()
#class MiPrimeraClase6:
#    pass
#myFirts6=MiPrimeraClase()
#/////////////////////////////////////////////////////////////

class Employee:
    empCount = 0
    def __init__(self,name, salary):
        Employee.empCount +=1
        def displayCount(self):
            print ("Total Employee %d", Employee.empCount)
        def displayEmployee(self):
            print("Name : ", self.name, "Salary: ",self.salary)
empleado1=Employee("Jefferson", 800)
empleado2=Employee("Genesis", 850)
empleado3=Employee("Said",700)
print("Total Employee %d" % Employee.empCount)
