# TAGLINE

用于 Kismet 数据的无线侦察可视化工具

# TLDR

**导入 Kismet NETXML 数据**

```giskismet -x [kismet-output.netxml]```

**按 ESSID 查询特定接入点**

```giskismet -q "select * from wireless where ESSID='[MyNetwork]'"```

**将结果导出为 KML 文件**

```giskismet -x [data.netxml] -o [output.kml]```

**按加密类型过滤**

```giskismet -x [data.netxml] --encryption [WPA]```

**按 BSSID 过滤**

```giskismet -x [data.netxml] --bssid [AA:BB:CC:DD:EE:FF]```

# SYNOPSIS

**giskismet** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

**-x** _FILE_, **--xml** _FILE_
> 解析 Kismet NETXML 文件。

**--csv** _FILE_
> 解析 Kismet CSV 文件。

**--bssid** _FILTER_
> 按 BSSID 过滤（文件或逗号分隔列表）。

**--essid** _FILTER_
> 按 ESSID 过滤（文件或逗号分隔列表）。

**--encryption** _FILTER_
> 按加密类型过滤（文件或逗号分隔列表）。

**--channel** _FILTER_
> 按信道过滤（文件或逗号分隔列表）。

**-a**, **--ap**
> 仅插入接入点。

**-q** _SQL_, **--query** _SQL_
> 对数据库执行 SQL 查询。

**-o** _FILE_, **--output** _FILE_
> 指定 KML 导出的输出文件名。

**-n** _NAME_, **--name** _NAME_
> 设置 KML 图层名称。

**-s**, **--silent**
> 添加接入点时抑制输出。

**-d** _LEVEL_, **--debug** _LEVEL_
> 调试信息级别。

# DESCRIPTION

**giskismet** 是一个基于 Perl 的工具，处理由 **Kismet** 收集的无线侦察数据并将其存入 SQLite 数据库。用户可以对数据运行 SQL 查询，并生成 **Google Earth KML** 文件来绘制接入点位置的地图。

该工具支持按 BSSID、ESSID、加密类型和信道过滤，适用于无线安全评估和站点勘测。

# CAVEATS

需要以 Kismet NETXML 输出文件作为输入。Kismet 捕获数据中必须包含 GPS 数据才能生成有意义的 KML 输出。该工具已被弃用，建议改用较新的 Kismet 内置可视化功能。

# SEE ALSO

[kismet](/man/kismet)(1), [aircrack-ng](/man/aircrack-ng)(1)
