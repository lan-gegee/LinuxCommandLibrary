# TAGLINE

显示最大的已安装软件包

# TLDR

**显示 10 个最大的已安装软件包**

```dpigs```

**显示 N 个最大的软件包**

```dpigs -n [20]```

**以人类可读格式显示**

```dpigs -H```

**显示最大的源码包**

```dpigs -S```

# SYNOPSIS

**dpigs** [_options_]

# DESCRIPTION

**dpigs** 显示基于 Debian 的系统上哪些已安装软件包占用最多磁盘空间。它查询 dpkg 数据库来确定每个包的已安装大小并进行排序，找出占用空间的元凶。

当磁盘空间紧张、需要找出可移除对象时，这个工具特别有用。它既可以按二进制包显示，也可以按源码包聚合显示，方便看出哪些软件项目消耗的空间最多。

dpigs 是 debian-goodies 包的一部分，这是一组面向 Debian 系统管理员的实用工具集。

# PARAMETERS

**-n, --lines** _n_
> 显示 n 个最大的软件包（默认：10）

**-s, --status** _file_
> 使用其他的 dpkg status 文件

**-S, --source**
> 改为显示源码包

**-H, --human-readable**
> 人类可读的大小

**-h, --help**
> 显示帮助

# CAVEATS

显示的是安装后大小，而非下载大小。仅适用于 Debian/Ubuntu。属于 debian-goodies 包。

# SEE ALSO

[dpkg-query](/man/dpkg-query)(1), [apt](/man/apt)(8), [du](/man/du)(1)
