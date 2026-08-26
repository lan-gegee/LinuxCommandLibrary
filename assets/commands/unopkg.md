# TAGLINE

LibreOffice 扩展包管理器

# TLDR

**添加**扩展

```unopkg add [path/to/extension]```

**移除**扩展

```unopkg remove [extension_id]```

**列出**扩展

```unopkg list```

打开 **GUI** 对话框

```unopkg gui```

**重新安装**所有扩展

```unopkg reinstall```

# SYNOPSIS

**unopkg** _COMMAND_ [_OPTIONS_] [_EXTENSION_]

# COMMANDS

**add**
> 添加并部署一个扩展

**remove**
> 移除一个扩展

**list**
> 列出已部署的扩展

**gui**
> 打开扩展对话框

**reinstall**
> 重新安装所有已部署的扩展

# PARAMETERS

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**unopkg** 是 LibreOffice 的扩展管理器。它允许从命令行安装、移除和管理扩展。扩展可以为 LibreOffice 应用程序添加功能。

扩展可以从 LibreOffice 官方扩展网站下载，并使用该工具安装。

# CAVEATS

某些扩展需要重启 LibreOffice。移除时需要扩展 ID。GUI 模式需要有显示服务器。

# INSTALL

```apk: sudo apk add libreoffice-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libreoffice](/man/libreoffice)(1)
