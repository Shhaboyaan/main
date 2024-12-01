
class MyList:
        def __init__(self):
            self.lst = []

        def append(self, *args):
            self.lst.append(*args)

        def extend(self, new):
            self.lst.extend(new)

        def insert(self, index, item):
            self.lst.insert(index, item)

        def remove(self, item):
            try:
                self.lst.remove(item)
            except ValueError:
                print(f"{item} not found in the list.")

        def pop(self, index=-1):
            try:
                return self.lst.pop(index)
            except IndexError:
                print("Index not found")
                return None

        def clear(self):
            self.lst.clear()

        def index(self,item, start=0, end=None):
            try:
                return self.lst.index(item, start, end)
            except Exception:
                return f"{item} not found in the list."

        def count(self, item):
            return self.lst.count(item)

        def sort(self, reverse=False):
            self.lst.sort(reverse=reverse)

        def reverse(self):
            self.lst.reverse()

        def __getitem__(self, index):
            try:
                return self.lst[index]
            except IndexError:
                print("Index out of range.")
                return None

        def __setitem__(self, index, value):
            try:
                self.lst[index] = value
            except IndexError:
                print("Index out of range.")

        def __delitem__(self, index):
            try:
                del self.lst[index]
            except IndexError:
                print("Index out of range.")

        def __contains__(self, item):
            return item in self.lst

        def __len__(self):
            return len(self.lst)

        def __str__(self):
            return str(self.lst)

        def __repr__(self):
            return f"MyList({repr(self.lst)})"


list = MyList()
list.append(1)
list.append(4)
list.append(3)
list.remove(2)
print(list)
print(list.count(1))
list.sort(reverse=True)
print(list)
print(list.index(2))
print(len(list))
