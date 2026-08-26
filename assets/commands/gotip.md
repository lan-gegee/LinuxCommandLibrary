# TAGLINE

来自 Go 开发树的每日构建版本

# TLDR

**运行** Go 开发版本

```gotip [go-commands]```

**安装**最新开发版本

```gotip download```

**构建**特定的 CL

```gotip download [CL-number]```

# SYNOPSIS

**gotip** [_options_] _command_

# PARAMETERS

**download** [_CL_]
> 获取并构建当前 Go 开发树到 **$HOME/sdk/gotip**。如果提供了 Gerrit 变更列表（change-list）编号，则会在构建前先应用该 CL。

任何其他参数都会原样传递给已安装的 gotip SDK 中的 **go** 工具，因此 **gotip build**、**gotip test**、**gotip env** 等命令都能直接使用。

# DESCRIPTION

**gotip** 提供来自 Go 开发树的每日构建版本。它让开发者能够在即将发布的特性与缺陷修复进入稳定版本之前先行测试。

与带版本号的 `go1.XX` 下载包装器不同，**gotip download** 会从 **golang/go** 仓库最新的 **master** 提交开始从源码构建工具链，因此需要一个可用的 Go 安装来进行引导。要刷新安装，删除 **~/sdk/gotip/.unpacked-success**（或整个目录）后重新运行 **gotip download** 即可。

# USAGE

安装最新开发版本：

```gotip download```

像普通 go 命令一样使用 gotip：

```gotip run main.go```
```gotip test ./...```
```gotip build```

# CAVEATS

开发版本可能不稳定。不建议用于生产环境。下载时需要联网。二进制文件体积较大。

# HISTORY

**gotip** 由 Go 团队创建，目的是让测试开发版本更加方便，取代了早期访问 Go 预发布版本的种种变通方法。

# INSTALL

```nix: nix profile install nixpkgs#gotip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1)
