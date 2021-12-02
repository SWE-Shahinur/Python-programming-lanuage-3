#dictionary te 2 element thak(key-index,value-value),{}use
dic={
    'first': 'red',
    'second': 'yellow',
    'third': 'greeen'
}

print(dic['first'])
print(dic.get('five','the valu is empty'))
print(dic.get('second','the valu is empty'))
print(dic.values())


#update
dics={
    'name': 'shahinur',
    'rool': '120'
}
print("befoe update:",dics.values())
dics.update({'cgpa':'3.63'})
print("after update", dics.values())

#delet
print('before delet:',dics.values())
del dics['rool']
print("after delet:",dics.values())
#totaly delet
dics.clear()




student={
    101: 'shahinur',
    102: 'sharmin'
}
print(student[101])
print(student.get(103,'there have no  value'))
print(student.values())


