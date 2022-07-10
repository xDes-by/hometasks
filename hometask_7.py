import sqlite3 as sql


class database:
    def __init__(self, name):
        self.connect = sql.connect(name + ".db")
        cursor = self.connect.cursor()
        with self.connect:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Employees (
                  empId INTEGER PRIMARY KEY,
                  username TEXT NOT NULL,
                  dept TEXT NOT NULL,
                  job_id TEXT NOT NULL,
                  salary INTEGER NOT NULL,
                  department_id INTEGER NOT NULL,
                  date_job DATE NOT NULL,
                  manager_id INTEGER NOT NULL
                )
            """)
            datas = (
                (1, 'Nine', 'Sales', 'IT_PROG', 56000, 23, '2021-12-03', 5),
                (2, 'David', 'Accounting', 'HR', 12050, 54, '2021-05-23', 3),
                (3, 'Ave', 'Buy', 'PROG', 43000, 50, '2019-02-27', 5),
                (4, 'Ava', 'Sales', 'IT_PROG', 42000, 50, '2019-02-27', 4),
                (5, 'Nine', 'Sales', 'IT_PROG', 56000, 23, '2021-12-03', 5),
                (6, 'David', 'Accounting', 'HR', 12150, 54, '2021-05-23', 3),
                (7, 'Ave', 'Buy', 'PROG', 43000, 50, '2019-02-27', 5),
                (8, 'Ava', 'Sales', 'IT_PROG', 42000, 50, '2019-02-27', 4),
                (9, 'Nine', 'Sales', 'IT_PROG', 56000, 23, '2021-12-03', 5),
                (10, 'David', 'Accounting', 'HR', 12050, 54, '2021-05-23', 3),
                (11, 'Ave', 'Buy', 'PROG', 43000, 50, '2019-02-27', 5),
                (12, 'Ava', 'Sales', 'IT_PROG', 42000, 50, '2019-02-27', 4),
            )
            cursor.executemany("INSERT INTO Employees VALUES(?, ?, ?, ?, ?, ?, ?, ?)", datas)

        self.connect.close()

    def asks(self, name):
        self.connect = sql.connect(name + ".db")
        cursor = self.connect.cursor()

        cursor.execute("SELECT * FROM Employees")
        cursor.execute("SELECT * FROM Employees WHERE username = 'David'")
        cursor.execute("SELECT * FROM Employees WHERE job_id = 'IT_PROG'")
        cursor.execute("SELECT * FROM Employees WHERE department_id = 50 AND salary > 4000")
        cursor.execute("SELECT * FROM Employees WHERE username LIKE '%a'")
        cursor.execute("SELECT * FROM Employees WHERE username LIKE '%n%n%'")
        cursor.execute("""
                        SELECT department_id,
                        MIN(salary) as min_salary,
                        MAX(salary) max_salary,
                        MIN(date_job) min_date_job,
                        MAX(date_job) max_date_job,
                        COUNT(*) count
                        FROM Employees
                        GROUP BY department_id
                        order by count(*) desc
                        """)
        cursor.execute("""
                        SELECT manager_id
                        FROM Employees 
                        GROUP BY manager_id 
                        HAVING COUNT(*) > 5 AND SUM(salary) > 50000
                        """)
        self.connect.close()


d = database("Employees")
d.asks("Employees")
