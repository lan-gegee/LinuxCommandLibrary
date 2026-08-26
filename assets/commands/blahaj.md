# TAGLINE

用骄傲旗配色为文本着色并打印鲨鱼

# TLDR

**显示一只彩色鲨鱼**

```blahaj --shark```

**显示一面骄傲旗**

```blahaj --flag```

**为输入文本着色**（跨性别旗配色）

```echo "[text]" | blahaj```

**用指定的旗帜配色**着色

```echo "[text]" | blahaj --colors [rainbow]```

**为单个单词**着色

```echo "[text]" | blahaj --words```

**为背景着色**而非文字

```echo "[text]" | blahaj --background```

**列出所有可用旗帜**

```blahaj --flags```

**使用随机配色方案**

```echo "[text]" | blahaj --random```

# SYNOPSIS

**blahaj** [_options_] [_text_]

# DESCRIPTION

**blahaj** 是一个类似 lolcat 的命令行工具，使用骄傲旗配色为文本输入着色，并可显示 ASCII 艺术鲨鱼。它以宜家（IKEA）广受欢迎的鲨鱼玩偶命名，为你的终端带来缤纷色彩。

该工具可以使用各种骄傲旗配色方案按字符、单词或行为文本着色，还可以用 ASCII 艺术展示深受喜爱的 BLAHAJ 鲨鱼。

# PARAMETERS

**-s, --shark**
> 显示 BLAHAJ 鲨鱼 ASCII 艺术

**-f, --flag**
> 显示一面骄傲旗

**-c, --colors** _flag_
> 使用的配色方案（默认：trans）

**-r, --random**
> 使用随机配色方案

**-i, --individual**
> 为单个字符着色

**-w, --words**
> 为单个单词着色

**-b, --background**
> 为背景着色而非文字

**-m, --multiplier** _n_
> 旗帜尺寸的倍率

**--flags**
> 列出所有可用的配色方案/旗帜

**-h, --help**
> 显示帮助信息

# AVAILABLE FLAGS

常见配色方案包括：trans、rainbow、gay、lesbian、bi、pan、nonbinary、ace、aro、genderqueer、genderfluid 等等。

# CAVEATS

输出需要支持 ANSI 颜色代码的终端。某些配色方案在颜色支持有限的终端上可能无法正确显示。该工具主要用于娱乐和终端个性化。

# HISTORY

BLAHAJ 由 **GeopJr** 创建，是一个有趣的终端工具，灵感来自 lolcat 以及宜家 BLAHAJ 鲨鱼玩偶的爆红人气，尤其在 LGBTQ+ 社群中。目前存在 Crystal、Node.js 和 Rust 等多种实现。

# INSTALL

```nix: nix profile install nixpkgs#blahaj```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lolcat](/man/lolcat)(1), [figlet](/man/figlet)(1), [cowsay](/man/cowsay)(1)

# RESOURCES

```[Source code](https://codeberg.org/GeopJr/BLAHAJ)```

<!-- verified: 2026-06-19 -->
