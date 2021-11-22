class Car:
        def __init__(self, license, brand, color):
            # c = Car('AA1234', 'Honda',  'White')
            # มีตัวแปร reportเก็บประวัติ
            self.license = license
            self.brand = brand
            self.color = color
            self.report = []

        def __str__(self):
            #return string of car exemple 'AA1234 - White Honda'
                return f'{self.license} - {self.brand} {self.color}'

        def __lt__(self, rhs):
                #sort number of car by string
                return self.license < rhs.license
        
        def add_report(self, new_report):
                # เพิ่มประวัติซ่อมบำรุงโดยไม่ต้องคืนค่า
                # new_report เก็บ tuple ('Date','Discription','price')
                # exemple(('25 May 2017', 'change tires' , '1500'))
                # c1.add_report(('25 May 2017', 'change tires' , 1500))

                self.new_report = ()
                self.report.append(new_report)
                self.new_report = tuple(self.report)
                

        def total_payment(self):
                # return all pass maintenance price

                total = 0
                for i in self.report:
                        total += i[2]
                return f'All pass maintenance price is {total}'
                

        def max_payment(self):
                #return all maintenance record (Date, discription, price) that have maximun price
                #in case there is no maintenance record return empty list.
                self.max = ""
                if len(self.report) > 0:
                    for i in range(0 ,len(self.report)):
                        if i+2 > len(self.report):
                                break;
                        elif(self.report[i][2] < self.report[i+1][2]):
                                self.max = self.report[i+1]   
                        elif(self.report[i][2] > self.report[i+1][2]):
                                self.max = self.report[i]
                return list(self.max)

c1 = Car('AB1234', 'Honda',  'White')
c2 = Car('AA1234', 'Toyota', 'Black')

print(c1)
print(c2)

print(c1 > c2)

c1.add_report(('25 May 2017', 'change tires' , 1500))
c1.add_report(('25 May 2017', 'change Break' , 2000))
c1.add_report(('25 May 2017', 'change Break' , 9999))
c1.add_report(('25 May 2017', 'change Break' , 2000))
c1.add_report(('25 May 2017', 'change Break' , 10000))



print(c1.total_payment())
print(c1.max_payment())

