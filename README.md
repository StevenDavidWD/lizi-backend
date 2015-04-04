# lizi-backend

### 介绍
栗子点名的后台服务, 采用 django + mysql 完成后台


### 权限介绍

在用户登录时会获取到两个token, 用以访问用户的个人信息.

AccessToken 有效期为24小时, 对用户的信息更改, 课程添加, 点名等权限操作中都需要AccessToken进行权限验证

RefreshToken 有效期为一个月, 用以在AccessToken过期后, 获取最新的 AccessToken. RefreshToken 仅在登录操作时进行分发, 所以, 单个用户在登录后, 最长在一个月内不需要再次进行登录操作

AccessToken 和 RefreshToken 使用jwt进行处理, 由后台生成, 解密验证.

### [API介绍](https://github.com/SundayDX/lizi-backend/blob/master/api.md)

### [状态码列表](https://github.com/SundayDX/lizi-backend/blob/master/status.md)
