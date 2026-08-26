# TAGLINE

将补丁文件中描述的更改应用到原始文件

# TLDR

**应用补丁**

```patch < [patchfile.patch]```

**以指定剥离层级应用补丁**

```patch -p1 < [patchfile.patch]```

**将补丁应用到指定文件**

```patch [file] < [patchfile.patch]```

以 **dry-run 模式应用补丁**

```patch --dry-run < [patchfile.patch]```

**撤销补丁**

```patch -R < [patchfile.patch]```

为原文件**创建备份**

```patch -b < [patchfile.patch]```

使用不同前缀**应用补丁**

```patch -d [/path/to/directory] -p1 < [patchfile.patch]```

忽略错误**强制应用**

```patch -f < [patchfile.patch]```

# SYNOPSIS

**patch** [_options_] [_original_] [_patchfile_]

# DESCRIPTION

**patch** 将补丁文件中描述的更改应用到原始文件。补丁文件通常由 diff 创建，包含添加、修改或删除行的指令。

该工具读取补丁文件，并尝试将其中的每个 hunk（一段更改）应用到目标文件。如果某个 hunk 无法精确匹配，patch 会尝试寻找一个可以带模糊度（fuzz，允许部分上下文行不同）应用的位置。

patch 对软件开发、源代码更新以及管理以补丁形式分发的代码更改都至关重要。

# PARAMETERS

**-p** _num_
> 剥离路径开头 num 个组成部分。

**-R**, **--reverse**
> 撤销补丁。

**-N**, **--forward**
> 忽略已应用的补丁。

**-b**, **--backup**
> 创建备份文件。

**-d** _dir_, **--directory=** _dir_
> 先切换到指定目录。

**--dry-run**
> 不修改文件，只显示将会发生什么。

**-f**, **--force**
> 假定用户最清楚情况，不再询问。

**-i** _file_, **--input=** _file_
> 从文件读取补丁。

**-o** _file_, **--output=** _file_
> 输出到文件。

**-F** _num_, **--fuzz=** _num_
> 设置最大模糊因子。

**-l**, **--ignore-whitespace**
> 忽略空白字符变化。

**--verbose**
> 输出调试信息。

**-V** _method_, **--version-control=** _method_
> 备份版本管理方式（simple、numbered、existing）。

**-E**, **--remove-empty-files**
> 打补丁后删除空文件。

# CAVEATS

如果文件在 diff 生成之后发生了变化，补丁可能失败。模糊匹配可能导致补丁被应用到错误的位置。对不熟悉的补丁务必先用 --dry-run。撤销多个补丁时应按相反顺序进行。

# HISTORY

**patch** 由 **Larry Wall** 于 **1985 年**编写，是他对 Unix 工具的贡献之一。在版本控制系统普及之前，它是分发软件更改的重要手段。该工具在内核开发中依然重要，因为补丁是提交更改的标准方式。

# INSTALL

```apt: sudo apt install patch```

```dnf: sudo dnf install patch```

```pacman: sudo pacman -S patch```

```apk: sudo apk add patch```

```zypper: sudo zypper install patch```

```nix: nix profile install nixpkgs#patch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [git-apply](/man/git-apply)(1), [quilt](/man/quilt)(1)
