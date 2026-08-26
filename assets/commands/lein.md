# TAGLINE

Clojure 构建工具

# TLDR

**创建新项目**

```lein new [template] [project-name]```

**运行项目**

```lein run```

**启动 REPL**

```lein repl```

**运行测试**

```lein test```

**构建 JAR**

```lein jar```

**构建 uberjar**

```lein uberjar```

**安装依赖**

```lein deps```

# SYNOPSIS

**lein** _task_ [_options_]

# PARAMETERS

**new** _TEMPLATE_ _NAME_
> 创建项目。

**run**
> 运行主函数。

**repl**
> 启动 REPL。

**test**
> 运行测试。

**jar**
> 构建 JAR。

**uberjar**
> 构建独立 JAR。

**deps**
> 下载依赖。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Leiningen** 是 Clojure 的构建工具。它负责管理项目、依赖和构建。

该工具为项目创建提供了模板。它与 Maven 软件仓库集成。

# CAVEATS

需要 Java。使用 project.clj 配置。较新的项目可考虑改用 deps.edn。

# HISTORY

Leiningen 由 **Phil Hagelberg** 创建，是 Clojure 项目的标准构建工具。

# INSTALL

```pacman: sudo pacman -S leiningen```

```apk: sudo apk add leiningen```

```zypper: sudo zypper install leiningen```

```brew: brew install leiningen```

```nix: nix profile install nixpkgs#leiningen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clojure](/man/clojure)(1), [java](/man/java)(1), [boot](/man/boot)(1)
