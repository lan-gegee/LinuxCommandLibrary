# TAGLINE

高性能 Minecraft 服务器

# TLDR

**启动 Minecraft 服务器**

```java -jar paper.jar```

**以内存限制启动**

```java -Xms2G -Xmx4G -jar paper.jar```

**接受 EULA**

```java -jar paper.jar --accepteula```

**指定世界文件夹**

```java -jar paper.jar --world-dir [worlds]```

# SYNOPSIS

**java** **-jar** paper.jar [_options_]

# PARAMETERS

**--accepteula**
> 自动接受 EULA。

**--world-dir** _DIR_
> 世界存档目录。

**--plugins** _DIR_
> 插件目录。

**--config** _FILE_
> 配置文件。

**nogui**
> 不带图形界面启动。

# DESCRIPTION

**PaperMC** 是一个高性能 Minecraft 服务器。它是 Spigot 的分支，附带大量优化。

该服务器提供更好的性能。插件与 Bukkit/Spigot 兼容。

# CAVEATS

需要 Java。内存分配很重要。各插件的兼容性不一。

# HISTORY

PaperMC 从 **Spigot** 分支而来，目的是提升 Minecraft 服务器的性能。

# INSTALL

```nix: nix profile install nixpkgs#papermc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [screen](/man/screen)(1)
