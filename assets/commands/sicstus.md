# TAGLINE

SICStus Prolog 开发系统

# TLDR

**启动 SICStus Prolog** 交互式解释器

```sicstus```

启动时**加载 Prolog 文件**

```sicstus -l [path/to/file.pl]```

启动时**恢复已保存的状态**

```sicstus -r [path/to/saved.sav]```

即使输入被重定向也**强制以交互模式启动**

```sicstus -i```

**不显示横幅**启动

```sicstus --nologo```

启动时**执行一个目标**

```sicstus -e "[goal]"```

向 Prolog **传递额外参数**启动

```sicstus -- [arg1] [arg2]```

# SYNOPSIS

**sicstus** [_options_] [**--**] [_prolog-arguments_]

# PARAMETERS

**-l** _file_
> 启动时加载一个 Prolog 文件。这会在加载任何初始化文件之前进行。只允许一个 **-l** 参数。

**-r** _file_
> 启动时恢复已保存的状态。

**-i**
> 强制交互模式。即使标准输入被重定向也会提示用户输入。

**-e** _goal_
> 启动时执行指定的目标。

**--nologo**
> 不显示启动横幅和版本信息。

**--iso**
> 以 ISO Prolog 模式启动。

**--sicstus**
> 以 SICStus Prolog 模式启动（默认）。

**--**
> 标志结束。其余参数作为 Prolog 参数传递。

# DESCRIPTION

**sicstus** 是 SICStus Prolog 的命令行界面。SICStus Prolog 是由瑞典计算机科学研究所（SICS）开发的商业 Prolog 开发系统。它提供用于运行 Prolog 程序的交互式解释器，同时支持 ISO Prolog 和 SICStus 特有的扩展。

启动后，解释器会显示提示符（**| ?-**），你可以在这里输入查询。每次给出答案后，按回车键终止查询；输入 **;** 再按回车则请求下一个解。可以用 **^C** 中断执行，用 **^D** 或 **halt.** 目标退出解释器。

SICStus Prolog 包含约束求解、C 与 Java 接口以及健壮应用开发等特性。运行开发系统需要有效的许可证。

# CAVEATS

SICStus Prolog 是商业软件，需要有效许可证。在执行已保存状态时，所有命令行参数都会被视为 Prolog 参数，因此 **-l** 和 **-r** 等标志不可用。**-l** 选项只接受一个文件；如需加载更多文件，请在启动后用解释器加载。

# HISTORY

**SICStus Prolog** 由 SICS（瑞典计算机科学研究所）智能系统实验室开发，该实验室现隶属于 RISE SICS。开发始于 **20 世纪 80 年代**，使其成为持续开发历史最悠久的 Prolog 系统之一。SICStus 以其健壮的约束求解能力和高效的执行而著称。系统目前仍在活跃开发 4.x 系列，在保持兼容性的同时加入现代特性。

# SEE ALSO

[swipl](/man/swipl)(1), [gprolog](/man/gprolog)(1)
