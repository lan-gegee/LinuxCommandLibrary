# TAGLINE

更改 SELinux 安全类别

# TLDR

**列出**所有可用的类别

```sudo chcat -L```

为文件**添加**一个类别

```sudo chcat +[CategoryName] [path/to/file]```

从文件**移除**一个类别

```sudo chcat -- -[CategoryName] [path/to/file]```

为文件**设置**特定类别

```sudo chcat [CategoryName1,CategoryName2,...] [path/to/file]```

**显示**文件的类别

```ls -Z [path/to/file]```

从文件中移除**所有**类别

```sudo chcat -d [path/to/file]```

# SYNOPSIS

**chcat** [_options_] _category_ _file_...

# DESCRIPTION

**chcat** 更改文件的 SELinux 安全类别。类别是多类别安全（MCS）的一部分，在传统 SELinux 类型之外提供额外的访问控制。

MCS 类别允许对数据进行分隔，用户或进程只能访问具有匹配类别的文件。

# PARAMETERS

**-L, --list**
> 列出所有可用的类别

**-d, --delete**
> 移除文件的所有类别

**+**_category_
> 添加一个类别

**-**_category_
> 移除一个类别（需在其前使用 --）

# CAVEATS

需要启用 SELinux 并使用 MCS 策略。类别名称必须在策略中定义。更改会立即影响访问控制。

# SEE ALSO

[chcon](/man/chcon)(1), [semanage](/man/semanage)(8), [ls](/man/ls)(1)

# RESOURCES

```[Source code](https://github.com/SELinuxProject/selinux)```

<!-- verified: 2026-06-22 -->
