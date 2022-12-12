from copy import deepcopy
import sys, math
from typing import List, Tuple, Set, Dict, Optional

class Monkey:
    name: int #monkey 'number'
    items: List[int]
    oper: str #string function
    test: int
    if_true: int #which monkey to throw to
    if_false: int #which monkey to throw to

    def __init__(self, name: int, items: List[int], oper: str, test: int, if_true: int, if_false: int):
        self.name = name
        self.items = items
        self.oper = oper
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        print(f' new Monkey: {name}, {items}, {oper}, {test}, {if_true}, {if_false}')

    def operation(self, old: int) -> Optional[int]:
        _, _, sx, operand, sy = self.oper.split()

        if sx == 'old': x = old
        else: x = int(sx)

        if sy == 'old': y = old
        else: y = int(sy)

        match operand:
            case '*':
                return int(x * y)
            case '-':
                return int(x - y)
            case '+':
                return int(x + y)
            case '/':
                return int(x / y)
        
        return None

    def test_it(self, new: int) -> bool:
        return new % self.test == 0

    def throw_it(self, new:int) -> int:
        #new = math.floor(new / 3)
        if self.test_it(new): return self.if_true
        else: return self.if_false

    def add_it(self, new:int) -> None:
        #new = math.floor(new / 3)
        self.items.append(new)

def main():
    instructions = [line.strip('\n').split() for line in sys.stdin]
    monkeys: List[Monkey] = []

    #first step: parse input to build some Monkeys
    monkey = 0
    items = []
    oper = ""
    test = 0
    if_true = 0
    if_false = 0

    for parse in instructions:

        if len(parse) == 0:
            monkeys.append(Monkey(monkey, items, oper, test, if_true, if_false))
            items = []

        else:
            match parse[0]:
                case 'Monkey':
                    monkey = int(parse[1].strip(':'))

                case "Starting":
                    for i in parse[2:]:
                        items.append(int(i.strip(',')))
                    #print(items)

                case 'Operation:':
                    oper = " ".join(parse[1:])

                case 'Test:':
                    test = int(parse[-1])

                case 'If':
                    if parse[1] == 'true:': if_true = int(parse[-1])
                    else: if_false = int(parse[-1])

    monkeys.append(Monkey(monkey, items, oper, test, if_true, if_false))

    all_that_for_this: List[int] = [0 for i in range(len(monkeys))]

    why_does_eric_love_mod = math.prod([monkey.test for monkey in monkeys])
    print([monkey.test for monkey in monkeys])
    print(why_does_eric_love_mod)

    for i in range(1,10001):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                monkey.items[0] %=why_does_eric_love_mod
                #print(f'i: {i}, monkey: {monkey.name}, has: {monkey.items}')
                worry_level = monkey.operation(monkey.items[0])
                #print(f'worry level: {worry_level}')
                #print(f'{monkey.items[0]*why_does_eric_love_mod} became {monkey.items[0]}')

                next_monkey = monkey.throw_it(worry_level)
                #print(f'next monkey: {next_monkey}')

                monkeys[next_monkey].add_it(worry_level)
                #print(monkeys[next_monkey].items[-1])
                monkey.items.pop(0)
                all_that_for_this[monkey.name] += 1

    print(all_that_for_this)
    all_that_for_this.sort()
    print(all_that_for_this[-1]*all_that_for_this[-2])
    return 1

if __name__ == '__main__':
    sys.exit(main())
