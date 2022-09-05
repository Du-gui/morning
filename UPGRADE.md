# 更新说明

## 2022.08.22

1. 增加天气范围（最高温、最低温）
2. 支持多个接收人
3. 所有字段都是彩色的

示例模板：

今天是 {{ date.DATA }}

天气 {{ weather.DATA}}

今天温度：{{ lowest.DATA }}度 - {{ highest.DATA }}度

明日天气：{{ wea_tomo.DATA}}

明日温度：{{ lowest_tomo.DATA }}度 - {{ highest_tomo.DATA }}度

当前温度：{{ temperature.DATA }}

低温：{{ lowest.DATA }}

最高温：{{ highest.DATA }}

我们已经相恋 {{ love_days.DATA }} 天啦

距离你的生日还有：{{ birthday_left.DATA }} 天

武汉新增无症状: {{ wzzadd.DATA}}

{{ words.DATA }}




今天是： {{date.DATA}} 
今日天气：{{weather.DATA}} 
今天温度：{{ lowest.DATA }}度 - {{ highest.DATA }}度 
明日天气：{{wea_tomo.DATA}} 
明日温度：{{lowest_tomo.DATA}}度 - {{highest_tomo.DATA}}度 
距离你生日还有：{{birthday_left.DATA}}天
武汉市昨日新增：
确诊：{{ confirm.DATA }}
无症状：{{ wzzadd.DATA }}
{{words.DATA}}	