# TAGLINE

定义和管理 Pixi 项目任务

# TLDR

**向项目添加任务**

```pixi task add [name] [command]```

**列出任务**

```pixi task list```

**移除任务**

```pixi task remove [name]```

**添加带别名的任务**

```pixi task alias [name] [existing_task]```

# SYNOPSIS

**pixi** **task** _command_ [_options_]

# PARAMETERS

**add** _name_ _command_
> 添加新任务。

**list**
> 列出所有任务。

**remove** _name_
> 移除任务。

**alias** _name_ _target_
> 创建任务别名。

**--depends-on** _tasks_
> 任务依赖。

# DESCRIPTION

**pixi task** 用于管理项目任务。任务是可在项目环境中运行的预定义命令，类似于 npm scripts 或 Makefile 目标。支持任务之间的依赖关系。

# INSTALL

```pacman: sudo pacman -S pixi```

```brew: brew install pixi```

```nix: nix profile install nixpkgs#pixi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pixi](/man/pixi)(1)
