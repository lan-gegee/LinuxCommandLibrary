# TAGLINE

独立的以太坊账户管理器与交易签名器

# TLDR

**首次初始化 clef**，生成主种子

```clef init```

以默认设置在主网上**启动 clef**

```clef```

使用自定义密钥库在 **Sepolia 测试网上启动 clef**

```clef --chainid 11155111 --keystore [path/to/keystore]```

**使用自定义的**配置目录启动 clef

```clef --configdir [path/to/clef/config]```

**启动 clef 并启用自动的**基于规则的交易审批

```clef --rules [path/to/rules.js]```

为密钥库账户**设置密码**

```clef setpw [0xaddress]```

以 stdio 模式**启动 clef**，用于外部签名请求

```clef --stdio-ui```

**创建新账户**

```clef newaccount```

# SYNOPSIS

**clef** [_options_] [_command_]

# SUBCOMMANDS

**init**
> 初始化签名器，生成主种子并创建必要的目录。

**attest**
> 证明将使用某个 JavaScript 规则文件（存储其 sha256 哈希）。

**setpw**
> 为密钥库文件存储一个凭据。

**delpw**
> 移除密钥库文件的凭据。

**newaccount**
> 创建新账户。

**gendoc**
> 生成关于 JSON-RPC 格式的文档。

# PARAMETERS

**--keystore** _DIR_
> 密钥库目录（默认：$HOME/.ethereum/keystore）。

**--configdir** _DIR_
> Clef 配置目录（默认：$HOME/.clef）。

**--chainid** _ID_
> 用于交易签名的链 ID（默认：1）。常见取值：1=主网、11155111=sepolia。

**--rules** _FILE_
> 用于自动交易审批的 JavaScript 规则文件路径。

**--stdio-ui**
> 使用标准输入/输出作为用户界面（用于与外部工具集成）。

**--ipcpath** _PATH_
> IPC 套接字/管道的文件名。

**--ipcdisable**
> 禁用 IPC-RPC 服务器。

**--http**
> 启用 HTTP-RPC 服务器以处理远程签名请求。

**--http.addr** _ADDR_
> HTTP 服务器监听地址（默认：localhost）。

**--http.port** _PORT_
> HTTP 服务器监听端口（默认：8550）。

**--http.vhosts** _HOSTS_
> 以逗号分隔的虚拟主机名列表（默认：localhost）。

**--signersecret** _FILE_
> 包含加密主种子的文件。

**--auditlog** _FILE_
> 审计日志文件（默认：audit.log）。

**--loglevel** _LEVEL_
> 输出到屏幕的日志级别（默认：4）。

**--lightkdf**
> 以牺牲一定 KDF 强度为代价，降低密钥派生的内存和 CPU 占用。

**--advanced**
> 对高级操作发出警告而非拒绝执行。

**--suppress-bootwarn**
> 不显示启动警告。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Clef** 是 go-ethereum 项目提供的独立以太坊账户管理与签名工具。它将私钥的安全存储和交易签名能力与主以太坊客户端分离开来。

Clef 充当签名预言机，可以批准或拒绝交易签名请求。它支持硬件钱包和加密密钥库，并能以分离模式运行，由 JavaScript 规则引擎根据预定义策略自动处理签名请求。

该工具旨在通过将密钥管理与面向网络的组件隔离来增强安全性。它可以通过 IPC 或 HTTP 接口服务多个客户端，因此既适合个人使用，也适合作为大型基础设施部署的一部分。

# CAVEATS

Clef 要求妥善备份初始化时创建的主种子。种子丢失后无法恢复。在生产环境中，只有配置了适当的防火墙规则才应启用 HTTP 接口。基于规则的自动签名需要经过彻底的安全审计。

# HISTORY

Clef 由 **go-ethereum**（Geth）团队于 **2018 年**推出，是其改进以太坊账户安全性工作的一部分。它的设计目的是用一个更安全的独立签名方案取代 Geth 中集成的账户管理功能，从而减少攻击面。

# INSTALL

```apk: sudo apk add geth-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[geth](/man/geth)(1)
