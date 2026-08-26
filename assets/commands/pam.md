# TAGLINE

可插拔认证模块

# TLDR

**检查 PAM 配置**

```pam-auth-update```

**测试 PAM 认证**

```pamtester [service] [user] authenticate```

**查看 PAM 配置**

```cat /etc/pam.d/[service]```

**调试 PAM**

```pam-auth-update --package```

# SYNOPSIS

**pam** modules configured in /etc/pam.d/

# PARAMETERS

/etc/pam.d/ 中的配置文件：

**auth**
> 验证认证令牌。

**account**
> 校验账户。

**password**
> 更新密码。

**session**
> 会话建立/清理。

# DESCRIPTION

**PAM** 即可插拔认证模块（Pluggable Authentication Modules）。它是系统认证的框架。

该系统提供灵活的认证机制。按服务分别配置。

# CAVEATS

这是关键系统组件。配置不当可能把用户锁在系统外。请谨慎测试。

# HISTORY

PAM 由 **Sun Microsystems** 开发，是一个可插拔的认证框架。

# INSTALL

```dnf: sudo dnf install pam```

```pacman: sudo pacman -S pam```

```zypper: sudo zypper install pam```

```nix: nix profile install nixpkgs#pam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pam.conf](/man/pam.conf)(5), [pam.d](/man/pam.d)(5), [login](/man/login)(1)
