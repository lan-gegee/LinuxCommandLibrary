# TAGLINE

Go 应用的热重载开发服务器

# TLDR

在当前目录**启动热重载**

```air```

**初始化一个默认配置**文件

```air init```

**运行并向构建产物传递参数**

```air -- [--port] [8080]```

**使用自定义配置**文件

```air -c [path/to/.air.toml]```

不使用配置文件时**直接指定构建和运行命令**

```air --build.cmd "go build -o bin/api cmd/run.go" --build.bin "./bin/api"```

**显示帮助**

```air -h```

# SYNOPSIS

**air** [_OPTIONS_] [_ARGS_...]

**air** **init**

# PARAMETERS

**init**
> 在当前目录生成默认的 .air.toml 配置文件。

**-c** _FILE_
> 指定自定义配置文件路径。

**--build.cmd** _COMMAND_
> 直接在命令行设置构建命令。

**--build.bin** _PATH_
> 设置构建产物的路径。

**--build.entrypoint** _PATH_
> 设置二进制文件的入口点。

**--build.exclude_dir** _DIRS_
> 以逗号分隔的排除监视目录列表。

**--build.include_ext** _EXTS_
> 以逗号分隔的要监视的文件扩展名列表（默认：go,tpl,tmpl,html）。

**--build.delay** _MS_
> 变更后重建前的延迟毫秒数（默认：1000）。

**-d**
> 启用带详细输出的调试模式。

**--**
> 分隔符，其后的参数将传给构建出的二进制文件。

# DESCRIPTION

**Air** 是一款专为 Go 应用开发设计的热重载命令行工具。它监视源文件的变化并自动重新构建、重启应用，省去了开发过程中手动停止、构建、重启的麻烦。

在项目根目录运行 air，它会根据配置的扩展名和目录来监视文件变化。检测到变化后，Air 会重建应用并重启二进制文件。配置通过 **.air.toml** 文件管理，控制监视目录、排除路径、文件扩展名、构建命令和环境变量。

Air 可以在构建和运行前从 .env 文件加载环境变量。该工具仅面向开发工作流，并非为生产热部署场景设计。

# CONFIGURATION

**.air.toml**
> 项目级配置文件，控制监视目录、排除路径、文件扩展名、构建命令和环境变量。可通过 `air init` 生成。

# CAVEATS

Air 是开发工具，不应用于生产部署。默认配置监视常见的 Go 文件模式，但对布局非标准的项目可能需要调整。构建错误会在终端显示，但监视进程会继续运行等待修复。

# HISTORY

Air 作为开源项目而创建，旨在满足 Go 开发中的热重载需求，类似其他生态中的 nodemon（Node.js）等工具。该项目由 GitHub 上的 air-verse 组织维护，已成为 Go 社区最流行的热重载方案之一。

# INSTALL

```aur: yay -S air```

```nix: nix profile install nixpkgs#air```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [make](/man/make)(1), [nodemon](/man/nodemon)(1)
