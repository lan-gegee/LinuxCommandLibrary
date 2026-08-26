# TAGLINE

从口令生成 WPA 预共享密钥

# TLDR

从标准输入读取口令来**计算** WPA-PSK 密钥

```wpa_passphrase [SSID]```

以参数形式提供口令来**计算** WPA-PSK 密钥

```wpa_passphrase [SSID] [passphrase]```

**生成并追加**到 wpa_supplicant 配置

```wpa_passphrase [SSID] [passphrase] >> /etc/wpa_supplicant/wpa_supplicant.conf```

# SYNOPSIS

**wpa_passphrase** _ssid_ [_passphrase_]

# PARAMETERS

**ssid**
> 为其生成密钥的网络名称（SSID）

**passphrase**
> WiFi 密码，必须为 8 到 63 个可打印 ASCII 字符（若省略则从标准输入读取）

# DESCRIPTION

**wpa_passphrase** 根据给定网络 SSID 的 ASCII 口令生成 WPA-PSK（预共享密钥）配置。输出采用 wpa_supplicant.conf 格式，可以直接追加到配置文件中。

该工具会用 PBKDF2 预先计算 PSK，比让 wpa_supplicant 每次重新计算更快。输出同时包含明文口令（注释形式）和计算得到的 PSK。

# CAVEATS

在命令行上提供口令会使它暴露在进程列表和 shell 历史记录中。为了安全起见，建议从标准输入读取。口令长度必须在 8 到 63 个字符之间。SSID 区分大小写，必须完全匹配。属于 wpa_supplicant 软件包的一部分。

# INSTALL

```apt: sudo apt install wpasupplicant```

```dnf: sudo dnf install wpa_supplicant```

```pacman: sudo pacman -S wpa_supplicant```

```apk: sudo apk add wpa_supplicant```

```zypper: sudo zypper install wpa_supplicant```

```nix: nix profile install nixpkgs#wpa_supplicant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wpa_supplicant](/man/wpa_supplicant)(8), [wpa_cli](/man/wpa_cli)(8)
