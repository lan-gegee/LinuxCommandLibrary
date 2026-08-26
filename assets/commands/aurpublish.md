# TAGLINE

将软件包发布到 Arch 用户仓库（AUR）

# TLDR

将软件包**发布**到 AUR

```aurpublish [package_name]```

向当前仓库**添加 githooks**

```aurpublish setup```

# SYNOPSIS

**aurpublish** [_options_] [_package_]

# DESCRIPTION

**aurpublish** 用于简化将软件包发布到 Arch 用户仓库的流程。它会验证 PKGBUILD 完整性、生成 **.SRCINFO** 文件、创建提交信息模板，并处理推送到 AUR 的 git push。

该工具专为 AUR 软件包维护者设计，用于简化更新和发布工作流。

# SUBCOMMANDS

**setup**
> 在当前仓库中安装 git 钩子以执行自动化检查

# PARAMETERS

**-h, --help**
> 显示帮助信息

# CAVEATS

需要先配置好 AUR 的 SSH 访问。PKGBUILD 必须通过校验才能发布。已有的 **.SRCINFO** 文件会被自动重新生成。

# INSTALL

```pacman: sudo pacman -S aurpublish```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[makepkg](/man/makepkg)(8), [git](/man/git)(1), [pacman](/man/pacman)(8)
