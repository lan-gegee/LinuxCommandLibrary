# TAGLINE

以列格式视图列出 IP 路由表

# TLDR

**列出所有路由**（默认的 main 表）

```routel```

**列出指定的路由表**（按名称或 id）

```routel [main]```

**仅显示 IPv4 路由**

```routel -4```

**仅显示 IPv6 路由**

```routel -6```

**过滤出特定目的地**（额外的 ip route 参数会透传）

```routel main [10.0.0.0/8]```

**显示 local 表**

```routel [local]```

# SYNOPSIS

**routel** [_options_] [_tablenr_ [_ip-route-options_...]]

# PARAMETERS

**-4**
> `--family inet` 的简写 —— 仅 IPv4。

**-6**
> `--family inet6` 的简写 —— 仅 IPv6。

**-f**, **--family** _inet_|_inet6_
> 限定为给定的地址族。

**-h**, **--help**
> 显示帮助。

_tablenr_
> 路由表名称（例如 `main`、`local`、`default`）或数字 id。

_ip-route-options_
> 任何额外参数都会原样传递给 `ip route list`（destination、via、dev 等）。

# OUTPUT

该脚本输出以下列：

```
target            gateway           source            proto     scope     dev    tbl
```

没有值的列显示为 `-`。

# DESCRIPTION

**routel** 是 **iproute2** 附带的一个小型 shell 脚本，它封装了 `ip route list` 并把输出重新格式化为固定列，一些用户觉得这比原始的 `ip` 输出更容易阅读。任何额外参数都会转发给 `ip route list`，因此在后者可用的过滤器在这里同样适用。

还有一个姊妹脚本 `routef`，用于清空路由。两者都是轻量级辅助工具；它们能完成的事情用 `ip route` 同样可以做到。

# CAVEATS

纯粹的封装 —— 除了 `ip route list` 提供的功能之外没有任何新增特性。某些发行版将它打包在单独的 `iproute2-extras` 或类似的软件包中。在非常窄的终端中，列对齐可能显得不太美观。

# HISTORY

**routel** 最初由 **Stephen R. van den Berg** 编写，后由 **Stephen Hemminger** 作为 **iproute2** 软件包的一部分重写并维护。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip-route](/man/ip-route)(8), [ip](/man/ip)(8), [route](/man/route)(8), [netstat](/man/netstat)(8), [ss](/man/ss)(8)
