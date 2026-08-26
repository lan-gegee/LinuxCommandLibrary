# TAGLINE

安全地创建临时文件或目录并输出其名称

# TLDR

创建空的**临时文件**并输出其路径

```mktemp```

在**自定义目录**中创建临时文件

```mktemp -p [/path/to/directory]```

使用**自定义模板**（X 会被替换为随机字符）

```mktemp [/tmp/example.XXXXXXXX]```

创建带**指定后缀**的临时文件

```mktemp --suffix [.txt]```

创建空的**临时目录**

```mktemp -d```

**试运行**：只打印名称而不实际创建

```mktemp -u```

# SYNOPSIS

**mktemp** [**-d**] [**-u**] [**-q**] [**-p** _dir_] [**--suffix** _suff_] [_template_]

# PARAMETERS

**-d**, **--directory**
> 创建目录而不是文件。

**-u**, **--dry-run**
> 只打印名称而不实际创建（不安全；见 CAVEATS）。

**-q**, **--quiet**
> 创建失败时抑制错误消息。

**-p** _dir_, **--tmpdir**[=_dir_]
> 相对于指定目录创建临时文件；默认为 $TMPDIR 或 /tmp。

**-t**
> 将模板解释为相对于临时目录的文件名（已弃用）。

**--suffix** _suff_
> 在模板后追加后缀；后缀不能包含斜杠。

# DESCRIPTION

**mktemp** 安全地创建临时文件或目录并输出其路径。模板的最后一段必须包含至少 3 个连续的 X 字符，它们会被替换为随机的字母数字字符以确保唯一性。

未提供模板时，mktemp 默认在系统临时目录中使用 tmp.XXXXXXXXXX。文件以 u+rw 权限创建，目录以 u+rwx 权限创建，两者均受 umask 影响。

这种安全的创建方式可避免竞态条件——即在检查存在性与创建之间另一进程抢先创建了同名文件。这对编写安全的脚本至关重要。

# CAVEATS

-u（试运行）选项不适合生产脚本，因为在打印名称与实际使用之间其他进程可能抢先创建该文件。请始终让 mktemp 直接创建文件。临时文件会一直存在直到被显式删除；在脚本中可用 trap 进行清理。

# HISTORY

**mktemp** 起源于 **OpenBSD**，后来被其他系统采用。GNU 版本属于 **coreutils**。该命令为 mkstemp(3) 和 mkdtemp(3) 库函数提供了安全接口。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [trap](/man/trap)(1)
