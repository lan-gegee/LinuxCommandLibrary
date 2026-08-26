# TAGLINE

将 Angular 应用部署到托管服务商

# TLDR

**部署默认项目**

```ng deploy```

**部署指定项目**

```ng deploy [project-name]```

**使用构建配置进行部署**

```ng deploy --configuration production```

**跳过构建直接部署**

```ng deploy --no-build```

# SYNOPSIS

**ng deploy** [_project_] [_options_]

# PARAMETERS

_project_
> 要部署的项目。默认为工作区中的默认项目。

**--configuration** _name_
> 部署时使用的构建配置。

**--no-build**
> 跳过部署前的构建步骤。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng deploy** 构建 Angular 应用并将其部署到远程托管服务商。deploy 命令要求在项目的 **angular.json** 文件中配置部署构建器（builder），通常通过添加托管服务商软件包来完成，例如 **@angular/fire**、**@azure/ng-deploy** 或 **@netlify-builder/deploy**。

该命令首先执行构建流程，然后调用配置的构建器将输出上传到目标托管环境。

# CONFIGURATION

使用此命令前必须先通过 **ng add** 添加部署构建器：

```ng add @angular/fire```
```ng add @netlify-builder/deploy```
```ng add @azure/ng-deploy```

这会在 **angular.json** 中该项目的 architect 区段注册 deploy 目标。

# CAVEATS

需要安装并配置部署构建器软件包，否则该命令会因"没有部署目标"而失败。通常还需要向托管服务商进行身份验证。属于 Angular CLI 的一部分。

# HISTORY

**ng deploy** 于 Angular CLI **8.3 版本**（**2019 年**）加入，通过可插拔的构建器为不同托管平台提供了统一的标准化部署接口。

# SEE ALSO

[ng](/man/ng)(1), [ng-build](/man/ng-build)(1), [firebase](/man/firebase)(1)
