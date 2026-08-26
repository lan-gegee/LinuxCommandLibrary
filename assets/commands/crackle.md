# TAGLINE

破解蓝牙低功耗（BLE）加密

# TLDR

**从 pcap 文件破解 BLE 加密**

```crackle -i [capture.pcap]```

**使用指定 LTK 破解**

```crackle -i [capture.pcap] -l [ltk_hex]```

**输出解密后的流量**

```crackle -i [capture.pcap] -o [decrypted.pcap]```

# SYNOPSIS

**crackle** [_options_] **-i** _input.pcap_

# PARAMETERS

**-i** _file_
> 包含 BLE 流量的输入 pcap 文件。

**-o** _file_
> 用于保存解密流量的输出文件。

**-l** _ltk_
> 十六进制形式的长期密钥（Long Term Key）。

# DESCRIPTION

**crackle** 用于破解蓝牙低功耗（BLE）加密。它利用 BLE 配对过程中的弱点来恢复加密密钥并解密捕获的流量。

需要捕获到包含配对交换过程的 BLE 数据包。适用于 BLE 传统配对（Legacy Pairing）。

# CAVEATS

仅对 BLE 传统配对（Bluetooth 4.0/4.1）有效。LE 安全连接（4.2 及以上）不受影响。只能用于经授权的安全测试。

# INSTALL

```nix: nix profile install nixpkgs#crackle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wireshark](/man/wireshark)(1)
