# TAGLINE

Common Lisp 实现管理器

# TLDR

**安装 Roswell**

```ros setup```

**安装 Common Lisp 实现**

```ros install [sbcl]```

**运行 Lisp REPL**

```ros run```

**运行脚本**

```ros [script.ros]```

**安装 Quicklisp 系统**

```ros install [system-name]```

# SYNOPSIS

**ros** [_options_] [_command_] [_args_]

# PARAMETERS

**setup**
> 初始设置。

**install** _impl_
> 安装实现。

**run**
> 启动 REPL。

**use** _impl_
> 切换实现。

**list**
> 列出可用项。

**init** _name_
> 创建脚本模板。

# DESCRIPTION

**Roswell** 是一个 Common Lisp 实现管理器和启动器。它负责安装不同的 Lisp 实现、管理 Quicklisp，并提供脚本执行功能。

# EXAMPLES

```bash
# Initial setup
ros setup

# Install SBCL
ros install sbcl

# Install CCL
ros install ccl-bin

# List installed
ros list installed

# Start REPL with specific impl
ros use sbcl
ros run

# Create script
ros init my-script

# Run script
ros my-script.ros

# Install library
ros install alexandria
```

# SCRIPT FORMAT

```lisp
#!/bin/sh
#|-*- mode:lisp -*-|#
#|
exec ros -Q -- $0 "$@"
|#

(defun main (&rest args)
  (format t "Hello, World!~%"))
```

# CAVEATS

需要进行初始设置。会下载相应的实现。脚本可在不同实现之间移植。

# HISTORY

Roswell 由 **Masatoshi Sano** 创建，旨在简化 Common Lisp 开发环境的管理。

# INSTALL

```pacman: sudo pacman -S roswell```

```brew: brew install roswell```

```nix: nix profile install nixpkgs#roswell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbcl](/man/sbcl)(1), [quicklisp](/man/quicklisp)(1), [clisp](/man/clisp)(1)
