# TAGLINE

文件变化时运行命令

# TLDR

**监视并运行命令**

```reflex [command]```

**监视特定模式**

```reflex -r '\.go$' [go build]```

**监视目录**

```reflex -d [src/] [command]```

**多个模式**

```reflex -r '\.go$' -r '\.html$' [command]```

**启动时不执行初始运行**

```reflex -s [command]```

**装饰模式**

```reflex -d [.] -- [sh -c "echo changed"]```

**排除模式**

```reflex -r '\.go$' -R 'vendor/' [command]```

# SYNOPSIS

**reflex** [_-r regex_] [_-d dir_] [_-R exclude_] [_options_] _command_

# PARAMETERS

**-r** _REGEX_
> 包含模式。

**-R** _REGEX_
> 排除模式。

**-d** _DIR_
> 监视目录。

**-s**
> 启动服务（不执行初始运行）。

**-g** _GLOB_
> Glob 模式。

**-c** _CONFIG_
> 配置文件。

**--all**
> 匹配所有文件。

**--decoration** _MODE_
> 输出装饰。

# DESCRIPTION

**reflex** 监视文件并在文件变化时运行命令。它是一款灵活的面向开发的文件监视工具。

正则模式用于过滤哪些文件触发。多个模式可组合实现复杂匹配。

服务模式运行一个长期存活的进程。进程在文件变化时重启。

排除规则可以忽略 vendor 目录或构建输出，避免不必要的重建。

配置文件定义复杂的监视规则。一个文件中可包含多个监视器。

# CONFIGURATION

**.reflex**
> 项目级配置文件，每行定义一条监视规则，包括正则模式和命令。当前目录存在时自动加载。

# CAVEATS

某些文件系统会退化为轮询。快速连续的变化可能被合并处理。初始运行有时并非所需。

# HISTORY

**Reflex** 的设计目标是成为简单灵活的文件监视工具。它专注于以最少配置实现开发工作流自动化。

# INSTALL

```apt: sudo apt install reflex```

```apk: sudo apk add reflex```

```brew: brew install reflex```

```nix: nix profile install nixpkgs#reflex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[entr](/man/entr)(1), [watchman](/man/watchman)(1), [fswatch](/man/fswatch)(1), [inotifywait](/man/inotifywait)(1)
