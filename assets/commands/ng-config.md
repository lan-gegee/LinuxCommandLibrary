# TAGLINE

获取或设置 Angular CLI 配置值

# TLDR

**读取配置值**

```ng config [jsonPath]```

**设置配置值**

```ng config [jsonPath] [value]```

**读取 schematic 集合**

```ng config cli.schematicCollections```

**设置默认包管理器**

```ng config cli.packageManager [npm|yarn|pnpm]```

**读取全局配置值**

```ng config --global [jsonPath]```

**显示全部项目配置**

```ng config```

# SYNOPSIS

**ng config** [_jsonPath_] [_value_] [_options_]

# PARAMETERS

_jsonPath_
> 使用点号表示法访问配置值的 JSON 路径（例如 **projects.myApp.architect.build**）。

_value_
> 要写入指定 JSON 路径的新值。如果省略，则打印当前值。

**--global**, **-g**
> 访问全局 Angular CLI 配置，而非项目级的 angular.json。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng config** 读写 Angular 工作区配置文件（**angular.json**）中的值。配置值通过 JSON 路径点号表示法访问。仅提供路径时显示当前值；同时提供值时则更新配置。

该命令适用于脚本化 Angular 工作区设置，以及检查或修改构建配置、默认 schematic 和 CLI 行为。

# CAVEATS

属于 Angular CLI。配置文件必须是合法的 JSON。无效的 JSON 路径会报错。对 angular.json 的更改会影响参与该项目的所有开发者。

# HISTORY

**ng config** 于 **2018 年**随 **Angular CLI 6** 推出，是工作区配置体系重构的一部分——此次重构以 **angular.json** 取代了 **.angular-cli.json**。

# SEE ALSO

[ng](/man/ng)(1), [ng-new](/man/ng-new)(1), [ng-build](/man/ng-build)(1)
