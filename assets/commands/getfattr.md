# TAGLINE

扩展属性读取工具

# TLDR

以详细格式检索文件的**所有扩展属性**

```getfattr -d [path/to/file]```

获取文件的**特定属性**

```getfattr -n user.[attribute_name] [path/to/file]```

# SYNOPSIS

**getfattr** [_options_] _file_...

# PARAMETERS

**-d**, **--dump**
> 输出所有扩展属性的名称和值

**-n**, **--name** _NAME_
> 获取特定属性的值

**-m**, **--match** _PATTERN_
> 只显示匹配正则表达式模式的属性

**-e**, **--encoding** _ENC_
> 将值编码为 text、hex 或 base64

**-R**, **--recursive**
> 递归列出属性

**-L**, **--logical**
> 跟随符号链接（默认）

**-P**, **--physical**
> 不跟随符号链接

**--only-values**
> 只打印属性的值，不打印名称

# DESCRIPTION

**getfattr** 从文件和目录中读取扩展属性（xattr）。扩展属性是与文件关联的名称:值对，独立于普通文件数据存储。

常见的命名空间包括：**user.** 用于用户自定义属性，**security.** 用于安全标签（如 SELinux），**system.** 用于系统属性（如 ACL），以及 **trusted.** 用于受信任属性（仅 root）。

扩展属性适合存储校验和、标签、来源或应用专属数据等元数据，而无需修改文件内容。

# CAVEATS

扩展属性的支持取决于文件系统（ext4、XFS、Btrfs 支持它们；FAT 不支持）。user 命名空间是非 root 用户唯一可写的命名空间。不带特殊选项复制文件时，属性可能不会被保留。

# HISTORY

21 世纪初，随着 Linux 内核 2.6 的发布，扩展属性得到广泛可用。getfattr 和 setfattr 命令是 attr 软件包的一部分，为 xattr 系统调用提供命令行访问方式。

# INSTALL

```apt: sudo apt install attr```

```dnf: sudo dnf install attr```

```pacman: sudo pacman -S attr```

```apk: sudo apk add attr```

```zypper: sudo zypper install attr```

```brew: brew install attr```

```nix: nix profile install nixpkgs#attr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setfattr](/man/setfattr)(1), [attr](/man/attr)(1), [getfacl](/man/getfacl)(1)
