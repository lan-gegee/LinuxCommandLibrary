# TAGLINE

过滤 scamper warts 文件中的记录

# TLDR

**过滤 warts 文件记录**

```sc_wartsfilter -i [input.warts] -o [output.warts] -t [traceroute]```

**按目的地过滤**

```sc_wartsfilter -i [input.warts] -o [output.warts] -d [192.168.0.0/16]```

# SYNOPSIS

**sc_wartsfilter** [_options_]

# PARAMETERS

**-i** _file_
> 输入 warts 文件。

**-o** _file_
> 输出 warts 文件。

**-t** _type_
> 按测量类型过滤。

**-d** _prefix_
> 按目的地前缀过滤。

# DESCRIPTION

**sc_wartsfilter** 按多种条件过滤 scamper warts 文件。scamper 工具集的一部分。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc_wartscat](/man/sc_wartscat)(1), [scamper](/man/scamper)(1)
