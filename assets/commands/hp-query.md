# TAGLINE

从 HPLIP 的型号数据库查询 HP 打印机的静态型号信息

# TLDR

按设备 URI 为打印机**查询单个键**

```hp-query -d [device-uri] -k [key]```

**查询全部键**，使用规范化型号名称（models.dat 中使用的形式）

```hp-query -m [model-name] -a```

使用设备 MDL: 字段中的原始型号名称**查询某个键**

```hp-query -r [model-name] -k [key]```

**查询全部键**并使用自定义分隔符

```hp-query -m [model-name] -a -s [tab]```

**抑制输出末尾的换行符**（编写脚本时很有用）

```hp-query -m [model-name] -k [key] -x```

# SYNOPSIS

**hp-query** [_MODE_] [_OPTIONS_]

# PARAMETERS

**-d** _device-uri_, **--device**=_device-uri_
> 按 CUPS 设备 URI 指定型号。

**-m** _model_, **--model**=_model_
> 指定规范化型号名称，即 HPLIP models.dat 中使用的形式。

**-r** _model_, **--raw**=_model_
> 指定原始型号名称，取自设备 IEEE-1284 设备 ID 的 **MDL:** 字段。

**-k** _key_, **--key**=_key_
> 要查询的键（models.dat 的字段名）。

**-a**, **--all**
> 查询全部键而非单个键。

**-s** _sep_, **--sep**=_sep_
> 配合 **-a** 使用时各值之间的分隔符：字面字符，或 tab、newline、cr、lf、crlf 之一。

**-x**
> 抑制输出末尾的换行符。

**-n**, **--non-interactive**
> 以非交互方式运行，不弹出提示。

**-l** _level_, **--logging**=_level_
> 设置日志详细程度：none、info（默认）、error、warn 或 debug。

**-g**
> 以调试级别日志运行（等价于 **-l debug**）。

**-h**, **--help**
> 显示帮助后退出。

# DESCRIPTION

**hp-query** 从 HPLIP 内部的型号数据库（models.dat）查找 HP 打印机的静态型号信息，输入可以是设备 URI、规范化的 HPLIP 型号名称，或取自打印机 IEEE-1284 设备 ID 的原始 **MDL:** 字符串。

它被设计为由其他程序和安装脚本调用，而不是交互式使用；返回某型号的一个字段（**-k**）或所有字段（**-a**）：支持的数据类型、所需的插件、后端能力等在 HPLIP 其他地方使用的元数据。

# CAVEATS

属于 HPLIP 软件包。它查询的是 HPLIP 本地的型号数据库，而非直接查询打印机，因此结果完全取决于该型号是否存在于 models.dat 中；很新或未收录的型号几乎不会返回内容。通过 **-d** _device-uri_ 解析型号仍需要设备可达足够长的时间以读取其设备 ID。

# HISTORY

**hp-query** 是 **HPLIP**（HP Linux Imaging and Printing）中的型号查询工具之一。HPLIP 是 HP 面向 Linux 的开源打印/扫描驱动套件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-info](/man/hp-info)(1), [hp-setup](/man/hp-setup)(1), [hp-check](/man/hp-check)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/hplip/)```

```[Homepage](https://developers.hp.com/hp-linux-imaging-and-printing)```

```[Documentation](https://developers.hp.com/hp-linux-imaging-and-printing/tech_docs/man_pages/index)```

<!-- verified: 2026-07-19 -->
