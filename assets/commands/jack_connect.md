# TAGLINE

在 JACK 端口之间创建音频连接

# TLDR

**连接输出到输入**

```jack_connect [system:capture_1] [app:input_1]```

**连接应用程序端口**

```jack_connect [app1:output] [app2:input]```

**列出所有端口**

```jack_lsp```

**连同连接关系一起列出**

```jack_lsp -c```

**断开端口连接**

```jack_disconnect [source] [destination]```

# SYNOPSIS

**jack_connect** [_options_] _source_port_ _destination_port_

# PARAMETERS

_source_port_
> 输出端口（client:port 格式）。

_destination_port_
> 输入端口（client:port 格式）。

**-s**, **--server** _servername_
> 连接到指定名称的 JACK 服务器。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**jack_connect** 在 JACK 端口之间创建音频连接。JACK（JACK Audio Connection Kit）为应用程序之间提供低延迟的音频路由。

该命令将输出端口连接到输入端口，使音频能够在应用程序之间流动。使用 **jack_lsp** 列出可用端口，使用 **jack_disconnect** 移除连接。

# CAVEATS

需要正在运行的 JACK 服务器。端口名包含客户端名称。连接不会在重启后保留。图形化管理可考虑 QjackCtl。

# HISTORY

JACK 由 **Paul Davis** 等人于 **2002 年**开始创建。它在 Linux 和 macOS 上提供专业级音频路由，在音频制作领域被广泛使用。

# INSTALL

```apt: sudo apt install jack-example-tools```

```pacman: sudo pacman -S jack-example-tools```

```zypper: sudo zypper install jack-example-tools```

```nix: nix profile install nixpkgs#jack-example-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jackd](/man/jackd)(1), [pulseaudio](/man/pulseaudio)(1), [pipewire](/man/pipewire)(1)
