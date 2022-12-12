import sys, queue
from typing import Optional, Tuple, TypeAlias, List, Set

Point: TypeAlias = Tuple[int, int]
Forest: TypeAlias = dict[Point, int]

def elevation(c: str) -> int:
    if c == 'S':
        return 1
    if c == 'E':
        return 26
    return ord(c) - ord('a') + 1

def valid_moves(curr: Point, forest: Forest) -> List[Point]:
    up = (curr[0], curr[1] - 1)
    down = (curr[0], curr[1] + 1)
    left = (curr[0] - 1, curr[1])
    right = (curr[0] + 1, curr[1])

    valid_move: List[Point] = []

    if up in forest.keys():
        if forest[up] - forest[curr] <= 1:
            valid_move.append(up)

    if down in forest.keys():
        if forest[down] - forest[curr] <= 1:
            valid_move.append(down)

    if left in forest.keys():
        if forest[left] - forest[curr] <= 1:
            valid_move.append(left)

    if right in forest.keys():
        if forest[right] - forest[curr] <= 1:
                valid_move.append(right)

    return valid_move    

def bfs(curr: Point, end: Point, forest: Forest) -> Optional[int]:
    q: queue.Queue[Tuple[Point,int]] = queue.Queue()
    q.put((curr, 0))

    seen: Set[Tuple[int,int]] = set()

    while curr != end and not q.empty():
        curr, count = q.get()

        if curr in seen:
            continue
        moves = valid_moves(curr, forest)
        #print(f'{i}: {curr}, moves: {moves}, seen: {seen}')
        for item in moves:
            if item not in seen:
                q.put((item, count + 1))

        seen.add(curr)
        if curr == end:
            return curr, count
        
        # print(', '.join(str(p) for p in q))
        #print(f'after evaluating items in round {i}: q is :{q.qsize()}, and {curr, count}')

    return None

def main() -> int:

    forest: Forest = {}
    start: Point = (0,0)
    end: Point = (0,0)

    for j, l in enumerate(sys.stdin):
        for i, c in enumerate(l.strip()):
            if c == 'S':
                start = (i,j)
            elif c == 'E':
                end = (i,j)
            forest[(i,j)] = elevation(c)

    curr = start

    i = 0

    _, steps = bfs(start, end, forest)
    print(steps)
    best_start = (start, steps)
    for k, v in forest.items():
        if v == 1:
            result = bfs(k, end, forest)
            if result is not None:
                _, next_steps = result
            if next_steps < best_start[1]:
                best_start = (k, next_steps)
                print(f'new best: {best_start}')

    print(best_start)

    return 1

if __name__ == '__main__':
    sys.exit(main())
