# TAGLINE

专用服务器，为非对称多人游戏运行无头游戏服务端

# TLDR

以**默认设置**启动服务器

```[path/to]/server_linux```

为服务器指定**自定义名称**，显示在服务器浏览器中

```[path/to]/server_linux -name '[server_name]'```

指定服务器的**连接端口**

```[path/to]/server_linux -port [27015]```

指定**最大玩家数**

```[path/to]/server_linux -limit [2..24]```

指定服务器启动时的**初始地图**

```[path/to]/server_linux -map [ns2_summit]```

用**密码**限制对服务器的访问

```[path/to]/server_linux -password [password]```

以 **webui 管理**界面启动服务器

```[path/to]/server_linux -webadmin -webport [8080]```

# SYNOPSIS

**server_linux** [_options_]

# PARAMETERS

**-name _name_**
> 服务器浏览器中显示的服务器名称

**-port _port_**
> 用于客户端连接的 UDP 端口（默认：27015）

**-limit _n_**
> 最大玩家数（2-24）

**-map _mapname_**
> 要加载的初始地图

**-password _pass_**
> 私密游戏使用的服务器密码

**-webadmin**
> 启用 Web 管理界面

**-webport _port_**
> Web 管理界面的端口

**-config _file_**
> 自定义配置文件

# DESCRIPTION

**Natural Selection 2** 专用服务器为这款非对称多人 FPS/RTS 混合游戏运行无头游戏服务端。玩家可以选择加入海军陆战队或异形阵营，由指挥官实时指挥团队战略。

Linux 服务端二进制文件（server_linux）通过 SteamCMD 或游戏的专用服务器工具提供。它管理在线对局的游戏状态、玩家连接和地图轮换。

服务器配置可以通过命令行参数或服务器目录中的配置文件完成。

# CAVEATS

需要足够的系统资源（CPU、内存、网络带宽）以保证流畅游戏。公共服务器可能需要端口转发。服务器文件必须通过 Steam 获取。性能很大程度上取决于玩家数量和地图复杂度。

# SEE ALSO

[steamcmd](/man/steamcmd)(1)
