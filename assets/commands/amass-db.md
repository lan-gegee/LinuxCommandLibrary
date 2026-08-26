# TAGLINE

查询和管理已存储的 amass 枚举结果

# TLDR

**列出**某个域名的枚举记录

```amass db -list -d [example.com]```

**显示**特定枚举索引的结果

```amass db -show -d [example.com] -enum [1]```

仅**打印发现的名称**

```amass db -names -d [example.com]```

**显示**某个域名发现的 IP 地址

```amass db -show -ip -d [example.com]```

将某个域名的全部结果**导出**为 JSON

```amass db -d [example.com] -json [output.json]```

**打印**某个域名的 ASN **摘要**

```amass db -summary -d [example.com]```

# SYNOPSIS

**amass db** [_options_]

# DESCRIPTION

**amass db** 查询本地图数据库，其中存储了以往 **amass enum** 运行的结果。它可以列出过去的枚举记录、打印发现结果、导出为 JSON，并可按域名、枚举索引和数据源限定查询范围。

数据库会持久保存发现的资产，因此可以跟踪多次扫描之间的变化，并在多次运行之间关联结果。

# PARAMETERS

**-d** _domain_
> 用于过滤的域名，逗号分隔。可重复使用。

**-df** _file_
> 包含根域名的文件，每行一个。

**-list**
> 打印带编号的枚举列表，按提供的域名过滤。

**-show**
> 打印所提供枚举索引和域名的结果。

**-enum** _index_
> 通过 **-list** 输出的索引标识某次枚举。

**-names**
> 仅打印发现的 DNS 名称。

**-ip**
> 显示发现名称对应的 IP 地址。

**-ipv4**
> 仅显示 IPv4 地址。

**-ipv6**
> 仅显示 IPv6 地址。

**-src**
> 打印每个发现名称的数据来源。

**-summary**
> 仅打印 ASN 表摘要。

**-demo**
> 对输出进行遮蔽处理，使其适合演示场合。

**-nocolor**
> 禁用彩色输出。

**-silent**
> 执行期间禁用所有输出（配合 **-json**/**-o** 时很有用）。

**-config** _file_
> INI 配置文件的路径。

**-dir** _path_
> 图数据库所在目录的路径（默认：`~/.config/amass`）。

**-json** _file_
> JSON 输出文件的路径。

**-o** _file_
> 捕获 stdout/stderr 的文本文件路径。

**-h**, **-help**
> 显示程序用法信息。

# CONFIGURATION

**~/.config/amass/config.ini**
> Amass 配置文件，定义数据源、API 密钥和范围设置。

**~/.config/amass/**
> 图数据库的默认位置（可通过 **-dir** 覆盖）。

# CAVEATS

数据库会随时间增长得很大；定期清理或轮换 **-dir** 路径是明智的做法。**db** 子命令在 Amass v4 中已被弃用，由独立的 **oam_subs** / **oam-tools** 工具取代；本页面记录的是仍存在于许多发行版中的 v3 时代命令行界面。

# HISTORY

**amass** 是 **OWASP** 项目，最初由 **Jeff Foley**（caffix）创建，用于深度攻击面测绘。图数据库和 **db** 子命令在 v3 系列中加入，以支持枚举结果的持久存储和变化跟踪。在 **v4** 中，数据库工具被拆分为 **oam-tools**（`oam_subs` 等）。

# INSTALL

```aur: yay -S amass```

```brew: brew install amass```

```nix: nix profile install nixpkgs#amass```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amass](/man/amass)(1), [amass-enum](/man/amass-enum)(1), [amass-track](/man/amass-track)(1)
