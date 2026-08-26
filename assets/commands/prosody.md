# TAGLINE

轻量级 XMPP/Jabber 聊天服务器

# TLDR

**启动 Prosody**

```prosodyctl start```

**停止 Prosody**

```prosodyctl stop```

**添加用户**

```prosodyctl adduser [user@domain]```

**检查配置**

```prosodyctl check```

**显示状态**

```prosodyctl status```

# SYNOPSIS

**prosodyctl** _command_ [_options_]

# PARAMETERS

**start**
> 启动服务器。

**stop**
> 停止服务器。

**restart**
> 重启服务器。

**status**
> 显示服务器状态。

**adduser** _jid_
> 添加 XMPP 用户。

**passwd** _jid_
> 更改密码。

**deluser** _jid_
> 删除用户。

**check**
> 检查配置。

# DESCRIPTION

**Prosody** 是一个用 Lua 编写的轻量级 XMPP/Jabber 服务器。它的设计目标是易于安装和配置，同时可通过模块进行扩展。

# EXAMPLES

```bash
# Start server
prosodyctl start

# Add user
prosodyctl adduser alice@example.com

# Change password
prosodyctl passwd alice@example.com

# Check configuration
prosodyctl check config

# Check DNS records
prosodyctl check dns

# View certificates
prosodyctl check certs
```

# CONFIGURATION

```lua
-- /etc/prosody/prosody.cfg.lua
VirtualHost "example.com"
  enabled = true

admins = { "admin@example.com" }

modules_enabled = {
  "roster"; "saslauth"; "tls";
}
```

# CAVEATS

需要 Lua。配置位于 /etc/prosody/。TLS 需要证书。

# HISTORY

Prosody 由 **Matthew Wild** 自 2008 年起开发，是一个现代、轻量的 XMPP 服务器。

# INSTALL

```apt: sudo apt install prosody```

```dnf: sudo dnf install prosody```

```pacman: sudo pacman -S prosody```

```apk: sudo apk add prosody```

```zypper: sudo zypper install prosody```

```nix: nix profile install nixpkgs#prosody```

<!-- packages: 2026-07-22 -->

# SEE ALSO

