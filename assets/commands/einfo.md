# TAGLINE

NCBI Entrez 数据库信息工具

# TLDR

**打印**所有数据库名称

```einfo -dbs```

**以 XML 格式打印**数据库的全部信息

```einfo -db [protein]```

**打印**数据库的所有字段

```einfo -db [nuccore] -fields```

**打印**数据库的所有链接

```einfo -db [protein] -links```

# SYNOPSIS

**einfo** [_options_]

# DESCRIPTION

**einfo** 提供 NCBI Entrez 数据库的信息。它显示每个字段中索引的记录数、最后更新日期以及可用的跨数据库链接。

属于 NCBI EDirect 工具集，用于以编程方式访问生物学数据库。

# PARAMETERS

**-dbs**
> 列出所有数据库名称。

**-db** _database_
> 指定要查询的数据库。

**-fields**
> 显示数据库可用的搜索字段。

**-links**
> 显示可用的跨数据库链接。

**-help**
> 打印用法信息。

**-email** _address_
> 随请求发送的电子邮件地址。

# CAVEATS

属于 NCBI 的 edirect 软件包。需要互联网连接。输出默认为 XML 格式。

# INSTALL

```apt: sudo apt install epub-utils```

```dnf: sudo dnf install ebook-tools```

```pacman: sudo pacman -S ebook-tools```

```apk: sudo apk add ebook-tools```

```zypper: sudo zypper install ebook-tools```

```brew: brew install ebook-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[esearch](/man/esearch)(1), [elink](/man/elink)(1)
