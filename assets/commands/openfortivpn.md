# TAGLINE

用于 Fortinet 专有 PPP+TLS VPN 的开源 VPN 客户端

# TLDR

使用**用户名和密码**连接 VPN

```openfortivpn -u [username] -p [password]```

使用指定的**配置文件**连接 VPN

```sudo openfortivpn -c [path/to/config]```

通过指定**主机和端口**连接

```openfortivpn [host]:[port]```

通过**证书 SHA256 校验和**信任网关

```openfortivpn --trusted-cert [sha256_sum]```

# SYNOPSIS

**openfortivpn** [_host_:_port_] [**-u** _user_] [**-p** _pass_] [**-c** _config_] [_options_]

# PARAMETERS

**-c**, **--config=**_file_
> 配置文件（默认：/etc/openfortivpn/config）

**-u**, **--username=**_user_
> VPN 账户用户名

**-p**, **--password=**_pass_
> VPN 账户密码

**--trusted-cert=**_sha256_
> 信任具有此 SHA256 指纹的网关证书

**--user-cert=**_file_
> 用于身份验证的客户端证书文件

**--user-key=**_file_
> 客户端私钥文件

**--realm=**_realm_
> 指定身份验证域（realm）

**-o**, **--otp=**_otp_
> 双因素认证所需的一次性密码

**--otp-prompt=**_prompt_
> 用于搜索的 OTP 提示字符串

**--otp-delay=**_delay_
> 发送 OTP 前的延迟秒数

**--saml-login**[=_port_]
> 使用 SAML/SSO 身份验证

**--pinentry=**_program_
> 使用 pinentry 程序输入密码

**--persistent=**_seconds_
> 断开连接后按指定延迟重新连接

**--no-routes**
> 不将 VPN 路由添加到路由表

**--half-internet-routes**
> 添加两条 /1 路由而非默认路由

**--set-routes=**_bool_
> 配置路由（0 为禁用）

**--set-dns=**_bool_
> 配置 DNS（0 为禁用）

**--pppd-log=**_file_
> pppd 的日志文件

**--pppd-ifname=**_name_
> 设置 ppp 接口名称

**--pppd-use-peerdns=**_bool_
> 使用对端提供的 DNS 服务器

**--user-agent=**_string_
> 设置自定义 HTTP User-Agent

**-v**, **--verbose**
> 提高详细程度（可多次使用）

**-q**, **--quiet**
> 降低详细程度

# DESCRIPTION

**openfortivpn** 是一款面向 Fortinet 专有 PPP+TLS VPN 解决方案的开源 VPN 客户端，该解决方案通常称为 FortiClient SSL VPN。它通过 TLS/SSL 上的 PPP 建立安全隧道，以连接 FortiGate 设备和 FortiClient VPN 服务器。

该客户端负责处理身份验证（包括双因素认证）、证书验证和路由配置。它会为 VPN 连接创建一个 PPP 接口，并可以管理路由，让流量经由 VPN 隧道传输。

# CAVEATS

创建网络接口和修改路由表需要 root 权限。在命令行上提供的密码可能会在进程列表中可见；建议将凭据放在配置文件中。某些 Fortinet 服务器可能要求特定的受信证书指纹或 realm 设置。

# HISTORY

作为专有 FortiClient for Linux 的开源替代品而创建。其开发目的是为在企业环境中广泛使用的 FortiGate SSL VPN 服务器提供命令行方式的 VPN 连接。该项目源于对兼容 Fortinet 基础设施的轻量级、可脚本化 VPN 客户端的需求。

# INSTALL

```apt: sudo apt install openfortivpn```

```dnf: sudo dnf install openfortivpn```

```pacman: sudo pacman -S openfortivpn```

```zypper: sudo zypper install openfortivpn```

```brew: brew install openfortivpn```

```nix: nix profile install nixpkgs#openfortivpn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openvpn](/man/openvpn)(8), [pppd](/man/pppd)(8), [ip](/man/ip)(8)
