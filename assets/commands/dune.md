# TAGLINE

面向 OCaml 项目的可组合构建系统

# TLDR

**构建项目**

```dune build```

**运行测试**

```dune test```

**运行可执行程序**

```dune exec [program]```

**清理构建产物**

```dune clean```

**构建并监视变更**

```dune build --watch```

**格式化代码**

```dune fmt```

**创建新项目**

```dune init project [name]```

# SYNOPSIS

**dune** _command_ [_options_]

# PARAMETERS

**build** [_targets_]
> 构建指定目标或全部目标。

**test**
> 运行测试。

**exec** _program_
> 构建并执行程序。

**clean**
> 移除构建产物。

**init** _component_ _name_
> 初始化新组件（project、library、executable、test）。

**fmt**
> 使用 ocamlformat 格式化源代码。

**promote**
> 提升预期的测试输出。

**cache**
> 管理共享的构建产物缓存。

**install**
> 安装项目中定义的软件包。

**--watch**, **-w**
> 文件变化时持续重新构建。

**--force**
> 强制重新构建所有目标。

**--verbose**
> 显示所执行程序的完整命令行。

# CONFIGURATION

**dune**
> 每个目录的构建配置文件，使用 S 表达式语法定义库、可执行程序和测试。

**dune-project**
> 位于仓库根目录的项目级配置，指定项目元数据和语言版本。

**dune-workspace**
> 可选的工作区配置，用于多上下文构建和高级项目设置。

# DESCRIPTION

**Dune** 是 OCaml 和 Reason 项目的标准构建系统。它能自动发现项目结构、处理依赖，并借助缓存提供快速的增量构建。

项目通过使用 S 表达式语法的 **dune** 文件进行配置。Dune 与 opam 集成以进行软件包管理，并支持交叉编译、多个构建上下文和 IDE 集成。

# DUNE FILE EXAMPLE

```lisp
(library
 (name mylib)
 (libraries str unix))

(executable
 (name main)
 (libraries mylib))

(test
 (name test_mylib)
 (libraries mylib alcotest))
```

# CAVEATS

需要 OCaml 或 Reason 编译器。构建产物放在 _build 目录中。Dune 文件使用 S 表达式语法，而不是 YAML 或 TOML。软件包管理依赖 opam。

# HISTORY

Dune 最初名为 **jbuilder**，由 **Jane Street** 于 **2016 年**创建。它在 **2018 年**更名为 Dune，并成为 OCaml 生态事实上的标准构建系统。该项目致力于提供现代、快速且对用户友好的构建体验。

# INSTALL

```apt: sudo apt install ocaml-dune```

```dnf: sudo dnf install ocaml-dune```

```pacman: sudo pacman -S dune```

```apk: sudo apk add dune```

```zypper: sudo zypper install ocaml-dune```

```brew: brew install dune```

```nix: nix profile install nixpkgs#dune```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocaml](/man/ocaml)(1), [opam](/man/opam)(1), [ocamlfind](/man/ocamlfind)(1), [make](/man/make)(1)
