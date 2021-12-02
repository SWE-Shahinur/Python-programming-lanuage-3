#nested dictionary
print("nested dictionary")
dictionary={
    "class one":{
        'roll 1': 'rbib',
        'roll 2': 'rakib',
        'roll 3': 'rbiya',

    },
    "class two": {
        'roll 1': 'shahinur',
        'roll 2': 'SHARMIN',
        'roll 3': 'SHAHJADI',

    }
}
print(dictionary['class one']['roll 1'])



world={
    'europ':{
        'france':{
            'capital':'parish'
        },
        'germany':{
            'capital':'berlin'
        }
    }

}

print(world['europ']['france']['capital'])
