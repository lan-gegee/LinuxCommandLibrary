# TAGLINE

管理 GitHub CLI 的设置与偏好

# TLDR

**获取配置值**

```gh config get [key]```

**设置配置值**

```gh config set [key] [value]```

**列出全部配置**

```gh config list```

**设置默认编辑器**

```gh config set editor [vim]```

**设置默认浏览器**

```gh config set browser [firefox]```

# SYNOPSIS

**gh config** _command_ [_options_]

# PARAMETERS

**get** _KEY_
> 获取配置值。

**set** _KEY_ _VALUE_
> 设置配置值。

**list**
> 列出所有配置项。

**--host** _HOSTNAME_
> 应用于特定的 GitHub 主机。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh config** 管理 GitHub CLI 的配置。它控制偏好编辑器、浏览器、默认提示方式、协议选择等行为设置。

配置按主机存储，因此 github.com 和 GitHub Enterprise 实例可以有不同的设置。设置可以是特定环境的或全局的。

常见设置包括 git_protocol（https/ssh）、editor、browser 和 pager。

# CONFIGURATION

**~/.config/gh/config.yml**
> 主配置文件，存放用户偏好、默认设置和按主机的配置。

# CAVEATS

配置保存在 ~/.config/gh/config.yml 中。环境变量可能覆盖设置。某些设置需要重新认证才能生效。

# HISTORY

gh config 是 **GitHub CLI** 的一部分，遵循 Unix 系统上的 XDG Base Directory 规范提供用户自定义能力。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-auth](/man/gh-auth)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_config)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
