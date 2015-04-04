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

#### 学生添加课程

URL: http://xxx/lizi/addCourse/

POST:

| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 | 
