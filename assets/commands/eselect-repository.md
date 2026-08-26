# TAGLINE

Gentoo ebuild 软件仓库配置

# TLDR

**列出**所有 ebuild 软件仓库

```eselect repository list```

列出**已启用**的软件仓库

```eselect repository list -i```

**启用**一个软件仓库

```eselect repository enable [name|index]```

**添加**一个未注册的软件仓库

```eselect repository add [name] [git|rsync|svn] [sync_uri]```

**禁用**软件仓库但保留其内容

```eselect repository disable [repo1] [repo2]```

**移除**软件仓库及其内容

```eselect repository remove [repo1] [repo2]```

**创建**一个本地软件仓库

```eselect repository create [name] [path/to/repo]```

# SYNOPSIS

**eselect repository** _action_ [_options_]

# DESCRIPTION

**eselect repository** 为 Gentoo 系统上的 Portage 配置 ebuild 软件仓库。它可以启用、禁用、添加或移除 Gentoo 软件仓库列表中的仓库。

启用软件仓库后，运行 `emerge --sync repo_name` 下载 ebuild。

# PARAMETERS

**list**
> 列出所有已注册的软件仓库

**-i**
> 只显示已安装/启用的仓库

**enable** _repo_
> 启用一个软件仓库

**disable** _repo_
> 禁用但不移除内容

**remove** _repo_
> 禁用并移除内容

**add** _name_ _type_ _uri_
> 添加未注册的软件仓库

**create** _name_ _path_
> 创建本地软件仓库

# CAVEATS

仅适用于 Gentoo Linux。启用软件仓库后必须进行同步。属于 app-eselect/eselect-repository 软件包。

# SEE ALSO

[eselect](/man/eselect)(1), [emerge](/man/emerge)(1), [emaint](/man/emaint)(1)

# RESOURCES

```[Source code](https://github.com/gentoo/eselect-repository)```

```[Documentation](https://wiki.gentoo.org/wiki/Eselect/Repository)```

<!-- verified: 2026-07-14 -->
