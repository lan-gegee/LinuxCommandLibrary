# TAGLINE

Perl 5 语言解释器

# TLDR

**运行 Perl 脚本**

```perl [script.pl]```

**执行单行命令**

```perl -e 'print "Hello\n"'```

**原地编辑**文件并进行替换

```perl -i -pe 's/old/new/g' [file]```

**带备份地原地编辑**（原文件保存为 .bak）

```perl -i.bak -pe 's/old/new/g' [file]```

**借助自动分割打印指定列**

```perl -ane 'print "$F[0]\n"' [file]```

**检查语法**而不运行

```perl -c [script.pl]```

**逐行处理输入**（类似 sed/awk）

```perl -ne 'print if /[pattern]/' [file]```

**在命令行加载模块**

```perl -MJSON -e 'print encode_json({key => "value"})'```

# SYNOPSIS

**perl** [_options_] [_program_] [_arguments_]

# PARAMETERS

_PROGRAM_
> 要执行的 Perl 脚本文件。

**-e** _CODE_
> 把给定的代码作为单行命令执行。允许出现多个 -e 选项。

**-E** _CODE_
> 类似 -e，但会启用所有可选特性（say、state 等）。

**-n**
> 将代码包裹进 while(<>) 循环，逐行读取输入但不打印。

**-p**
> 类似 -n，但每轮迭代结束后还会打印 $_。

**-i**[_EXT_]
> 原地编辑文件。若给出扩展名，则以该后缀创建备份。

**-a**
> 开启自动分割模式（与 -n 或 -p 搭配），把每行拆分到 @F。

**-F** _PATTERN_
> 指定自动分割模式的分隔模式（默认：空白字符）。

**-l**
> 启用自动行尾处理。输入时去掉换行符，输出时补上换行符。

**-0**[_OCTAL_]
> 以八进制值指定输入记录分隔符。-0777 表示一次性读入整个文件。

**-w**
> 启用警告（脚本中更推荐 `use warnings;`）。

**-W**
> 无条件启用所有警告。

**-c**
> 仅做语法检查；不执行程序。

**-M**_MODULE_
> 在执行前加载模块（相当于 `use MODULE`）。

**-T**
> 启用用于安全目的的污染（taint）模式。不可信的数据无法影响系统。

**-S**
> 用 PATH 查找脚本。在不支持 #! 的平台上模拟该机制。

**-d**
> 在调试器下运行程序。

**-v**
> 打印版本与配置摘要。

# DESCRIPTION

**perl** 是 Perl 5 语言解释器。Perl 是一种通用编程语言，最初为文本处理而生，融合了 C、sed、awk 和 Shell 脚本的特性。

凭借强大的内置正则表达式支持，这门语言在文本处理方面尤为出色。它被广泛用于系统管理、Web 开发、网络编程和数据处理。综合 Perl 归档网络（CPAN）提供了庞大的可复用模块仓库。

# CAVEATS

现代 Perl 脚本应使用 `use strict;` 和 `use warnings;` 来编写更安全的代码。不带扩展名的 -i 选项会在没有备份的情况下原地修改文件。CPAN 模块可通过 cpan 命令安装。

# HISTORY

Perl 由 **Larry Wall** 于 **1987 年**创造，是一门实用的文本处理与报表生成语言。1994 年发布的 Perl 5 引入了引用、对象和模块等重要特性。

# INSTALL

```apt: sudo apt install perl-base```

```dnf: sudo dnf install perl-base```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl```

```zypper: sudo zypper install perl-base```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [ruby](/man/ruby)(1), [awk](/man/awk)(1), [sed](/man/sed)(1), [grep](/man/grep)(1), [cpan](/man/cpan)(1), [perldoc](/man/perldoc)(1)
