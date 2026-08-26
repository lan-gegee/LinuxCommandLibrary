# TAGLINE

管理加密卷映射

# TLDR

**挂载**（打开）加密卷

```systemd-cryptsetup attach [mapping_name] [/dev/sdXY]```

带**选项**挂载

```systemd-cryptsetup attach [mapping_name] [/dev/sdXY] none [crypttab_options]```

使用**密钥文件**挂载

```systemd-cryptsetup attach [mapping_name] [/dev/sdXY] [/path/to/keyfile] [options]```

**卸载**（关闭）映射

```systemd-cryptsetup detach [mapping_name]```

# SYNOPSIS

**systemd-cryptsetup** attach _VOLUME_ _DEVICE_ [_KEY_] [_OPTIONS_]

**systemd-cryptsetup** detach _VOLUME_

# DESCRIPTION

**systemd-cryptsetup** 创建或移除加密 LUKS 卷的解密映射。它相当于 systemd 版的 `cryptsetup open` 和 `cryptsetup close`。

参数格式与 `/etc/crypttab` 条目相同。该工具主要由 systemd 在内部使用，根据 crypttab 配置在启动时解锁加密设备。

# CAVEATS

通常由 systemd 自动调用，而非手动执行。映射会出现在 `/dev/mapper/<name>`。支持所有 crypttab 选项，如 luks、discard 等。

# HISTORY

**systemd-cryptsetup** 将加密卷管理整合进 systemd 的启动流程，可根据 `/etc/crypttab` 配置实现自动解锁。

# INSTALL

```apt: sudo apt install systemd-cryptsetup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [crypttab](/man/crypttab)(5), [systemd-cryptenroll](/man/systemd-cryptenroll)(1)
