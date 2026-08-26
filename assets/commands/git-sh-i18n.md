# TAGLINE

Git shell 脚本的国际化支持库

# TLDR

**引入以获得 i18n 支持**

```. "$(git --exec-path)/git-sh-i18n"```

# SYNOPSIS

**git-sh-i18n**

# DESCRIPTION

**git-sh-i18n** 是一个 shell 脚本片段，供以 shell 脚本实现的 Git 高层命令通过 **.** 引入（source）。它为 GNU **gettext** 和 **eval_gettext** 函数提供封装——这些函数可通过 **gettext.sh** 脚本访问——并在没有 GNU gettext 的系统上提供直通式的回退实现。

**gettext** 函数翻译给定字符串并输出结果。**eval_gettext** 函数翻译带有变量占位符的字符串，并使用 **git-sh-i18n--envsubst** 对结果中的变量求值。它不是给最终用户用的，而是面向 Git 内部的 shell 脚本。

# CAVEATS

内部库，不是独立命令。Git 的 shell 脚本通过 **. "$(git --exec-path)/git-sh-i18n"** 引入。不打算供最终用户直接使用。在没有 GNU gettext 的系统上，这些函数是简单的直通实现，只会原样输出未翻译的字符串。

# HISTORY

git-sh-i18n 是 **Git** 国际化体系的一部分，让基于 shell 的 git 命令能够显示翻译后的消息。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-sh-setup](/man/git-sh-setup)(1), [gettext](/man/gettext)(1)
