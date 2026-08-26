# TAGLINE

显示或设置系统的 NIS/YP 域名

# TLDR

**显示当前 NIS 域名**

```domainname```

**设置 NIS 域名**

```sudo domainname [example.com]```

**从文件设置 NIS 域名**

```sudo domainname -F [/etc/nisdomain]```

**清除域名**

```sudo domainname ""```

# SYNOPSIS

**domainname** [_name_]

# DESCRIPTION

**domainname** 显示或设置系统的 NIS（Network Information Service）域名。它与 DNS 域名是两回事，专用于 NIS/YP 服务。

不带参数时显示当前 NIS 域；带参数时设置域名（需要 root 权限）。如果不做额外配置，该设置通常无法在重启后保留。

# PARAMETERS

**-v**, **--verbose**
> 详细输出操作信息。

**-F** _file_, **--file** _file_
> 从指定文件读取域名。

**-y**, **--yp**, **--nis**
> 显示 NIS 域名（以 domainname 调用时的默认行为）。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本信息并退出。

# CAVEATS

不要把它与 DNS 域名混淆；查询 DNS 域名请用 **dnsdomainname**。默认情况下设置不会跨重启保留。NIS 已逐渐被 LDAP 和 Kerberos 取代。在现代系统上很少使用。

# HISTORY

**domainname** 的历史可追溯到 **NIS**（最初名为 Yellow Pages，简称 YP）诞生的年代，该技术由 **Sun Microsystems** 在 **20 世纪 80 年代**开发，为 Unix 网络提供集中式身份验证和配置服务。虽然如今大多已被 LDAP 和 Kerberos 取代，这个命令仍因兼容性而保留至今。

# INSTALL

```apt: sudo apt install hostname```

```dnf: sudo dnf install hostname```

```pacman: sudo pacman -S net-tools```

```apk: sudo apk add net-tools```

```zypper: sudo zypper install hostname```

```brew: brew install net-tools```

```nix: nix profile install nixpkgs#hostname```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostname](/man/hostname)(1), [dnsdomainname](/man/dnsdomainname)(1)
