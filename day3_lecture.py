"""
A department store has departments in it, and each department can have one or
more types of items in the inventory. Stores have a type (e.g. grocery,
sporting goods).  You can query the store to see all the departments, and query
each department to see all the items in that department.
​
1. What are the nouns? These tend to be classes. Find the "things".
   * Store
   * Depts
   * Items
   * Inventory
​
2. What are the verbs? What can we do to the nouns? These tend to be "methods"
   (functions) on the class.
   * query depts in the store
   * query items in the dept
​
3. Look for "has-a" relationships. These tend to be attributes on the object.
   * store has depts
   * store has a type
   * dept has types of items in inventory
​
4. Look for "is-a" relationships. These tend to indicate "class hierarchy".
   More on this tomorrow.
​
"""
​


class Store:
    def __init__(self, store_type, depts=[]):
        """Constructor"""
        self.store_type = store_type
        self.depts = depts


​
   def add_dept(self, dept):
        """Adds a department to this store."""
        self.depts.append(dept)

    def max_dept_num(self):
        return len(self.depts) - 1
​
   def get_dept(self, num):
        return self.depts[num]
​
   def __str__(self):  # for human consumption
        s = f"Store (type: {self.store_type})\n"
​
   for d in self.depts:
        s += f"    {d}\n"
​
   return s
​
   def __repr__(self):  # for programmer consumption
        # return f'Store("{self.store_type}")'
        return f'Store({repr(self.store_type)},{repr(self.depts)})'
​


class Dept:
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory

​
   def __str__(self):  # for human consumption
        return f"Dept {self.name}"
​
   def __repr__(self):  # for programmer consumption
        # return f'Store("{self.store_type}")'
        return f'Dept({repr(self.name)},{repr(self.inventory)})'
​


class Item:
    pass

​
d0 = Dept("dairy")
d1 = Dept("produce")
d2 = Dept("bakery")
​
# print(d)
​
s = Store("grocery", [d0, d1, d2])  # instantiate a new Store object
​
# print(s)
# print(repr(s))
​
dn = input(f"Enter a dept number 0-{s.max_dept_num()}: ")
​
dn = int(dn)  # convert from string to number
​
if dn < 0 or dn > s.max_dept_num():
    print("Invalid department")
else:
    print(s.get_dept(dn))
