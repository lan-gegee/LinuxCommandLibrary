# TAGLINE

比较 scamper 数据中的 traceroute 路径

# TLDR

**比较两条 traceroute 路径**

```sc_tracediff [trace1.warts] [trace2.warts]```

# SYNOPSIS

**sc_tracediff** [_options_] _file1_ _file2_

# PARAMETERS

**-a**
> 显示所有差异。

**-d**
> 显示详细输出。

# DESCRIPTION

**sc_tracediff** 比较两个 scamper traceroute 文件并突出显示路径差异。可用于检测路由变化。scamper 工具集的一部分。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scamper](/man/scamper)(1), [sc_wartsdump](/man/sc_wartsdump)(1)
