with open('all.txt') as f:
    with open('out.txt', 'a') as the_file:
        for line in f:
            print(line)
            result = ''.join([i for i in line if not i.isdigit()])
            the_file.write(result) 

