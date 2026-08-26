# TAGLINE

用于与 JFrog 平台服务交互的 JFrog CLI

# TLDR

**配置 Artifactory**

```jf config add```

**上传制品**

```jf rt u [file.jar] [repo/path/]```

**下载制品**

```jf rt dl [repo/path/file.jar]```

**搜索制品**

```jf rt s [repo/] --include-dirs```

**发布构建信息**

```jf rt bp [build-name] [build-number]```

**Docker 推送**

```jf docker push [image:tag] [repo]```

对构建**执行 Xray 扫描**

```jf xr scan --watches "[watch_name]"```

**显示服务器配置**

```jf config show```

# SYNOPSIS

**jf** _command_ [_options_]

# PARAMETERS

**config** _CMD_
> 配置服务器连接。

**rt** _CMD_
> Artifactory 命令。

**docker** _CMD_
> Docker registry 命令。

**npm** _CMD_
> npm registry 命令。

**pip** _CMD_
> Python registry 命令。

**xr** _CMD_
> Xray 安全扫描命令。

**go** _CMD_
> Go registry 命令。

**--server-id** _ID_
> 已配置服务器的 Server ID。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jf** 是与 JFrog 平台服务交互的 JFrog CLI，涵盖 Artifactory、Xray、Distribution 和 Pipelines。它管理制品的上传/下载、构建信息收集、安全扫描以及 CI/CD 集成。

该工具支持所有主流软件包类型（Maven、npm、Docker、Go、Python、NuGet 等），并提供交互式和适合自动化的两种接口。`rt` 子命令前缀专门针对 Artifactory 操作。

# CAVEATS

是 jfrog CLI 的别名。需要先配置服务器。企业版功能可能需要许可证。

# HISTORY

jf 是 **JFrog CLI** 的简短别名，旨在简化 JFrog 平台服务的命令行使用。

# INSTALL

```nix: nix profile install nixpkgs#jf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jfrog](/man/jfrog)(1), [docker](/man/docker)(1), [npm](/man/npm)(1), [mvn](/man/mvn)(1)
