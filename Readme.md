# 使用方法

```shell
# 生成迁移文件
python manage.py makemigrations
# 进行迁移
python manage.py migrate
```

这时会出现一个 `db.sqlite3`的文件， 你可以使用搜索相应的软件将其打开，其中包含所创建的数据表结构

### 接着运行服务

```shell
python manage.py runserver
```

浏览器中输入localhost:8000/account/