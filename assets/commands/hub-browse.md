# TAGLINE

在 Web 浏览器中打开 GitHub 仓库页面

# TLDR

**在浏览器中打开仓库**

```hub browse```

**打开 issues 页面**

```hub browse -- issues```

**打开 pull request 页面**

```hub browse -- pulls```

**打开特定 issue**

```hub browse -- issues/[123]```

**打开 wiki**

```hub browse -- wiki```

**打开其他仓库**

```hub browse [owner/repo]```

**只打印 URL 而不打开浏览器**

```hub browse -u```

**将 URL 复制到剪贴板**

```hub browse -c```

# SYNOPSIS

**hub** **browse** [_options_] [_owner/repo_] [-- _subpage_]

# PARAMETERS

**-u**, **--url**
> 只打印 URL 而不打开浏览器。

**-c**, **--copy**
> 将 URL 复制到剪贴板。

**--**
> 子页面路径的分隔符。

# DESCRIPTION

**hub browse** 会在 Web 浏览器中打开 GitHub 仓库页面。你可以指定子页面，例如 issues、pulls、wiki、commits 或具体的文件路径。默认作用于当前仓库，也可以指定其他仓库。

# CAVEATS

Hub 已被弃用。建议改用 **gh browse**。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [gh-browse](/man/gh-browse)(1)
