# TAGLINE

移除 bun link 创建的软件包符号链接

# TLDR

**从全局链接注册表中注销当前软件包**

```bun unlink```

**从当前项目中取消链接特定软件包**

```bun unlink [package-name]```

# SYNOPSIS

**bun** **unlink** [_package-name_]

# DESCRIPTION

**bun unlink** 移除由 **bun link** 创建的符号链接。在软件包目录中不带参数运行时，它会从全局链接注册表中注销该软件包。带上软件包名称运行时，它会从当前项目的 node_modules 中移除该符号链接。

这是本地软件包开发中 `bun link` 工作流的逆操作。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-link](/man/bun-link)(1), [bun-install](/man/bun-install)(1)
