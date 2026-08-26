# TAGLINE

X11 授权凭据管理

# TLDR

**列出所有授权条目**

```xauth list```

**显示授权文件信息**

```xauth info```

**添加一条授权条目**

```xauth add [display_name] [protocol_name] [hex_key]```

**通过服务器生成新的授权条目**

```xauth generate [display_name] [protocol_name]```

**移除一条授权条目**

```xauth remove [display_name]```

**将当前 display 的条目提取到文件**

```xauth extract [path/to/file] $DISPLAY```

**合并来自文件的条目**

```xauth merge [path/to/file]```

**使用指定的授权文件**

```xauth -f [path/to/file] list```

# SYNOPSIS

**xauth** [_options_] [_command_ [_args_]]

# COMMANDS

**add** _DISPLAY_ _PROTOCOL_ _HEXKEY_
> 为指定的 display 添加授权条目。

**generate** _DISPLAY_ _PROTOCOL_ [_options_]
> 联系服务器生成并添加授权条目。

**remove** _DISPLAY_
> 移除匹配的授权条目。

**list** [_DISPLAY_]
> 列出授权条目（未指定 display 时列出全部）。

**nlist** [_DISPLAY_]
> 以数字格式列出条目。

**extract** _FILE_ _DISPLAY_
> 将授权条目写入文件。

**nextract** _FILE_ _DISPLAY_
> 以数字格式提取条目，便于非二进制传输。

**merge** _FILE_...
> 从文件读取并合并授权条目。

**nmerge** _FILE_...
> 合并以数字格式表示的条目。

**source** _FILE_
> 执行脚本文件中的 xauth 命令。

**info**
> 显示授权文件的相关信息。

**exit**
> 保存更改并退出。

**quit**
> 不保存更改直接退出。

**help**
> 列出可用命令。

# PARAMETERS

**-f** _FILE_
> 使用指定的授权文件而不是 ~/.Xauthority。

**-v**
> 详细模式。为操作打印状态信息。

**-q**
> 安静模式。抑制主动输出的状态信息。

**-i**
> 忽略授权文件锁。

**-b**
> 尝试解除失效的授权文件锁。

**-n**
> 不解析主机名；直接显示存储的地址。

**-V**
> 显示 xauth 版本号。

# DESCRIPTION

**xauth** 编辑和显示用于连接 X 服务器的授权信息。它管理 ~/.Xauthority 文件（或 XAUTHORITY 环境变量指定的文件），其中包含用于 X11 身份验证的凭据。

该工具常用于从一台机器提取授权记录并在另一台机器上合并，以便进行远程显示访问、通过 SSH 的 X11 转发以及 X 安全管理。

# CAVEATS

授权文件包含敏感凭据，应设置严格的权限（仅所有者可读）。SSH 的 X11 转发需要正确配置 xauth。除使用 `generate` 命令外，程序不会联系 X 服务器。

# INSTALL

```apt: sudo apt install xauth```

```apk: sudo apk add xauth```

```zypper: sudo zypper install xauth```

```brew: brew install xauth```

```nix: nix profile install nixpkgs#xauth```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xhost](/man/xhost)(1), [ssh](/man/ssh)(1), [xdpyinfo](/man/xdpyinfo)(1)
