# TAGLINE

以脚本友好的格式获取网络接口信息

# TLDR

**获取 IP 地址**

```ifdata -pa [eth0]```

**获取子网掩码**

```ifdata -pn [eth0]```

**获取广播地址**

```ifdata -pb [eth0]```

**获取 MAC 地址**

```ifdata -ph [eth0]```

**获取 MTU**

```ifdata -pm [eth0]```

**检查接口是否存在**

```ifdata -e [eth0]```

**获取网络地址**

```ifdata -pN [eth0]```

# SYNOPSIS

**ifdata** [_options_] _interface_

# PARAMETERS

**-e**
> 测试接口是否存在（通过退出码）。

**-pa**
> 打印 IP 地址。

**-pn**
> 打印子网掩码。

**-pN**
> 打印网络地址。

**-pb**
> 打印广播地址。

**-pm**
> 打印 MTU。

**-ph**
> 打印硬件（MAC）地址。

**-pf**
> 打印标志。

# DESCRIPTION

**ifdata** 以脚本友好的格式获取网络接口信息，属于 moreutils 软件包。与 ifconfig 或 ip 不同，它直接返回单一干净的值，无需解析。退出码可用于脚本中的条件判断，表示成功/失败。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(1), [ifconfig](/man/ifconfig)(1)

