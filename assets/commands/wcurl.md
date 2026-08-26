# TAGLINE

简化下载操作的 curl 封装

# TLDR

**下载文件**

```wcurl [https://example.com/file.zip]```

**下载多个文件**

```wcurl [url1] [url2]```

**断点续传**

```wcurl -c [url]```

**指定输出文件名**

```wcurl -o [filename] [url]```

# SYNOPSIS

**wcurl** [_-c_] [_-o file_] [_options_] _urls_

# PARAMETERS

**-c**
> 继续/恢复下载。

**-o** _FILE_
> 输出文件名。

**--help**
> 显示帮助。

# DESCRIPTION

**wcurl** 是 curl 的轻量封装，为下载文件这一常见任务提供了合理的默认值。它会自动启用进度条、跟随重定向，并使用远程文件名作为输出名，从而免去为简单下载指定常见 curl 参数的麻烦。

断点续传支持让你无需手动配置 curl 的 range 选项即可继续中断的下载。可以指定多个 URL 以下载多个文件；当远程文件名不合适时，也可以提供自定义输出文件名。

该工具面向经常使用 curl 下载、但觉得其默认行为（输出到 stdout 且无进度提示）对这种用例不方便的用户。

# CAVEATS

只是 curl 的封装。灵活性较低。专注于下载场景。

# HISTORY

**wcurl** 为使用 curl 下载文件这一常见场景提供了更简单的接口。

# INSTALL

```apt: sudo apt install curl```

```dnf: sudo dnf install curl```

```pacman: sudo pacman -S curl```

```apk: sudo apk add curl```

```zypper: sudo zypper install curl```

```brew: brew install curl```

```nix: nix profile install nixpkgs#curl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [aria2c](/man/aria2c)(1)
