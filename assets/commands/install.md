# TAGLINE

复制文件的同时设置权限和所有者

# TLDR

**以指定权限复制文件**

```install -m [755] [source] [dest]```

**将文件复制到目标目录**

```install -t [/usr/local/bin/] [file1] [file2]```

**创建目录（含父目录）**

```install -d [/path/to/dir]```

**设置所有者和组**

```install -o [user] -g [group] [file] [dest]```

**复制时保留时间戳**

```install -p [file] [dest]```

**安装时剥离二进制文件**

```install -s [binary] [/usr/local/bin/]```

**仅当源文件不同才复制**（避免不必要的写入）

```install -C [file] [dest]```

**先创建父目录再复制**

```install -D [source] [/path/to/new/dir/dest]```

# SYNOPSIS

**install** [_options_] [**-s**] [**--strip-program**=_PROGRAM_] _source_... _dest_

**install** [_options_] -t _DIRECTORY_ _source_...

**install** [_options_] -d _directories_...

# DESCRIPTION

**install** 在复制文件的同时设置权限和所有者。它主要用于 Makefile 和安装脚本中，以正确的属性放置文件。

该工具集 cp、chmod、chown 和 mkdir 功能于一体，简化安装任务。它还能剥离二进制文件并备份已有文件。默认权限模式为 **rwxr-xr-x**（755）。

# PARAMETERS

**-m** _mode_, **--mode**=_mode_
> 设置权限模式（同 chmod），替代默认的 rwxr-xr-x。

**-o** _owner_, **--owner**=_owner_
> 设置所有者（仅超级用户）。

**-g** _group_, **--group**=_group_
> 设置组所有权，替代进程的当前组。

**-d**, **--directory**
> 将所有参数视为目录名；创建指定目录的所有组成部分。

**-D**
> 创建 dest 的全部父目录组件，然后把 source 复制为 dest。

**-t** _DIRECTORY_, **--target-directory**=_DIRECTORY_
> 将所有 source 参数复制到 DIRECTORY 中。

**-T**, **--no-target-directory**
> 将 dest 视为普通文件而非目录。

**-C**, **--compare**
> 比较 source 与目标；若内容、所有权和权限均未变化则不修改目标。

**-s**, **--strip**
> 从安装的二进制文件中剥离符号表。

**--strip-program**=_PROGRAM_
> 用于剥离二进制文件的程序（默认：strip）。

**-p**, **--preserve-timestamps**
> 将源文件的访问/修改时间应用到目标文件。

**-b**
> 为每个已存在的目标文件创建备份。

**--backup**[=_CONTROL_]
> 为每个已存在的目标文件创建备份，可选版本控制方式。

**-S** _suffix_, **--suffix**=_suffix_
> 覆盖常用的备份后缀。

**-v**, **--verbose**
> 打印每个被创建的文件或目录的名称。

**-c**
> 被忽略；仅为兼容旧版 Unix。

**-Z**, **--context**
> 将目标文件的 SELinux 安全上下文设为默认类型。

# CAVEATS

不适用于一般性文件复制。默认权限模式是 755（rwxr-xr-x），与 cp 会保留源文件权限不同。更改所有权需要相应权限。

# HISTORY

**install** 是传统 Unix 工具，在 Linux 上属于 **GNU coreutils**。自早期 Unix 起，它就被用于 Makefile 以实现标准化的软件安装流程。

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

[cp](/man/cp)(1), [chmod](/man/chmod)(1), [chown](/man/chown)(1), [mkdir](/man/mkdir)(1), [make](/man/make)(1)
