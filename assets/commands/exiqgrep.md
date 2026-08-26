# TAGLINE

Exim 邮件队列搜索工具

# TLDR

匹配**发件人**地址（不区分大小写）

```exiqgrep -f '<[email@example.com]>'```

匹配发件人并只显示**消息 ID**

```exiqgrep -i -f '<[email@example.com]>'```

匹配**收件人**地址

```exiqgrep -r '[email@example.com]'```

**删除**所有匹配发件人的消息

```exiqgrep -i -f '<[email@example.com]>' | xargs exim -Mrm```

检测**退信**消息

```exiqgrep -f '^<>$'```

显示退信消息的**数量**

```exiqgrep -c -f '^<>$'```

# SYNOPSIS

**exiqgrep** [_options_] [_pattern_]

# PARAMETERS

**-f** _pattern_
> 匹配发件人地址

**-r** _pattern_
> 匹配收件人地址

**-i**
> 只显示消息 ID

**-c**
> 只显示数量

**-o** _seconds_
> 匹配早于指定秒数的消息

**-y** _seconds_
> 匹配晚于指定秒数的消息

**-z**
> 只匹配冻结的消息

**-x**
> 只匹配非冻结的消息

**-b**
> 简短格式输出

**-R**
> 反转输出顺序

# DESCRIPTION

**exiqgrep** 是一个用于搜索 Exim 邮件队列的 Perl 脚本。它按发件人、收件人、时间、冻结状态等条件过滤队列输出。必须至少给出一个筛选选项或 **-c**。

它常与 **exim -Mrm** 配合使用，从队列中删除匹配的消息。

# CAVEATS

仅适用于 Exim 邮件服务器。模式采用 Perl 正则表达式。需要相应的权限才能访问邮件队列。

# INSTALL

```apt: sudo apt install exim4-base```

```apk: sudo apk add exim-scripts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exim](/man/exim)(8)
