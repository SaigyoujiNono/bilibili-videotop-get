import random
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import re,time

####各分区cate_id表####
# 动画区=[MAD_AMV:24,MMD_3D:25,短片_手书_配音:47,综合:27]
# 音乐区=[原创音乐:28,翻唱:31,VOCALOID_UTAU:30,演奏:59,三次元音乐:29,OP_ED_OST:54,音乐选集:130]
# 舞蹈区=[宅舞:20,三次元舞蹈:154,舞蹈教程:156]
# 游戏区=[单机游戏:7,电子竞技:171,手机游戏:172,网络游戏:65,桌游棋牌:173,GMV:121,音游:136,Mugen:19]
# 科技区=[趣味科普人文:124,野生技术协会:122,演讲_公开课:39,星海:96,数码:95,机械:98,汽车:176]
# 生活区=[搞笑:138,日常:21,美食圈:76,动物圈:75,手工:161,绘画:162,运动:163,其他:174]
# 鬼畜区=[鬼畜调教:22,音MAD:26,人力VOCALLOID:126,教程演示:127]
cartoon_cate_id = [24, 25, 47, 27]
cartoon_name=['MAD_AMV','MMD_3D','shoushu','zonghe']
music_cate_id =[28,31,30,59,29,54,130]
music_name=['yuanchuang','fanchang','VOCALOID_UTAU','yanzou','sanciyuanyinyue','OP_ED_OST','yinyuexuanji']
dance_cate_id =[20,154,156]
dance_name=['zhaiwu','sanciyuanwudao','wudaojiaocheng']
game_cate_id =[7,171,172,65,173,121,136,19]
game_name=['danjiyouxi','dianzijingji','shoujiyouxi','wangluoyouxi','zhuoyouqipai','GMV','yinyou','Mugen']
science_cate_id =[124,122,39,96,95,98,176]
science_name=['quweikepurenwen','yeshengjishuxiehui','yanjiang','xinghai','shuma','jixie','qiche']
life_cate_id =[138,21,76,75,161,162,163,174]
life_name=['gaoxiao','richang','meishiquan','shougong','huihua','yundong','qita']
ghostAnimal_cate_id =[22,26,126,127]
ghostAnimal_name=['guichutiaojiao','yinMAD','renli','jiaohcengyanshi']
#分区列表
cate_id_all=[cartoon_cate_id,music_cate_id,dance_cate_id,game_cate_id,science_cate_id,life_cate_id,ghostAnimal_cate_id,]
cate_name_all=[cartoon_name,music_name,dance_name,game_name,science_name,life_name,ghostAnimal_name]
partition=['donghua','yinyue','wudao','youxi','keji','shenghuo','guichu']

head='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

def get_one_bilibiliTop(cate_id,page,user_agent):
    headers = {
        'User-Agent': user_agent
    }
    ran = 'jqueryCallback_bili_'+str(random.randint(5770214083336537, 9770214083336537))
    # 'time_from','time_to'表示从x年x月x日--->x年x月x日的区间
    data={
        'callback':ran,
        'main_ver':'v3',
        'search_type':'video',
        'view_type':'hot_rank',
        'order':'click',
        'copy_right':'-1',
        'cate_id':cate_id,
        'page':page,
        'pagesize':'100',
        'jsonp':'jsonp',
        'time_from':'20181001',
        'time_to':'20181031',
        '_':str(time.time()*1000)[:13]
    }
    url="https://s.search.bilibili.com/cate/search?"+urlencode(data)
    try:
        response=requests.get(url,headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def write_to_file(content,file_name):
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(content+'\n')

def parse_one_partitionPage(html,type,partition):
    pattern=re.compile('\{.*?play":"(.*?)".*?pubdate":"(.*?)".*?title":"(.*?)".*?review":(.*?),.*?mid":(.*?),.*?id":(.*?),.*?video_review":(.*?),.*?author":"(.*?)".*?favorites":(.*?),.*?\}',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'video_id': item[5],
            'title': item[2],
            'update': item[1],
            'play': item[0],
            'star': item[8],
            'review': item[3],
            'author': item[7],
            'author_id': item[4],
            'danmu': item[6],
            'type':type,
            'partition':partition
        }

def getData(partition,cate_id_group,cate_name):
    car_count = 0
    for cate_id in cate_id_group:
        print('接下来是'+cate_name[car_count])
        for page in range (1000):
            page_count=page+1
            html = get_one_bilibiliTop(cate_id, page_count, head).encode('utf-8').decode('unicode_escape')
            items = parse_one_partitionPage(html, cate_name[car_count], partition)
            items_count=0

            for item in items:
                items_count+=1
                wr=item['video_id']+","+item['title']+","+item['update'][:10]+","+item['play']+","+item['star']+","\
                       +item['review']+","+item['author']+","+item['author_id']+","+item['danmu']+","+item['type']+","\
                       +item['partition']
                strinfo = re.compile('\\\\')
                wr=strinfo.sub('',wr)
                write_to_file(wr,partition+'.txt')
                if items_count==100:
                    items_count=0

            print(partition + '分区' + cate_name[car_count] + '类：第' + str(page_count) + '页')
            time.sleep(round(random.uniform(0,3),2))
            #当 page 结束时跳转到下一个page
            if items_count!=0:
                break

        car_count+=1
        if car_count==cate_name.__len__():
            car_count=0

def main():
    for g in range(partition.__len__()):
        getData(partition[g],cate_id_all[g],cate_name_all[g])

if __name__ == '__main__':
    main()

###结尾说明###
#get_one_bilibiliTop(cate_id,page,user_agent):传入类型id、页码、headers，得到当前页面数据
#parse_one_partitionPage(html,type,partition):传入当前获取到的页面、类型、大分区
#getData(partition,cate_id_group,cate_name):传入分区、cate_id、名字
