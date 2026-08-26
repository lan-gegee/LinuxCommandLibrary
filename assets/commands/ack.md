# TAGLINE

面向程序员的类 grep 源代码搜索工具

# TLDR

在当前目录中递归**搜索**模式

```ack [pattern]```

在**特定文件类型**中搜索模式

```ack --type=[perl|python|ruby|js] [pattern]```

进行**忽略大小写**的搜索

```ack -i [pattern]```

只**列出匹配的文件**而不显示匹配内容

```ack -l [pattern]```

显示匹配行周围的**上下文行**

```ack -C [3] [pattern]```

# SYNOPSIS

**ack** [_options_] _pattern_ [_file_|_directory_...]

# DESCRIPTION

**ack** 是一款代码搜索工具，定位为 grep 的替代品，专为程序员优化。它在源代码中递归搜索时，会自动跳过备份文件、版本控制目录（.git、.svn）和二进制文件。

该工具内置文件类型过滤功能，可将搜索限定为特定编程语言。输出带有彩色高亮和按文件分组，便于阅读。它使用 Perl 正则表达式，提供强大的模式匹配能力。

# PARAMETERS

**-i**, **--ignore-case**
> 忽略大小写搜索

**-v**, **--invert-match**
> 反转匹配；选择不匹配的行

**-w**, **--word-regexp**
> 仅匹配完整单词

**-l**, **--files-with-matches**
> 只打印包含匹配项的文件名

**-L**, **--files-without-matches**
> 打印不包含匹配项的文件名

**-c**, **--count**
> 打印每个文件中匹配行的数量

**-C** _num_, **--context=**_num_
> 打印匹配处前后各 num 行上下文

**-A** _num_, **--after-context=**_num_
> 打印每个匹配之后的 num 行

**-B** _num_, **--before-context=**_num_
> 打印每个匹配之前的 num 行

**--type=**_TYPE_
> 只搜索 TYPE 类型的文件（perl、python、ruby、js 等）

**--nocolor**
> 禁用彩色输出

**-f**
> 打印将被搜索的文件（试运行）

**--ignore-dir=**_name_
> 忽略指定目录名

**--help-types**
> 列出所有可识别的文件类型

# CONFIGURATION

**~/.ackrc**
> 用户级配置文件，用于设置默认选项。每行包含一个命令行选项（如 --type-add=xml:ext:xsl）。在命令行参数之前加载。

**/etc/ackrc**
> 系统级配置文件，在 ~/.ackrc 之前加载。

**.ackrc**
> 当前目录下的项目级配置文件。对该项目覆盖系统和用户设置。

# CAVEATS

在大型代码库上，**ack** 比 **ripgrep** 或 **ag**（The Silver Searcher）等较新的工具慢。它需要已安装 Perl。部分文件类型默认无法识别，需要在 .ackrc 中自定义配置。

# HISTORY

**ack** 由 Andy Lester 创建，首次发布于 **2005** 年。它的设计目标是成为更适合程序员使用的 grep，解决在代码库中搜索时的常见痛点。该工具影响了后来的 **ag** 和 **ripgrep** 等搜索工具。

# INSTALL

```dnf: sudo dnf install ack```

```aur: yay -S ack```

```apk: sudo apk add ack```

```zypper: sudo zypper install ack```

```brew: brew install ack```

```nix: nix profile install nixpkgs#ack```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[grep](/man/grep)(1), [ag](/man/ag)(1), [rg](/man/rg)(1), [git-grep](/man/git-grep)(1)

# RESOURCES

```[Source code](https://github.com/beyondgrep/ack3)```

```[Homepage](https://beyondgrep.com/)```

<!-- verified: 2026-06-10 -->
