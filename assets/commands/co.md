# TAGLINE

RCS 版本检出

# TLDR

检出文件的**最新版本**（只读）

```co [file.txt]```

**检出文件以进行编辑**（加锁）

```co -l [file.txt]```

**检出特定版本**

```co -r[1.2] [file.txt]```

**检出并解锁**文件

```co -u [file.txt]```

**按日期检出某个版本**

```co -d"[2024-01-15]" [file.txt]```

**安静地检出**，不打印诊断信息

```co -q [file.txt]```

**强制检出**，即使工作文件已存在

```co -f [file.txt]```

# SYNOPSIS

**co** [_options_] _file_...

# PARAMETERS

**-l**
> 锁定检出的版本，防止他人编辑。

**-u**
> 解锁版本；不加锁检出。

**-r**_REV_
> 检出指定版本 REV。

**-d**_DATE_
> 检出 DATE 当天或之前最新的版本。

**-f**
> 若工作文件已存在则强制覆盖。

**-q**
> 安静模式；抑制诊断输出。

**-p**
> 将版本内容打印到 stdout，而不是创建工作文件。

**-j**_JOINLIST_
> 通过合并版本之间的差异来生成新版本。

**-k**_SUBST_
> 设置关键字替换模式（kv、kvl、k、o、b、v）。

**-s**_STATE_
> 检出具有给定状态的最新版本。

**-w**_LOGIN_
> 检出由 LOGIN 提交的最新版本。

**-T**
> 将工作文件的修改时间设为版本的提交时间。

**-V**
> 打印 RCS 版本号。

# DESCRIPTION

**co** 是 RCS（Revision Control System，一种用于管理文件版本的早期版本控制系统）的检出命令。它从 RCS 文件中取出修订版本，放入工作目录供查看或编辑。

默认情况下，co 以只读模式检索最新版本。**-l** 标志会锁定该版本以便独占编辑，防止他人检出同一版本进行修改。编辑完成后，再用 **ci** 将文件检入回去。

RCS 将版本历史存储在特殊文件中（通常以 **,v** 结尾），co 基于这种基于增量的存储重建工作文件。虽然它在很大程度上已被分布式版本控制系统取代，但对简单的单文件版本管理仍然有用。

# CAVEATS

RCS 操作单个文件而非仓库。锁只是建议性的，依赖用户自觉配合。默认情况下，工作文件的时间戳会被设为版本的提交时间。若文件已被锁定，检出时需要锁的持有者先释放，或使用 **rcs -u** 强制解除锁定。

# HISTORY

RCS 由 Purdue University 的 Walter Tichy 创建，于 **1982 年**首次发布。它开创了版本控制中增量存储的概念。虽然 CVS 及后来的系统都建立在 RCS 的概念之上，但独立的 co/ci 工作流程在大多数类 Unix 系统上依然可用。

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

[ci](/man/ci)(1), [rcs](/man/rcs)(1), [rlog](/man/rlog)(1), [rcsdiff](/man/rcsdiff)(1), [git](/man/git)(1)
