import sqlite3
import pandas as pd

conn = sqlite3.connect('attendance.db')
df = pd.read_sql_query("SELECT * FROM attendance", conn)
df.to_excel("attendance_export.xlsx", index=False)

print("✅ Attendance data exported to attendance_export.xlsx")
conn.close()
