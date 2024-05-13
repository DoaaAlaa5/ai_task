from pyamaze import maze,agent, textLabel, COLOR
from collections import deque

def BFS(m, start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier=deque()
    frontier.append(start)
    bfsPath = {}
    explored=[start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
                bSearch.append(childCell)
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch, bfsPath,fwdPath

if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze(loopPercent=100,theme='light')
    bSearch,bfsPath, fwdPath=BFS(m)

    a=agent(m,shape='square' ,footprints=True, filled=True, color=COLOR.yellow)
    b=agent(m,shape='arrow' ,footprints=True, filled=False, color=COLOR.red)
    #c=agent(m, shape='arrow', footprints=True, filled=True, goal=m.rows)

    m.tracePath({a:bSearch}, delay=40)
    m.tracePath({b:fwdPath}, delay=30)
    #m.tracePath({c:bfsPath})
    l=textLabel(m,'Length of the shortest parh', len(fwdPath)+1)
    m.run()