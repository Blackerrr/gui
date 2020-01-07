import pymssql
import game_function as gf
import tkinter as tk


class DB:
    # 将数据库封装成类
    def __init__(self):
        self.conn = pymssql.connect(host = 'localhost',
                                    port = '56678',
                                    user = 'lwa',
                                    password = '210619',
                                    database = 'Student_manage')
        self.cursor = self.conn.cursor()


"""
def main():
    root = tk.Tk()
    db1 = DB()
    gf.query_avg_grade(db1.cursor, '2018001', root)


if __name__ == '__main__':
    main()
"""