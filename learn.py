from __future__ import annotations
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next: Node | None = next
        return 

class Linked_List:
    def __init__(self, head=None) -> None:
        self.head = head
        return 

    def Add_To_Start(self, data) -> None:
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        return

    def Print_List(self) -> None:
        if self.head == None:
            print("list is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")        
            current = current.next
        print("end")
        return

    def Add_To_End(self, data) -> None:
        new_node = Node(data)
        current = self.head

        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node
        return
    
    def Count_Nodes(self) -> int:
        count = 0
        current = self.head
        if current is None:
            return 0
        else:
            while current is not None:
                count += 1
                current = current.next
            return count

    def Search_Value(self, value):
        current = self.head

        if current is None:
            return False
        else:
            while current is not None:
                if current.data == value:
                    return True
                else:
                    current = current.next
            return False

    def Reverse_List(self):
        prev = None
        current = self.head

        if self.Count_Nodes() <= 1:
            return

        
        while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
        self.head = prev


                

                    
        return

    def Find_Middle(self):
        current = self.head
        fast = current
        slow = current

        if current is None:
            return None

        while fast is not None and fast.next is not None:
            slow = slow.next
    
            fast = fast.next.next

        return slow.data

    def Find_Loop(self):
        current = self.head
        fast, slow = current, current

        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False

list = Linked_List()
list.Add_To_Start(3)
list.Add_To_Start(2)
list.Add_To_Start(1)
list.Add_To_End(4)



list.Print_List()
print(list.Find_Loop())

