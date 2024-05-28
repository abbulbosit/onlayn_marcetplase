import psycopg2 as psql


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database='exam_4',
            user='postgres',
            password='2009',
            host='localhost',
            port='5432',
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'delete', 'update', 'insert', 'alter']
        if query_type in data:
            db.commit()
            if query_type == "create":
                return f" create successful"
            return f"{query_type} query successful"
        else:
            return cursor.fetchall()