# TAGLINE

gNMI 网络管理 CLI 客户端

# TLDR

**获取配置**

```gnmic -a [router:57400] get --path [/interfaces]```

**设置值**

```gnmic -a [router:57400] set --update-path [/interface/name] --update-value "[eth0]"```

**订阅遥测数据**

```gnmic -a [router:57400] subscribe --path [/interfaces/interface/statistics]```

**列出能力**

```gnmic -a [router:57400] capabilities```

# SYNOPSIS

**gnmic** [_global-flags_] _command_ [_command-flags_]

# PARAMETERS

**capabilities**
> 查询目标的 gNMI 能力。

**get**
> 获取配置/状态。

**set**
> 设置配置。

**subscribe**
> 订阅遥测数据。

**path**
> 从已加载的模型生成或搜索 YANG 路径。

**prompt**
> 支持路径自动补全的交互模式。

**diff**
> 比较 gNMI GetResponse 或配置状态。

**version**
> 显示 gnmic 版本。

**-a**, **--address** _TARGET_
> 一个或多个目标的地址，逗号分隔，格式为 host:port。

**-u**, **--username** _USER_
> 身份验证用户名。

**-p**, **--password** _PASS_
> 身份验证密码。

**--path** _PATH_
> YANG/gNMI 路径。

**-e**, **--encoding** _ENCODING_
> 数据编码：json、json_ietf、bytes、proto、ascii 或 config。

**--insecure**
> 禁用与目标连接的 TLS。

**--skip-verify**
> 跳过对目标 TLS 证书的验证。

**--tls-ca** _FILE_
> TLS CA 证书文件。

**--tls-cert** _FILE_
> TLS 客户端证书文件。

**--tls-key** _FILE_
> TLS 客户端私钥文件。

**--timeout** _DURATION_
> gRPC 超时时间，超过后请求被取消（默认 10s）。

**--config** _FILE_
> 配置文件（默认查找 .gnmic.yaml）。

**--log**
> 启用向 stderr 的日志输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnmic** 是一个 gNMI（gRPC Network Management Interface）CLI 客户端。它与支持 gNMI 的网络设备交互，实现配置检索、修改和流式遥测采集。

该工具支持 get、set、subscribe 和 capabilities 操作。用于配合现代网络操作系统的网络自动化和监控。

# CONFIGURATION

**~/.gnmic.yaml**
> 全局配置文件，保存目标、凭据和默认设置。

**.gnmic.yaml**
> 各目录下的配置文件，用于项目特定的设置。

# CAVEATS

目标设备必须支持 gNMI。可能需要身份验证。了解 YANG 模型会有帮助。

# HISTORY

gnmic 由 **Nokia** 创建，旨在为网络自动化和遥测采集提供一个灵活的 gNMI 客户端。

# INSTALL

```brew: brew install gnmic```

```nix: nix profile install nixpkgs#gnmic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnmic-get](/man/gnmic-get)(1), [gnmic-set](/man/gnmic-set)(1), [gnmic-subscribe](/man/gnmic-subscribe)(1)

# RESOURCES

```[Source code](https://github.com/openconfig/gnmic)```

```[Documentation](https://gnmic.openconfig.net/)```

<!-- verified: 2026-07-17 -->
