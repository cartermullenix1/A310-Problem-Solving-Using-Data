class LinkedList:
    def __init__(self, num, next):
        self.num = num
        self.next = next
    def show(self):
        temp = self
        result = ""
        while (temp):
            result = result + "|" + temp.num + "|"
            temp = temp.next
        print(result)

print("--------------------Test Cases-----------------------")

a = LinkedList("Christa", None)
a = LinkedList("Ahmed", a)
a.show()