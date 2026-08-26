# TAGLINE

在本地为已安装的软件包打补丁

# TLDR

**准备一个待打补丁的软件包**

```bun patch [package-name]```

**准备特定版本**以待修补

```bun patch [package-name]@[1.2.3]```

**修改完成后提交补丁**

```bun patch --commit [package-name]```

**使用自定义的补丁目录提交**

```bun patch --commit [package-name] --patches-dir=[mypatches]```

**使用 node_modules 中软件包的路径**打补丁

```bun patch --commit node_modules/[package-name]```

# SYNOPSIS

**bun** **patch** [_options_] _package-name_

# PARAMETERS

**--commit** _path-or-pkg_
> 根据修改生成 .patch 文件。接受软件包名、name@version 或已修补软件包的路径。

**--patches-dir** _dir_
> 存储补丁文件的目录（仅与 --commit 一起使用）。默认：patches。

**-p, --production**
> 不安装 devDependencies

**--frozen-lockfile**
> 不允许更改 lockfile

**--dry-run**
> 不安装任何东西，只显示将要执行的操作

**--ignore-scripts**
> 跳过项目 package.json 中的生命周期脚本

**-f, --force**
> 始终从软件仓库请求最新版本并重新安装所有依赖

**--verbose**
> 启用详细日志输出

# DESCRIPTION

**bun patch** 允许你以可维护、对 Git 友好的方式持久地为 node_modules 打补丁。它会提取一个软件包供编辑，修改完成后，**--commit** 会创建一个 .patch 文件，该文件会在以后的安装中被应用。

补丁文件存储在一个 patches 目录中，并通过 package.json 中的 "patchedDependencies" 进行跟踪。它们可以提交到你的仓库中，并在多次安装、多个项目和多台机器上重复使用。

你可以提供软件包名称、精确版本（如果安装了多个版本），或者 node_modules 中该软件包的路径。

# CAVEATS

补丁存储在 patches 目录中，必须提交到版本控制。软件包更新时补丁可能会失效。

# SEE ALSO

[bun](/man/bun)(1), [bun-install](/man/bun-install)(1), [bun-add](/man/bun-add)(1), [bun-update](/man/bun-update)(1)
