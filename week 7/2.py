class shopping_cart:
    def __init__(self, id):
        #book เก็บ list ของหนังสือในตะกร้า [[b1,2],[b3,3]]
        self.id = id
        self.book = []



    def add_book(self, book, n ,total):
        # เพิ่มข้อมูลการซื้อหนังสืออีก n เล่มโดยไม่ต้องคืนค่า
        # หากไม่มีหนังสือในตะกร้า ให้เพิ่ม List [book, n] ต่อท้าย books
        # หากเคยมีหนังสือในตะกร้าแล้ว ให้เพิ่มจำนวนที่ซื้ออีก n เล่ม
        # เช่น ถ้า books = [[b1,2]] และเราสั่ง add_book(b1,3) จะได้ books = [[b1,5]]
        num = n
        self.total = total
        self.book.append([book, n, total])
        for i in range(len(self.book)):
            if i+2 > len(self.book):
                break;
            elif book in self.book[i][0]:
                self.book[i][1] += num
                self.book.pop(i+1)
    
        

        
    
    def delete_book(self, book):
        # ลบข้อมูลการซื้อหนังสือ book ออกจากตะกร้า โดยไม่ต้องคืนค่า
        # ถ้าในตะกร้าไม่มีหนังสือ book ไม่ต้องทำอะไร
        for i in range(len(self.book)):
            if i+2 > len(self.book):
                break;
            elif book in self.book[i][0]:
                self.book.pop(i)
        

    def get_total(self):
        # คืนค่าราคารวมของหนังสือในตะกร้า
        total = 0
        for i in self.book:
            total += i[2]
        return f'All total is {total}'

    def __lt__(self, rhs):
        # ตะกร้าที่มีราคารวมของหนังสือน้อยกว่า จะเป็นตะกร้าที่น้อยกว่า
        return self.total > rhs.total


Komet_shop = shopping_cart(64015060)
Komet_shop.add_book('b1', 1, 500)
Komet_shop.add_book('b1', 5, 500)
Komet_shop.add_book('b3', 5, 700)
Komet_shop.add_book('b2', 15,100)
Komet_shop.add_book('b2', 15,100)
Komet_shop.delete_book('b4')
print(Komet_shop.get_total())

Ko_shop = shopping_cart(6239010028)
Ko_shop.add_book('b1', 1, 500)
Ko_shop.add_book('b1', 5, 500)
Ko_shop.add_book('b3', 5, 700)
Ko_shop.add_book('b2', 15,600)
Ko_shop.add_book('b2', 15,600)
print(Ko_shop.get_total())


print(Komet_shop > Ko_shop)