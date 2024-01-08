尚硅谷Python爬虫教程小白零基础速通（含python基础+爬虫案例）
https://www.bilibili.com/video/BV1Db4y1m7Ho

```
清华大学开源软件镜像站：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云开源镜像站：https://mirrors.aliyun.com/pypi/simple/
豆瓣：https://pypi.douban.com/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
```
eg: pip install [包名] -i https://pypi.tuna.tsinghua.edu.cn/simple 

配置镜像源方法：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip的freeze命令用于生成将当前项目的pip类库列表生成 requirements.txt 文件
生成requirements.txt文件：
pip freeze > requirements.txt

下载requirements.txt文件中的包：
pip install -r requirements.txt

