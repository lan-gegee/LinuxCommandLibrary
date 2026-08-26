# TAGLINE

解析 roff 文档中的文件包含

# TLDR

**处理文件**并用被包含文件的内容替换 .so 请求

```soelim [path/to/file]```

**使用额外的包含目录处理**

```soelim -I [path/to/includes] [path/to/file]```

**处理时不输出 .lf 请求**

```soelim -r [path/to/file]```

**为 TeX 处理输出**（带 TeX 风格注释）

```soelim -t [path/to/file]```

**处理多个文件**

```soelim [file1] [file2] [file3]```

# SYNOPSIS

**soelim** [**-Crtv**] [**-I** _dir_] [_file_...]

# PARAMETERS

**-C**
> 即使 .so 请求后面跟的不是空格或换行符也能识别。

**-I** _dir_
> 将目录添加到被包含文件的搜索路径。可以多次指定。

**-r**
> 不输出 **.lf** 行号请求。对非 groff 文件很有用。

**-t**
> 用 TeX 风格的注释行（**%**）代替 **.lf** 请求来跟踪文件和行号。

**-v**, **--version**
> 打印版本号并退出。

**--help**
> 显示用法信息并退出。

# DESCRIPTION

**soelim** 是 groff 文档排版系统的预处理器。它处理 roff 输入文件，将 **.so**（source）请求替换为所引用文件的实际内容，递归地将文档包含树展平。

roff 文档中的 **.so** 请求用于包含其他文件，类似于 C 语言中的 **#include**。不过，这些包含通常由 troff（排版器）而非预处理器处理。soelim 让被包含的文件可以在排版之前先经过预处理，当被包含文件含有预处理指令时这是必需的。

当 groff 使用 **-s** 选项时，通常会自动调用 soelim。未指定文件时它从标准输入读取。

# CAVEATS

点号与"so"之间必须没有空白字符，soelim 才能识别该请求。如果存在空白，则只有 groff/troff 会处理该请求，soelim 会忽略它。除非指定了 **-I** 路径，否则被包含文件的路径相对于当前目录。

如果同时给出 **-r** 和 **-t**，则后指定的那个决定行为。

# HISTORY

**soelim** 是 GNU **groff**（GNU troff）软件包的一部分，groff 是传统 Unix 文档排版系统 troff 的 GNU 实现。groff 系统自 20 世纪 80 年代末开始开发，作为专有 Unix troff 的自由软件替代品。soelim 提供了与传统 troff 预处理工作流的兼容性。

# INSTALL

```apt: sudo apt install groff-base```

```dnf: sudo dnf install groff-base```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [troff](/man/troff)(1), [nroff](/man/nroff)(1), [eqn](/man/eqn)(1), [tbl](/man/tbl)(1), [refer](/man/refer)(1), [man](/man/man)(1)
