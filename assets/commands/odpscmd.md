# TAGLINE

maxCompute 控制台

# TLDR

**启动交互式控制台**

```odpscmd```

**执行 SQL**

```odpscmd -e "[SELECT * FROM table]"```

**运行脚本文件**

```odpscmd -f [script.sql]```

**使用特定项目**

```odpscmd --project [project_name]```

# SYNOPSIS

**odpscmd** [_options_]

# PARAMETERS

**-e** _SQL_
> 执行 SQL 语句。

**-f** _FILE_
> 执行脚本文件。

**--project** _NAME_
> 指定项目。

**--endpoint** _URL_
> 服务端点。

**-u** _CONFIG_
> 用户配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odpscmd** 即 MaxCompute 控制台。它是面向阿里云大数据服务的交互式 CLI。

该工具提供 SQL 执行和管理功能，是基于 Java 的客户端。

# CAVEATS

需要 Java。属于旧版工具名。较新的 CLI 请使用 odps。

# HISTORY

odpscmd 是阿里云数据处理最早的 **MaxCompute CLI**。

# INSTALL

```aur: yay -S odpscmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[odps](/man/odps)(1), [odpscmd-tunnel](/man/odpscmd-tunnel)(1)
