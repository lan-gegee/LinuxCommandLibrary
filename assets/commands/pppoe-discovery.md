# TAGLINE

发现 PPPoE 接入集中器

# TLDR

**发现 PPPoE 服务器**

```pppoe-discovery -I [eth0]```

**详细模式的发现**

```pppoe-discovery -I [eth0] -V```

**指定服务名**

```pppoe-discovery -I [eth0] -S [service]```

# SYNOPSIS

**pppoe-discovery** [_options_]

# PARAMETERS

**-I** _INTERFACE_
> 网络接口。

**-V**
> 详细输出。

**-S** _NAME_
> 服务名过滤器。

**-A** _NAME_
> AC 名称过滤器。

# DESCRIPTION

**pppoe-discovery** 在网络接口上发送 PPPoE 主动发现发起（PADI）包，以查找可用的 PPPoE 接入集中器。它会报告所有响应的集中器的名称及其提供的服务，而不会实际建立连接。

这个诊断工具可用于在尝试完整 PPPoE 连接之前，验证 DSL 调制解调器或网络是否配置正确、ISP 的接入集中器是否可达。

# CAVEATS

只做发现，不建立连接。要求接口已启用。

# HISTORY

pppoe-discovery 提供 **PPPoE 服务器发现**功能。

# INSTALL

```apt: sudo apt install ppp```

```dnf: sudo dnf install ppp```

```pacman: sudo pacman -S ppp```

```apk: sudo apk add ppp-pppoe```

```zypper: sudo zypper install ppp```

```nix: nix profile install nixpkgs#ppp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-connect](/man/pppoe-connect)(8)
