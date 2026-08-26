# TAGLINE

详细转储 scamper warts 文件中的信息

# TLDR

**显示 warts 文件的详细内容**

```sc_wartsdump [input.warts]```

**转储多个 warts 文件**

```sc_wartsdump [file1.warts] [file2.warts]```

# SYNOPSIS

**sc_wartsdump** [_file_...]

# DESCRIPTION

**sc_wartsdump** 对一系列 warts 文件（scamper 的二进制输出格式）中的信息进行详细转储。输出结构清晰，适合对结果做初步分析，但该格式不保证保持稳定，不适合自动化解析。

如需机器可解析的输出，请改用 **sc_warts2json** 或 **sc_warts2text**。它是 CAIDA 开发的 scamper 互联网测量工具集的一部分。

# CAVEATS

sc_wartsdump 的输出格式可能随版本变化，不应依赖它进行自动化处理。需要稳定的结构化输出请使用 sc_warts2json。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc_warts2text](/man/sc_warts2text)(1), [scamper](/man/scamper)(1)
