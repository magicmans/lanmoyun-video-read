烂模晕秒刷视频python版
1.描述
有次在52破解里发现一位老哥发现了烂模晕的奥秘，本来就只看看，结果自己老师也干了一样的事情。加之python课刚刚讲爬虫到了这一节就顺便做了一下，没想到成功了。（对不起，我该好好学习！对不起，我该好好学习！x10）具体原理就看那位老哥帖子详解了，这里只提供方法
附上老哥原贴链接：https://www.52pojie.cn/thread-913736-1-1.html
2.依赖
python3.x
requests(pip install requests)
google chrome(带抓包的浏览器都可)
3.具体流程
step1：打开你要刷的视频，打开开发者工具，并且点到network，点击左上角的clear(方便数据查看)
step2：打开视频，播放2s，然后暂停，在开发者工具中发现name为index.php?c=res&m=save_watch_to的数据包打开
step3：打开代码，将base_url赋值为数据包中General选框中的Request URL后跟的地址(大概是https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to)
step4：把数据包中Request Headers选框中的User-Agent以及Cookie(特别重要)替换掉代码中header对应的数据
(注1：以上的数据更改了一次就没有必要每打开一个视频就更改一次。如果后面post请求打印的数据始终是“error”的话建议也检查一下上面的数据是否填错)
step5：把数据包中Form Data选框中的clazz_course_id，res_id，watch_to，duration，current_watch_to，一一替换代码里对应的数据，并且将watch_to的数据更改为duration相同的数据
(注2：step5每次打开一个视频都要执行一次，就是5个数据的复制粘贴，没啥难度)
step6：更改完后报存代码，运行此代码，如果返回值是"success",刷新浏览器你就会发现你视频看完了，并且获得了经验值
(注3：如果返回打印的值是"error"返回step1依次检查一下对应参数更改是否有问题)
