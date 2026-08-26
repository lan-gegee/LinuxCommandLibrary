# TAGLINE

支持数学语法和用户自定义函数的科学计算器

# TLDR

**启动交互式计算器**

```kalker```

**求表达式的值**

```kalker "sin(pi/4) + sqrt(2)"```

**定义变量**

```kalker "x = 42"```

**计算导数**

```kalker "f(x) = x^2; f'(3)"```

**计算积分**

```kalker "∫(0, pi, sin(x) dx)"```

# SYNOPSIS

**kalker** [_expression_]

# DESCRIPTION

**kalker**（也称 **kalk**）是一个采用数学语法的科学计算器，支持用户自定义的**变量**和**函数**、**复数**，以及**导数**和**积分**的估算。它提供 REPL 界面并支持特殊符号补全（输入 "sqrt" 再按 Tab 会转换为 "√"）。

功能包括基于牛顿法的求根、自动微分、数值积分，以及对常见数学常数和函数的支持。它可运行于 Linux、macOS、Windows、Android，并通过 WebAssembly 在 web 浏览器中运行。

# CAVEATS

数值积分和微分是近似计算，对某些函数可能存在精度限制。当结果需要时才会自动启用复数支持。

# HISTORY

**kalker** 由 **Oliver Waldemar**（PaddiM8）创建，用 **Rust** 编写。它的设计目标是提供一个自然数学语法的计算器，让书写表达式的感觉像在纸上演算而非编程。

# INSTALL

```apk: sudo apk add kalker```

```brew: brew install kalker```

```nix: nix profile install nixpkgs#kalker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [python3](/man/python3)(1)
