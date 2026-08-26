# TAGLINE

设置文件的扩展属性

# TLDR

在文件上设置一个**用户自定义属性**

```setfattr -n user.[attribute_name] -v "[value]" [path/to/file]```

设置一个**没有值的属性名**

```setfattr -n user.[attribute_name] [path/to/file]```

从文件中**移除**特定属性

```setfattr -x user.[attribute_name] [path/to/file]```

从转储文件中**恢复**属性

```setfattr --restore=[dumpfile]```

修改**符号链接**本身的属性（而非目标文件）

```setfattr -h -n user.[attribute_name] -v "[value]" [path/to/symlink]```

# SYNOPSIS

**setfattr** [**-h**] **-n** _name_ [**-v** _value_] _pathname_...

**setfattr** [**-h**] **-x** _name_ _pathname_...

**setfattr** [**-h**] **--restore**=_file_

# PARAMETERS

**-n, --name** _name_
> 指定要设置的扩展属性的名称

**-v, --value** _value_
> 指定扩展属性的新值。值可以是字符串、十六进制（0x 前缀）或 base64（0s 前缀）

**-x, --remove** _name_
> 完全移除指定名称的扩展属性

**-h, --no-dereference**
> 不跟随符号链接；直接操作链接本身

**--restore** _file_
> 从 getfattr --dump 创建的文件恢复扩展属性

**--raw**
> 不解码属性值

**--version**
> 打印版本并退出

**--help**
> 打印帮助信息

# DESCRIPTION

**setfattr** 设置或修改文件和目录上的扩展属性。扩展属性是与文件永久关联的名称-值对，类似于环境变量，但存储在文件系统中。属性名的格式必须为 **namespace.name**，其中 namespace 通常是 **user**、**system**、**security** 或 **trusted**。

**user** 命名空间可供普通用户存储任意数据。系统命名空间需要相应的能力或 root 权限。值可以指定为带转义序列的引号字符串、带 **0x** 前缀的十六进制，或带 **0s** 前缀的 base64。

# CAVEATS

并非所有文件系统都支持扩展属性；常见的支持文件系统包括 ext2/3/4、XFS、Btrfs 和 JFS。在某些挂载配置下 **user** 命名空间可能被禁用。属性名最大长度为 255 字节。每个文件的属性总存储空间取决于文件系统（通常为 4KB-64KB）。

# HISTORY

Linux 内核 **2.4** 加入了对扩展属性的支持，并在 **2.6** 中完全集成。**setfattr** 命令是 **attr** 软件包的一部分，该软件包最初是 SGI 的 XFS 项目的一部分开发，后来被推广用于通用 Linux 文件系统。

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

[getfattr](/man/getfattr)(1), [attr](/man/attr)(1), [setfacl](/man/setfacl)(1), [getfacl](/man/getfacl)(1)
