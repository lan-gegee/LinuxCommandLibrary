# TAGLINE

支持多厂商的 Python SSH 库，简化与网络设备的命令行交互

# TLDR

**连接并发送命令（Python）**

```from netmiko import ConnectHandler; net_connect = ConnectHandler(**device); print(net_connect.send_command("show ip int brief"))```

**发送配置命令**

```net_connect.send_config_set(["interface gi0/1", "description WAN"])```

**保存配置**

```net_connect.save_config()```

**进入特权模式**

```net_connect.enable()```

# SYNOPSIS

**netmiko** - 用于通过 SSH 连接网络设备的 Python 库

# DESCRIPTION

**Netmiko** 是一个支持多厂商的 Python SSH 库，可简化与网络设备的命令行交互。它负责处理连接建立、权限提升和输出解析。

Netmiko 支持 Cisco、Juniper、Arista、HP 等众多厂商的设备。

# EXAMPLE

```python
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version")
net_connect.disconnect()
```

# SUPPORTED PLATFORMS

```
cisco_ios, cisco_xe, cisco_nxos
juniper_junos, arista_eos
hp_procurve, fortinet
linux, generic_termserver
```

# CAVEATS

设备上必须启用 SSH。某些设备需要特殊处理。默认为阻塞式操作。

# HISTORY

Netmiko 由 **Kirk Byers** 于 **2014 年**创建，旨在简化基于 Python 的 SSH 网络自动化。

# SEE ALSO

[napalm](/man/napalm)(1), [ansible](/man/ansible)(1), [ssh](/man/ssh)(1)
