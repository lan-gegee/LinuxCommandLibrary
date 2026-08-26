# TAGLINE

可深度定制的终端文件管理器

# TLDR

**启动 xplr**

```xplr```

**在指定目录中启动**

```xplr [/path/to/dir]```

**将选中项通过管道传给命令**

```xplr | xargs [command]```

**使用配置文件启动**

```xplr --config [config.lua]```

**从标准输入读取路径**

```find . -name "*.txt" | xplr```

**输出并退出**（基于当前选中项）

```xplr --print-pwd-as-result```

# SYNOPSIS

**xplr** [_--config file_] [_--print-pwd-as-result_] [_options_] [_paths_]

# PARAMETERS

**--config** _FILE_
> 配置文件。

**--print-pwd-as-result**
> 退出时输出当前目录而不是焦点所在路径。

**-C** _NAME=VALUE_
> 覆盖配置值。

**--read-only**
> 只读模式（禁用所有写操作）。

**--vroot** _PATH_
> 设置虚拟根目录以限制浏览范围。

**-m** _MSG_
> 向 xplr 发送一条消息进行处理。

**-M** _MSG_
> 向 xplr 发送消息但不为值加引号。

**--version**, **-V**
> 显示版本信息。

**--help**, **-h**
> 显示帮助信息。

# KEY BINDINGS

**j/k** 或 **down/up**
> 导航。

**Enter**
> 打开/选择。

**q**
> 退出。

**/**
> 搜索。

**space**
> 切换选中状态。

**h**
> 返回上级目录。

**g**
> 前往指定路径。

**.**
> 切换隐藏文件显示。

**ctrl-c**
> 取消。

# DESCRIPTION

**xplr** 是一个可深度定制、极简的终端文件管理器。它用 Rust 编写，速度快且高度可配置。

Lua 配置支持完全自定义。模式、按键绑定和界面都可以被彻底重新定义。

选中项的处理结果通过管道输出到 stdout，因此可以与其他命令和脚本集成。

模式定义了一组行为。普通模式、选择模式和自定义模式提供上下文相关的按键绑定。

插件可以扩展功能。社区插件提供了预览、批量重命名和集成等特性。

它的设计理念是与 Unix 工具组合使用，而不是内置所有功能。

# CAVEATS

配置学习曲线陡峭。内置功能比 ranger 少。掌握 Lua 对自定义会有帮助。

# HISTORY

**xplr** 由 **Arijit Basu** 于 **2021 年**前后创建，是一个可扩展的文件管理器。它强调可定制性和与工具的组合能力，而非堆砌内置功能。

# INSTALL

```pacman: sudo pacman -S xplr```

```apk: sudo apk add xplr```

```zypper: sudo zypper install xplr```

```brew: brew install xplr```

```nix: nix profile install nixpkgs#xplr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [vifm](/man/vifm)(1), [nnn](/man/nnn)(1), [lf](/man/lf)(1)
