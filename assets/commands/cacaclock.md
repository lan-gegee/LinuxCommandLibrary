# TAGLINE

在终端中以 ASCII 艺术形式显示时间

# TLDR

以 ASCII 艺术形式显示**时间**

```cacaclock```

更改**字体**

```cacaclock -f [font]```

更改时间**格式**

```cacaclock -d "[strftime_arguments]"```

# SYNOPSIS

**cacaclock** [_options_]

# DESCRIPTION

**cacaclock** 使用 libcaca 库在终端中以 ASCII 艺术形式显示当前时间。它用文本字符呈现出视觉效果独特的时钟。

显示格式可通过 strftime 格式说明符自定义。

# PARAMETERS

**-f, --font** _font_
> 使用指定的字体显示

**-d, --dateformat** _format_
> 时间格式，使用 strftime 说明符（如 %H:%M:%S）

# INSTALL

```apt: sudo apt install caca-utils```

```dnf: sudo dnf install caca-utils```

```apk: sudo apk add libcaca-apps```

```zypper: sudo zypper install caca-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cacademo](/man/cacademo)(1), [cacafire](/man/cacafire)(1), [cacaview](/man/cacaview)(1)

# RESOURCES

```[Source code](https://github.com/cacalabs/libcaca)```

<!-- verified: 2026-06-22 -->
