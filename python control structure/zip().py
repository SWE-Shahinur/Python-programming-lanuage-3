 #zip akadik itarable obj
men=['rahim','karim']
women=['sophia','ritika']
for couple in zip(men,women):
    print(couple)

name=['piash','sumon','saleh']
position=['ceo','swe','supervisor']
salry=[190000,70000,50000]
for i in zip(name,position,salry):
    print(i)

for name,position,salry in zip(name, position, salry):
    print(f"{name} is the {position} and  he is paid {salry} per week")