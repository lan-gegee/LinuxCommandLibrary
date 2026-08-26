# TAGLINE

Factorio 无头多人游戏服务器

# TLDR

**创建**新的存档文件

```[path/to]/factorio --create [path/to/save_file.zip]```

**启动** Factorio 服务器

```[path/to]/factorio --start-server [path/to/save_file.zip]```

使用设置启动服务器

```[path/to]/factorio --start-server [path/to/save_file.zip] --server-settings [path/to/server-settings.json]```

使用**指定地图设置**创建存档

```[path/to]/factorio --create [path/to/save.zip] --map-gen-settings [path/to/map_gen_settings.json] --map-settings [path/to/map_settings.json]```

优雅地**关闭**服务器（交互模式）

```/quit```

显示**帮助**

```[path/to]/factorio [-h|--help]```

# SYNOPSIS

**factorio** [_options_]

# DESCRIPTION

**factorio** 以无头服务器模式运行 Factorio 游戏以支持多人游戏。它无需图形界面即可创建和托管游戏世界。

用于专用 Factorio 服务器和自动化测试。

# PARAMETERS

**--create** _file_
> 创建新的存档文件

**--start-server** _file_
> 使用存档文件启动服务器

**--map-gen-settings** _file_
> 地图生成设置 JSON

**--map-settings** _file_
> 地图设置 JSON

**-h, --help**
> 显示帮助信息

**--port** _number_
> 服务器端口号（默认：34197）。

**--server-settings** _file_
> 服务器配置 JSON 文件（名称、描述、可见性、密码）。

**--server-adminlist** _file_
> 列出管理员用户名的 JSON 文件。

**--server-banlist** _file_
> 列出被封禁用户名的 JSON 文件。

**--console-log** _file_
> 将服务器控制台输出写入日志文件。

**--mod-directory** _dir_
> 覆盖 mod 目录路径。

# CAVEATS

需要安装 Factorio 游戏。服务器设置通过 JSON 文件配置。无头模式不需要 X 服务器。商业游戏，需单独购买许可。默认端口为 34197/UDP。

# INSTALL

```nix: nix profile install nixpkgs#factorio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1)
