# bilibili-videotop-get
爬取b站目标分区某个月份的视频数据

获取的目标数据：
｛视频av,标题,更新时间,播放量,收藏数量,评论数量,作者,作者uid,弹幕数量,子分区,大分区｝

参数
数据url:https://s.search.bilibili.com/cate/search?


<table>
  <tr><th>key</th> <th>value</th></tr>
	<tr><td>callback</td> <td>ran</td></tr>
  <tr><td>main_ver</td> <td>v3</td></tr>
  <tr><td>search_type</td> <td>video</td></tr>
	<tr><td>view_type</td> <td>hot_rank</td>
		<tr><td>order</td> <td>click</td></tr>
	<tr><td>copy_right</td> <td>-1</td></tr>
	<tr><td>cate_id</td> <td>分区id</td></tr>
	<tr><td>page</td> <td>页数</td></tr>
	<tr><td>pagesize</td> <td>每页显示x（最大100）条数据</td></tr>
	<tr><td>jsonp</td> <td>jsonp</td></tr>
	<tr><td>time_from</td> <td>'20181001' #日期段</td></tr>
	<tr><td>time_to</td> <td>'20181031' #日期段</td></tr>
	<tr><td>_</td> <td>当前时间（毫秒）</td></tr>
  </tr>
</table>
