# TAGLINE

重现电影《Sneakers》（通天神偷）中的屏幕解密效果

# TLDR

**对管道输入的文本解密（按任意键揭示）**

```echo "[text]" | nms```

**自动解密，无需等待按键**

```echo "[text]" | nms -a```

**设置揭示文本的前景色**

```echo "[text]" | nms -f green```

**运行前清屏并在结束后恢复**

```ls -l | nms -c```

**除可见字符外也遮蔽空格**

```echo "[text]" | nms -s```

**解密某个命令的输出**

```curl -s wttr.in | nms -a -f cyan```

# SYNOPSIS

**nms** [_-acsv_] [**-f** _color_]

# PARAMETERS

**-a**
> 自动解密：立即开始揭示，无需等待按键。

**-s**
> 也遮蔽单个空格（制表符和换行符保持不遮蔽）。

**-f** _COLOR_
> 揭示文本的前景色。接受 `white`、`yellow`、`black`、`magenta`、`blue`（默认）、`green`、`red`、`cyan` 或 `#RRGGBB` 十六进制值。

**-c**
> 运行前清屏，完成后恢复终端状态。

**-v**
> 打印版本号并退出。

# DESCRIPTION

**nms**（"No More Secrets"）从标准输入读取文本，将其显示为随机噪点，然后逐字符动画式解密出原始内容，重现了 1992 年电影《Sneakers》中著名的数据解密场景。

由于从 stdin 读取数据，**nms** 可以自然地与管道组合，让你把这种效果叠加到任何命令的输出之上。该项目还附带一个配套程序 **sneakers**，提供电影场景的交互式终端版本。

# CAVEATS

纯粹是视觉效果——不会修改管道中的数据，只改变它的显示方式。需要支持 ANSI 转义序列且尺寸至少能容纳输入文本的终端。非常大的输入可能需要较长时间才能完全揭示；可用 **-a** 跳过按键暂停。

# HISTORY

**No More Secrets** 由 **Brian Barto** 创建，于 **2016 年**首次发布在 GitHub 上。它已成为 Linux 社区中流行的趣味工具，并被大多数主流发行版打包收录。

# INSTALL

```nix: nix profile install nixpkgs#nms```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [figlet](/man/figlet)(1), [cowsay](/man/cowsay)(1)
