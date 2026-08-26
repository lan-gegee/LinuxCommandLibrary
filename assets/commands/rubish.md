# TAGLINE

用纯 Ruby 编写的 UNIX shell

# TLDR

**启动**交互式 Rubish 会话

```rubish```

**运行**单条命令后退出

```rubish -c '[echo hello]'```

**执行** shell 脚本文件

```rubish [script.sh]```

以受限模式**启动**，为运行不受信任的脚本禁用 Ruby 集成

```rubish -r```

将命令输出通过 Ruby 方法进行**管道处理**

```rubish -c '[ls().sort.uniq]'```

# SYNOPSIS

**rubish** [_-c command_] [_-r_] [_script_] [_arguments..._]

# DESCRIPTION

**rubish** 是一个完全用 Ruby 实现的交互式 UNIX shell。它解析大家熟悉的 bash 语法并将其编译为 Ruby 执行，因此现有脚本可以继续工作，同时完整的 Ruby 语言也能在命令行上使用。可以通过 **chsh** 将其用作登录 shell。

这个 shell 模糊了 shell 与脚本语言之间的界限。外部命令返回的对象可以用点号链接调用（例如 **ls().sort.uniq**），输出可以用 **.each** 和 **.map** 等 Ruby 迭代器逐行处理，Ruby 表达式还可以包裹在 **{ }** 中，作为 **if**、**while** 和 **until** 的条件。以大写字母开头的行会直接作为 Ruby 代码求值，函数可以用 Ruby 的 **def...end** 语法定义。

为了保持熟悉的使用体验，它还支持不少 zsh 的便利特性，包括 **setopt**、**autoload** 和缩写路径展开，此外还支持自定义动态生成的提示符，以及在后台线程中延迟加载耗时的初始化工作。

# PARAMETERS

**-c** _command_
> 将 _command_ 作为单个字符串执行后退出。

**-r**
> 受限模式：禁用 Ruby 集成特性，用于运行不受信任的脚本。

# CONFIGURATION

Rubish 使用 Ruby 而非专门的配置语言进行配置。提示符被定义为 Ruby 函数，从而实现完全动态的提示符字符串；选项可以用 zsh 风格的 **setopt** 切换；耗时的启动工作可以借助延迟加载推迟执行，使 shell 保持响应灵敏。

# CAVEATS

Rubish 要求系统中有可用的兼容 Ruby 解释器。作为一个年轻的项目，日常使用时最好将其视为实验性软件；深度的 Ruby 集成在运行不受信任的输入时会带来安全问题，这正是 **-r** 受限模式存在的原因。

# HISTORY

**rubish** 由著名的 Ruby on Rails 核心贡献者 **Atsushi Matsuda**（amatsuda）创建，是一个用纯 Ruby 编写的 shell。它以开源软件形式发布，采用 **MIT** 许可证。

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [ruby](/man/ruby)(1), [irb](/man/irb)(1)
