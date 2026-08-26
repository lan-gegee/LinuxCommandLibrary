# TAGLINE

从抓包文件中提取 WPA 握手数据

# TLDR

**清理抓包文件**

```wpaclean [output.cap] [input.cap]```

**清理多个文件**

```wpaclean [output.cap] [file1.cap] [file2.cap]```

# SYNOPSIS

**wpaclean** _output_ _input_ ...

# PARAMETERS

_output_
> 清理后的输出文件。

_input_
> 输入的抓包文件。

# DESCRIPTION

**wpaclean** 清理抓包文件，只保留四次握手和一个信标帧。它生成的输出文件只包含离线密码分析所需的 EAPOL 认证帧，通过移除所有非握手流量显著减小文件体积。

多个输入抓包文件可以被处理并合并为一个清理后的输出文件。该工具属于 aircrack-ng 套件，通常用于在授权的安全评估中，将抓包文件送入 aircrack-ng 或 hashcat 进行 WPA/WPA2 密码恢复之前做预处理。

注意：参数顺序上，输出文件要写在输入文件**之前**。

# CAVEATS

属于 aircrack-ng 套件。只提取 WPA/WPA2 四次握手和信标帧；所有其他帧都会被丢弃。除位置参数外没有任何命令行选项。输入文件必须是 pcap 格式。

# HISTORY

**wpaclean** 是 **aircrack-ng** 套件的一部分。aircrack-ng 是一组用于 802.11 无线网络安全审计的工具。

# INSTALL

```apt: sudo apt install aircrack-ng```

```dnf: sudo dnf install aircrack-ng```

```pacman: sudo pacman -S aircrack-ng```

```apk: sudo apk add aircrack-ng```

```zypper: sudo zypper install aircrack-ng```

```brew: brew install aircrack-ng```

```nix: nix profile install nixpkgs#aircrack-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [hashcat](/man/hashcat)(1)
