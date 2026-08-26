# TAGLINE

列出 Bun 项目中已安装的软件包

# TLDR

**列出已安装的包**（顶层）

```bun pm ls```

**列出所有包**，包括嵌套依赖

```bun pm ls --all```

# SYNOPSIS

**bun** **pm** **ls** [**--all**]

# PARAMETERS

**--all**
> 显示完整的依赖树，包括传递性依赖。

# DESCRIPTION

**bun pm ls**（有时以 **bun list** 调用）打印当前项目 **node_modules** 目录中安装的软件包。默认只显示 **package.json** 中声明的直接依赖；传入 **--all** 可查看完整解析后的依赖树。

输出包含每个包解析后的版本和位置，便于快速审计已安装的内容。若需要机器可读的输出，请通过 **bun pm** 子命令检查 **bun.lockb**。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm-ls](/man/bun-pm-ls)(1), [bun-outdated](/man/bun-outdated)(1)
