# TAGLINE

用于文件版本管理的版本控制系统（RCS）

# TLDR

**为文件初始化 RCS**（检入初始版本）

```ci [filename]```

**检出文件以供编辑**（加锁）

```co -l [filename]```

**检出只读副本**

```co [filename]```

**带日志消息检入更改**

```ci -m "[message]" [filename]```

**查看修订历史**

```rlog [filename]```

**显示**工作文件与最新修订之间的差异

```rcsdiff [filename]```

**检出特定修订**

```co -r[1.2] [filename]```

# SYNOPSIS

**rcs** [_options_] _file_...

**ci** [_options_] _file_...

**co** [_options_] _file_...

# PARAMETERS

**ci** (check-in)
> 将新修订存入 RCS 文件

**co** (check-out)
> 从 RCS 文件取出修订

**rcs**
> 更改 RCS 文件属性

**rcsdiff**
> 比较 RCS 修订

**rcsmerge**
> 合并 RCS 修订

**rlog**
> 打印修订日志消息

**-l**
> 为独占编辑锁定修订（配合 co 使用）

**-u**
> 检入后解锁（配合 ci 使用）

**-r**_rev_
> 指定修订号

**-m**_msg_
> 指定日志消息

**-q**
> 安静模式，抑制诊断输出

**-d**_date_
> 选择不晚于给定日期的最新修订（配合 co 使用）

**-w**_login_
> 选择由指定用户检入的最新修订（配合 co 使用）

**-k**_sub_
> 设置关键字替换模式（如 -kv、-kvl、-ko）

# DESCRIPTION

**RCS**（Revision Control System）管理文件的多个修订版本，为单个文件提供版本控制。它自动完成修订的存储、检索、记录和合并，适用于源代码、文档和配置文件。

工作流程围绕 **ci**（check-in，检入）和 **co**（check-out，检出）展开。检入会存储新修订，默认还会移除工作文件。检出生成某个修订；配合 **-l** 可锁定文件以便独占编辑。

RCS 使用反向增量高效存储修订——最新修订完整保存，较旧的修订则以差异形式保存。这使得检索当前版本非常快。

修订按层次编号（1.1、1.2、1.3 等）。第一个数字是发行号（release），第二个是级别号（level）。分支会增加额外的编号字段（如 1.2.1.1）。

# CAVEATS

RCS 只针对单个文件操作，不能管理目录或项目。对于多文件版本控制，Git 等现代工具更为合适。

默认的检入行为会删除工作文件。使用 **ci -u** 保留一份未锁定的副本，或 **ci -l** 保留一份已锁定的副本以继续编辑。

RCS 文件（以 **,v** 结尾）存储在同一目录或 **RCS/** 子目录中。协作使用时请确保权限设置正确。

# HISTORY

RCS 由普渡大学的 **Walter F. Tichy** 开发，于 **1982 年**首次发布。它是最早的版本控制系统之一，影响了后来的 CVS（增加了网络支持）乃至 Git。RCS 属于 GNU 项目的一部分，至今仍可在大多数类 Unix 系统上使用。

# INSTALL

```apt: sudo apt install rcs```

```dnf: sudo dnf install rcs```

```pacman: sudo pacman -S rcs```

```apk: sudo apk add rcs```

```zypper: sudo zypper install rcs```

```brew: brew install rcs```

```nix: nix profile install nixpkgs#rcs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cvs](/man/cvs)(1), [git](/man/git)(1), [svn](/man/svn)(1), [diff](/man/diff)(1)
