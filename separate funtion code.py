def kilo_to_pounds(kilos):
    return(kilos*2.204)

if __name__=='__main__':
    kilos = float(input('What is the amount? '))
    pounds = kilo_to_pounds(kilos)
    print(pounds, 'lbs')