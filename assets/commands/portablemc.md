# TAGLINE

跨平台命令行 Minecraft 启动器

# TLDR

**启动**最新发行版

```portablemc start```

**启动**特定版本

```portablemc start [1.16.5]```

**搜索**可用版本

```portablemc search```

**搜索**发行渠道并限制结果数量

```portablemc search --channel release -l[10]```

以用户名**离线启动**

```portablemc start -u [MyUsername]```

使用 Microsoft 账户**登录**

```portablemc auth login```

**列出**已认证的账户

```portablemc auth list```

**使用已认证账户**启动

```portablemc start -u [username] -a```

# SYNOPSIS

**portablemc** *command* [*options*] [*args*]

# DESCRIPTION

**portablemc** 是一款跨平台命令行工具，用于快速、可靠地安装和启动 Minecraft。它支持 Mojang 官方版本，并无缝安装流行的模组加载器，包括 Forge、NeoForge、Fabric、Quilt、LegacyFabric 和 Babric。

它可以离线运行或使用 Microsoft 账户运行，浏览受支持的版本，并行下载游戏文件，定位兼容的系统 Java 运行时（必要时回退到 Mojang 提供的运行时），并应用已知的启动修复。它还提供输出详细程度控制和机器可读模式，便于编写脚本。

可通过发行版二进制文件、**cargo install portablemc-cli**、AUR 软件包（**portablemc** / **portablemc-bin**）或 nixpkgs 安装。

# PARAMETERS

**start** [*version*]

> 安装（如需要）并启动某个游戏版本。**\-u** 设置用户名；**\-a** 使用已认证的账户。JVM、目录和加载器选项见 **portablemc start --help**。

**search**

> 列出或搜索受支持的版本。**--channel** 用于过滤（例如 **release**）；**-l** 限制结果数量。

**auth login**

> 认证 Microsoft 账户以便在线游玩。

**auth list**

> 列出已存储的已认证账户。

完整的标志集请使用 **portablemc --help** 和各子命令的 **--help** 查看你所安装版本的说明。

# CAVEATS

在线游玩需要有效的 Microsoft 账户流程。部分不受支持的架构可能需要额外的标志。模组加载器的安装取决于上游加载器的可用性。首次下载需要联网。

# INSTALL

```nix: nix profile install nixpkgs#portablemc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [minecraft](/man/minecraft)(1)

# RESOURCES

```[Source code](https://github.com/theorzr/portablemc)```

```[Documentation](https://docs.rs/portablemc/latest/portablemc)```

<!-- verified: 2026-07-19 -->
