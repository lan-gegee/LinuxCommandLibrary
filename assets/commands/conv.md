# TAGLINE

单位换算终端实用工具

# TLDR

**转换一个值**——在其后直接附加单位缩写

```conv [100f]```

**将米转换为**其他距离单位

```conv [50m]```

**转换以千克计的重量**

```conv [75kg]```

**转换以 Mbps 计的数据传输速率**

```conv [100mbps]```

**显示帮助**并列出所有受支持的单位缩写

```conv --help```

# SYNOPSIS

**conv** _value__unit_

**conv** **-h**|**--help**

**conv** **-v**|**--version**

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并列出所有受支持的单位缩写。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**conv** 是一款轻量、自包含的终端实用工具，用于换算日常计量单位。数值和单位缩写合在一起作为单个参数（例如 `100f` 表示 100 华氏度），conv 会打印同一类别下所有其他单位的等值结果。

支持的类别及其缩写：

- **温度：** c（摄氏度）、f（华氏度）
- **距离：** cm（厘米）、ft（英尺）、in（英寸）、km（千米）、m（米）、mi（英里）、nm（海里）、yd（码）
- **重量：** ct（克拉）、g（克）、kg（千克）、oz（盎司）、lb（磅）、st（英石）
- **体积：** cum（立方米）、l（升）、guk（英制加仑）、gus（美制加仑）
- **速度：** kmh（千米/小时）、kn（节）、mph（英里/小时）、mps（米/秒）
- **数据速率：** bps、kbps、mbps（比特/秒系列）；bs、kbs、mbs（字节/秒系列）
- **功率：** hp（马力）、w（瓦特）
- **其他：** bbl（石油桶）

# CAVEATS

数值和单位缩写必须写成单个参数，中间不能有空格（例如 `conv 100f`，而非 `conv 100 f`）。仅支持上面列出的单位类别；不支持货币和任意单位表达式。该项目于 2019 年归档，不再活跃维护。

# HISTORY

**conv** 由 Ben Garrett 编写，使用 Go 实现。它为 Linux、macOS、Windows 和 ARM 提供了预编译的二进制文件。github.com/bengarrett/conv 仓库已于 2019 年 9 月归档。

# INSTALL

```apt: sudo apt install gmtsar-core```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[units](/man/units)(1), [bc](/man/bc)(1), [qalc](/man/qalc)(1)
