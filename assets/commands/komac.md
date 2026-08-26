# TAGLINE

面向 WinGet 的社区清单创建工具

# TLDR

**创建新的软件包清单**

```komac new```

**更新已有软件包**

```komac update [package-id]```

**更新到指定版本**

```komac update [package-id] --version [1.0.0] --urls [url1] [url2]```

**移除软件包版本**

```komac remove [package-id] --version [1.0.0]```

**将 fork 与上游同步**

```komac sync-fork```

# SYNOPSIS

**komac** [_options_] _command_ [_args_...]

# PARAMETERS

**new**
> 从零开始创建软件包。

**update** _package-id_
> 更新已有的软件包清单。

**remove** _package-id_
> 从 winget-pkgs 中移除版本。

**sync-fork**
> 将 fork 与 microsoft/winget-pkgs 同步。

**--version** _version_
> 软件包版本。

**--urls** _urls_
> 安装程序 URL。

**--submit**
> 自动提交 PR。

# DESCRIPTION

**komac** 是面向 WinGet 的社区清单创建工具。它自动化了向 winget-pkgs 仓库创建和提交软件包清单的过程，具备针对 Inno Setup、NSIS、MSI 和 Burn 安装程序的高级安装器分析能力。

# CAVEATS

提交拉取请求需要具有 public_repo 权限范围的经典 GitHub token。细粒度 token 可能无法用于创建 PR。

# INSTALL

```brew: brew install komac```

```nix: nix profile install nixpkgs#komac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [brew](/man/brew)(1)
