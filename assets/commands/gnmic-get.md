# TAGLINE

从 gNMI 设备获取配置或状态

# TLDR

**获取接口配置**

```gnmic get -a [router:57400] --path [/interfaces]```

**指定编码获取**

```gnmic get -a [router:57400] --path [/system] --encoding json```

**获取多个路径**

```gnmic get -a [router:57400] --path [/interfaces] --path [/system]```

**按类型获取**

```gnmic get -a [router:57400] --path [/interfaces] --type config```

**只打印值而不打印完整路径**

```gnmic get -a [router:57400] --path [/system/name] --values-only```

**为所有路径应用公共前缀**

```gnmic get -a [router:57400] --prefix [/interfaces] --path [interface[name=eth0]]```

# SYNOPSIS

**gnmic get** [_options_]

# PARAMETERS

**-a**, **--address** _ADDRESS_
> 目标地址，属于 gnmic 的全局标志。

**--path** _PATH_
> 要检索的 YANG 路径。可重复使用以获取多个路径。

**--prefix** _PATH_
> 应用到所有 **--path** 值的公共前缀。

**--encoding** _ENC_
> 数据编码（json、json_ietf、proto、bytes、ascii）。

**--type** _TYPE_
> 要请求的数据类型：ALL、CONFIG、STATE 或 OPERATIONAL。默认为 ALL。

**--model** _NAME_
> 要包含在请求中的 YANG 模型名称。

**--target** _NAME_
> 写入 gNMI 前缀中的目标名称，用于网关/代理场景。

**--values-only**
> 只打印返回的值，省略完整的路径结构。

**--depth** _N_
> gNMI 扩展的深度值，限制结果返回的层级深度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnmic get** 从支持 gNMI 的设备检索配置或状态数据。它按指定的 YANG 路径获取数据，并以请求的编码返回。

该命令支持多个路径、多种编码以及数据类型过滤。在网络自动化工作流中用于配置检索和状态检查。

# CAVEATS

路径必须是有效的 YANG 路径。设备必须支持所请求的编码。大数据集可能超时。

# HISTORY

gnmic get 是 **gnmic** 的子命令，后者是由 Nokia 创建的 gNMI 客户端。

# INSTALL

```brew: brew install gnmic```

```nix: nix profile install nixpkgs#gnmic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnmic](/man/gnmic)(1), [gnmic-set](/man/gnmic-set)(1), [gnmic-subscribe](/man/gnmic-subscribe)(1)

# RESOURCES

```[Documentation](https://gnmic.openconfig.net/cmd/get/)```

```[Source code](https://github.com/openconfig/gnmic)```

<!-- verified: 2026-07-17 -->
