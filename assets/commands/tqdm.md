# TAGLINE

为命令管道添加进度条

# TLDR

**为管道添加进度条**

```cat [file] | tqdm --bytes | wc -l```

**指定预估总量**

```cat [file] | tqdm --total [1000] | process```

**自定义单位**

```cat [files] | tqdm --unit files | process```

**写入文件**

```cat [input] | tqdm > [output]```

**带描述前缀**

```seq [100] | tqdm --desc "[Processing]" | process```

# SYNOPSIS

**tqdm** [_--total n_] [_--unit name_] [_--desc text_] [_options_]

# PARAMETERS

**--total** _N_
> 预期的迭代次数。

**--unit** _NAME_
> 单位名称。

**--desc** _TEXT_
> 描述前缀。

**--bytes**
> 字节计数模式。

**--null**
> 使用空字符作为行分隔符。

**--ncols** _N_
> 进度条输出的宽度。

**--ascii**
> 进度条使用 ASCII 字符而非 unicode。

**--colour** _COLOUR_
> 进度条颜色（如 red、green、#00ff00）。

**--mininterval** _SECONDS_
> 最小显示刷新间隔（默认：0.1）。

# DESCRIPTION

**tqdm**（源自阿拉伯语 "taqaddum"，意为进步）通过包装标准输入/输出流为命令行管道添加进度条。它实时显示迭代速度、已用时间和预计剩余时间等统计信息。

该工具既可作为 CLI 管道包装器，也可作为 Python 库使用。在 CLI 模式下，它会统计经过的行数或字节数，并在 stderr 上渲染可视化进度条。指定 **--total** 时显示百分比进度条；否则显示带速度估计的简单计数器。

# CAVEATS

需要 Python。输出到 stderr。可能会轻微拖慢管道。

# HISTORY

**tqdm**（源自阿拉伯语，意为"progress"）最初是为 Python 和 CLI 打造的快速、可扩展的进度条。

# INSTALL

```apk: sudo apk add py3-tqdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pv](/man/pv)(1), [progress](/man/progress)(1), [bar](/man/bar)(1)
