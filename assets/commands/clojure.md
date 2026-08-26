# TAGLINE

官方 Clojure 语言启动器

# TLDR

**启动 Clojure REPL**

```clojure```

**运行 Clojure 脚本**

```clojure -M [script.clj]```

**执行指定函数**

```clojure -X [namespace/function]```

**附带额外依赖运行**

```clojure -Sdeps '{:deps {org.clojure/data.json {:mvn/version "2.4.0"}}}'```

从 deps.edn **以指定别名启动 REPL**

```clojure -A:[alias]```

**求值表达式**

```clojure -M -e '(println "Hello, World!")'```

使用 tools.build **构建 uberjar**

```clojure -T:build uber```

不运行而只**显示 classpath**

```clojure -Spath```

# SYNOPSIS

**clojure** [_dep-opts_] [_init-opts_] [_main-opts_] [_args_]

# PARAMETERS

**-M** [_:aliases_]
> 使用串联的别名运行 main 入口点。

**-X** [_:aliases_]
> 以 exec 参数执行函数。

**-T** [_:aliases_]
> 以 exec 参数调用工具。

**-A** [_:aliases_]
> 为 REPL 使用串联的别名。

**-Sdeps** _EDN_
> EDN 格式的额外依赖。

**-Spath**
> 打印 classpath 后退出。

**-Stree**
> 打印依赖树。

**-Sdescribe**
> 打印环境和命令信息。

**-e**, **--eval** _STRING_
> 求值给定的表达式。

**-r**, **--repl**
> 运行 REPL。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**clojure** 是 Clojure 编程语言的官方命令行启动器。它通过 **deps.edn** 配置文件管理依赖，为 REPL 驱动的开发、脚本执行和应用构建提供精简的工作流。

该 CLI 与 Maven 和 Git 仓库集成以解析依赖，并按需自动下载和缓存库。deps.edn 中的别名允许为开发、测试和生产环境定义不同的配置。

Clojure 提供三种主要执行模式：用于传统 main 函数执行的 **-M**、用于以关键字参数执行函数的 **-X**，以及用于调用工具的 **-T**。REPL 支持即时反馈的交互式开发，这是 Clojure 开发的核心实践。

# CONFIGURATION

**deps.edn**
> 项目级的依赖声明、别名和路径配置。

**~/.clojure/deps.edn**
> 用户级默认依赖和别名，应用于所有项目。

# CAVEATS

需要 Java Runtime Environment（JRE）8 或更高版本。初次下载依赖可能耗时较长，但会缓存在本地。CLI 需要 deps.edn 文件才能进行项目级配置；没有它则应用全局默认值。

# HISTORY

Clojure 由 Rich Hickey 创建并于 **2007 年**发布，是一门面向 JVM 的现代 Lisp。**clojure** CLI 和 deps.edn 工具于 **2018 年**推出，作为 Leiningen 和 Boot 的官方替代方案，提供了更简单、更可组合的依赖管理方式。

# INSTALL

```dnf: sudo dnf install clojure```

```pacman: sudo pacman -S clojure```

```apk: sudo apk add clojure```

```zypper: sudo zypper install clojure```

```brew: brew install clojure```

```nix: nix profile install nixpkgs#clojure```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lein](/man/lein)(1), [java](/man/java)(1), [clj](/man/clj)(1)

# RESOURCES

```[Source code](https://github.com/clojure/brew-install)```

```[Documentation](https://clojure.org/reference/deps_and_cli)```

<!-- verified: 2026-06-22 -->
