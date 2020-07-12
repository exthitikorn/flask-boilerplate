import psycopg2
import os

try:
    # db_secret = os.environ["DATABASE_URL"]
    db_secret = 'postgres://xanrjxwnnjfcat:ee47a4bf184c8177c5f3b943397a21a120628c11d472d737c11112d5a4cc05b0@ec2-52-200-48-116.compute-1.amazonaws.com:5432/d3jno2a52ealhp'
    connection = psycopg2.connect(db_secret)
    connection.set_session(autocommit=True)

    cur = connection.cursor()
    cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE';
    """)
    rows = cur.fetchall()
    print('Table list:')
    for row in rows:
        print("   ", row[0])
    cur.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

def get_student_data():
    cur = connection.cursor()
    cur.execute("""
    select firstname,lastname,age,gpa
    from student;
    """)
    rows = cur.fetchall()
    print('Student :')
    print(rows)
    cur.close()
    return rows


get_student_data()