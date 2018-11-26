# bilibili-videotop-get
爬取b站目标分区某个月份的视频数据

获取的目标数据：
｛视频av,标题,更新时间,播放量,收藏数量,评论数量,作者,作者uid,弹幕数量,子分区,大分区｝

参数
数据url:https://s.search.bilibili.com/cate/search?

data={data=
  'callback':ran,
  'main_ver':'v3',
  'search_type':'video',
  'view_type':'hot_rank',
  'order':'click',
  'copy_right':'-1',
  'cate_id':分区id,
  'page':页数,
  'pagesize':每页显示x（最大100）条数据,
  'jsonp':'jsonp',
  'time_from':'20181001',#日期段
  'time_to':'20181031',#日期段
  '_':当前时间（毫秒）
}
