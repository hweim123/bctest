import pymysql
import time

conn = pymysql.connect(host="47.106.85.252", port=3306, user="root", passwd="123456", db="mcp_test",
                       charset="utf8")
cur = conn.cursor()


def search_printer(printer_Code):
    # printer_Code = request.GET.get("printer", "")
    sql = "select * from mcp_equipment where equipment_code = %s"
    cur.execute(sql, printer_Code)
    printer_list = cur.fetchall()
    for i in printer_list:
        pass
       # print(i)
    return i

    # print(printer_list)


search_printer('17080894UI')
