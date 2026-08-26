# TAGLINE

利用社会工程学的 WiFi 安全审计工具

# TLDR

**启动 Fluxion**

```fluxion```

**以指定语言运行**

```fluxion -l [en]```

**从会话恢复**

```fluxion --restore```

**执行特定攻击**

```fluxion -a [handshake]```

# SYNOPSIS

**fluxion** [_options_]

# PARAMETERS

**-l** _LANGUAGE_
> 界面语言。

**-a** _ATTACK_
> 要发起的攻击类型。

**--restore**
> 恢复之前的会话。

**-d**, **--debug**
> 启用调试模式。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**Fluxion** 是一款通过社会工程学攻击测试 WiFi 网络安全的安全审计工具。它会创建虚假接入点来捕获 WPA/WPA2 凭据。

该工具结合了无线扫描、去认证和强制门户技术。它向受害者展示伪造的登录页面来捕获密码，并用捕获的握手包进行验证。

Fluxion 将复杂的无线攻击流程自动化为菜单驱动的界面。

# CAVEATS

**仅限授权测试。**需要兼容的无线硬件。未经许可使用属于违法行为。存在相应的检测手段。

# HISTORY

Fluxion 由早期的 WiFi 审计工具演化而来，提供了一个通过社会工程途径对无线网络进行安全测试的自动化框架。

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [wifite](/man/wifite)(1), [hostapd](/man/hostapd)(1)

# RESOURCES

```[Source code](https://github.com/FluxionNetwork/fluxion)```

<!-- verified: 2026-07-15 -->
