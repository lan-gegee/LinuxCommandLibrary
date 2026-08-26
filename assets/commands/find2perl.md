# TAGLINE

将 find 命令行翻译成等价的 Perl 代码

# TLDR

**将 find 命令转换为 Perl 脚本**

```find2perl [directory] -name "[*.txt]"```

**生成包含 -exec 翻译的脚本**

```find2perl [.] -type f -exec cat {} \;```

**翻译复杂的 find 表达式并保存到文件**

```find2perl [/var] -mtime +[30] -name "[*.log]" > [cleanup.pl]```

**直接运行生成的 Perl 脚本**

```find2perl [.] -name "[*.bak]" | perl```

# SYNOPSIS

**find2perl** [_paths_] [_predicates_]

# PARAMETERS

_PATHS_
> 搜索的起始目录。

_PREDICATES_
> find 风格的表达式，会被翻译为对应的 Perl 代码。

**-name** _PATTERN_
> 用 shell glob 模式匹配文件名。

**-type** _TYPE_
> 文件类型：f（普通文件）、d（目录）、l（符号链接）。

**-mtime** _N_
> 以天计的修改时间（+N 更早，-N 更新，N 表示恰好）。

**-size** _N_
> 文件大小。

**-exec** _CMD_
> 对匹配的文件执行命令。

**-print**
> 打印匹配的路径（默认动作）。

**-depth**
> 先处理目录的内容，再处理目录本身。

# DESCRIPTION

**find2perl** 利用 File::Find 模块把 find 命令表达式翻译成等价的 Perl 脚本。生成的 Perl 代码通常比原来的 find 命令跑得更快，而且可以再加工，添加 find 本身不支持的自定义处理。

该工具帮助用户在复杂的文件处理任务中从 shell 层面的 find 命令迁移到 Perl。它的输出是一个完整的 Perl 脚本，既可以直接用管道传给 perl，也可以保存下来再做修改。

# CAVEATS

并非所有 find 谓词都受支持。遇到边界情况时，生成的代码可能需要手动清理。find2perl 已在 **5.22.0 版本中从 Perl 核心移除**（2015 年），自 Perl 5.20.0 起就被标记弃用。现在可以从 CPAN 单独获取 **App::find2perl** 发行包。

# HISTORY

find2perl 曾随 **Perl** 一同附带，是用于翻译 find 命令的工具。它在 **Perl 5.22.0** 中被移出核心发行版，如今必须从 CPAN 单独安装。

# INSTALL

```apk: sudo apk add perl-app-find2perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [perl](/man/perl)(1)
