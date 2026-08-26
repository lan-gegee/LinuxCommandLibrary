# TAGLINE

显示 Perl 文档

# TLDR

**查看模块文档**

```perldoc [Module::Name]```

**查询内置函数**

```perldoc -f [function_name]```

**在 FAQ 中搜索关键词**

```perldoc -q "[keyword]"```

**查询内置变量**

```perldoc -v '[variable]'```

**查看模块的源代码**

```perldoc -m [Module::Name]```

**以纯文本显示文档**（无格式）

```perldoc -t [Module::Name]```

**查看 Perl 教程**

```perldoc perlintro```

# SYNOPSIS

**perldoc** [_options_] [_PageName_|_ModuleName_|_ProgramName_|_URL_]

# PARAMETERS

_TOPIC_
> 要显示的模块名、程序名或文档页。

**-f** _FUNCTION_
> 按名称查询 Perl 内置函数。

**-q** _QUERY_
> 在 Perl 常见问题集（perlfaq）中搜索匹配某正则表达式的条目。

**-v** _VARIABLE_
> 查询 Perl 内置变量（例如 -v '$!'）。

**-m** _MODULE_
> 显示模块的源代码而不是它的文档。

**-t**
> 纯文本输出（不做 man page 格式化）。

**-T**
> 不经过分页器，直接把输出发送到 STDOUT。

**-l**
> 显示模块的文件路径而不是它的文档。

**-U**
> 以不安全模式运行，允许以 root 身份执行 perldoc。

# DESCRIPTION

**perldoc** 是标准的 Perl 文档查看器。它负责查找并显示嵌入在 Perl 模块、脚本和核心文档页中、以 POD（Plain Old Documentation）格式编写的文档。以模块名调用时，它会搜索 **@INC** 路径找到该模块并渲染其 POD。不带参数调用时则显示自身的用法。

常见的文档页包括 **perlintro**（教程）、**perlfunc**（内置函数）、**perlvar**（特殊变量）、**perlre**（正则表达式）和 **perlop**（运算符）。

# CAVEATS

只有已安装的模块才有文档可用。显示时使用系统分页器（通常是 **less** 或 **more**）。使用 **-v** 时必须给变量加引号，以免被 Shell 展开。

# HISTORY

**perldoc** 自 **Perl 5.004**（1997 年）起就是 Perl 核心发行版的一部分。它让手动查找和排版 POD 文档成为历史。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perl](/man/perl)(1), [pod2man](/man/pod2man)(1), [pod2html](/man/pod2html)(1)
