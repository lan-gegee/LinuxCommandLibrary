# TAGLINE

Linux 平台的 GlobalProtect VPN 客户端

# TLDR

使用门户服务器**连接** GlobalProtect VPN

```gpclient connect [vpn_gateway_url]```

与当前连接的 VPN 服务器**断开连接**

```gpclient disconnect```

启动用于 VPN 管理的**图形用户界面**

```gpclient launch-gui```

生成 **HIP 报告**（主机完整性保护）

```gpclient hip```

使用 **OpenSSL 变通方案**绕过旧式重协商错误

```gpclient connect --fix-openssl [vpn_gateway_url]```

连接期间**忽略 TLS 错误**

```gpclient connect --ignore-tls-errors [vpn_gateway_url]```

显示**版本**

```gpclient --version```

显示任意命令的**帮助**

```gpclient help [command]```

# SYNOPSIS

**gpclient** _command_ [_options_]

# PARAMETERS

**connect** _URL_
> 连接到 GlobalProtect VPN 网关

**disconnect**
> 断开当前 VPN 会话

**launch-gui**
> 打开图形界面

**hip**
> 生成 HIP（主机完整性保护）报告

**--fix-openssl**
> 应用针对 OpenSSL 旧式重协商问题的变通方案

**--ignore-tls-errors**
> 跳过 TLS 证书验证

**-g**, **--gateway** _URL_
> 直接连接到此网关而不进行提示

**--auto-gateway**
> 按优先级顺序自动尝试各网关，无需提示

**-u**, **--user** _USERNAME_
> 指定用于身份验证的用户名

**--browser** [_BROWSER_]
> 使用外部浏览器进行 SSO 身份验证（chrome、firefox、default 或 remote）

**--as-gateway**
> 将服务器参数视为网关而不是门户

# DESCRIPTION

**gpclient** 是 Palo Alto Networks GlobalProtect VPN 的 Linux 客户端，构建于 OpenConnect 之上。它同时提供命令行和图形界面，用于连接使用 GlobalProtect 的企业 VPN 网关。

该客户端支持 SAML 身份验证、双因素身份验证，以及门户和网关两种连接方式。它是官方 GlobalProtect 客户端的开源替代品，后者对 Linux 的支持十分有限。

# CAVEATS

需要支持 GlobalProtect 的 OpenConnect。某些身份验证方式（如硬件令牌）的支持可能有限。**--ignore-tls-errors** 选项仅应用于测试，因为它绕过了安全机制。

# HISTORY

**gpclient** 是 **GlobalProtect-openconnect** 项目的一部分，该项目是为需要连接 GlobalProtect VPN 的 Linux 用户打造的开源方案。它利用了 OpenConnect 对 GlobalProtect 协议的支持（OpenConnect 8.0 中加入）。在 2.x 系列中，项目从 Python/Qt 重写为 **Rust** 和 **Tauri**。

# INSTALL

```nix: nix profile install nixpkgs#gpclient```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openconnect](/man/openconnect)(8), [openvpn](/man/openvpn)(8), [nmcli](/man/nmcli)(1)

# RESOURCES

```[Source code](https://github.com/yuezk/GlobalProtect-openconnect)```

<!-- verified: 2026-07-17 -->
