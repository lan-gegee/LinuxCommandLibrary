# TAGLINE

显示可用的数据库配置选项

# TLDR

**列出数据库引擎选项**

```doctl databases options engines```

**列出可用区域**

```doctl databases options regions```

**列出可用规格**

```doctl databases options slugs```

**列出可用版本**

```doctl databases options versions [engine]```

# SYNOPSIS

**doctl** **databases** **options** _command_

# SUBCOMMANDS

**engines**
> 列出可用的数据库引擎。

**regions**
> 列出可用的区域。

**slugs**
> 列出可用的规格。

**versions**
> 列出指定引擎的可用版本。

# DESCRIPTION

**doctl databases options** 显示 DigitalOcean 托管数据库的可用配置选项，包括支持的引擎、区域和规格。该命令帮助用户在创建或修改数据库集群时确定有效取值。

该工具查询 DigitalOcean 的 API，提供关于受支持数据库引擎（PostgreSQL、MySQL、Redis、MongoDB）、可部署数据库的地理区域，以及可用实例规格（slug）及其配置的最新信息。版本信息帮助用户根据兼容性要求选择合适的引擎版本。

这些信息对于规划数据库部署以及确保配置符合 DigitalOcean 当前提供的服务至关重要。选项可能因区域而异，并会随 DigitalOcean 更新其托管数据库服务而变化。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1)
