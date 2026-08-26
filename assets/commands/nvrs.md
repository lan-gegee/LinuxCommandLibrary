# TAGLINE

快速的软件新版本检查工具

# TLDR

**检查新版本**

```nvrs```

**检查特定软件包**

```nvrs check [package_name]```

# SYNOPSIS

**nvrs** [_command_] [_options_]

# DESCRIPTION

**nvrs** 是一款用于跟踪和更新软件版本的 CLI 工具。它可以从多个来源检查软件包更新，包括 GitHub、GitLab、AUR、crates.io 以及通过正则表达式定义的 URL。

它以速度见长，可以并行监控大量软件包，并报告哪些有可用的新版本。

# CAVEATS

需要配置软件包来源。某些来源（如 GitHub）可能受 API 速率限制。

# HISTORY

**nvrs** 使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#nvrs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1)
