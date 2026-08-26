# TAGLINE

Jujutsu 版本控制系统的 TUI

# TLDR

在当前仓库启动 jjui

```jjui```

# SYNOPSIS

**jjui** [_options_]

# DESCRIPTION

**jjui** 是一个用于操作 **Jujutsu**（jj）版本控制系统的终端用户界面。它提供交互式修订树，支持变基修订、压缩变更、编辑描述，以及通过预览窗口查看 diff。

主要功能包括：编辑 revset 时自动补全与签名提示；将修订或分支变基到其他修订；按 **S** 键压缩修订；以及一个预览窗口（按 **p** 切换），可显示 jj show、jj diff 或 jj op show 的输出。

# CAVEATS

需要安装 **jj** 0.36 或更新版本。仅适用于以 Jujutsu 初始化的仓库。

# HISTORY

**jjui** 由 **Ibrahim Dursun**（idursun）创建，用 **Go** 编写。它旨在为 Jujutsu 基于修订的版本控制模型提供可视化、交互式的界面。

# INSTALL

```brew: brew install jjui```

```nix: nix profile install nixpkgs#jjui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [lazyjj](/man/lazyjj)(1), [lazygit](/man/lazygit)(1)
