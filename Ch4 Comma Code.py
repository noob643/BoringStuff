spam = ['apples', 'bananas', 'tofu', 'cats']
counter = 1
print(len(spam))
if len(spam) == 0:
    print("List is empty")
else:
    print(spam[0], end ='')
    while counter <= len(spam)-1:
        for z in spam[1:len(spam)]:
            if counter < len(spam)-1:
                print(' ,', end ='')
                print(z, end ='')
                counter +=1
            else:
                print(' and ', end ='')
                print(z, end ='')
                counter +=1
print('')
