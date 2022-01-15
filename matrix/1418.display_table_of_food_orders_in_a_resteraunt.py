# 给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。

# 请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

# 注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

# 输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# 输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
# 解释：
# 点菜展示表如下所示：
# Table,Beef Burrito,Ceviche,Fried Chicken,Water
# 3    ,0           ,2      ,1            ,0
# 5    ,0           ,1      ,0            ,1
# 10   ,1           ,0      ,0            ,0
# 对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
# 而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
# 餐桌 10：Corina 点了 "Beef Burrito" 

from collections import defaultdict

class Solution:
    def displayTable(self, orders):

        dishes = set()
        tables = set()
        c = Counter()

        # 数据准备
        for name, table, dish in orders:
            tables.add(int(table))
            dishes.add(dish)
            c[(table, dish)] += 1
       
        dishes = sorted(dishes)
        tables = sorted(tables)

        #构建一个空的二维数组，第一个位置空出来
        result = [[ '0' for _ in range(len(dishes) + 1)] for _ in range(len(tables) + 1)]
        


        result[0][0] = 'Table'
        print(c)

      
        # 填第一行
        for i in range(1, len(dishes) + 1):
            result[0][i] = dishes.pop(0)

        # 填第一列
        for i in range(1, len(tables) + 1):
            result[i][0] = str(tables.pop(0))

        # 填 table - dish 出现次数结果
        for i in range(1, len(result)):
            for j in range(1, len(result[0])):
                table_num = result[i][0]
                dish_name = result[0][j]
                result[i][j] = str(c[(table_num, dish_name)])


        return result
        

