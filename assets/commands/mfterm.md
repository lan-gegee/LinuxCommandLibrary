# TAGLINE

交互式 MIFARE 终端

# TLDR

**启动交互式终端**

```mfterm```

**加载转储文件**

```mfterm -l [dump.mfd]```

**加载密钥**

```mfterm -k [keys.txt]```

**读取卡片**

```mfterm -r```

**写入卡片**

```mfterm -w [dump.mfd]```

# SYNOPSIS

**mfterm** [_options_]

# PARAMETERS

**-l** _FILE_
> 加载转储文件。

**-k** _FILE_
> 加载密钥文件。

**-r**
> 读取卡片。

**-w** _FILE_
> 将转储内容写入卡片。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mfterm** 是一个交互式 MIFARE 终端，用于读取、写入和操作 MIFARE Classic 卡。

该工具提供扇区操作、密钥管理和数据分析等命令。

# CAVEATS

安全研究工具。需要 NFC 读卡器。仅限合法用途。

# HISTORY

mfterm 为安全研究目的提供交互式的 **MIFARE Classic** 卡操作能力。

# INSTALL

```brew: brew install mfterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mfoc](/man/mfoc)(1)
