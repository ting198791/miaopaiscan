from .sql import Sql
from twisted.internet.threads import deferToThread
from miaopaiscan.items import MiaopaiscanItem


class miaopaiscanPipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        if isinstance(item, MiaopaiscanItem):
          videohref = item['videohref']
          look = item['look']
          suid = item['suid']
          videoabout = item['videoabout']
          like = item['like']
          commen= item['commen']
          date=item['date']
          # print(type(suid))
          # result=Sql.select_account(self,suid)
          # print(suid)
          # if result==None:
          Sql.insert_video(videohref,look,suid,videoabout,like,commen,date)
          print('插入数据')
          # else:
          #   print('已有该用户')

          return item

