# TAGLINE

启动 Minecraft 游戏

# TLDR

**启动 Minecraft**

```minecraft-launcher```

**运行服务器**

```java -Xmx[2G] -jar [server.jar] nogui```

**指定版本**

```minecraft-launcher --version [1.20]```

**指定游戏目录**

```minecraft-launcher --gameDir [/path/to/minecraft]```

**试玩模式**

```minecraft-launcher --demo```

# SYNOPSIS

**minecraft-launcher** [_options_]

# PARAMETERS

**--version** _VER_
> 游戏版本。

**--gameDir** _DIR_
> 游戏目录。

**--demo**
> 试玩模式。

**--server** _HOST_
> 自动连接到服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**minecraft** 启动 Minecraft 游戏。启动器管理版本和配置档案。

该工具下载游戏文件并管理 Java 运行时。支持模组和自定义配置。

# CAVEATS

需要购买。服务器需要 Java。下载体积较大。

# HISTORY

Minecraft 由 **Markus "Notch" Persson** 于 2009 年创建，现由 Mojang Studios（微软）开发。

# SEE ALSO

[java](/man/java)(1), [mcli](/man/mcli)(1)
