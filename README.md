# 烂模晕秒刷视频python版
## 描述
有次在52破解里发现一位老哥发现了烂模晕的奥秘，本来就只看看，结果自己老师也干了一样的事情。加之python课刚刚讲爬虫到了这一节就顺便做了一下，没想到成功了。*（对不起，我该好好学习！对不起，我该好好学习！x10）*具体原理就看那位老哥帖子详解了，这里只提供**方法**<br>
附上老哥原贴链接：***https://www.52pojie.cn/thread-913736-1-1.html***<br>
## 依赖
python3.x<br>
requests(pip install requests)<br>
google chrome(带抓包的浏览器都可)<br>
## 具体流程
>* step1：打开你要刷的视频，打开`开发者工具`，并且点到`network`，点击左上角的`clear`(方便数据查看)<br>
>* step2：打开视频，播放2s，然后暂停，在`开发者工具`中发现`NAME`为`index.php?c=res&m=save_watch_to`的数据包打开<br>
>* step3：打开代码，将`base_url`赋值为数据包中`General`选框中的`Request URL`后跟的地址(大概是`https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to`)<br>
>* step4：把数据包中`Request Headers`选框中的`User-Agent`以及`Cookie`***(特别重要)***替换掉代码中`header`的数据<br>
**(注1：以上的数据更改了一次就没有必要每打开一个视频就更改一次。如果后面post请求打印的数据始终是`“error”`的话建议也检查一下上面的数据是否填错)**<br>
>* step5：把数据包中`Form Data`选框中的`clazz_course_id`，`res_id，watch_to`，`duration`，`current_watch_to`，一一替换代码里对应的数据，并且将`watch_to`的数据更改为`duration`***相同***的数据<br>
**(注2：step5每次打开一个视频都要执行一次，就是5个数据的复制粘贴，没啥难度)***<br>
>* step6：更改完后报存代码，运行此代码，如果返回值是`"success"`,刷新浏览器你就会发现你视频看完了，并且获得了经验值<br>
**(注3：如果返回打印的值是`"error"`返回step1依次检查一下对应参数更改是否有问题)<br>**

