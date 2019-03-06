import pymysql
import time

conn = pymysql.connect(host="120.79.101.183", port=3306, user="ymuser", passwd="yingmei2018", db="mcp_tcp",
                       charset="utf8")

cur = conn.cursor()
sql = "select order_id,received_time,modified_on,TIMESTAMPDIFF(SECOND, received_time, modified_on) AS result " \
      "from mcp_printer_task where printer_code = '17080894UI' and created_on between '2018-10-18 12:00:00'" \
      "and '2018-10-18 13:00:00' and order_status = 1 order by TIMESTAMPDIFF(SECOND, received_time, modified_on) desc"

cur.execute(sql)
rows = cur.fetchall()
print(len(rows))
print(rows)


for row in rows:
    ''' 
    if row[11] is not None:
          a = time.strptime(row[10], "%Y-%m-%d %H:%M:%S")
          created_time = time.mktime(a)
          print(created_time)
          modified_time = time.mktime(time.strptime(row[11], "%Y-%m-%d %H:%M:%S"))
          answer_time = modified_time - created_time
          print(answer_time)
    print("order_status:" row[3], "created_on:" row[10], "modified_on:"  row[11]) '''
    a = row[0]
    b = row[1]
    c = row[2]
    d = row[3]
    if d < 10:
        print("订单号：%s, 订单状态：%s, 创建时间：%s, 完成时间：%s，打印时间：%s") % (a, b, c, d)


