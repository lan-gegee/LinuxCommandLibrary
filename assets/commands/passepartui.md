# TAGLINE

pass 密码管理器的终端用户界面

# TLDR

**启动密码库 TUI**

```passepartui```

# SYNOPSIS

**passepartui** [_options_]

# DESCRIPTION

**passepartui** 是 **pass**（password-store）密码管理器的终端用户界面。它提供快速、键盘驱动的导航（含 Vim 键位绑定）、密码搜索和过滤、密码与一次性密码的剪贴板复制，以及有限的鼠标支持。它是一个只读界面，用于访问你的密码库——添加或删除条目请直接使用 **pass**。

# CAVEATS

需要已安装并配置好 **pass**（password-store）。不支持创建或删除密码条目。

# HISTORY

**passepartui** 由 **kardwen** 创建，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#passepartui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [pass-cli](/man/pass-cli)(1), [gopass](/man/gopass)(1)
