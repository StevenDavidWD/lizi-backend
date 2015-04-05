# lizi-backend

#### 介绍
栗子点名的后台服务, 采用 django + mysql 完成后台

#### 配置需求

```
env
	- bcrypt 1.1.1
	- cffi 0.9.2
	- Django 1.7.7
	- MySQL-python 1.2.5
	- Pillow 2.8.1
	- pip 6.0.8
	- pycparser 2.10
	- setuptools 14.3.1
	- South 1.0.2
```

#### 权限介绍

在用户登录时会获取到两个token, 用以访问用户的个人信息.

AccessToken 有效期为24小时, 对用户的信息更改, 课程添加, 点名等权限操作中都需要AccessToken进行权限验证

RefreshToken 有效期为一个月, 用以在AccessToken过期后, 获取最新的 AccessToken.

AccessToken 和 RefreshToken 使用jwt进行处理, 由后台生成, 解密验证.

#### [API介绍](https://github.com/SundayDX/lizi-backend/blob/master/api.md)

#### [状态码列表](https://github.com/SundayDX/lizi-backend/blob/master/status.md)
