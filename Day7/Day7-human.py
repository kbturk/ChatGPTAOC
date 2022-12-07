import sys
from enum import Enum, auto
from typing import List
from pprint import pprint

def totals(key, dir_info, total = 0):
    for value in dir_info[key]:
        if type(value) == int:
            total += value
        else:
            dir_info, total = totals(value, dir_info, total)
    return dir_info, total

def dumb_totals(key, dir_info, total = 0):
    for value in dir_info[key]:
        if type(value) == int:
            total = int(value)
        else:
            dir_info, dir_info[key][dir_info[key].index(value)] = dumb_totals(value, dir_info, dir_info[key][0])
    return dir_info, total

def main():
    max_size = 100000
    current_dir = []
    dir_info = {}

    for line in sys.stdin: 
        #if this is a user prompt...
        if line.startswith('$'):

            user_prompt = line.split()
            #just for cleaner code...
            if len(user_prompt) <= 2: user_prompt.append(None)

            if user_prompt[1] == "cd":
                if user_prompt[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(user_prompt[2])
                if "/".join(current_dir) not in dir_info.keys():
                    dir_info["/".join(current_dir)] = [0]

        else:
              output = line.split()
              if output[0].isdigit():
                  dir_info["/".join(current_dir)][0] += int(output[0])
              elif output[0] == 'dir':
                  if output[1] not in dir_info["/".join(current_dir)]:
                      #add the sub directory
                      dir_info["/".join(current_dir)].append("/".join(current_dir + [output[1]]))
              else: print("DANGER WILL ROBINSON: {output}")
    for key in dir_info.keys():
        print(f"key: {key}, values: {dir_info[key]}")
    pt1 = 0
    sum_dirs = {}
    for key in dir_info.keys():
        _, sum_dirs[key] = totals(key,dir_info,0)
    for k,v in sum_dirs.items():
        print(f'too many formulars {k}:{v}')
    dir_info, _ = dumb_totals('/', dir_info, 0)
    for key in dir_info.keys():
        if sum(dir_info[key]) <= max_size:
            pt1 += sum(dir_info[key])
    print(f'pt1: {pt1}')

    #part2:
    total_space = 70000000
    goal = 30000000
    l = sorted(list(sum_dirs.values()))
    for x in l:
        if total_space - sum_dirs['/'] + x >= goal:
            print(x)
            break
        
    return 1

if __name__ == '__main__':
    sys.exit(main())
