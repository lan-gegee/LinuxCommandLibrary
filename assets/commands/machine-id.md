# TAGLINE

包含唯一机器标识符的文件

# TLDR

**查看 machine ID**

```cat /etc/machine-id```

**生成新的 machine ID**

```systemd-machine-id-setup```

**检查 ID 是否存在**

```test -f /etc/machine-id && echo "exists"```

**比较 machine ID**

```diff /etc/machine-id /var/lib/dbus/machine-id```

# SYNOPSIS

**/etc/machine-id**

# DESCRIPTION

**machine-id** 是一个包含唯一机器标识符的文件，该标识符在安装或首次启动时建立。它是一个 32 字符的小写十六进制字符串，不含连字符。

systemd、D-Bus 及其他服务使用这个 ID 来唯一标识系统。它应在重启后保持稳定，但在不同机器之间必须唯一。

# FILE LOCATIONS

```
/etc/machine-id          - Primary location
/var/lib/dbus/machine-id - D-Bus symlink
```

# GENERATION

```bash
# Regenerate (for cloned systems)
rm /etc/machine-id
systemd-machine-id-setup

# Or manually
dbus-uuidgen --ensure=/etc/machine-id
```

# CAVEATS

每台机器应唯一。克隆的虚拟机需要重新生成 ID。某些软件用它进行授权。不适合当作加密密钥材料。

# HISTORY

machine-id 由 **systemd** 引入，旨在提供标准的机器标识机制，取代各种发行版各自的方案。

# SEE ALSO

[systemd-machine-id-setup](/man/systemd-machine-id-setup)(1), [hostnamectl](/man/hostnamectl)(1)
