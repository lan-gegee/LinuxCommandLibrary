# TAGLINE

显示或设置系统的主机名

# TLDR

**显示当前主机名**

```hostname```

**显示完全限定域名**（FQDN）

```hostname -f```

**显示短主机名**（不含域名）

```hostname -s```

**显示主机的所有 IP 地址**

```hostname -I```

**显示 DNS 域名**

```hostname -d```

**设置主机名**（临时，重启后失效）

```sudo hostname [new_hostname]```

**从文件读取主机名**

```sudo hostname -F [/etc/hostname]```

**显示 NIS/YP 域名**

```hostname -y```

# SYNOPSIS

**hostname** [_options_] [_name_]

**hostname** [-f|--fqdn]

**hostname** [-I|--all-ip-addresses]

# PARAMETERS

**-a**, **--alias**
> 显示主机的别名

**-d**, **--domain**
> 显示 DNS 域名

**-f**, **--fqdn**, **--long**
> 显示完全限定域名（FQDN）

**-A**, **--all-fqdns**
> 显示机器的所有 FQDN

**-i**, **--ip-address**
> 显示主机名对应的 IP 地址

**-I**, **--all-ip-addresses**
> 显示主机的所有网络地址（不包括回环和 IPv6 链路本地地址）

**-s**, **--short**
> 显示短主机名（截取第一个点之前的部分）

**-y**, **--yp**, **--nis**
> 显示或设置 NIS/YP 域名

**-F**, **--file** _FILE_
> 从指定文件读取主机名

**-b**, **--boot**
> 总是设置一个主机名；若未指定则使用默认值

**-v**, **--verbose**
> 详细输出所执行的操作

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 显示版本信息

# DESCRIPTION

**hostname** 用于显示或设置系统的主机名。主机名被许多网络程序用来标识机器。该命令可以显示多种名称组成部分，包括短名称、FQDN、域名和 IP 地址。

不带参数调用时，它显示 gethostname 系统调用返回的当前主机名。带参数调用时，它会设置主机名（需要 root 权限）。相关命令 **domainname**、**dnsdomainname** 和 **nisdomainname** 通常是指向 hostname 的符号链接。

**-I** 选项对脚本特别有用，因为它列出所有已配置的 IP 地址而不依赖 DNS 解析。FQDN（**-f**）由短主机名与 DNS 域组合而成。

# CAVEATS

用该命令设置的主机名是临时的，重启后不会保留。要永久更改，请编辑 **/etc/hostname** 或在基于 systemd 的系统上使用 **hostnamectl**。**-i** 选项依赖 DNS 解析，若主机名无法解析可能失败。更改需要 root 权限。

# HISTORY

hostname 命令自 20 世纪 80 年代早期 BSD 版本起就是 Unix 系统的一部分。随着 TCP/IP 网络成为标准，它从简单的主机名显示演变为包含域名处理。在现代 Linux 系统上，systemd 提供的 **hostnamectl** 为持久化主机名配置提供了更多功能，包括静态、瞬态（transient）和友好（pretty）主机名。

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

[hostnamectl](/man/hostnamectl)(1), [domainname](/man/domainname)(1)
