# TAGLINE

ASCII 奶牛对话气泡生成器

# TLDR

**说出**消息

```cowsay ["Hello World"]```

**思考**消息

```cowthink ["Hmm..."]```

**换一头**奶牛

```cowsay -f [dragon] ["Message"]```

**列出**可用的奶牛

```cowsay -l```

**死亡**状态的奶牛

```cowsay -d ["Message"]```

# SYNOPSIS

**cowsay** [_options_] [_message_]

# DESCRIPTION

**cowsay** 生成一头说着消息的 ASCII 艺术奶牛。它是一个趣味程序，将文本显示在语音气泡中，并搭配各种动物的 ASCII 艺术，常用于搞笑消息、fortune 名言或 MOTD 展示。

该程序支持多个 "cow 文件"，代表不同的动物和角色，每个都有自己的 ASCII 图案。消息可以显示为说话（cowsay）或思考（cowthink），还可以通过不同的眼睛和舌头状态改变奶牛的外观。

cowsay 已成为 Unix 文化中的标志性存在，经常与 fortune 搭配显示随机名言，或与 lolcat 搭配产生彩色输出。虽然纯属娱乐，但它被广泛用于登录消息、shell 提示符和文档中，为命令行界面增添个性。

# PARAMETERS

**-f** _cowfile_
> 使用指定的 cow 文件。

**-l**
> 列出当前 COWPATH 上可用的 cow 文件。

**-e** _eyes_
> 设置眼睛外观（前两个字符；默认 **oo**）。

**-T** _tongue_
> 设置舌头外观（两个字符；默认为空白）。

**-W** _width_
> 自动换行列宽（默认 40）。

**-n**
> 禁用自动换行；按原样保留输入。

**-b**
> Borg 模式（眼睛 **==**）。

**-d**
> 死亡模式（眼睛 **XX**，舌头 **U**）。

**-g**
> 贪婪模式（眼睛 **$$**）。

**-p**
> 偏执模式（眼睛 **@@**）。

**-s**
> 嗑药模式（眼睛 **\*\***，舌头 **U**）。

**-t**
> 疲惫模式（眼睛 **--**）。

**-w**
> 兴奋模式（眼睛 **OO**）。

**-y**
> 年轻模式（眼睛 **..**）。

注意：如果同时给出任何模式标志，**-e** 和 **-T** 将被忽略。

# AVAILABLE COWS

列出全部：`cowsay -l`

常见角色：
- **default** - 经典奶牛
- **dragon** - 龙
- **tux** - 企鹅 Tux
- **elephant** - 大象
- **moose** - 驼鹿
- **stegosaurus** - 恐龙
- **vader** - 达斯·维达

# WORKFLOW

```bash
# Basic message
cowsay "Hello World"

# Thinking cow
cowthink "What to do..."

# Different animal
cowsay -f dragon "Roar!"

# Custom eyes and tongue
cowsay -e ^^ -T "U " "Happy cow"

# Dead cow
cowsay -d "I'm not feeling well"

# Pipe input
fortune | cowsay

# With lolcat
cowsay "Rainbow!" | lolcat
```

# RELATED COMMANDS

**cowthink**
> 思考中的奶牛（用思考气泡代替语音气泡）

**fortune | cowsay**
> 让奶牛说随机名言

# CUSTOMIZATION

自定义 cow 文件位于：`/usr/share/cowsay/cows/`

来创作你自己的 ASCII 艺术奶牛吧！

# CAVEATS

纯娱乐性质。过长的消息可能排版异常。自定义 cow 文件需要正确的格式。有人认为在严肃场合使用不够专业。原始版本用 Perl 编写，存在多种移植版。

# HISTORY

**cowsay** 由 Tony Monroe 于 **1999** 年编写，成为深受喜爱的 Unix 趣味程序，并启发了大量衍生作品。

# INSTALL

```dnf: sudo dnf install cowsay```

```pacman: sudo pacman -S cowsay```

```zypper: sudo zypper install cowsay```

```brew: brew install cowsay```

```nix: nix profile install nixpkgs#cowsay```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fortune](/man/fortune)(6), [figlet](/man/figlet)(6), [lolcat](/man/lolcat)(1)
