# TAGLINE

自托管的媒体整理与元数据服务器

# TLDR

在默认端口（9999）上**启动** Stash 服务器

```stash```

将服务器**绑定**到指定的主机和端口

```stash --host [127.0.0.1] --port [9999]```

**使用**自定义配置文件

```stash -c [path/to/config.yml]```

**使用**自定义 CPU 剖析文件路径

```stash --cpuprofile [path/to/cpu.prof]```

**以生成的配置目录运行**

```STASH_CONFIG_FILE=[/data/config.yml] stash```

**显示**版本并退出

```stash --version```

# SYNOPSIS

**stash** [_flags_]

# PARAMETERS

**--host** _host_
> 要绑定的主机名或网络接口（默认 **0.0.0.0**）。

**--port** _port_
> 要监听的 TCP 端口（默认 **9999**）。

**-c**, **--config** _file_
> **config.yml** 文件的路径。覆盖默认位置。

**--cpuprofile** _file_
> 将 Go CPU profile 写入 _file_ 以进行性能分析。

**--nobrowser**
> 首次启动时不自动打开 Web UI。

**--version**
> 打印 Stash 版本信息并退出。

**-h**, **--help**
> 显示可用标志并退出。

# DESCRIPTION

**Stash** 是一个用 **Go** 编写的开源自托管 Web 应用程序，用于整理和提供个人媒体库服务。它为视频和图像收藏建立索引，从配置的数据源（StashDB、ThePornDB、社区爬虫）抓取元数据，并在 **http://localhost:9999** 上提供一个功能丰富的 Web UI，包含标签、演员、工作室、图库、统计信息和 GraphQL API。

**stash** 二进制文件会启动 HTTP/GraphQL 服务器，调度后台扫描（scan）、生成（generate）和识别（identify）任务，并将状态持久化到 SQLite 数据库。插件可以通过 Python、JavaScript 或 shell 脚本为服务器扩展自定义任务、爬虫和 UI 钩子。

Stash 默认是单用户的，但也支持密码保护的访问。首次运行时若不存在 **FFmpeg** 和 **FFprobe** 则会捆绑安装，转码、精灵图生成和预览都依赖它们。

# CONFIGURATION

服务器默认从 **~/.stash/config.yml** 读取配置。可以使用 **-c** _file_ 或 **STASH_CONFIG_FILE** 环境变量覆盖。命令行标志和环境变量值的优先级高于 YAML 文件。

常用选项（位于 **config.yml** 中）：

> **host** / **port** — 监听地址。
> **stash** — 要扫描的媒体库路径列表。
> **database** — SQLite 数据库路径（默认 **~/.stash/stash-go.sqlite**）。
> **generated** — 存放生成的预览和精灵图的目录。
> **cache** — 存放转码与图像缓存的目录。
> **username** / **password** — Web UI 的凭据。
> **plugins_path** / **scrapers_path** — 社区插件与爬虫的位置。

# CAVEATS

默认绑定地址为 **0.0.0.0**，会将 UI 暴露给局域网——对外暴露前请将 **host** 设为 **127.0.0.1** 或启用身份验证。Stash 由社区维护且更新频繁；升级前请备份 **config.yml** 和 SQLite 数据库。名称 **stash** 与 **git stash**（git 子命令，并非独立二进制文件）、已弃用的 **Atlassian Stash**（现 **Bitbucket Server**）以及若干较小的 CLI 重名——请确认你安装的是正确的 **stashapp/stash** 发行版。

# HISTORY

Stash 由 **WithoutPants** 于 **2018 年**发起，作为商业媒体管理器的开源替代品。项目后来迁至 **stashapp** GitHub 组织，聚集了大量插件和爬虫贡献者。它以单个静态二进制文件的形式分发，支持 **Linux**、**macOS** 和 **Windows**，并提供官方 Docker 镜像，采用 **AGPL-3.0** 许可证。

# INSTALL

```nix: nix profile install nixpkgs#stash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1)
