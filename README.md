# A*-Pathfinding-Algorithm-Visualization-Tool-in-Python



**Purpose of the Pathfinding Tool**

The purpose of this program is to implement the well-known A* informed search algorithm in a visual way, in order to find the shortest path between 2 points. The user of the program will be in full control of the 2 points and other metrics such as barriers, which will further be explained. A short introduction to the A* algorithm is paramount to understanding how this tool will perform its search. This algorithm can be useful in mapping applications such as finding the shortest travelling distances using state highways, finding the most cost-efficient travelling paths, and so on. 



**Brief explanation of the A* algorithm**

The A* search algorithm is an **informed** search algorithm. This simply denotes that it depends on weighted paths between 2 points on a grid, and is always going to try and find the lowest-cost path, whether that's in terms of distance, time travelled, etc. In this case, we will be trying to find the shortest path in terms of distance on a 2-D grid. The algorithm does this using the following equation ***f(n) = g(n) + h(n)***. F(n) represents the shortest path from the start node to the end node. G(n) represents the shortest path from the start or beginning node to the current node n. H(n), known as the Heuristic function estimates the length of the shortest path from the current node n, to the end node. This estimation of the heuristic function is calculated using an absolute distance, such as Manhattan distance, Euclidian etc. For the sake of this implementation, Manhattan distance (aka L distance) was used. It can intuitively be seen that the overall shortest distance from start to end node is the sum of the shortest distance from the beginning node to the current node (aka g(n)), and the estimated shortest distance from current node n to the end node (aka h(n)). 

**Pre-requisite for running the program**

The end-user will have to pip-install the open-source cross-platform library **pygame** ,  locally when trying to run the program.  For more information visit

https://pypi.org/project/pygame/ 

**User guide for the Python visualization tool**

1. When running the program, a 40 by 40 square grid will appear. The user is supposed to select one square as the beginning node by left-clicking on it. That square will be represented in the ORANGE colour. ![image-20210114225735410](C:\Users\Boris\AppData\Roaming\Typora\typora-user-images\image-20210114225735410.png)

2. After completing the previous step, the user will right click a square that is NOT the beginning node, and that square will be the end node. 

   That square will be represented in the BLUE colour![image-20210114225809266](C:\Users\Boris\AppData\Roaming\Typora\typora-user-images\image-20210114225809266.png)

3. The user can select more than one square (that isn't the beginning or end square) to be the BORDERS. The search algorithm will have to avoid those borders, thus making the search a little more difficult and interesting. 

   The borders will be represented in the BLACK colour.![image-20210114225859981](C:\Users\Boris\AppData\Roaming\Typora\typora-user-images\image-20210114225859981.png)

4. When the beginning, end, and borders have been selected, the user can press the space button to run the algorithm. While the algorithm is running the user cannot change any of the beginning, end, and border nodes.

5. While the algorithm is running, green squares that appear will represent nodes of the open set, that are being checked by the algorithm for a possible shortest path. The red squares are ones that have been checked and certainly won't fulfill the shortest path. 

   ![image-20210114230149716](C:\Users\Boris\AppData\Roaming\Typora\typora-user-images\image-20210114230149716.png)

6. At the end, a purple path will show up, showing the shortest path calculated by the A* algorithm 

   ![image-20210114230222940](C:\Users\Boris\AppData\Roaming\Typora\typora-user-images\image-20210114230222940.png)

   

   **Additional Notes:**  

   To reset everything back to a white grid, simply press the "c" key. To un-select a coloured square and make it its default white colour, simply right-click it.

   To close the whole program, press the x button in the top right corner. 



