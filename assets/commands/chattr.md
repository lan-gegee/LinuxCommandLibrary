# TAGLINE

在 Linux 文件系统上更改文件属性

# TLDR

设置**不可变**属性

```sudo chattr +i path/to/file```

移除**不可变**属性

```sudo chattr -i path/to/file```

**递归**设置不可变属性

```sudo chattr -R +i path/to/dir```

**大小写折叠**目录

```chattr +F path/to/dir```

**仅追加**模式

```sudo chattr +a path/to/file```

# SYNOPSIS

**chattr** [_OPTIONS_] [_mode_] _files_...

# DESCRIPTION

**chattr** 更改 Linux 文件系统上的文件属性。这些扩展属性提供了标准权限之外的安全与管理控制，例如将文件设为不可变或仅追加。

不可变属性 (+i) 对于保护关键系统文件尤其有用，因为在移除该属性之前，即使是 root 也无法修改、删除或重命名不可变文件。仅追加属性 (+a) 常用于日志文件，既能防止篡改，又允许写入新条目。

# PARAMETERS

**+attribute**
> 为文件添加属性

**-attribute**
> 从文件移除属性

**=attribute**
> 仅设置指定的属性

**-R**
> 递归地更改属性

**i**
> 不可变 - 无法修改、删除或重命名

**a**
> 仅追加 - 只能追加内容

**s**
> 安全删除 - 被覆盖的数据块以零填充

**S**
> 同步更新

**A**
> 不更新访问时间

**c**
> 压缩

**e**
> 区段格式（ext4 上的默认格式）

**F**
> 大小写折叠目录（不区分大小写）

# CAVEATS

需要相应的 capabilities 或 root 权限。在移除属性之前，即使是 root 也无法更改不可变文件。并非所有文件系统都支持全部属性。

# HISTORY

**chattr** 是 **e2fsprogs** 的一部分，为 ext2/ext3/ext4 及其他 Linux 文件系统提供扩展属性管理。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs-extra```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsattr](/man/lsattr)(1), [chmod](/man/chmod)(1)

# RESOURCES

```[Source code](https://github.com/tytso/e2fsprogs)```

```[Documentation](https://man7.org/linux/man-pages/man1/chattr.1.html)```

<!-- verified: 2026-06-22 -->
