# TAGLINE

在 MaxMind DB 文件中查找 IP 地址

# TLDR

在 GeoLite2 City 数据库中**查找** IPv4 地址

```mmdblookup --file [path/to/GeoLite2-City.mmdb] --ip [8.8.8.8]```

只查找**国家 ISO 代码**

```mmdblookup --file [path/to/GeoLite2-Country.mmdb] --ip [8.8.8.8] country iso_code```

通过嵌套 map 路径查找**英文城市名称**

```mmdblookup --file [path/to/GeoLite2-City.mmdb] --ip [1.1.1.1] city names en```

查找 **IPv6** 地址

```mmdblookup --file [path/to/GeoLite2-City.mmdb] --ip [2001:4860:4860::8888]```

在输出记录的同时打印**数据库元数据**

```mmdblookup --verbose --file [path/to/GeoLite2-City.mmdb] --ip [8.8.8.8]```

# SYNOPSIS

**mmdblookup** **--file** _FILE_ **--ip** _ADDRESS_ [_DATA_PATH_...]

# PARAMETERS

**-f**, **--file** _FILE_
> MaxMind DB（`.mmdb`）文件的路径。必填。

**-i**, **--ip** _ADDRESS_
> 要查找的 IPv4 或 IPv6 地址。必填。

_DATA_PATH_
> 可选的记录键路径。map 键是字符串；数组索引是从 0 开始的整数。

**-v**, **--verbose**
> 同时打印数据库元数据。

**--version**
> 打印程序版本并退出。

**-h**, **-?**, **--help**
> 显示用法信息。

# DESCRIPTION

**mmdblookup** 是随 **libmaxminddb** 发布的命令行查询工具。它会打开一个 MaxMind DB 文件，找到某个 IP 地址对应的记录，并以带类型标注、类似 JSON 的结构打印该记录。map 用 `{}` 表示，数组用 `[]` 表示，每个值后面都跟有一个类型标注。

如果记录是 map 或数组，**--ip** 之后的额外参数就构成一条指向该结构的查找路径。例如 `country iso_code` 选择 `country` map 内的 `iso_code` 字段，`cities 1` 选择 `cities` 数组的第二个元素。不提供路径时则打印整条记录。

该工具不会下载数据库。典型输入是从 MaxMind（或其他 MMDB 生产者）获取并保存在本地的 GeoIP2 或 GeoLite2 `.mmdb` 文件。

# CAVEATS

输出**不是 JSON**，也不能当作 JSON 来解析。类型标注和 `{}` / `[]` 包装使它只适合人类阅读。若需要机器可读的 JSON，MaxMind 推荐改用 **mmdbinspect**。

**--file** 和 **--ip** 都是必填项。数据库缺失、路径在记录中不存在，或地址不存在时，只会返回很少甚至没有数据，而不会报出 GeoIP2 特定的错误。该命令对 GeoIP2 字段名一无所知；那些键来自你所指定的数据库。

# HISTORY

**mmdblookup** 由 **MaxMind** 的 **Boris Zentner** 和 **Dave Rolsky** 编写，是 **libmaxminddb** 的一部分——这是供 GeoIP2 与 GeoLite2 使用的 MaxMind DB 格式 C 库。该库与这个工具最早出现于约 **2013-2014 年**，当时 MaxMind 正以新格式取代旧版 GeoIP 格式。该项目基于 **Apache 2.0** 许可证发布。

# INSTALL

```apt: sudo apt install mmdb-bin```

```dnf: sudo dnf install libmaxminddb```

```pacman: sudo pacman -S libmaxminddb```

```apk: sudo apk add libmaxminddb```

```zypper: sudo zypper install mmdblookup```

```brew: brew install libmaxminddb```

```nix: nix profile install nixpkgs#libmaxminddb```

<!-- packages: 2026-08-19 -->

# SEE ALSO

[ipinfo](/man/ipinfo)(1), [whois](/man/whois)(1), [dig](/man/dig)(1), [host](/man/host)(1)

# RESOURCES

```[Source code](https://github.com/maxmind/libmaxminddb)```

```[Documentation](https://maxmind.github.io/libmaxminddb/mmdblookup.html)```

<!-- verified: 2026-08-19 -->
