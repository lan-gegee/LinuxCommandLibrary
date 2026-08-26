# TAGLINE

终止活动的 PPPoE 连接

# TLDR

**停止 PPPoE 连接**

```sudo pppoe-stop```

**停止指定接口的连接**

```sudo pppoe-stop -I [eth0]```

**使用配置文件停止连接**

```sudo pppoe-stop [/etc/ppp/pppoe.conf]```

# SYNOPSIS

**pppoe-stop** [_options_] [_config-file_]

# PARAMETERS

**-I** _interface_
> 网络接口。

**config-file**
> 配置文件路径。

# DESCRIPTION

**pppoe-stop** 终止活动的 PPPoE（Point-to-Point Protocol over Ethernet）连接。它是 pppoe-start 的对应工具，属于 rp-pppoe 软件包。

# EXAMPLES

```bash
# Stop default connection
sudo pppoe-stop

# Stop specific interface
sudo pppoe-stop -I eth1

# Using custom config
sudo pppoe-stop /etc/ppp/pppoe-custom.conf

# Check status first
pppoe-status
sudo pppoe-stop
```

# RELATED COMMANDS

```bash
pppoe-start   - Start PPPoE connection
pppoe-status  - Check connection status
pppoe-connect - Manual connection
pppoe-setup   - Configure PPPoE
```

# CAVEATS

需要 root 权限。属于 rp-pppoe 软件包。NetworkManager 对 PPPoE 的管理方式可能有所不同。

# HISTORY

pppoe-stop 是 **David F. Skoll** 编写的 **rp-pppoe**（Roaring Penguin PPPoE）的一部分，用于 Linux 上的 PPPoE 连接。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppd](/man/pppd)(8), [pppoe](/man/pppoe)(8)
