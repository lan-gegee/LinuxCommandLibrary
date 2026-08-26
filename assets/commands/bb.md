# TAGLINE

用于脚本编写的原生 Clojure 解释器

# TLDR

**运行** Clojure 项目脚本

```bb [script.clj]```

**启动** REPL

```bb repl```

**执行**表达式

```bb -e ["(println (+ 1 2 3))"]```

**使用**任务运行器

```bb tasks```

# SYNOPSIS

**bb** [_options_] [_file_] [_args_]

# DESCRIPTION

**bb**（Babashka）是用于脚本编写的原生 Clojure 解释器。它启动速度极快，无需 JVM 开销即可运行 Clojure 脚本，适合 Shell 脚本编写和任务自动化。

该工具让 Clojure 能够胜任通常由 bash 或 Python 脚本处理的任务。

# PARAMETERS

**-e**, **--eval** _expr_
> 求值表达式

**-f**, **--file** _file_
> 运行文件

**-m**, **--main** _ns_
> 调用命名空间中的 main 函数

**--repl**
> 启动 REPL

**--nrepl-server**
> 启动 nREPL 服务器

**--classpath** _cp_
> 设置类路径

**--uberscript** _file_
> 创建独立脚本

# FEATURES

- 启动迅速（毫秒级）
- 覆盖大部分 Clojure 核心
- 内置常用库
- 任务运行器（bb.edn）
- 用于原生绑定的 Pod 系统
- 兼容 Clojure 语法
- 支持调用外部 Shell 命令

# TASK RUNNER

在 bb.edn 中定义任务：
```clojure
{:tasks
 {test {:doc "Run tests"
        :task (shell "clojure -M:test")}}}
```

# CONFIGURATION

**bb.edn**
> 项目配置文件，用于定义任务、依赖和类路径设置。

# CAVEATS

并非完整的 Clojure（缺少部分特性）。不如编译后的代码快。Java 互操作受限。部分库无法使用。Pod 会增加复杂度。

# HISTORY

**Babashka** 由 Michiel Borkent 于 **2019** 年创建，目的是让 Clojure 脚本摆脱 JVM 启动开销、实现快速运行。

# INSTALL

```nix: nix profile install nixpkgs#babashka```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clojure](/man/clojure)(1), [lein](/man/lein)(1)
