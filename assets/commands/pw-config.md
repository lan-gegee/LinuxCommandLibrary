# TAGLINE

查看 PipeWire 配置文件与配置节

# TLDR

列出将要使用的所有**配置文件**

```pw-config```

列出 **PipeWire PulseAudio** 服务器的配置文件

```pw-config -n pipewire-pulse.conf```

列出 PipeWire PulseAudio 使用的所有配置**节**

```pw-config -n pipewire-pulse.conf list```

列出 JACK 客户端使用的 **context.properties 片段**

```pw-config -n jack.conf list context.properties```

列出 JACK 客户端使用的**合并后的 context.properties**

```pw-config -n jack.conf merge context.properties```

列出合并后的 **context.modules** 并重新格式化

```pw-config -n pipewire.conf -r merge context.modules```

# SYNOPSIS

**pw-config** [_options_] [_command_] [_section_]

# PARAMETERS

**-n**, **--name** _config_
> 指定配置文件名称

**-r**, **--recurse**
> 对嵌套结构重新格式化/递归展开

**list** [_section_]
> 列出配置片段

**merge** [_section_]
> 显示合并后的配置

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-config** 显示 PipeWire 服务器和客户端所使用的配置路径与配置节。它帮助理解 PipeWire 的拆分式配置文件是如何组合起来的，显示哪些文件对特定设置做出了贡献。

该工具可以检查不同的配置上下文（pipewire.conf、pipewire-pulse.conf、jack.conf），并显示单独的片段和合并后的结果。

# CAVEATS

配置文件会在多个位置（/etc/pipewire、~/.config/pipewire 等）搜索并按优先级合并。理解合并顺序对排查配置问题很重要。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。添加该工具是为了帮助管理员和用户理解 PipeWire 灵活的配置系统。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [wpctl](/man/wpctl)(1)
