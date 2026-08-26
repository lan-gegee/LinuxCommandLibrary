# TAGLINE

转储 scamper warts 分析数据

# TLDR

**转储 scamper warts 分析数据**

```sc_analysis_dump [input.warts]```

**输出指定格式**

```sc_analysis_dump -t [traceroute] [input.warts]```

# SYNOPSIS

**sc_analysis_dump** [_options_] _file_

# PARAMETERS

**-t** _type_
> 分析类型（traceroute、ping 等）。

**-c**
> CSV 输出格式。

# DESCRIPTION

**sc_analysis_dump** 从 scamper warts 文件中提取并显示分析数据。scamper 网络测量工具集的一部分。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc_wartsdump](/man/sc_wartsdump)(1), [scamper](/man/scamper)(1)
