# TAGLINE

校验 PostScript 打印机描述（PPD）文件

# TLDR

**测试 PPD 文件**

```cupstestppd [file.ppd]```

以详细输出模式测试

```cupstestppd -v [file.ppd]```

**详细一致性检查并显示全部 PPD 信息**

```cupstestppd -vv [file.ppd]```

安静模式（只显示错误）

```cupstestppd -q [file.ppd]```

从 stdin 测试

```cat [file.ppd] | cupstestppd -```

放宽一致性要求进行测试

```cupstestppd -r [file.ppd]```

# SYNOPSIS

**cupstestppd** [_options_] _file.ppd_ [_files..._]

# PARAMETERS

**-v**
> 详细的合规性测试结果。

**-vv**
> 在详细合规性结果之外，显示全部 PPD 信息。

**-q**
> 安静模式，只显示错误。

**-r**
> 放宽的合规性：将常见的空白、控制字符和格式问题视为非致命问题。

**-W** _category_
> 将某一类错误报告为警告：filters、profiles、sizes、translations、all 或 none。

**-I** _category_
> 忽略某一类错误：filename 或 filters。

**-R** _root_
> 设置替代的根目录。

# DESCRIPTION

**cupstestppd** 测试 PPD 文件是否符合 Adobe PostScript Printer Description 文件格式规范 4.3 版。它也可用于列出 PPD 文件支持的选项和可用字体。它接受命令行上的文件名，或在给定短横线（-）参数时从标准输入读取。

退出码为 0 表示该 PPD 文件有效。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsd](/man/cupsd)(8), [lpadmin](/man/lpadmin)(8)
