# TAGLINE

Tcl 脚本语言 Shell

# TLDR

**启动交互式 Tcl Shell**

```tclsh```

**运行 Tcl 脚本**

```tclsh [script.tcl]```

**带参数运行脚本**

```tclsh [script.tcl] [arg1] [arg2]```

**在执行脚本后进入交互模式**

```tclsh -i [script.tcl]```

**指定读取脚本的编码**

```tclsh -encoding utf-8 [script.tcl]```

**直接执行 Tcl 命令**

```echo 'puts "Hello World"' | tclsh```

# SYNOPSIS

**tclsh** [_-encoding name_] [_-i_] [_-norc_] [_--_] [_filename_] [_arg ..._]

# PARAMETERS

**-encoding** _name_
> 指定读取脚本文件所用的字符编码（例如 utf-8）。

**-i**
> 即使提供了脚本文件也强制进入交互模式。

**-f**
> 强制将第一个非选项参数视为脚本文件。

**-norc**
> 不加载用户的启动文件（~/.tclshrc）。

**-t**
> 等价于 **-i**，强制进入交互模式。

**--**
> 选项结束；其后的所有参数都是脚本文件及其参数。

# DESCRIPTION

**tclsh** 是 Tcl（Tool Command Language）脚本语言的标准 Shell。它从标准输入或脚本文件读取并求值 Tcl 命令。不带参数调用时以 **%** 提示符交互式运行。

脚本中可以使用若干预设变量：**argc** 是参数个数，**argv** 是参数列表，**argv0** 是脚本名，**tcl_interactive** 表示 Shell 是否处于交互模式。

在交互模式下，Shell 在接受命令之前会先读取 **~/.tclshrc** 启动文件。提示符可以通过 **tcl_prompt1** 和 **tcl_prompt2** 变量自定义。

# CAVEATS

Tcl 的语法与大多数 Unix Shell 不同。花括号 **{}** 用于分组，方括号 **[]** 用于命令替换，**$** 用于变量展开。字符串引号和列表处理遵循 Tcl 的约定而非 POSIX Shell 约定。

# HISTORY

Tcl 由 **John Ousterhout** 于 **1988 年**在加州大学伯克利分校创建，是一种可嵌入的脚本语言。名字是 "Tool Command Language" 的缩写。随着 Tk GUI 工具包的流行，Tcl 也广受欢迎。20 世纪 90 年代开发工作转移到 Sun Microsystems 继续，现由 Tcl Core Team 维护。当前主版本为 Tcl 8.6，Tcl 9.0 正在开发中。

# INSTALL

```dnf: sudo dnf install tcl```

```pacman: sudo pacman -S tcl```

```zypper: sudo zypper install tcl```

```nix: nix profile install nixpkgs#tcl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wish](/man/wish)(1), [expect](/man/expect)(1), [bash](/man/bash)(1), [python](/man/python)(1)
