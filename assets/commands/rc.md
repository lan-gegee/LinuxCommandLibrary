# TAGLINE

Unix 上的 Plan 9 命令 shell

# TLDR

**启动交互式 rc shell**

```rc```

**执行脚本**

```rc [script.rc]```

**执行命令字符串**

```rc -c '[command]'```

**不读取 profile 启动 rc**

```rc -n```

**启动登录 shell**

```rc -l```

# SYNOPSIS

**rc** [**-einvxl**] [**-c** _command_] [_file_ [_arguments_]]

# PARAMETERS

**-c** _command_
> 执行给定的命令字符串后退出

**-e**
> 任何命令返回非零状态时退出

**-i**
> 以交互方式运行（从终端读取命令）

**-l**
> 表现为登录 shell（读取 profile）

**-n**
> 不读取个人 profile（$home/lib/profile）

**-v**
> 在读取输入时将其回显到标准错误

**-x**
> 在执行命令时打印命令和参数

# DESCRIPTION

**rc** 是 Plan 9 的命令解释器，是 Bourne shell 的一个更简洁的替代品。它最初为贝尔实验室的 Plan 9 设计，后来被移植到 Unix 系统，提供了更简单、更一致的语法。

与 Bourne shell 的字符串变量不同，rc 将列表值变量（字符串数组）作为基本类型。这消除了许多引号问题，使参数处理更加自然。

Rc 的控制结构采用类似 C 的语法：用 **if**、**while**、**for**、**switch** 进行流程控制，用 **fn** 定义函数。其语法定义由形式文法（使用 yacc 实现）描述，因此无歧义且行为可预测。

管道、重定向和命令替换的用法与其他 shell 类似。后台执行使用 **&**，命令分组使用 **{}** 而不是子 shell。

# SYNTAX DIFFERENCES FROM BOURNE SHELL

**Variables**: `var=value` 写法相同，但 `$var` 会展开为列表
**Lists**: `list=(a b c)` 定义一个列表，以 `$list(1)`、`$list(2)` 等方式访问
**Functions**: 用 `fn name { commands }` 而不是 `name() { commands }`
**If/else**: `if(test) cmd`，以及 `if not cmd` 或 `else cmd`
**For loop**: `for(i in list) cmd`
**Quoting**: 只有单引号；要表示字面单引号需写两次：`'it''s'`

# CAVEATS

Rc 不兼容 POSIX。为 bash 或 sh 编写的脚本不经修改无法在 rc 中正确运行。

各 Unix 移植版（Rakitzis 实现和 Plan 9 from User Space）与原始 Plan 9 rc 存在细微差异，尤其是在 profile 位置和某些功能方面。

默认软件仓库中较少提供。可能需要从源码构建或安装 Plan 9 移植版。

# HISTORY

Rc 由贝尔实验室的 **Tom Duff** 于 **1989 年**为 Research Unix Version 10 创建，后来成为 Plan 9 的标准 shell。名字代表 "run commands"。Byron Rakitzis 于 **1991 年**创建了一个广受欢迎的 Unix 重实现，至今仍在维护。Duff 还以 "Duff's device"（一种 C 语言优化技巧）闻名。

# INSTALL

```dnf: sudo dnf install rc```

```nix: nix profile install nixpkgs#rc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sh](/man/sh)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [es](/man/es)(1)
