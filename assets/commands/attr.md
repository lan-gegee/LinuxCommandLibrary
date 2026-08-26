# TAGLINE

操作文件系统对象上的扩展属性

# TLDR

**在文件上设置扩展属性**

```attr -s [attribute_name] -V [value] [path/to/file]```

**获取扩展属性的值**

```attr -g [attribute_name] [path/to/file]```

**移除扩展属性**

```attr -r [attribute_name] [path/to/file]```

**列出文件上的所有扩展属性**

```attr -l [path/to/file]```

**在 user 命名空间设置属性**

```setfattr -n user.[attribute_name] -v [value] [path/to/file]```

**用 getfattr 获取所有属性**

```getfattr -d [path/to/file]```

# SYNOPSIS

**attr** [**-LRSq**] **-s** _attrname_ [**-V** _attrvalue_] _pathname_

**attr** [**-LRSq**] **-g** _attrname_ _pathname_

**attr** [**-LRSq**] **-r** _attrname_ _pathname_

**attr** [**-LRSq**] **-l** _pathname_

# PARAMETERS

**-s** _attrname_
> 将指定属性设置为从 stdin 读取的值。若该属性已存在，其值会被替换。配合 **-V** 可改为在命令行上直接提供值。

**-g** _attrname_
> 获取与指定属性关联的值并打印到 stdout。

**-r** _attrname_
> 移除指定属性（若存在）。

**-l**
> 列出对象上所有属性的名称及每个值的字节数。

**-V** _attrvalue_
> 直接为 **-s** 操作提供值，从而不从 stdin 读取。

**-L**
> 当对象是符号链接时，对链接的目标而非链接本身进行操作。

**-R**
> 在根（trusted）属性命名空间而非默认的 user 命名空间中操作。需要特权。

**-S**
> 在 security 属性命名空间中操作。

**-q**
> 安静模式；错误消息输出到 stderr，同时抑制 stdout 上的状态消息。

# DESCRIPTION

**attr** 用于操作文件系统对象上的扩展属性。扩展属性是与文件和目录永久关联的名值对，可提供传统 Unix 权限之外的元数据存储。

属性存在于不同的命名空间中：**user** 存放任意用户数据，**system** 存放 ACL 等操作系统特性，**security** 存放 SELinux 标签，**trusted** 面向特权应用。attr 命令主要作用于 user 命名空间。

只要工具支持，扩展属性就能在复制和备份操作中保留下来。常见用途包括存储文件元数据、校验和、capabilities 以及应用专属数据，而无需修改文件内容。

相关命令 **getfattr** 和 **setfattr** 提供更细致的控制，脚本场景下更推荐使用它们。

# CAVEATS

并非所有文件系统都支持扩展属性；ext4、XFS 和 Btrfs 在启用 user_xattr 挂载选项时支持。属性大小限制因文件系统而异（通常为 64KB）。许多备份和文件传输工具默认不保留扩展属性。user 命名空间仅限对该文件有读写权限的进程使用。

# HISTORY

扩展属性受 IRIX 等其他 Unix 系统类似特性的启发，于内核 **2.6**（2003 年）加入 Linux。其实现遵循 POSIX 1003.1e 扩展安全属性草案标准。提供这些工具的 **attr** 软件包自扩展属性引入以来一直是管理它们的标准接口。

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

[getfattr](/man/getfattr)(1), [setfattr](/man/setfattr)(1), [getfacl](/man/getfacl)(1), [setfacl](/man/setfacl)(1), [lsattr](/man/lsattr)(1), [chattr](/man/chattr)(1)

# RESOURCES

```[Source code](https://git.savannah.nongnu.org/git/attr.git)```

```[Homepage](https://savannah.nongnu.org/projects/attr)```

<!-- verified: 2026-06-17 -->
