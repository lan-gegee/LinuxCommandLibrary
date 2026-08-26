# TAGLINE

管理 Cradle 框架软件包

# TLDR

**创建软件包**

```cradle package create [package_name]```

**列出软件包**

```cradle package list```

**更新软件包**

```cradle package update [package_name]```

# SYNOPSIS

**cradle** **package** _command_ [_options_]

# DESCRIPTION

**cradle package** 管理 Cradle PHP 框架中的软件包。它负责 Cradle 模块和扩展的软件包创建、列出与更新。

该命令提供软件包的开发与维护能力。创建软件包会为新模块生成所需的目录结构和配置文件。列出操作会显示所有已安装的软件包及版本信息。更新软件包会在遵守依赖约束的前提下获取最新版本。

Cradle 软件包是模块化组件，可以在多个应用之间共享，也可以发布供社区使用。软件包体系让 Cradle 应用得以实现代码复用与关注点分离。

# SEE ALSO

[cradle](/man/cradle)(1), [cradle-install](/man/cradle-install)(1)

# RESOURCES

```[Source code](https://github.com/CradlePHP/cradle)```

```[Homepage](https://cradlephp.github.io/)```

<!-- verified: 2026-06-23 -->
