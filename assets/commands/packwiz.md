# TAGLINE

管理 Minecraft 整合包

# TLDR

**初始化整合包**

```packwiz init```

**从 CurseForge 添加模组**

```packwiz curseforge add [mod-name]```

**从 Modrinth 添加模组**

```packwiz modrinth add [mod-name]```

**更新所有模组**

```packwiz update --all```

**导出为 CurseForge 格式**

```packwiz curseforge export```

**刷新整合包索引**

```packwiz refresh```

# SYNOPSIS

**packwiz** _command_ [_options_]

# PARAMETERS

**init**
> 初始化新的整合包。

**curseforge**
> CurseForge 相关操作。

**modrinth**
> Modrinth 相关操作。

**update**
> 更新模组。

**refresh**
> 刷新整合包索引。

**serve**
> 启动 HTTP 服务器。

**--all**
> 应用于所有模组。

# DESCRIPTION

**packwiz** 管理 Minecraft 整合包。它处理模组的依赖和更新。

通过命令行创建整合包，无需图形界面。

支持 CurseForge 和 Modrinth，可从两个平台下载模组。

基于 TOML 的整合包格式，配置易于阅读。

# CAVEATS

Minecraft 专用工具。Minecraft 需要 Java。各模组的兼容性不一。

# HISTORY

**packwiz** 的创建目的是利用基于文本的工作流简化 Minecraft 整合包的开发与分发。

# INSTALL

```nix: nix profile install nixpkgs#packwiz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [curl](/man/curl)(1)
