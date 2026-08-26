# TAGLINE

终端中的键盘测试工具

# TLDR

**启动键盘测试器**

```kbt```

# SYNOPSIS

**kbt** [_options_]

# DESCRIPTION

**kbt** 是一个基于终端的键盘测试器，它会显示可视化的键盘布局，并在按键按下时高亮对应按键。它支持多种键盘布局，是那些往往表现不一致的在线键盘测试工具的可靠替代品。

TUI 显示一张键盘示意图，会在你按键时实时点亮，因此适合测试新键盘、检查失效按键，或在维护后验证键轴。

# CAVEATS

按键检测取决于终端模拟器传递按键事件的能力。某些组合键可能在到达 kbt 之前就被操作系统或终端拦截。

# HISTORY

**kbt** 由 **bloznelis** 创建，用 **Rust** 编写。它的诞生源于对不可靠的在线键盘测试工具的不满。

# INSTALL

```pacman: sudo pacman -S kbt```

```brew: brew install kbt```

```nix: nix profile install nixpkgs#kbt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[showkey](/man/showkey)(1)
