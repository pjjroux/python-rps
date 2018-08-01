import psycopg2
import string
import random

class DB:

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

            print(game_id)
            

            # cursor.execute("INSERT INTO python_rps (game_id, round, user_play, com_play, winner) VALUES (%s, %s, %s, %s, %s)", (var1,var2,var3,var4,var5))
            # self.conn.commit()
            # cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()


    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        """Generate a random id string with a length"""
        return ''.join(random.choice(chars) for _ in range(size))

    def new_game_id(self):
        """Get a new game id and test for duplication"""
        game_id = self.id_generator()

        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT game_id FROM python_rps WHERE game_id = '%s'""", (game_id))
            row = cursor.fetchone()

            # If game_id already exists in table get new id and try again
            while row is not None:
                self.new_game_id()

            return game_id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


db = DB()
db.store_match_data(())