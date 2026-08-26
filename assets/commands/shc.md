# TAGLINE

将 shell 脚本编译为二进制可执行文件

# TLDR

**编译 shell 脚本**

```shc -f [script.sh]```

**设置过期日期**

```shc -e [31/12/2026] -f [script.sh]```

**设置过期提示消息**

```shc -m "[Script expired]" -f [script.sh]```

**自定义输出名称**

```shc -o [binary] -f [script.sh]```

**宽松安全模式**

```shc -r -f [script.sh]```

**强化且不可追踪的**二进制文件

```shc -U -H -f [script.sh]```

**详细输出**

```shc -v -f [script.sh]```

# SYNOPSIS

**shc** [**-f** _script_] [**-o** _output_] [**-e** _date_] [**-m** _message_] [**-r**] [**-U**] [**-H**] [**-v**]

# PARAMETERS

**-f** _SCRIPT_
> 要编译的输入 shell 脚本

**-o** _FILE_
> 输出二进制文件名

**-e** _DATE_
> 过期日期，格式为 dd/mm/yyyy

**-m** _MESSAGE_
> 过期时显示的消息（默认："Please contact your provider"）

**-r**
> 宽松安全模式，允许二进制文件在不同系统间再分发

**-v**
> 输出详细的编译信息

**-U**
> 使二进制不可追踪（阻止 truss、strace、ltrace 等）

**-H**
> 强化：针对转储、代码注入和 ptrace 的额外保护

**-S**
> 为 root 可调用的程序启用 setuid

**-B**
> 针对 BusyBox 编译

**-D**
> 启用 exec 调用调试

**-i** _inline_option_
> 传给 Shell 解释器的内联选项

**-x** _command_
> exec 命令，作为 printf 格式串

# DESCRIPTION

**shc** 通过加密脚本内容并将其包装在自动生成的 C 代码中，把 shell 脚本转换为编译后的二进制可执行文件。生成的 C 源码由系统的 C 编译器编译，产出一个独立二进制，在运行时解密并执行原始脚本。

该工具提供的是基本的源码混淆而非真正的安全保护，因为只要投入足够的精力，脚本仍可从二进制中恢复。可选功能包括过期日期——使二进制在指定日期之后拒绝运行；以及严格模式——将二进制绑定到当前主机以防止再分发。宽松模式（**-r**）则允许二进制在不同系统上运行。

除二进制外还会生成一个包含 C 源码的中间 **.x.c** 文件，可以查看、修改或用不同选项手动编译。

# CAVEATS

并非真正的编译——脚本可以被还原。其安全性是混淆而非加密。需要 C 编译器。

# HISTORY

**shc**（Shell Compiler）由 **Francisco Javier Rosales Garcia** 创建。它用于对 shell 脚本进行基本保护和分发。

# INSTALL

```dnf: sudo dnf install shc```

```brew: brew install shc```

```nix: nix profile install nixpkgs#shc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [gcc](/man/gcc)(1)
