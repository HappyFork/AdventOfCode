# AOC22-D11P1.py
# Advent of code 2022, day 11 part 2


from math import floor

#FILENAME = "testd11"
FILENAME = "inputd11"


class Monkey:
    # Monkey has the following member variables:
    #   num: what number monkey it is
    #   items: a list of items it's holding
    #   ins_times: number of times this monkey inspected an item
    #   ins_op: the operation done to items when inspected
    #   ins_val: the value operated on each item when inspected
    #   test: the number divided to test
    #   true_mon: the monkey to throw to if test is true
    #   false_mon: the monkey to throw to if test is false

    monkeys = []    # List of all monkeys

    def __init__(self, num, list, op, val, test, trmon, famon ) -> None:
        self.num = num
        self.items = list.copy()
        self.ins_times = 0
        self.ins_op = op
        self.ins_val = val
        self.test = test
        self.true_mon = trmon
        self.false_mon = famon
        Monkey.monkeys.append( self )
    
    def __str__(self) -> str:
        s = f"Monkey {self.num} has the following items: \n["
        for i in range(len(self.items)):
            if i == len(self.items) - 1:
                s += str(self.items[i])
            else:
                s += f"{self.items[i]}, "
        s += "]"
        return s
    
    def inspect_test_and_throw(self):
        # First, if the list is empty, there's nothing to do
        if len(self.items) == 0:
            return

        # Take the first item in items list
        curr_item = self.items.pop(0)
        
        # Increment ins_times by one
        self.ins_times += 1

        # Inspect it. Do ins_op with ins_val
        if self.ins_val == "old":
            curr_val = curr_item
        else:
            curr_val = self.ins_val

        match self.ins_op:
            case "*":
                curr_item = curr_item * curr_val
            case "+":
                curr_item = curr_item + curr_val

        # Divide the result by 3, then round down to int
        #curr_item = floor( curr_item / 3 )

        # Modulo current value by test
        curr_test = curr_item % self.test

        # If result is 0, throw to true_mon
        if curr_test == 0:
            for m in Monkey.monkeys:
                if m.num == self.true_mon:
                    throw_monkey = m
                    break
        # Else, throw to false_mon
        else:
            for m in Monkey.monkeys:
                if m.num == self.false_mon:
                    throw_monkey = m
                    break
        
        throw_monkey.add_item( curr_item )

        # Repeat until list is empty
        self.inspect_test_and_throw()

    def add_item(self, item):
        self.items.append( item )


with open( FILENAME ) as f:

    lines = f.readlines()

    for l in lines:
        if l == "\n":
            Monkey( mnum, ilist, mop, mval, mtest, tm, fm )
        else:
            ls = l.strip().split()
            match ls[0]:
                case "Monkey":
                    mnum = int(ls[1][0])
                case "Starting":
                    ilist = []
                    for x in range(2, len(ls)):
                        if x == len(ls) - 1:
                            ilist.append( int(ls[x]) )
                        else:
                            ilist.append( int(ls[x][:-1]) )
                case "Operation:":
                    mop = ls[-2]
                    if( ls[-1] ) == "old":
                        mval = "old"
                    else:
                        mval = int(ls[-1])
                case "Test:":
                    mtest = int(ls[-1])
                case "If":
                    if ls[1] == "true:":
                        tm = int(ls[-1])
                    else:
                        fm = int(ls[-1])

    Monkey( mnum, ilist, mop, mval, mtest, tm, fm )


# Run 100 rounds
for x in range(10000):
    print( x )
    for m in Monkey.monkeys:
        m.inspect_test_and_throw()

# Multiply two largest numbers
largest = 0
second_largest = 0
for m in Monkey.monkeys:
    if largest < m.ins_times:
        second_largest = largest
        largest = m.ins_times
    elif second_largest < m.ins_times:
        second_largest = m.ins_times

print( largest * second_largest )