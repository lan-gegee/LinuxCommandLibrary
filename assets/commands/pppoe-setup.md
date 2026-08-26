# TAGLINE

以交互方式配置 PPPoE 连接

# TLDR

**配置 PPPoE 连接**

```pppoe-setup```

**运行交互式设置**

```pppoe-setup```

# SYNOPSIS

**pppoe-setup** [_options_]

# PARAMETERS

交互式配置工具。

# DESCRIPTION

**pppoe-setup** 是一个交互式脚本，引导用户逐步配置 PPPoE DSL 宽带连接。它会提示输入网络接口、ISP 用户名和密码、DNS 设置以及防火墙选项。

配置保存到 **/etc/ppp/pppoe.conf** 及相关文件中，随后由 **pppoe-connect** 和 **pppoe-start** 用来建立连接。在初次设置 DSL 或更改 ISP 设置时运行一次即可。

# CAVEATS

仅支持交互式操作。会创建 /etc/ppp/pppoe.conf。

# HISTORY

pppoe-setup 为 DSL 连接提供 **交互式 PPPoE** 配置。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-connect](/man/pppoe-connect)(8), [pppoeconf](/man/pppoeconf)(8)
