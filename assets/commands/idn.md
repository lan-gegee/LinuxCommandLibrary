# TAGLINE

对国际化域名进行编码和解码

# TLDR

**将 Unicode 域名编码为 ACE/Punycode（默认模式）**

```echo "münchen.de" | idn```

**将 Punycode 域名解码回 Unicode**

```echo "xn--mnchen-3ya.de" | idn --idna-to-unicode```

**对输入应用 Nameprep stringprep 处理**

```echo "[string]" | idn --stringprep```

**对参数显式执行 IDNA ToASCII**

```idn --idna-to-ascii [münchen.de]```

**编码或解码原始 Punycode（不做 IDNA 包装）**

```echo "[label]" | idn --punycode-encode```

**安静模式（抑制提示信息）**

```idn --quiet [domain]```

# SYNOPSIS

**idn** [_options_] [_strings_...]

# PARAMETERS

_strings_
> 要转换的域名或标签。未提供时从标准输入读取。

**-a**, **--idna-to-ascii**
> 按照 IDNA 将输入转换为 ACE。这是默认模式。

**-u**, **--idna-to-unicode**
> 使用 IDNA 将输入从 ACE（Punycode）转换回 Unicode。

**-s**, **--stringprep**
> 按 Nameprep 概要（profile）处理字符串。

**-e**, **--punycode-encode**
> 用 Punycode 算法编码原始输入，不经过 IDNA 前置/后置处理。

**-d**, **--punycode-decode**
> 解码原始 Punycode 输入，不经过 IDNA 前置/后置处理。

**-n**, **--nfkc**
> 按 Unicode v3.2 NFKC 规范化输入。

**-p** _profile_, **--profile**=_profile_
> 使用指定的 stringprep 概要。有效值：`Nameprep`、`iSCSI`、`Nodeprep`、`Resourceprep`、`trace`、`SASLprep`。

**--allow-unassigned**
> 切换 IDNA 的 `AllowUnassigned` 标志（默认关闭）。

**--usestd3asciirules**
> 切换 IDNA 的 `UseSTD3ASCIIRules` 标志（默认关闭）；禁止非 LDH 字符。

**--no-tld**
> 跳过针对 TLD 的有效性检查（仅影响 `--idna-to-ascii` / `--idna-to-unicode`）。

**--quiet**
> 静默运行。

**--debug**
> 打印调试信息，包括检测到的字符集。

**-h**, **--help**
> 打印帮助并退出。

**-V**, **--version**
> 打印版本并退出。

# DESCRIPTION

**idn** 在 Unicode 与 ASCII 兼容编码（ACE / Punycode）之间转换国际化域名。它实现了 IDNA（Internationalized Domain Names in Applications）标准，让包含非 ASCII 字符的域名能够在 DNS 中表示。

编码流程会先应用 Nameprep stringprep（大小写折叠、NFKC 规范化、禁用字符检查），再进行 Punycode 编码。经过 ACE 编码的标签使用 **xn--** 前缀。该工具从命令行参数读取字符串；若未提供参数，则从标准输入读取。

输入应使用区域设置的首选字符集；可通过设置 **CHARSET** 环境变量覆盖。要处理以 `-` 开头的字符串，请用 `--` 标记选项结束（如 `idn --quiet -a -- -foo`）。

# CAVEATS

该工具实现的是 **IDNA 2003**（RFC 3490）。对于较新的 **IDNA 2008** 标准（RFC 5891），请使用 libidn2 软件包中的 **idn2**。两个标准在若干字符的处理上存在差异（如德语 eszett `ß`、希腊语词尾 sigma `ς`）。属于 **GNU Libidn**。

# HISTORY

**idn** 是 **GNU Libidn** 的一部分，由 **Simon Josefsson** 编写。IDNA 标准于 **2003 年**作为 RFC 3490 发布，旨在让国际化域名进入 DNS。

# INSTALL

```apt: sudo apt install idn```

```dnf: sudo dnf install libidn```

```pacman: sudo pacman -S libidn```

```apk: sudo apk add libidn```

```brew: brew install libidn```

```nix: nix profile install nixpkgs#libidn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[host](/man/host)(1), [dig](/man/dig)(1)
