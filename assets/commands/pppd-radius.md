# TAGLINE

PPP 守护进程的 RADIUS 认证插件

# TLDR

**以 RADIUS 认证启动 PPP**

```pppd plugin radius.so```

**使用自定义 RADIUS 配置文件**

```pppd plugin radius.so radius-config-file [/etc/radiusclient/radiusclient.conf]```

**添加 RADIUS 属性-值对**

```pppd plugin radius.so avpair "[attribute=value]"```

# SYNOPSIS

**pppd** plugin radius.so [_options_]

# PARAMETERS

**plugin** radius.so
> 加载 RADIUS 插件。

**radius-config-file** _filename_
> 使用指定文件作为 radiusclient 配置文件 [default=/etc/radiusclient/radiusclient.conf]。

**avpair** _attribute=value_
> 添加一个属性-值对，随每次请求传给 RADIUS 服务器。

**map-to-ifname**
> 将 RADIUS NAS-Port 属性设置为与接口名对应的编号（默认）。

**map-to-ttyname**
> 通过 libradiusclient 库设置 RADIUS NAS-Port 属性值。

# DESCRIPTION

**pppd-radius** 是 PPP 守护进程的一个插件，用于启用 RADIUS（Remote Authentication Dial-In User Service，远程认证拨入用户服务）认证。它允许 pppd 针对 RADIUS 服务器执行 PAP、CHAP、MS-CHAP 和 MS-CHAPv2 认证，而不是使用常规的 /etc/ppp/pap-secrets 和 /etc/ppp/chap-secrets 文件。

该插件构建于 **radiusclient** 库之上，后者拥有自己的配置文件（通常位于 /etc/radiusclient）。ISP 和企业网络常用它来集中管理拨号、DSL 和 VPN 用户认证。

# CAVEATS

需要一台 RADIUS 服务器和 radiusclient 库。必须安装插件（radius.so）。配置主要通过 radiusclient 配置文件完成，而非直接通过 pppd 选项。

# HISTORY

pppd-radius 为将 **RADIUS 认证**与 PPP 集成而创建。

# INSTALL

```apt: sudo apt install ppp```

```dnf: sudo dnf install ppp```

```pacman: sudo pacman -S ppp```

```apk: sudo apk add ppp-daemon```

```zypper: sudo zypper install ppp```

```nix: nix profile install nixpkgs#ppp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppd](/man/pppd)(8), [radiusd](/man/radiusd)(8)
