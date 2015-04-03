# lizi-backend

### 介绍
栗子点名的后台服务, 采用 django + mysql 完成后台


### 权限介绍

在用户登录时会获取到两个token, 用以访问用户的个人信息.

AccessToken 有效期为24小时, 对用户的信息更改, 课程添加, 点名等权限操作中都需要AccessToken进行权限验证

RefreshToken 有效期为一个月, 用以在AccessToken过期后, 获取最新的 AccessToken. RefreshToken 仅在登录操作时进行分发, 所以, 单个用户在登录后, 最长在一个月内不需要再次进行登录操作

### API介绍

没有特殊声明情况下, 请使用 UTF-8 进行交互

#### 登录

URL: http://xxx/lizi/login/

POST:

| 参数 | 类型 | 可否为空 | 描述 |
| --- | ----- | ------- | ----- |
| phone\_number | 字符串 | 否 |  用户手机号 |
| password | 字符串 | 否 | 用户密码 |

响应示例:

```
{
	"status" : "0000",
	"AccessToken" : "sadhfksjdahfa",
	"RefreshToken" : "465466asrgasrgas"
}
```

#### 注册

URL: http://xxx/lizi/reg/

POST:

| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| phone\_number | 字符串 | 否 | 用户手机号 |
| password | 字符串 | 否 | 用户手机号 |
| real\_name | 字符串 | 可 | 用户姓名 |
| mail | 字符串 | 可 | 用户邮箱 |
| device\_token | 字符串 | 可 | 用户设备号 |

教师POST数据格式一致, 但是对应的地址不同, 为 http://xxx/lizi/t/reg/

响应示例

```
{
	"status" : "0000",
	"AccessToken" : "regOk",
	"RefreshToken" : "regOK"
}
```

#### 教师添加课程

URL: http://xxx/lizi/t/addCourse/

POST:

| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | ---- | ---- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| course\_name | 字符串 | 否 | 课程名称 |

响应示例

```
{
	"status" : "0000",
	"course_id" : "0000001"
}
```

####





















