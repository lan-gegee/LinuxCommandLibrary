# Shell 脚本编程

## 脚本基础
Shell 脚本是包含若干命令的文本文件，Shell 会按顺序执行这些命令。第一行应当是 **shebang**，用来告诉系统使用哪个解释器。
```#!/bin/bash```
```#!/usr/bin/env [bash](/man/bash)```

让脚本可执行并运行它。
```[chmod](/man/chmod) +x script.sh```
```./script.sh```

在脚本开头使用 **set** 选项可以尽早捕获错误：**-e** 遇到第一个错误就退出，**-u** 把未定义的变量视为错误，**-o pipefail** 使管道中任一命令失败时整个管道判定为失败。
```[set](/man/set) -euo pipefail```

## 变量
变量赋值时 **=** 两边**不能有空格**。给变量引用加上双引号可以防止分词。

| 表达式 | 说明 |
|-----|-------------|
| **VAR=value** | 赋值 |
| **VAR=$(command)** | 捕获命令输出（命令替换） |
| **$VAR** | 读取该值 |
| **${VAR}** | 以显式边界读取 |
| **"$VAR"** | 加引号安全地读取 |
| **${VAR:-default}** | VAR 未设置或为空时使用默认值 |
| **${VAR:=default}** | VAR 未设置或为空时赋予默认值 |
| **${VAR:+alternate}** | VAR 已设置且非空时使用替代值 |
| **${VAR:?error msg}** | VAR 未设置或为空时报错退出 |
| **${#VAR}** | 值的长度 |
| **readonly VAR** | 把变量设为只读 |
| **export VAR** | 让变量对子进程可用 |

## 引号规则
引号决定 Shell 会展开什么。拿不准时，就用双引号。

| 表达式 | 说明 |
|-----|-------------|
| **'text'** | 单引号：一切保持字面意义 |
| **"text"** | 双引号：$variables 和 $(commands) 会被展开 |
| **\$HOME** | 反斜杠转义单个字符 |

始终给变量引用加引号：**"$VAR"** 能保留值中的空格，不加引号的 **$VAR** 则会被拆分成独立的单词。

## 特殊变量
这些变量由 Shell 在脚本运行期间自动设置。

| 变量 | 说明 |
|-----|-------------|
| **$0** | 脚本的名称 |
| **$1..$9** | 位置参数（实参） |
| **${10}** | 第 9 个之后的位置参数 |
| **$#** | 参数的个数 |
| **$@** | 所有参数，各为一个独立单词 |
| `$*` | 所有参数合并成一个字符串 |
| **$?** | 上一条命令的退出状态码 |
| **$$** | 当前 Shell 的 PID |
| **$!** | 最后一个后台命令的 PID |
| **$_** | 上一条命令的最后一个参数 |

把参数传递给其他命令时优先使用 **"$@"**：它会把每个参数都保留为独立的单词。

## 字符串操作
Bash 内置了字符串处理功能，无需借助外部命令。

| 表达式 | 说明 |
|-----|-------------|
| **${VAR#pattern}** | 从开头删除最短匹配 |
| **${VAR##pattern}** | 从开头删除最长匹配 |
| **${VAR%pattern}** | 从结尾删除最短匹配 |
| **${VAR%%pattern}** | 从结尾删除最长匹配 |
| **${VAR/old/new}** | 替换第一次出现的内容 |
| **${VAR//old/new}** | 替换所有出现的内容 |
| **${VAR:offset}** | 从 offset 处开始的子串 |
| **${VAR:offset:length}** | 从 offset 处开始、长度为 length 的子串 |
| **${VAR^}** | 首字符转为大写 |
| **${VAR^^}** | 全部字符转为大写 |
| **${VAR,}** | 首字符转为小写 |
| **${VAR,,}** | 全部字符转为小写 |

大小写转换（**${VAR^^}**、**${VAR,,}**）需要 bash 4 或更高版本。

## 条件判断
在 bash 脚本中用 **[[ ]]** 做条件判断。它支持模式匹配和正则表达式匹配，比旧的 **[ ]** 形式更安全。方括号内侧的空格不可省略。
```if [[ -f "file.txt" ]]; then [echo](/man/echo) "exists"; fi```

| 运算符 | 说明 |
|-----|-------------|
| **-f file** | file 存在且为普通文件时为真 |
| **-d file** | file 存在且为目录时为真 |
| **-e file** | file 存在（任意类型）时为真 |
| **-r file** | file 可读时为真 |
| **-w file** | file 可写时为真 |
| **-x file** | file 可执行时为真 |
| **-s file** | file 存在且非空时为真 |
| **-z string** | string 为空时为真 |
| **-n string** | string 非空时为真 |
| **==** | 字符串相等（右侧可为 glob 模式） |
| **!=** | 字符串不相等 |
| **=~** | 正则表达式匹配（用于 [[ ]] 内） |
| **-eq** | 数值相等 |
| **-ne** | 数值不相等 |
| **-lt** | 数值小于 |
| **-le** | 数值小于等于 |
| **-gt** | 数值大于 |
| **-ge** | 数值大于等于 |

```if [[ "$count" -gt 0 ]]; then [echo](/man/echo) "positive"; elif [[ "$count" -eq 0 ]]; then [echo](/man/echo) "zero"; else [echo](/man/echo) "negative"; fi```
```if [[ "$input" =~ ^[0-9]+$ ]]; then [echo](/man/echo) "is a number"; fi```

**case** 语句用一个值去匹配若干 glob 模式。
```case "$1" in start) [echo](/man/echo) "Starting";; stop) [echo](/man/echo) "Stopping";; *) [echo](/man/echo) "Usage: $0 {start|stop}";; esac```

## 循环
**for** 循环遍历一个条目列表。
```for file in *.txt; do [echo](/man/echo) "$file"; done```
```for i in {1..10}; do [echo](/man/echo) "$i"; done```
```for ((i=0; i<10; i++)); do [echo](/man/echo) "$i"; done```

**while** 循环只要条件为真就一直运行。这是逐行读取文件的安全写法。
```while IFS= [read](/man/read) -r line; do [echo](/man/echo) "$line"; done < file.txt```

**until** 循环一直运行到条件成立为止。
```until [[ -f "ready.flag" ]]; do [sleep](/man/sleep) 1; done```

用 **break** 提前退出循环，用 **continue** 跳过本次迭代进入下一次。

## 函数
函数把可复用的命令组织在一起。在函数体内通过 **$1**、**$2** 等访问参数。使用 **local** 可以让变量的作用范围仅限于函数内部。
```greet() { local name="$1"; [echo](/man/echo) "Hello, $name"; }```
```greet "World"```

函数返回其最后一条命令的退出状态码；也可以用 **return** 显式设定退出码（0-255）。要返回字符串，可以使用命令替换。
```get_date() { [date](/man/date) +%Y-%m-%d; }```
```today=$(get_date)```

## 数组
Bash 支持索引数组。声明和操作方式如下。

| 表达式 | 说明 |
|-----|-------------|
| **arr=(a b c)** | 声明数组 |
| **arr[0]=value** | 按索引设置元素 |
| **${arr[0]}** | 按索引访问元素 |
| **"${arr[@]}"** | 所有元素，每个为一个独立单词 |
| **${#arr[@]}** | 元素的个数 |
| **${arr[@]:1:2}** | 切片：从索引 1 开始取 2 个元素 |
| **arr+=(d e)** | 追加元素 |
| **${!arr[@]}** | 所有的索引 |
| **unset 'arr[1]'** | 删除一个元素（索引会留下空洞） |

遍历所有元素时要给数组加上引号，这样含空格的元素就不会被拆散。
```for item in "${arr[@]}"; do [echo](/man/echo) "$item"; done```

关联数组（字符串键）需要显式声明。
```declare -A map```
```map[key]="value"```
```[echo](/man/echo) "${map[key]}"```

## 算术运算
用 **$(( ))** 求算术表达式的值，用 **(( ))** 执行算术语句。

| 表达式 | 说明 |
|-----|-------------|
| **$((a + b))** | 加法 |
| **$((a - b))** | 减法 |
| `$((a * b))` | 乘法 |
| **$((a / b))** | 整数除法 |
| **$((a % b))** | 取模 |
| `$((a ** b))` | 幂运算 |
| **$((a++))** | 后自增 |
| **$((++a))** | 前自增 |
| **((a += 5))** | 算术赋值 |

Shell 算术只支持整数。浮点运算可以通过管道交给 **bc** 处理。
```[echo](/man/echo) "scale=2; 10 / 3" | [bc](/man/bc)```

## 输入与输出
使用 **read** 从用户或文件获取输入。
```[read](/man/read) -p "Enter name: " name```
```[read](/man/read) -s -p "Password: " pass```
```[read](/man/read) -r -a items <<< "a b c"```

使用 **printf** 进行格式化输出，它比 **echo** 更具可移植性、行为更可预期。
```[printf](/man/printf) "Name: %s, Age: %d\n" "$name" "$age"```

**here document** 把多行文本传给命令的标准输入。
```
[cat](/man/cat) <<EOF
Hello, $USER
Your home is $HOME
EOF
```

使用带引号的 **<<'EOF'** 可以阻止 here document 内部发生变量展开。

## 退出码与陷阱
每个命令都会返回一个退出码：**0** 表示成功，其余表示失败。最后一条命令的退出码保存在 **$?** 中。使用 **exit** 可以设置脚本自身的退出码。
```command || [exit](/man/exit) 1```
```command && [echo](/man/echo) "succeeded"```

使用 **trap** 可以在脚本退出或收到信号时执行清理代码。EXIT 陷阱在任何退出情况下都会触发，包括发生错误时。
```tmpfile=$([mktemp](/man/mktemp))```
```[trap](/man/trap) '[rm](/man/rm) -f "$tmpfile"' EXIT```
```[trap](/man/trap) '[echo](/man/echo) "Interrupted"; exit 130' INT TERM```

## 调试
不执行脚本，仅检查语法。
```[bash](/man/bash) -n script.sh```

运行时逐条跟踪命令，并显示展开后的变量。
```[bash](/man/bash) -x script.sh```

在脚本内部开启和关闭跟踪。
```[set](/man/set) -x```
```[set](/man/set) +x```

对脚本做静态检查，找出常见错误和陷阱。
```[shellcheck](/man/shellcheck) script.sh```
