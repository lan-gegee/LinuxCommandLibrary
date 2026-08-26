# TAGLINE

标记变量供子进程使用的 Shell 内建命令

# TLDR

一步完成变量**赋值**并导出

```export [VARIABLE]=[value]```

**导出**已存在的 shell 变量

```export [VARIABLE]```

向 PATH **追加**一个目录

```export PATH="$PATH:[/path/to/append]"```

**移除**导出属性，变量保留在当前 shell 中

```export -n [VARIABLE]```

向子进程**导出** shell 函数（bash）

```export -f [function_name]```

以可重新读取的形式**打印**所有已导出的变量

```export -p```

一次**导出**多个变量

```export [EDITOR]=[vim] [PAGER]=[less]```

# SYNOPSIS

**export** _name_[=_value_] ...

**export** **-p**

**export** [**-fn**] _name_[=_value_] ...

# DESCRIPTION

**export** 标记 shell 变量，使其进入随后执行的命令的环境。被导出的变量成为每个子进程都会继承的环境变量；而未用 **export** 设置的变量只在当前 shell 内部可见。

这就是配置传递给你所运行程序的方式：**PATH** 告诉 shell 到哪里查找可执行文件，**EDITOR** 告诉工具打开哪个编辑器，而 **JAVA_HOME** 等应用专用变量则由需要它们的进程读取。赋值和导出可以合并在一条语句中（**export FOO=bar**），也可以拆成两条语句（先 **FOO=bar** 再 **export FOO**），后者对非常老的 shell 来说是更可移植的写法。

导出属性属于变量本身而不属于它的值：一旦某个名称被导出，之后对它的赋值也会自动导出，无需重复 **export**。**export -n** 移除该属性，同时让变量继续保留在当前 shell 中——这与删除变量不同；删除要用 **unset**。

不带操作数或带 **-p** 时，**export** 会以可作为 shell 输入重新读取的格式输出所有已导出变量的名称和值。

# PARAMETERS

**-p**
> 以可复用为 shell 输入的形式打印所有已导出的变量。

**-n**
> 移除每个 _name_ 的导出属性。变量仍设置在当前 shell 中，但不再传给子进程。非 POSIX 标准，是 bash、ksh 和 zsh 的扩展。

**-f**
> 将每个 _name_ 视为 shell 函数而非变量。bash 特有，可移植性差。

**--**
> 选项结束；其余内容一律视为名称，即使以连字符开头。

# CAVEATS

**export** 只影响当前 shell 以及它随后启动的进程。它无法改变父 shell 或已在运行的进程的环境，因此如果你希望脚本中的导出在你当前的会话中生效，必须 source 该脚本（**. script.sh**）而不是直接执行。

**export -n** 并不会取消变量的定义。值仍然对当前 shell 以及任何直接使用它的对象可见；停止的只是继承。要彻底移除请使用 **unset** _name_。

导出的函数（**export -f**）通过经过特殊编码的环境变量传给子进程，且仅在子进程同样是 bash 时才有效。这一机制正是 2014 年 **Shellshock** 漏洞的攻击载体，其编码方式也随修复一同更改了。

POSIX 只规定了 **-p**。**-f** 和 **-n** 是扩展功能，因此面向 **/bin/sh** 编写的脚本应避免使用它们。

# HISTORY

**export** 可追溯到 **1970 年代**末期的 **Bourne shell**，并由 POSIX 标准化。它在所有主流 shell 中都实现为内建命令，因为外部程序无法修改 shell 自身的环境。某些系统还提供一个用于符合标准的 **/usr/bin/export** 存根，但它没有任何实际作用。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unset](/man/unset)(1), [env](/man/env)(1), [printenv](/man/printenv)(1), [set](/man/set)(1), [declare](/man/declare)(1), [readonly](/man/readonly)(1), [typeset](/man/typeset)(1), [bash](/man/bash)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/bash.html#index-export)```

<!-- verified: 2026-07-16 -->
