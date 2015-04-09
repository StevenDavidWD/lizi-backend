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
	"status": "00000",
	"RefreshToken": "eyJhbGciOiJI...MMC5G2_aE",
	"AccessToken": "eyJhbGci...CYkrZuFjnvBd8g"
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
	"status": "00000",
	"RefreshToken": "eyJhbGciOiJI...MMC5G2_aE",
	"AccessToken": "eyJhbGci...CYkrZuFjnvBd8g"
}
```

### 更新AccessToken

URL: http://xxx/lizi/refresh/

POST:

| 参数 | 类型 | 可否为空 | 描述 |
| --- | ---- | ----- | --- |
| RefreshToken | 字符串 | 否 | 更新Token |

响应示例



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
| course_id | 字符串 | 否 | 课程编号 |

### 教师、学生发帖

URL: http://xxx/lizi/postMessage/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| costent | 字符串 | 可 | 希望需要发布的内容 |
| course_id | 字符串 | 否 | 课程编号 |
| user_type | 字符串 | 否 | 查询者类型('User' 或 'Teacher') |

### 回帖

URL: http://xxx/lizi/postReply/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| costent | 字符串 | 可 | 希望需要回复的内容 |
| square_id | 字符串 | 否 | 帖子编号 |
| user_type | 字符串 | 否 | 查询者类型('User' 或 'Teacher') |

### 查看帖子

URL: http://xxx/lizi/checkMessage/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| course_id | 字符串 | 否 | 相关课程编号 |

### 查看帖子

URL: http://xxx/lizi/checkReply/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| square_id | 字符串 | 否 | 帖子编号 |


### 查看相关课程学生

URL: http://xxx/lizi/checkclassmates/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| course_id | 字符串 | 否 | 课程编号 |

### 查找某门课程

URL: http://xxx/lizi/searchCourse/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| course_id | 字符串 | 可 | 需查询的课程编号 |
| course_name | 字符串 | 可 | 需查询的课程名 |
| teacher_name | 字符串 | 可 | 希望查询的课程的任课教师名 |

### 查看课表

URL: http://xxx/lizi/course_table/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| user_type | 字符串 | 否 | 查询者类型('User' 或 'Teacher') |

### 为某门课添加点名码

URL: http://xxx/lizi/t/addend_code/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| course_id | 字符串 | 否 | 课程编号 |

### 学生点名入口

URL: http://xxx/lizi/rollCall/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| course_id | 字符串 | 否 | 课程编号 |
| attend_code | 字符串 | 否 | 点名用校验码 |

### 教师查看成功点名结果

URL: http://xxx/lizi/t/checkAttendSec/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| course_id | 字符串 | 否 | 课程编号 |
| teacher_id | 字符串 | 否 | 任课老师编号 |

### 教师查看成功点名结果

URL: http://xxx/lizi/checkAttend/

POST:
| 参数 | 类型 | 可否为空 | 描述 |
| --- | --- | --- | --- |
| AccessToken | 字符串 | 否 | 用户权限验证 |
| user_type | 字符串 | 否 | 查询者类型('User' 或 'Teacher') |