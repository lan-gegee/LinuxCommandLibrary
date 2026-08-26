# JSON

## 入门
**jq** 是标准的命令行 JSON 处理器：它从文件或标准输入读取 JSON，应用过滤器，然后输出结果。最简单的过滤器 **.** 只是美化输出。
```[jq](/man/jq) "." file.json```
```[curl](/man/curl) -s https://api.github.com/users/torvalds | [jq](/man/jq) "."```
```[echo](/man/echo) '{"name": "Linux"}' | [jq](/man/jq) "."```

其他各有专长的替代工具：**jaq**（速度更快的 jq 克隆）、**dasel**（还支持 YAML、TOML、XML）、**fx** 与 **jless**（交互式查看器）、**gron**（让 JSON 可以用 grep 搜索）、**jo**（创建 JSON）、**jc**（把传统命令输出转换为 JSON）。

## 选择值
过滤器按路径定位值：**.key** 表示对象字段，**[0]** 表示数组索引，**[]** 用于遍历所有元素。**-r** 原样输出字符串，不带引号。
```[echo](/man/echo) '{"name": "Linux"}' | [jq](/man/jq) ".name"```
```[jq](/man/jq) ".user.address.city" file.json```
```[jq](/man/jq) ".items[0]" file.json```
```[jq](/man/jq) -r ".items[].name" file.json```

在其他工具中完成同样的选择：
```[echo](/man/echo) '{"name": "Linux"}' | [dasel](/man/dasel) -r json '.name'```
```[echo](/man/echo) '{"name": "Linux"}' | [fx](/man/fx) .name```
```[echo](/man/echo) '{"name": "Linux"}' | [jshon](/man/jshon) -e name```

## 过滤与转换
jq 过滤器可以像 Shell 管道一样用 **|** 串联。**select()** 保留匹配的元素，**map()** 对每个元素做变换。
```[jq](/man/jq) '.items[] | select(.price > 10)' file.json```
```[jq](/man/jq) '.items | map(.name)' file.json```
```[jq](/man/jq) '.items | length' file.json```
```[jq](/man/jq) 'keys' file.json```
```[jq](/man/jq) '.items | sort_by(.price)' file.json```

从现有字段构建新的对象。
```[jq](/man/jq) '.items[] | {title: .name, cost: .price}' file.json```

## 修改
用 **=** 设置或添加字段，用 **del()** 删除字段。jq 从不就地编辑；请把输出重定向到新文件。
```[echo](/man/echo) '{"name": "Linux"}' | [jq](/man/jq) '.year = 1991'```
```[echo](/man/echo) '{"name": "Linux", "year": 1991}' | [jq](/man/jq) 'del(.year)'```
```[echo](/man/echo) '{"name": "Linux"}' | [dasel](/man/dasel) put string -r json '.year' '1991'```
```[echo](/man/echo) '{"name": "Linux", "year": 1991}' | [dasel](/man/dasel) delete -r json '.year'```

## 创建
**jo** 用 Shell 参数构建 JSON；**jq -n** 仅凭过滤器构建 JSON。
```[jo](/man/jo) -p name=Linux year=1991```
```[jq](/man/jq) -n '{name: "Linux", year: 1991}'```

## 搜索与浏览
**gron** 把 JSON 展平为一条条独立的赋值语句，方便直接使用 **grep**，之后再用 **-u** 还原回去。**jless** 和 **fx** 支持折叠与搜索，可以交互式地浏览大型文档。
```[gron](/man/gron) file.json | [grep](/man/grep) "name"```
```[gron](/man/gron) file.json | [grep](/man/grep) "name" | [gron](/man/gron) -u```
```[jless](/man/jless) file.json```
```[fx](/man/fx) file.json```

## 格式转换
**yq** 对 YAML 应用 jq 风格的过滤器，**dasel** 可在各格式之间互相转换。**jc** 把传统命令的输出转换为 JSON，便于用 jq 继续处理。
```[yq](/man/yq) ".name" config.yaml```
```[dasel](/man/dasel) -r json -w yaml < file.json```
```[jc](/man/jc) ifconfig | [jq](/man/jq) ".[0].ipv4_addr"```

供机器读取的紧凑输出：**jq -c** 每个文档只打印一行，适用于 JSON Lines 流。
