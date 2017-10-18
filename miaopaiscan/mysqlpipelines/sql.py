import pymysql.cursors
from miaopaiscan import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

connection = pymysql.connect(host=MYSQL_HOSTS,
                             user=MYSQL_USER,
                             password=MYSQL_PASSWORD,
                             db=MYSQL_DB,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)






class Sql:
    @classmethod
    def insert_video(cls,videohref,look,suid,videoabout,like,commen,date):
      try:
         with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `miaopaivideo` (`videohref`,`look`,`suid`,`videoabout`,`like`,`commen`,`date`) VALUES (%(videohref)s, %(look)s,%(suid)s,%(videoabout)s,%(like)s,%(commen)s,%(date)s)"
            value = {
                'videohref': videohref,
                'look': look,
                'suid': suid,
                'videoabout': videoabout,
                'like': like,
                'commen': commen,
                'date':date
            }
            cursor.execute(sql, value)
      finally:
         connection.commit()

    def insert_account(cls,account,href,suid,video,follow,fan):
      try:
         with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `miaopaiuser` (`account`, `href`,`suid`,`video`,`follow`,`fan`) VALUES (%(account)s, %(href)s,%(suid)s,%(video)s,%(follow)s,%(fan)s)"
            value = {
                'account': account,
                'href': href,
                'suid': suid,
                'video': video,
                'follow': follow,
                'fan': fan
            }
            cursor.execute(sql, value)
      finally:
         connection.commit()


    def select_account(cls,suid):
      try:
         with connection.cursor() as cursor:
                # Read a single record
            sql = "SELECT `suid` FROM `miaopaiuser` WHERE `suid`=%(suid)s "
            value={
                'suid':suid,

            }
            cursor.execute(sql,value)
            result = cursor.fetchone()
            print(result)
            return result
      finally:
         connection.commit()
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()

    def select_count(cls,startint,endint):
        try:
            with connection.cursor() as cursor:
                sql="select count(*) from miaopaiuser where video>0 and fan >0  and (id BETWEEN %(startint)s and %(endint)s) "
                value = {
                    'startint': startint,
                    'endint':endint

                }
                cursor.execute(sql,value)
                result = cursor.fetchone()
                # print(result)
                return result
        finally:
            connection.commit()

    def select_countLimit(cls,startLimit,endLimit,startint,endint):
        try:
            with connection.cursor() as cursor:
                sql = "select * from miaopaiuser where video>0 and fan >0 and (id BETWEEN %(startint)s and %(endint)s) LIMIT %(startLimit)s,%(endLimit)s"
                value={
                    'startLimit':startLimit,
                    'endLimit':endLimit,
                    'startint': startint,
                    'endint': endint
                }
                cursor.execute(sql,value)
                result = cursor.fetchall()
                 # print(result)
                return result
        finally:
            connection.commit()

    def selectmaxid(cls,startint,endint):
        try:
            with connection.cursor() as cursor:
                sql="select max(u.id) 'id' from miaopaivideo v join miaopaiuser u on v.suid=u.suid  where u.id BETWEEN %(startint)s and %(endint)s"
                value = {
                    'startint': startint,
                    'endint': endint

                }
                cursor.execute(sql, value)
                result = cursor.fetchone()
                return result
        finally:
                connection.commit()

    #
    # @classmethod
    # def insert_dd_name(cls, xs_name, xs_author, category, name_id):
    #     sql = 'INSERT INTO dd_name (`xs_name`, `xs_author`, `category`, `name_id`) VALUES (%(xs_name)s, %(xs_author)s, %(category)s, %(name_id)s)'
    #     value = {
    #         'xs_name': xs_name,
    #         'xs_author': xs_author,
    #         'category': category,
    #         'name_id': name_id
    #     }
    #     cur.execute(sql, value)
    #     cnx.commit()
    #
    # @classmethod
    # def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
    #     sql = 'INSERT INTO dd_chaptername (`xs_chaptername`, `xs_content`, `id_name`, `num_id`, `url`) \
    #             VALUES (%(xs_chaptername)s, %(xs_content)s, %(id_name)s, %(num_id)s, %(url)s)'
    #     value = {
    #         'xs_chaptername': xs_chaptername,
    #         'xs_content': xs_content,
    #         'id_name': id_name,
    #         'num_id': num_id,
    #         'url': url
    #     }
    #     cur.execute(sql, value)
    #     cnx.commit()
    #
    # @classmethod
    # def id_name(cls, xs_name):
    #     sql = 'SELECT id FROM dd_name WHERE xs_name=%(xs_name)s'
    #     value = {
    #         'xs_name': xs_name
    #     }
    #     cur.execute(sql, value)
    #     for name_id in cur:
    #         return name_id[0]
    #
    # @classmethod
    # def select_name(cls, name_id):
    #     sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
    #     value = {
    #         'name_id': name_id
    #     }
    #     cur.execute(sql, value)
    #     return cur.fetchall()[0]
    #
    # @classmethod
    # def sclect_chapter(cls, url):
    #     sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
    #     value = {
    #         'url': url
    #     }
    #     cur.execute(sql, value)
    #     return cur.fetchall()[0]