# TAGLINE

针对速度优化的 POSIX 兼容 Shell

# TLDR

**运行脚本**

```dash [script.sh]```

**运行命令字符串**

```dash -c '[command]'```

**只检查语法而不执行**

```dash -n [script.sh]```

**调试模式（打印命令）**

```dash -x [script.sh]```

**详细模式（打印输入）**

```dash -v [script.sh]```

**交互式 Shell**

```dash -i```

# SYNOPSIS

**dash** [_options_] [_script-file_ [_arguments_]]

# DESCRIPTION

**dash** 是 Debian Almquist Shell，一个符合 POSIX 标准的 /bin/sh 实现，专为高效和标准合规而设计。它比 bash 明显更快、更小，是运行 shell 脚本和系统初始化的理想选择。

这个 Shell 把脚本执行速度、启动时间和最小内存占用置于交互特性之上。它的脚本执行速度约为 bash 的 4 倍，这正是 Debian 和 Ubuntu 将其用作默认 /bin/sh 的原因。

dash 源自 NetBSD 的 ash（Almquist shell），而 ash 本身是作为原版 Bourne shell 的 BSD 许可替代品创建的。它严格实现 POSIX shell 规范，不包含数组、[[ ]] 条件表达式或进程替换等 bash 扩展。

该 Shell 主要用于系统脚本、软件包管理器脚本，以及 POSIX 合规性和性能比高级交互特性更重要的场景。

# PARAMETERS

**-c** _string_
> 从字符串读取命令

**-s**
> 从 stdin 读取命令

**-i**
> 交互模式

**-l**
> 登录 Shell

**-f**
> 禁用文件名展开（noglob）

**-n**
> 仅检查语法（noexec）

**-u**
> 使用未定义变量时报错（nounset）

**-v**
> 打印输入行（verbose）

**-x**
> 执行前打印命令（xtrace）

**-e**
> 出错即退出（errexit）

**-I**
> 交互模式下忽略 EOF

**-C**
> 不允许用 > 覆盖已有文件（noclobber）

**-a**
> 导出所有已赋值的变量（allexport）

# PERFORMANCE

脚本执行速度约为 bash 的 4 倍。

# COMPATIBILITY

严格遵循 POSIX 标准。不支持 bash 特有功能：
- `[[ ... ]]` 条件表达式
- 进程替换 `<()`
- 数组
- 非标准 glob 匹配

# CAVEATS

使用 bash 特性的脚本会失败。bash 专属脚本请使用 `#!/bin/bash`。在 Debian/Ubuntu 上 dash 就是 /bin/sh。

# INSTALL

```apt: sudo apt install dash```

```dnf: sudo dnf install dash```

```pacman: sudo pacman -S dash```

```apk: sudo apk add dash```

```zypper: sudo zypper install dash```

```brew: brew install dash```

```nix: nix profile install nixpkgs#dash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [zsh](/man/zsh)(1)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/utils/dash/dash.git)```

```[Homepage](http://gondor.apana.org.au/~herbert/dash/)```

<!-- verified: 2026-07-11 -->
