# TAGLINE

执行 angular.json 中定义的 Architect 目标

# TLDR

**运行 Architect 目标**

```ng run [project]:[target]```

**以指定配置运行**

```ng run [project]:[target]:[configuration]```

**运行自定义构建器**

```ng run [project]:build:production```

# SYNOPSIS

**ng** **run** _project_:_target_[:_configuration_] [_options_]

# PARAMETERS

_project:target_
> 要运行的项目与 Architect 目标（例如 `my-app:build`）。

_project:target:configuration_
> 使用 angular.json 中定义的命名配置运行目标（例如 `my-app:build:production`）。

**--help**
> 显示指定目标的帮助。

**--configuration** _name_, **-c** _name_
> 要使用的命名构建器配置（第三段冒号分隔内容的替代写法）。

# DESCRIPTION

**ng run** 执行 **angular.json** 中定义的 Architect 目标。它是调用构建器的底层命令，可以运行 **ng build**、**ng serve** 或 **ng test** 等专用命令未能覆盖的自定义构建器或目标。

底层构建器所接受的任何选项都可以追加在目标名称之后。属于 Angular CLI 的一部分。

# CAVEATS

需要有效的 Angular 工作区（angular.json）。目标及其配置必须已在工作区配置中定义。

# SEE ALSO

[ng](/man/ng)(1), [ng-build](/man/ng-build)(1)
