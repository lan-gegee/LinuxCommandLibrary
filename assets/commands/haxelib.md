# TAGLINE

Haxe 编程语言的软件包管理器

# TLDR

**安装库**

```haxelib install [library]```

**安装指定版本**

```haxelib install [library] [version]```

**从 zip 文件安装**

```haxelib install [file.zip]```

**更新单个库**

```haxelib update [library]```

**更新所有已安装的库**

```haxelib update```

**列出已安装的库**

```haxelib list```

**搜索库**

```haxelib search [query]```

**移除库**

```haxelib remove [library]```

**使用 git 仓库作为库**

```haxelib git [library] [https://github.com/user/repo.git]```

**将库指向本地开发目录**

```haxelib dev [library] [path/to/source]```

# SYNOPSIS

**haxelib** _command_ [_arguments_]

# SUBCOMMANDS

**install** _name_ [_version_]
> 从 haxelib 仓库或本地 zip 安装库。

**update** [_name_]
> 更新单个库；不指定名称时更新所有已安装的库。

**upgrade**
> 将所有已安装的库更新到最新版本。

**remove** _name_ [_version_]
> 移除已安装的库。

**list**
> 列出已安装的库及其版本。

**search** _query_
> 在 haxelib 仓库中搜索匹配 _query_ 的库。

**info** _name_
> 显示某个库的信息。

**run** _name_ [_args..._]
> 执行库的运行脚本。

**dev** _name_ _path_
> 将库指向本地开发目录。不传路径则清除指向。

**git** _name_ _url_ [_branch_]
> 使用 git 仓库作为库的来源。

**hg** _name_ _url_ [_branch_]
> 使用 mercurial 仓库作为库的来源。

**path** _name..._
> 打印给定库的源码路径、依赖关系和编译器 define。

**libpath** _name..._
> 打印每个库的根路径，每行一个。

**version**
> 打印 haxelib 版本。

**config**
> 打印 haxelib 仓库路径。

**setup** [_path_]
> 配置 haxelib 仓库路径。

**newrepo**
> 在当前目录创建本地仓库。

**deleterepo**
> 移除当前目录中的本地仓库。

**selfupdate**
> 更新 haxelib 自身。

# DESCRIPTION

**haxelib** 是 **Haxe** 编程语言的软件包管理器。它可以从 `lib.haxe.org` 中央注册表安装、更新和移除库，也支持从 git 或 mercurial 仓库以及本地 zip 压缩包安装库。

`dev` 命令将某个库指向本地工作副本，这是开发库并在其他项目中测试它的标准工作流。`newrepo` 命令创建项目专属的库目录，使每个项目都可以固定自己的依赖版本。

# CAVEATS

默认仓库是全系统共享的；如需项目级安装，请使用 `haxelib newrepo`。在区分大小写的文件系统上，库名称区分大小写。

# INSTALL

```apt: sudo apt install haxe```

```dnf: sudo dnf install haxe```

```pacman: sudo pacman -S haxe```

```apk: sudo apk add haxe```

```zypper: sudo zypper install haxe```

```brew: brew install haxe```

```nix: nix profile install nixpkgs#haxe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1)
