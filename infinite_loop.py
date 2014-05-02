

#infinity loop
#carrot and donkey principle

carrot = range(10)

donkey = lambda piece : carrot.append(piece)

if __name__ == '__main__':
    #infinity loop
    map(donkey, carrot)
