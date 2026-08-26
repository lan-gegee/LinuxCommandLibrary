# TAGLINE

合并多个 PPD 打印机文件

# TLDR

**合并 PPD 文件**

```ppdmerge -o [output.ppd] [file1.ppd] [file2.ppd]```

**合并多个语言版本**

```ppdmerge -o [combined.ppd] [en.ppd] [de.ppd] [fr.ppd]```

# SYNOPSIS

**ppdmerge** [_options_] _files_

# PARAMETERS

_FILES_
> 输入的 PPD 文件。

**-o** _FILE_
> 输出文件名。未指定时，合并后的 PPD 文件会写到标准输出。

# DESCRIPTION

**ppdmerge** 将多个 PPD（PostScript Printer Description）文件合并为一个多语言 PPD 文件。它主要用于组合打印机驱动程序的本地化版本，使单个 PPD 文件支持多种语言，由 CUPS 根据用户的区域设置选择相应的翻译。

输入文件应当是同一打印机定义的不同变体，仅翻译字符串不同。合并后的输出包含所有语言变体，减少了需要分发和安装的 PPD 文件数量。ppdmerge 不会检查被合并的 PPD 文件是否属于同一设备；合并不同设备的 PPD 会产生不可预测的结果。

# CAVEATS

已弃用。PPD 文件和 ppdmerge 将在未来的 CUPS 版本中移除。

# HISTORY

ppdmerge 是 **CUPS** 的组成部分，用于合并 PPD 文件。

# INSTALL

```apt: sudo apt install cups-ppdc```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppdc](/man/ppdc)(1), [ppdi](/man/ppdi)(1), [ppdhtml](/man/ppdhtml)(1), [ppdpo](/man/ppdpo)(1), [cups](/man/cups)(1)
