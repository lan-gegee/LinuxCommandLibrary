# TAGLINE

用于恶意软件检测的模式匹配工具

# TLDR

**用规则扫描文件**

```yara [rules.yar] [file]```

**递归扫描目录**

```yara -r [rules.yar] [directory]```

**扫描进程**

```yara [rules.yar] [pid]```

**显示匹配的字符串**

```yara -s [rules.yar] [file]```

**显示元数据**

```yara -m [rules.yar] [file]```

**多个规则文件**

```yara [rules1.yar] [rules2.yar] [file]```

**限时扫描**

```yara -a [30] [rules.yar] [file]```

**统计匹配数**

```yara -c [rules.yar] [file]```

# SYNOPSIS

**yara** [_-r_] [_-s_] [_-m_] [_-a timeout_] [_options_] _rules_ _target_

# PARAMETERS

**-r**
> 递归扫描目录。

**-s**
> 显示匹配的字符串。

**-m**
> 显示元数据。

**-c**
> 仅统计匹配数。

**-a** _SECONDS_
> 每个文件的超时时间。

**-n**
> 取反（显示不匹配的项）。

**-g**
> 显示标签。

**-e**
> 显示命名空间。

**-w**
> 禁用警告。

**-f**
> 快速匹配模式。

**-p** _N_
> 并行线程数。

**-d** _VAR=VAL_
> 定义外部变量。

# DESCRIPTION

**yara** 将模式与文件或进程进行匹配。它是恶意软件分类与检测的主要工具。

规则通过字符串、正则表达式和条件定义模式，描述恶意软件家族的特征或可疑行为。

字符串匹配可以查找字面文本、十六进制字节或正则表达式模式。条件将匹配结果用逻辑组合起来，实现精确检测。

进程扫描会检查正在运行的程序的内存。这可以检测出可能不存在于磁盘上的恶意软件。

规则中的元数据提供上下文信息：作者、描述、严重性和参考资料，有助于事件响应。

外部变量使规则可以参数化。无需修改规则即可调整阈值和设置。

# CAVEATS

编写高质量的规则需要专业知识。误报需要调优。内存驻留型恶意软件更难检测。需要定期更新规则。

# HISTORY

**YARA** 由 **Victor M. Alvarez** 在 **VirusTotal** 于 **2007 年**前后创建。它已成为恶意软件分类的标准工具，被杀毒厂商、事件响应人员和安全研究人员广泛使用。

# INSTALL

```apt: sudo apt install yara```

```dnf: sudo dnf install yara```

```pacman: sudo pacman -S yara```

```apk: sudo apk add yara```

```zypper: sudo zypper install yara```

```brew: brew install yara```

```nix: nix profile install nixpkgs#yara```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clamav](/man/clamav)(1), [strings](/man/strings)(1), [file](/man/file)(1), [ssdeep](/man/ssdeep)(1)
