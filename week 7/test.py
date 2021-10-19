class test:
    def __init__(self):
        self.new_report = ()
    
    def __str__(self):
        return f'{self}'
    
    def addrepot(self, report):
        self.new_report = report
        price = report[2]
        mylist = []      
        mylist.append(price)
        print(*mylist)


c1 = test()
c1.addrepot(('25 May 2017', 'change tires' , '1500'))
c1.addrepot(('25 May 2017', 'change tires' , '9900'))