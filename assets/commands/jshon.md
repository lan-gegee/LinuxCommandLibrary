# TAGLINE

在 shell 脚本中解析 JSON

# TLDR

**提取键的值**

```echo '{"name":"test"}' | jshon -e name```

**获取字符串值**（不带引号）

```echo '{"name":"test"}' | jshon -e name -u```

**获取数组元素**

```echo '[1,2,3]' | jshon -e 0```

**列出对象的键**

```echo '{"a":1,"b":2}' | jshon -k```

**迭代数组并解包**值

```echo '["a","b","c"]' | jshon -a -u```

**从文件读取**并提取

```jshon -F [data.json] -e name -u```

# SYNOPSIS

**jshon** [_options_]

# PARAMETERS

**-F** _PATH_
> 从文件而非 stdin 读取 JSON。

**-S**
> 按键排序返回 JSON。

**-Q**
> 静默模式；不在 stderr 上报错。

**-C**
> 遇到可恢复错误时继续执行（例如提取不存在的键时添加 null）。

**-I**
> 原地编辑文件；需要配合 **-F**。会抑制正常输出。

**-0**
> 用 null 字节作为 **-u** 输出的分隔符，替代换行符。

**-e** _INDEX_
> 提取键或数组索引处的值。

**-s** _VALUE_
> 创建 JSON 字符串。

**-n** _VALUE_
> 创建 JSON 非字符串值（数字、true、false、null、{}、[]）。

**-u**
> 解包（去除引号）字符串值。

**-t**
> 显示当前值的类型（string、number、bool、null、object、array）。

**-l**
> 显示当前对象或数组的长度。

**-k**
> 返回以换行分隔的键列表。

**-a**
> 迭代数组元素。

**-p**
> 弹出栈上最近一次操作。

**-d** _INDEX_
> 删除键或数组索引处的元素。

**-i** _INDEX_
> 将栈上的子元素插入下方的数组/对象。

**--version**
> 打印版本并退出。

# DESCRIPTION

**jshon** 可以从 shell 中解析、读取和创建 JSON。它取代了用 grep/sed/awk 拼凑的脆弱临时解析方案，以及用 perl/python 编写的笨重单行解析器。

各操作基于一个栈式编辑历史串联起来。每次操作都会把结果压入栈中，最后打印最终值。**-I** 标志支持对文件进行原地编辑。

# CAVEATS

基于 C 的工具。语法采用链式调用。复杂查询建议改用 jq。

# HISTORY

jshon 的开发目标是提供一个对 shell 友好、面向管道接口的 JSON 解析器。

# INSTALL

```apt: sudo apt install jshon```

```pacman: sudo pacman -S jshon```

```apk: sudo apk add jshon```

```zypper: sudo zypper install jshon```

```brew: brew install jshon```

```nix: nix profile install nixpkgs#jshon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jo](/man/jo)(1), [json_pp](/man/json_pp)(1)
