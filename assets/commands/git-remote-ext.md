# TAGLINE

外部命令传输辅助程序

# TLDR

**通过外部命令克隆**

```git clone "ext::[command] [args]"```

**配合自定义传输使用**

```git remote add myremote "ext::[transport-cmd] %S [host]"```

# SYNOPSIS

**git-remote-ext** _url_

# PARAMETERS

_URL_
> 带命令模板的 ext:: URL。

**%s**
> 替换为服务名（例如 `upload-pack`、`receive-pack`、`upload-archive`），不含 `git-` 前缀。

**%S**
> 替换为长服务名（例如 `git-upload-pack`），含 `git-` 前缀。

**%G**
> 作为第一个参数放置；抑制服务名参数，使远程命令可以接受额外的位置参数。

**%V**
> 仅可作为第二个参数；以环境设置的形式注入 Git 协议版本（例如 `version=2`）。

**%%**
> 字面百分号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git-remote-ext** 是一个远程辅助程序（remote helper），允许任意外部命令处理 Git 传输。`ext::` URL 方案指定用于通信的命令，从而支持自定义传输机制，如特定的 SSH 命令或非标准协议。

模板变量（如 `%s`、`%S`、`%G`）允许根据所请求的 Git 服务动态构造命令。该辅助程序通常不会被直接调用，而是通过远程配置中的 `ext::` URL 使用。

# CAVEATS

安全敏感：命令来自 URL。属于内部辅助程序，通常不直接使用。通过 ext:: URL 使用。

# HISTORY

git-remote-ext 是 **Git** 的远程辅助程序，通过任意命令执行实现自定义传输机制。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-remote](/man/git-remote)(1), [git-remote-fd](/man/git-remote-fd)(1)
