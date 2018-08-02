import psycopg2
import string
import random

class Database:

    def __init__(self):
        """Open connection to postgre sql host"""
        try:
            connect_str = "dbname='onpvifdj' user='onpvifdj' host='dumbo.db.elephantsql.com' " + \
                        "port='5432' password='wlRRZhncI759WyadJ0F65AGznPeJp9Qg'"
            conn = psycopg2.connect(connect_str)
            self.conn = conn
        except Exception as e:
            print("Unable to connect to database:")
            print(e)

    def store_match_data(self, match_log):
        """ insert match data into database  """
        try:
            cursor = self.conn.cursor()
          
            # Get a game_id for the match
            game_id = self.new_game_id()

            for round_result in match_log:
                round_num = round_result['Round']
                user_result = round_result['User']
                com_result = round_result['Com']
                winner = round_result['Result'][0]

                cursor.execute("INSERT INTO python_rps (game_id, round, user_play, com_play, winner) VALUES (%s, %s, %s, %s, %s)", 
                    (game_id, round_num, user_result, com_result, winner,))
                self.conn.commit()
            
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        """Generate a random id string with a length"""
        return ''.join(random.choice(chars) for _ in range(size))

    def new_game_id(self):
        """Get a new game id and test for duplication"""
        game_id = self.id_generator()

        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT game_id FROM python_rps WHERE game_id = %s""", (game_id,))
            row = cursor.fetchone()

            # If game_id already exists in table get new id and try again
            while row is not None:
                self.new_game_id()

            cursor.close()
            return game_id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def print_all_data(self):
        """Get all the entries in database"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM python_rps""")
            rows = cursor.fetchall()

            for row in rows:
                print(row)
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def print_table_structure(self):
        """Display the table structure"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT
                    TABLE_NAME,
                    COLUMN_NAME,
                    DATA_TYPE,
                    CHARACTER_MAXIMUM_LENGTH
                FROM
                    information_schema.COLUMNS
                WHERE
                    TABLE_NAME = 'python_rps';
            """)
            rows = cursor.fetchall()

            for row in rows:
                print(row)
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        
        
        
        
        
        
        
      