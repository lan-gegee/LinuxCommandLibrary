# TAGLINE

Common Lisp 库管理器

# TLDR

**安装 Quicklisp**

```curl -O https://beta.quicklisp.org/quicklisp.lisp && sbcl --load quicklisp.lisp```

**加载一个系统**

```(ql:quickload "system-name")```

**搜索系统**

```(ql:system-apropos "keyword")```

**更新 Quicklisp**

```(ql:update-client)```

# SYNOPSIS

Quicklisp Common Lisp library manager

# DESCRIPTION

**Quicklisp** 是 Common Lisp 的库管理器。它会自动下载、安装和加载库及其依赖。它适用于大多数 Common Lisp 实现。

# INSTALLATION

```lisp
; Download and load installer
(load "quicklisp.lisp")

; Install to default location
(quicklisp-quickstart:install)

; Add to init file
(ql:add-to-init-file)
```

# EXAMPLES

```lisp
; Load a library
(ql:quickload "cl-ppcre")

; Load multiple
(ql:quickload '("alexandria" "cl-json"))

; Search for libraries
(ql:system-apropos "http")

; Update dist
(ql:update-dist "quicklisp")

; Update client
(ql:update-client)

; List installed
(ql:system-list)
```

# COMMON LIBRARIES

```
alexandria     - Utility functions
cl-ppcre       - Regular expressions
drakma         - HTTP client
cl-json        - JSON parsing
hunchentoot    - Web server
```

# CAVEATS

需要 Common Lisp 实现（SBCL、CCL 等）。库默认安装到 ~/quicklisp/。

# HISTORY

Quicklisp 由 **Zach Beane** 于 2010 年创建，用于简化 Common Lisp 的库管理。

# INSTALL

```pacman: sudo pacman -S quicklisp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbcl](/man/sbcl)(1), [clisp](/man/clisp)(1), [asdf](/man/asdf)(1)
