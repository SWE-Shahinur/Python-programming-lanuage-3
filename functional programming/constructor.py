#constructor-special type function /method
class student():
    roll=''
    cgpa=''
    def __init__(self,roll,cgpa): #parameter pass
        self.roll=roll
        self.cgpa=cgpa

    def disply(self):
        print(f"roll:{self.roll}, cgpa: {self.cgpa}")

rahim=student(121,3.67)
rahim.disply()

