# TAGLINE

多功能终端天气客户端

# TLDR

**显示当前天气**

```outside```

**显示指定地点的天气**

```outside -l "[city]"```

**以公制单位显示天气**

```outside -u metric```

**以 JSON 输出**

```outside -f json```

# SYNOPSIS

**outside** [_options_]

# PARAMETERS

**-l**, **--location** _LOCATION_
> 指定地点（默认通过 IP 自动检测）。

**-u**, **--units** _UNITS_
> 度量单位（metric 或 imperial）。

**-f**, **--format** _FORMAT_
> 输出格式（tui、simple、detailed、json、waybar）。

# DESCRIPTION

**outside** 是一款多功能终端天气客户端。它支持通过 IP 自动定位、多种输出格式、7 天预报，以及用于数据展示的可自定义模板。

# CAVEATS

需要联网。地点检测的准确性取决于 IP 地理定位。

# HISTORY

**outside** 由 **BaconIsAVeg** 创建，使用 **Rust** 编写。

# SEE ALSO

[curl](/man/curl)(1), [stormy](/man/stormy)(1), [rustormy](/man/rustormy)(1)
