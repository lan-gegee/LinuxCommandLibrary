# TAGLINE

匿名洋葱路由网络守护进程

# TLDR

启动 **Tor** 客户端

```tor```

使用指定的**配置文件**

```tor -f /etc/tor/torrc```

**校验**配置语法

```tor --verify-config```

为控制端口生成**哈希密码**

```tor --hash-password mypassword```

显示**版本**信息

```tor --version```

# SYNOPSIS

**tor** [_OPTION_ _value_]...

# DESCRIPTION

**tor** 是一种面向连接的匿名通信服务。用户通过分布式中继网络建立源路由路径，每个节点只知道与其相邻的节点，而不了解完整路径。这为网页浏览、FTP、SSH 等服务提供匿名的 TCP 流路由。

# PARAMETERS

**-h, --help**
> 显示帮助信息并退出

**-f, --torrc-file FILE**
> 指定配置文件位置

**--verify-config**
> 校验配置文件语法后退出

**--hash-password PASSWORD**
> 生成哈希后的控制端口密码

**--version**
> 显示版本信息

**--keygen**
> 为中继生成 ed25519 主身份密钥

**--list-fingerprint**
> 生成密钥并输出指纹

**--quiet**
> 启动期间只记录错误日志

# CONFIGURATION

**/etc/tor/torrc**
> 主配置文件，用于指定 SOCKS 端口、中继设置、隐藏服务、网桥配置和日志选项。

**-f** _file_
> 运行时使用其他配置文件。

# CAVEATS

默认情况下，Tor 仅作为客户端服务运行。SOCKS 协议不加密也不进行身份验证，因此将其暴露给不可信的网络可能泄露信息。配置文件使用 "OptionName OptionValue" 格式，而命令行使用 "--OptionName OptionValue" 格式。

# HISTORY

**tor** 即 "The Onion Router"（洋葱路由器），是第二代匿名网络，最初由美国海军研究实验室开发，现由 The Tor Project 维护。

# INSTALL

```apt: sudo apt install tor```

```dnf: sudo dnf install tor```

```pacman: sudo pacman -S tor```

```apk: sudo apk add tor```

```zypper: sudo zypper install tor```

```brew: brew install tor```

```nix: nix profile install nixpkgs#tor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[torsocks](/man/torsocks)(1), [torify](/man/torify)(1), [privoxy](/man/privoxy)(8)
