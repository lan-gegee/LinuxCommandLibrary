# TAGLINE

支持 NTLM/NTLMv2 认证的 HTTP 代理

# TLDR

**使用配置文件启动**

```cntlm -c [/etc/cntlm.conf]```

**以前台调试模式运行**

```cntlm -v -f```

**检测 NTLM 设置**

```cntlm -M http://test.com```

**生成密码哈希**

```cntlm -H -d [DOMAIN] -u [username]```

**启动 SOCKS5 代理**

```cntlm -O [1080]```

**指定代理与凭证**

```cntlm -u [user] -d [DOMAIN] -p [pass] [proxy:port]```

# SYNOPSIS

**cntlm** [_options_] [_proxy_host_:]_proxy_port_...

# DESCRIPTION

**cntlm** 是一个支持 NTLM/NTLMv2 认证的 HTTP 代理，位于应用程序与公司代理服务器之间。它以透明方式处理 NTLM 认证握手，因此应用程序只需使用简单的无认证代理连接即可。

该代理会缓存已认证的连接以便复用，相比每次请求都重新认证的替代方案能显著提升速度。它支持 NTLM、NTLMv2、NTLM2SR 和基本认证方式，并可通过 **-M** 标志自动检测所支持的最强认证方式。

除 HTTP 代理之外，cntlm 还提供 SOCKS5 代理支持和经由公司代理的 TCP/IP 隧道，使 HTTP 以外的协议也能穿越代理基础设施。可以存储密码哈希而非明文密码，以提高安全性。

# PARAMETERS

**-u** _user_
> 代理用户名

**-d** _domain_
> 代理域

**-p** _password_
> 代理密码

**-a** _auth_
> 认证类型：NTLMv2、NTLM2SR、NT、NTLM、LM

**-M** _url_
> Magic NTLM 检测模式

**-H**
> 生成密码哈希

**-c** _file_
> 配置文件

**-l** _[addr:]port_
> 在指定端口监听

**-O** _[addr:]port_
> 启用 SOCKS5 代理

**-N** _pattern_
> 不走代理的模式列表

**-f**
> 以前台模式运行

**-v**
> 详细/调试模式

**-g**
> 允许网关模式（非本地连接）

**-P** _pidfile_
> 创建 PID 文件

# CONFIGURATION

**/etc/cntlm.conf**
> 主配置文件，用于设置代理地址、凭证、监听端口和认证设置。

# AUTH TYPES

**NTLMv2**: 最强，推荐使用

**NTLM2SR**: 较强

**NTLM**: 旧版兼容

**LM**: 最弱，仅限旧服务器

# CAVEATS

使用 -M 自动检测可用的最强认证方式。存储密码哈希而非明文。配置文件语法与 OpenSSH 相同。

# INSTALL

```apt: sudo apt install cntlm```

```dnf: sudo dnf install cntlm```

```apk: sudo apk add cntlm```

```zypper: sudo zypper install cntlm```

```brew: brew install cntlm```

```nix: nix profile install nixpkgs#cntlm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squid](/man/squid)(8), [privoxy](/man/privoxy)(1), [tinyproxy](/man/tinyproxy)(8)

# RESOURCES

```[Homepage](https://cntlm.sourceforge.net/)```

<!-- verified: 2026-06-22 -->
