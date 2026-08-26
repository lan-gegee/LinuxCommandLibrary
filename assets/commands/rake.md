# TAGLINE

Ruby 构建自动化与任务运行器

# TLDR

**列出所有可用任务**

```rake -T```

**运行默认任务**

```rake```

**运行指定任务**

```rake [task_name]```

**运行命名空间中的任务**

```rake [namespace]:[task_name]```

**运行多个任务**

```rake [task1] [task2]```

**带参数运行任务**

```rake [task_name][[arg1],[arg2]]```

**以详细输出和完整回溯运行**

```rake --trace [task_name]```

**并行运行任务**

```rake -m [task_name]```

# SYNOPSIS

**rake** [**-f** _rakefile_] [**-T**] [**-t**] [**-v**] [**-j** _num_jobs_] [_task_...]

# PARAMETERS

**-T**, **--tasks** [_pattern_]
> 显示可用任务及其描述，可按模式过滤

**-f**, **--rakefile** _FILE_
> 使用指定文件作为 Rakefile

**-t**, **--trace**
> 开启调用/执行跟踪并启用完整回溯

**-v**, **--verbose**
> 将消息记录到标准输出

**-q**, **--quiet**
> 不将消息记录到标准输出

**-m**, **--multitask**
> 将所有任务视为多任务（并行执行）

**-j**, **--jobs** _NUM_
> 最大并行任务数（默认：CPU 核心数 + 4）

**-B**, **--build-all**
> 构建所有前置任务，包括已是最新的

**-n**, **--dry-run**
> 试运行，不执行动作

**-N**, **--no-search**
> 不在父目录中搜索 Rakefile

**-P**, **--prereqs**
> 显示任务及其前置依赖

**-D**, **--describe** [_pattern_]
> 描述任务（显示完整描述）

**-W**, **--where** [_pattern_]
> 显示任务的定义位置

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**rake** 是 Ruby 的类 make 构建工具。它执行 Rakefile 中用标准 Ruby 语法定义的任务，无需专门的 Makefile 语法或 XML 配置。

任务可以定义依赖关系，Rake 会自动确定正确的执行顺序。该工具支持用命名空间组织相关任务、通过修改时间进行追踪的文件任务，以及提升性能的并行执行。

自 Ruby 1.9 起 Rake 已包含在标准库中，被广泛用于 Ruby 项目，尤其是 Rails 应用，负责数据库迁移、资源编译等开发任务。

# CAVEATS

Rake 默认会在当前目录和父目录中搜索 Rakefile。使用 **-N** 可禁用此行为，或使用 **-f** 指定明确路径。

含特殊字符的任务名在 Shell 中可能需要加引号。传给任务的参数使用方括号语法，也可能需要转义。

并行任务执行（**-m**、**-j**）要求任务是线程安全的。并行任务间的共享状态可能导致竞态条件。

# HISTORY

Rake 由 **Jim Weirich** 于 **2003 年**创建，是 Make 的 Ruby 替代品。名字含义为 "Ruby Make"。2007 年起随 Ruby 1.9 纳入标准库。Weirich 于 2014 年去世后，该项目由 Ruby 社区继续维护。

# INSTALL

```pacman: sudo pacman -S ruby-rake```

```apk: sudo apk add ruby-rake```

```nix: nix profile install nixpkgs#rake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [ruby](/man/ruby)(1), [bundle](/man/bundle)(1), [rails](/man/rails)(1)
