# TAGLINE

从模板在当前目录创建 flake

# TLDR

**初始化 flake**，使用默认模板

```nix flake init```

**从内置模板初始化**

```nix flake init -t [templates#simpleContainer]```

**从 GitHub 仓库模板初始化**

```nix flake init -t [github:owner/repo#template]```

# SYNOPSIS

**nix flake init** [**-t** _template_] [_flags_]

# PARAMETERS

**-t**, **--template** _FLAKE_
> 要使用的模板。默认为 `templates#templates.default`。模板是一个 flake 引用，其后可跟 `#<attr>` 来选择具体的模板属性。

# DESCRIPTION

**nix flake init** 会复制模板 flake 中的文件，在当前目录创建新的 `flake.nix`。它不会覆盖已经存在的文件。

默认的模板来源是 `nixpkgs` 的 flakes 模板注册表。模板通过一个 flake 引用加上可选的属性路径来标识（例如 `templates#python`）。初始化完成后，模板中定义的所有 `welcomeText` 都会被打印到终端。

# CAVEATS

不会覆盖已有文件。必须在 Nix 配置中启用 Nix flakes（`experimental-features = nix-command flakes`）。

# HISTORY

Nix flakes 作为实验性特性在 **Nix 2.4**（2021 年）中引入，目的是提供可复现、可组合的构建。`nix flake init` 子命令是新式 `nix` CLI（`nix3`）的组成部分。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-flake](/man/nix-flake)(1), [nix-flake-show](/man/nix-flake-show)(1), [nix](/man/nix)(1)
