# TAGLINE

Arch Linux 软件包管理库

# TLDR

**库——通常通过 pacman 使用**

```pacman -S [package]```

**查询本地数据库**

```pacman -Q [package]```

**同步数据库**

```pacman -Sy```

**搜索软件包**

```pacman -Ss [pattern]```

# SYNOPSIS

**libalpm** - Arch Linux 软件包管理库

# DESCRIPTION

**libalpm** 是 Arch Linux 软件包管理库。它为 pacman 及 Arch Linux 及其衍生发行版中的其他软件包管理工具提供后端功能。

该库负责软件包数据库管理、依赖解析、软件包安装/卸载以及事务处理。

# KEY FEATURES

```
- Package database management
- Dependency resolution
- Delta/incremental updates
- Signature verification
- Transaction support
- Hook system
```

# API USAGE

```c
#include <alpm.h>

alpm_handle_t *handle;
handle = alpm_initialize("/", "/var/lib/pacman/", &err);
```

# CAVEATS

属于库 API，不可直接执行。被 pacman、yay、paru 使用。API 可能随大版本更迭而变化。仅适用于 Arch 系。

# HISTORY

libalpm 由 Arch Linux 团队作为 **pacman** 的一部分开发，引入库接口是为了允许第三方前端接入。

# INSTALL

```dnf: sudo dnf install libalpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [makepkg](/man/makepkg)(8), [yay](/man/yay)(8), [paru](/man/paru)(1)
