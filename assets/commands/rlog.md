# TAGLINE

显示 RCS 文件的修订历史

# TLDR

**显示文件历史**

```rlog [file.c]```

**显示指定修订版本**

```rlog -r[1.5] [file.c]```

**显示修订版本范围**

```rlog -r[1.1:1.5] [file.c]```

**按日期显示**

```rlog -d"[>2024-01-01]" [file.c]```

**只显示头部信息**

```rlog -h [file.c]```

**按状态显示**

```rlog -s[Exp] [file.c]```

**按作者显示**

```rlog -w[username] [file.c]```

# SYNOPSIS

**rlog** [_-r revisions_] [_-d dates_] [_-h_] [_options_] _files_

# PARAMETERS

**-r** _REV_
> 指定修订版本。

**-d** _DATE_
> 按日期筛选。

**-h**
> 只显示头部信息。

**-t**
> 显示头部和描述。

**-s** _STATE_
> 按状态筛选。

**-w** _AUTHOR_
> 按作者筛选。

**-b**
> 仅默认分支。

**-R**
> 只打印 RCS 文件名。

**-N**
> 不打印符号名称。

**-L**
> 忽略未设置锁的 RCS 文件。

**-l**
> 仅已加锁的修订版本。

**-V**
> 打印 RCS 版本号。

**-z** _zone_
> 指定日期输出格式和默认时区。

# DESCRIPTION

**rlog** 打印 RCS 文件的信息。不带选项时，rlog 会打印完整日志：先是头部信息（RCS 文件名、工作文件、头修订版本、默认分支、访问列表、锁、符号名称、注释引导符、修订版本总数），然后是每个修订版本的条目（编号、日期、作者、状态、增加/删除的行数以及日志消息）。

选项 **-d**、**-l**、**-s** 和 **-w** 按交集选择修订版本，而 **-b** 和 **-r** 按并集选择。只有满足所有指定条件的修订版本才会被打印。

# CAVEATS

RCS 已在很大程度上被 Git 取代。只支持文件级版本控制。在现代开发中已不常见。

# HISTORY

**rlog** 是 **RCS**（Revision Control System）的一部分，由 **Walter Tichy** 于 **20 世纪 80 年代**在普渡大学创建。RCS 是最早的版本控制系统之一。

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

[rcs](/man/rcs)(1), [ci](/man/ci)(1), [co](/man/co)(1), [rcsdiff](/man/rcsdiff)(1), [git](/man/git)(1)
