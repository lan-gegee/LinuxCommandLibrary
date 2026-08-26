# TAGLINE

检入 RCS 修订版本

# TLDR

**将文件检入 RCS（删除工作文件）**

```ci [path/to/file]```

**检入并保留一份只读工作副本**

```ci -u [path/to/file]```

**检入并立即检出为锁定状态以便编辑**

```ci -l [path/to/file]```

**以指定的修订号检入**

```ci -r[2.0] [path/to/file]```

**即使没有更改也强制检入**

```ci -f [path/to/file]```

**在命令行上附带日志消息检入**

```ci -m"[Log message]" [path/to/file]```

**以指定状态检入**

```ci -s[Exp] [path/to/file]```

# SYNOPSIS

**ci** [_options_] _file_...

# PARAMETERS

**-l**[_rev_]
> 检入并立即检出为锁定状态，以便继续编辑。

**-u**[_rev_]
> 检入并保留一份只读（未锁定）的工作副本。

**-r**_rev_
> 为新修订版本分配指定的修订号。

**-f**[_rev_]
> 即使文件与上一修订版本相比没有变化，也强制检入。

**-m**_msg_
> 使用 msg 作为日志消息，而不是交互式提示输入。

**-n**_name_
> 为检入的修订版本分配一个符号名。

**-N**_name_
> 与 **-n** 相同，但会覆盖该符号名的已有指派。

**-s**_state_
> 设置检入修订版本的状态（如 Exp、Stab、Rel）。

**-d**_date_
> 使用指定日期作为检入日期，而非当前时间。

**-w**_login_
> 使用 login 作为所存修订版本的作者字段。

**-k**[_rev_]
> 在工作文件中搜索 RCS 关键字值，以确定修订号、日期、作者和状态。

**-q**[_rev_]
> 安静模式；抑制诊断输出。

**-T**
> 仅当 RCS 文件的修改时间早于新修订版本的时间时，才将其设为新修订版本的时间。可保留 make 的依赖关系。

**-M**[_rev_]
> （配合 **-l** 或 **-u**）将工作文件的修改时间设为被取出修订版本的日期。

# DESCRIPTION

**ci**（check in）将工作文件的内容存入 RCS（Revision Control System）归档文件。RCS 文件保存一个文件的所有修订版本，从而实现版本跟踪和历史管理。

默认情况下，ci 在检入后会删除工作文件，只留下 RCS 归档。使用 **-u** 可保留只读副本，使用 **-l** 可保留锁定（可编辑）副本。

该命令会提示输入描述更改的日志消息。此消息随修订版本一起存储，供日后查阅。

# CAVEATS

要求调用者的登录名在 RCS 访问列表中（除非列表为空，或调用者是超级用户或文件所有者）。要向现有分支添加修订版本，分支顶端必须已被调用者锁定。

如果新修订版本与上一个相同，除非指定 **-f**，否则 ci 会回退到该版本。

# HISTORY

**RCS**（Revision Control System）由普渡大学的 Walter Tichy 开发，于 **1982** 年首次发布。它是最早的版本控制系统之一，影响了 CVS 等后来的系统。虽然已在很大程度上被 Git 等分布式系统取代，但 RCS 对于简单的单文件版本管理仍然有用。

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

[co](/man/co)(1), [rcs](/man/rcs)(1), [rcsdiff](/man/rcsdiff)(1), [rlog](/man/rlog)(1)
