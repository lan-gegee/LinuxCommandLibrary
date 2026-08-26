# TAGLINE

NetworkManager 的主配置文件

# TLDR

**基本配置**

```[main]\nplugins=ifupdown,keyfile```

**设置 DNS 模式**

```[main]\ndns=dnsmasq```

**禁用 MAC 随机化**

```[device]\nwifi.scan-rand-mac-address=no```

**设置主机名模式**

```[main]\nhostname-mode=dhcp```

# SYNOPSIS

**/etc/NetworkManager/NetworkManager.conf**

# PARAMETERS

**[main]**
> 主配置节。

**plugins**
> 系统设置插件名（keyfile 总会被追加）。

**dns**
> DNS 处理模式（default、dnsmasq、systemd-resolved、none）。

**dhcp**
> 要使用的 DHCP 客户端（internal、dhcpcd）。

**hostname-mode**
> 临时主机名的管理方式（default、dhcp、none）。

**no-auto-default**
> 不为其自动创建默认连接的设备。

**[keyfile]**
> keyfile 插件的专属设置。

**[ifupdown]**
> ifupdown 插件的设置（Debian/Ubuntu）。

**managed**
> /etc/network/interfaces 中列出的设备是否由 NetworkManager 管理（true/false）。

**[connection]**
> 连接属性的默认值。

**[device]**
> 每个设备的持久化配置。

**[logging]**
> 控制日志输出。

**level**
> 日志详细级别（OFF、ERR、WARN、INFO、DEBUG、TRACE）。

**domains**
> 按主题过滤日志消息（PLATFORM、WIFI、DHCP4、DNS、VPN 等）。

**[connectivity]**
> 可选的互联网连通性检查。

**uri**
> 用于连通性检查的 URL。

**interval**
> 检查频率，单位为秒（默认：300）。

**[global-dns]**
> 覆盖各连接设置的全局 DNS 配置。

# DESCRIPTION

**NetworkManager.conf** 是 NetworkManager 的主配置文件。它控制 DNS 处理、插件、设备管理以及各种全局设置。该文件采用 ini 风格的键值文件格式，由若干键值对小节组成。

额外的配置可以以 drop-in 文件的形式放在 /etc/NetworkManager/conf.d/ 中。

# EXAMPLE CONFIG

```ini
[main]
plugins=ifupdown,keyfile
dns=systemd-resolved

[ifupdown]
managed=false

[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.powersave=2

[logging]
level=WARN
```

# DNS MODES

```
default          - Update resolv.conf directly
dnsmasq          - Run local dnsmasq instance
systemd-resolved - Use systemd-resolved
none             - No DNS management
```

# CAVEATS

语法错误可能导致 NetworkManager 无法启动。drop-in 文件请使用 conf.d/。修改后需用 `systemctl restart NetworkManager` 重启 NetworkManager。

# SEE ALSO

[NetworkManager](/man/NetworkManager)(8), [nmcli](/man/nmcli)(1), [nmtui](/man/nmtui)(1), [nm-settings](/man/nm-settings)(5)
