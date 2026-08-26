# TAGLINE

Steel Bank Common Lisp 编译器与运行时

# TLDR

**启动 REPL**

```sbcl```

**运行 Lisp 脚本**

```sbcl --script [script.lisp]```

**加载文件并启动 REPL**

```sbcl --load [file.lisp]```

**求值表达式并退出**

```sbcl --eval "(print 'hello)" --quit```

**编译为可执行文件**

```sbcl --eval "(load \"app.lisp\")" --eval "(sb-ext:save-lisp-and-die \"app\" :executable t)"```

**使用指定的 core 镜像运行**

```sbcl --core [custom.core]```

**禁用调试器**（用于脚本）

```sbcl --disable-debugger --load [script.lisp]```

**加载 ASDF 系统**

```sbcl --eval "(asdf:load-system :system-name)"```

# SYNOPSIS

**sbcl** [_--script file_] [_--load file_] [_--eval expr_] [_--quit_] [_options_]

# PARAMETERS

**--script** _FILE_
> 运行脚本（无 REPL，隐含 --disable-debugger）。

**--load** _FILE_
> 加载 Lisp 文件。

**--eval** _EXPR_
> 求值表达式。可多次指定。

**--quit**
> 处理完所有 --load 和 --eval 选项后退出。

**--core** _CORE_
> 使用指定的 core 文件。

**--disable-debugger**
> 禁用 Lisp 调试器。

**--noinform**
> 不显示启动横幅。

**--noprint**
> 禁用 REPL 打印。

**--non-interactive**
> 非交互模式。

**--userinit** _FILE_
> 用户初始化文件（默认：~/.sbclrc）。

**--no-userinit**
> 跳过用户初始化文件。

**--sysinit** _FILE_
> 系统初始化文件。

**--no-sysinit**
> 跳过系统初始化文件。

**--dynamic-space-size** _MB_
> 堆大小（以 MB 为单位）。

**--control-stack-size** _MB_
> 栈大小（以 MB 为单位）。

# DESCRIPTION

**SBCL**（Steel Bank Common Lisp）是一个高性能的 Common Lisp 编译器。它将代码编译为原生代码并进行深度优化，是最快的 Lisp 实现之一。

REPL（Read-Eval-Print Loop，读取-求值-打印循环）支持交互式开发。无需重启即可加载、测试和修改代码。调试器提供重启点、回溯和检查功能。

ASDF（Another System Definition Facility）用于管理项目和依赖。Quicklisp 为 Common Lisp 库提供包管理器。两者结合可实现现代化的项目开发。

创建可执行文件需要用到 sb-ext:save-lisp-and-die，它会转储一个包含已加载代码的镜像。生成的结果是一个启动迅速的独立可执行文件。

SBCL 包含 SB-* 扩展包：线程（sb-thread）、网络（sb-bsd-sockets）、FFI（sb-alien）等。这些扩展对标准 Common Lisp 进行了增强。

类型系统支持可选的类型声明以便进行优化。编译器会提供关于优化机会的详细提示。

# CONFIGURATION

**~/.sbclrc**
> 启动时加载的用户初始化文件，常用于配置 Quicklisp、设置优化策略以及定义启动行为。

**/etc/sbclrc**
> 在用户初始化文件之前加载的系统级初始化文件。

# CAVEATS

core 文件体积很大（50MB 以上）。编译可能消耗大量内存。某些 POSIX 信号处理与其他实现不同。线程模型可能因平台而异。并非所有 CL 库都支持所有平台。

# HISTORY

**SBCL** 于 **1999 年**从 **CMUCL**（Carnegie Mellon University Common Lisp）分叉而来，由一群希望获得更积极维护的开发者创建。"Steel Bank" 这个名字是对 "Carnegie" 的戏称（Andrew Carnegie 是钢铁大亨）。它已成为最受欢迎的自由 Common Lisp 实现之一，以性能和活跃开发著称。

# INSTALL

```apt: sudo apt install sbcl```

```dnf: sudo dnf install sbcl```

```pacman: sudo pacman -S sbcl```

```apk: sudo apk add sbcl```

```zypper: sudo zypper install sbcl```

```brew: brew install sbcl```

```nix: nix profile install nixpkgs#sbcl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clisp](/man/clisp)(1), [ecl](/man/ecl)(1), [quicklisp](/man/quicklisp)(1), [roswell](/man/roswell)(1)
