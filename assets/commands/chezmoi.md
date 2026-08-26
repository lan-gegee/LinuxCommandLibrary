# TAGLINE

支持模板的跨平台 dotfile 管理器

# TLDR

**初始化** dotfiles

```chezmoi init```

**添加**文件到 dotfiles

```chezmoi add [~/.bashrc]```

**应用**更改

```chezmoi apply```

**编辑** dotfile

```chezmoi edit [~/.bashrc]```

从远程**更新**

```chezmoi update```

**显示**差异

```chezmoi diff```

# SYNOPSIS

**chezmoi** _command_ [_options_]

# DESCRIPTION

**chezmoi** 管理多台机器上的 dotfiles。它使用一个源目录（通常是 **~/.local/share/chezmoi** 处的 git 仓库）来存储 dotfiles 的目标状态，然后将该状态应用到主目录。

该工具支持用 Go 模板处理特定机器的配置，使单一源仓库能根据主机名、操作系统或自定义数据在不同机器上生成不同的文件。机密信息可通过与 1Password、Bitwarden、pass 等密码管理器的集成来管理，也可使用 age 或 gpg 加密文件。

与 GNU Stow 等基于符号链接的管理器不同，chezmoi 将文件复制到目标位置，因此目标文件是普通文件，可与任何工具配合使用。

# PARAMETERS

**init** [_repo_]
> 初始化 chezmoi

**add** _target_
> 将文件添加到源状态

**apply** [_target_]
> 将更改应用到目标位置

**edit** _target_
> 编辑源状态

**update**
> 拉取并应用更改

**diff** [_target_]
> 显示差异

**cd**
> 在源目录中打开 shell

**data**
> 显示模板数据

# FEATURES

- Git 集成
- 模板（Go templates）
- 特定机器的配置
- 机密管理（加密文件）
- 跨平台支持
- 自动初始化
- 试运行模式
- 脚本执行

# WORKFLOW

```bash
# Initialize with GitHub repo
chezmoi init https://github.com/username/dotfiles.git

# Add files to manage
chezmoi add ~/.bashrc
chezmoi add ~/.vimrc

# Edit managed file
chezmoi edit ~/.bashrc

# See what would change
chezmoi diff

# Apply changes
chezmoi apply

# Commit and push
chezmoi cd
git add .
git commit -m "Update dotfiles"
git push

# On new machine
chezmoi init --apply https://github.com/username/dotfiles.git
```

# TEMPLATING

使用模板处理特定机器的配置：
```
# .chezmoi.toml.tmpl
{{- if eq .chezmoi.hostname "work-laptop" }}
[data]
    email = "work@example.com"
{{- else }}
[data]
    email = "personal@example.com"
{{- end }}
```

# CONFIGURATION

**~/.config/chezmoi/chezmoi.toml**
> 主配置文件。设置源目录、合并工具、diff 设置、加密方式和密码管理器集成。

# CAVEATS

模板有一定学习曲线。Git 仓库默认公开（存放机密时应设为私有）。模板语法可能比较复杂。不适合大型二进制文件。需要理解 Go 模板。

# HISTORY

**chezmoi** 由 Tom Payne 于 **2018** 年创建，旨在提供一个现代化、灵活且支持模板和跨平台的 dotfile 管理器。

# INSTALL

```dnf: sudo dnf install chezmoi```

```pacman: sudo pacman -S chezmoi```

```apk: sudo apk add chezmoi```

```zypper: sudo zypper install chezmoi```

```brew: brew install chezmoi```

```nix: nix profile install nixpkgs#chezmoi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotfiles](/man/dotfiles)(1), [git](/man/git)(1), [stow](/man/stow)(1)

# RESOURCES

```[Source code](https://github.com/twpayne/chezmoi)```

```[Documentation](https://www.chezmoi.io/)```

<!-- verified: 2026-06-22 -->
