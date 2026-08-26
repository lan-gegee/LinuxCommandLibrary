# TAGLINE

支持会话的 CLI 密码管理器

# TLDR

向数据库**添加新条目**

```kure add```

**列出所有条目**

```kure ls```

将密码**复制到剪贴板**

```kure copy [entry_name]```

**生成随机密码**

```kure gen```

**开启会话**，以便运行多个命令时无需重新输入主密码

```kure session```

**导出数据库**

```kure export```

# SYNOPSIS

**kure** _command_ [_options_]

# DESCRIPTION

**kure** 是一款注重安全与隐私的 CLI 密码管理器，力求将攻击面降到最小。它完全离线工作，没有任何第三方连接。每条记录均使用 **AES-GCM 256 位**加密，并通过 **Argon2id** 派生唯一密码。

主密码从不存储在磁盘上——它会被加密后临时保存在受保护的内存缓冲区中，用完立即销毁。借助会话，只需输入一次主密码即可运行多个命令，超时时间和自定义脚本均可配置。

# CAVEATS

完全离线——没有内置的跨设备同步功能。数据库文件必须在各系统之间手动传输。一旦丢失主密码，存储的数据将永久无法找回。

# HISTORY

**kure** 由 **GGP1** 创建，使用 **Go** 编写，支持 Linux、macOS、BSD、Windows 和移动平台。

# INSTALL

```aur: yay -S kure```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [gopass](/man/gopass)(1)
