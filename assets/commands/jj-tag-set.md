# TAGLINE

创建或更新指向某修订的标签

# TLDR

在当前修订上创建标签

```jj tag set [tagname]```

在特定修订上创建标签

```jj tag set [tagname] -r [revision]```

# SYNOPSIS

**jj** **tag** **set** [_options_] _name_

# PARAMETERS

**-r**, **--revision** _rev_
> 要打标签的修订。

# DESCRIPTION

**jj tag set** 创建或更新指向某修订的标签。标签是指向特定提交的轻量级引用，适合标记发布点或重要提交。默认为当前工作副本的父修订打标签。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-tag](/man/jj-tag)(1), [jj-tag-delete](/man/jj-tag-delete)(1)
