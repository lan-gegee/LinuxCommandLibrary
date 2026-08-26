# TAGLINE

带 readline 支持的 Clojure CLI

# TLDR

**启动 REPL**

```clj```

**运行脚本文件**

```clj -M [script.clj]```

**执行函数**

```clj -X [namespace/function]```

**添加依赖别名**

```clj -A:[alias]```

**列出依赖**

```clj -X:deps list```

**显示依赖树**

```clj -X:deps tree```

使用额外 JVM 选项**运行**

```clj -J-Xmx[2g] -M [script.clj]```

# SYNOPSIS

**clj** [_clj-opts_] [_-M_|_-X_|_-T_] [_aliases_] [_args_]

# DESCRIPTION

**clj** 是 **clojure** 命令的包装器，通过 **rlwrap** 增加 readline 支持，在 REPL 中提供行编辑、历史记录和补全功能。它是启动交互式 Clojure 开发会话的推荐方式。

该工具通过 **deps.edn** 配置文件管理依赖，并支持多种执行模式：运行程序、执行函数和调用工具。deps.edn 中定义的别名允许在开发、测试和生产等不同依赖配置之间切换。

对于 shell 脚本和 CI 流水线等非交互场景，请直接使用 **clojure** 命令，因为 rlwrap 可能干扰管道输入和输出。

# EXECUTION MODES

**-M**
> 使用 clojure.main，调用 -main 函数

**-X**
> 以关键字参数映射执行函数

**-T**
> 与 -X 类似，但 classpath 仅设为 .

# PARAMETERS

**-A**:_aliases_
> 为依赖/路径使用别名

**-J** _opt_
> 将选项传给 JVM

**-Sdeps** _edn_
> 覆盖 deps.edn

**-Spath**
> 打印 classpath

**-Scp** _cp_
> 使用给定的 classpath

**-Sforce**
> 强制重新计算 classpath

**-Srepro**
> 忽略用户的 deps.edn

**-Stree**
> 打印依赖树

**-Sdescribe**
> 以 EDN 格式打印环境信息

**-P**
> 仅准备依赖，不执行

**-h**, **--help**
> 显示帮助

# BUILT-IN TOOLS

```
clj -X:deps list       # List all deps
clj -X:deps tree       # Dependency tree
clj -X:deps mvn-pom    # Generate pom.xml
```

# CONFIGURATION

**deps.edn**
> 项目级的依赖声明、别名和路径配置。

**~/.clojure/deps.edn**
> 用户级默认依赖和别名，应用于所有项目。

# CAVEATS

项目配置需要 deps.edn。脚本中请用 `clojure` 而非 `clj`（不带 rlwrap）。JVM 选项通过 -J 或 JAVA_OPTS 环境变量传入。

# INSTALL

```dnf: sudo dnf install clojure```

```pacman: sudo pacman -S clojure```

```apk: sudo apk add clojure```

```zypper: sudo zypper install clojure```

```brew: brew install clojure```

```nix: nix profile install nixpkgs#clojure```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lein](/man/lein)(1), [java](/man/java)(1), [clojure](/man/clojure)(1)

# RESOURCES

```[Source code](https://github.com/clojure/brew-install)```

```[Documentation](https://clojure.org/reference/deps_and_cli)```

<!-- verified: 2026-06-22 -->
