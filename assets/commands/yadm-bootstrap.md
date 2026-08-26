# TAGLINE

执行 yadm 引导程序

# TLDR

**运行引导脚本**

```yadm bootstrap```

# SYNOPSIS

**yadm** **bootstrap**

# DESCRIPTION

**yadm bootstrap** 会执行位于 `$HOME/.config/yadm/bootstrap` 的引导程序（如果存在）。这通常用于克隆后的设置工作，例如安装软件包、设置权限或配置应用程序。引导脚本必须是可执行文件。

`yadm clone` 成功克隆仓库后，如果找到引导程序，yadm 会询问是否运行它。可以通过 `yadm clone` 的 `--bootstrap` 或 `--no-bootstrap` 选项跳过该询问。

引导程序可以是任何可执行文件，不过 bash 脚本最为常见。建议让引导逻辑具备幂等性，以便在合并来自其他主机的更改时可以安全地重复执行。可以使用 `--yadm-bootstrap` 选项覆盖引导程序路径。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1), [yadm-clone](/man/yadm-clone)(1)
