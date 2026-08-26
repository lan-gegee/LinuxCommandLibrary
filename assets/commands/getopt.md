# TAGLINE

shell 脚本的命令行选项解析器

# TLDR

解析带简写形式的可选 **verbose/version 标志**

```getopt -o vV -l verbose,version -- --version --verbose```

添加带必需参数的 **--file 选项**

```getopt -o f: -l file: -- --file=somefile```

添加带可选参数的 **--verbose 选项**并传入一个非选项参数

```getopt -o v:: -l verbose:: -- --verbose arg```

解析参数要求各不相同的**多个选项**

```getopt -o rv::t: -l verbose,source::,target: -- -v --target target```

# SYNOPSIS

**getopt** [_options_] [**--**] _parameters_

# PARAMETERS

**-o**, **--options** _SHORT_
> 要识别的短选项（单个字母）。字母后跟冒号表示需要参数，双冒号表示参数可选。

**-l**, **--longoptions** _LONG_
> 要识别的长选项（逗号分隔）。冒号规则与短选项相同。

**-n**, **--name** _NAME_
> 错误消息中使用的名称

**-q**, **--quiet**
> 抑制错误消息

**-a**, **--alternative**
> 允许使用单横线形式的长选项

**-T**, **--test**
> 测试是否为增强版 getopt

# DESCRIPTION

**getopt** 为 shell 脚本解析命令行选项，同时处理短选项（-v）和长选项（--verbose）格式。它会规范化选项顺序、处理合并的短选项（-abc），并将选项与参数分离。

增强版 getopt（util-linux 版本）支持长选项、可选参数以及对含空格参数的正确处理。使用 **getopt -T** 可测试增强版是否可用。

输出通常配合 **eval set --** 使用，以便用规范化后的选项更新脚本的位置参数。

# OPTION ARGUMENT SYNTAX

在选项字符串中：
- **f** - 不带参数的标志
- **f:** - 带必需参数的选项
- **f::** - 带可选参数的选项

# CAVEATS

原始 BSD getopt 功能有限，不支持长选项。请始终用 **-T** 测试增强版 getopt 是否可用。可选参数必须直接附着在选项上（--opt=arg，而非 --opt arg）。

# HISTORY

getopt 的历史可追溯到早期 Unix 系统。util-linux 中的增强版本是为了克服原版的局限而开发的，增加了长选项支持，并对包含特殊字符的参数提供正确的引号处理。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getopts](/man/getopts)(1), [bash](/man/bash)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://www.man7.org/linux/man-pages/man1/getopt.1.html)```

<!-- verified: 2026-07-15 -->
