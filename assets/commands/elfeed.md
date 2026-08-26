# TAGLINE

Emacs 的可扩展 RSS/Atom 订阅阅读器

# TLDR

**在 Emacs 中打开 Elfeed**

```M-x elfeed```

**更新所有订阅源**

```M-x elfeed-update```

**设置默认搜索过滤条件**

```(setq elfeed-search-filter "@6-months-ago +unread")```

**在配置中添加订阅源**

```(setq elfeed-feeds '("https://example.com/feed.xml" "https://blog.example.org/rss"))```

# DESCRIPTION

**Elfeed** 是 Emacs 的一个可扩展 RSS/Atom 订阅阅读器。它提供快速、键盘驱动的界面来阅读和管理订阅源，并支持通过 Emacs Lisp 进行打标签、搜索和自定义。

Elfeed 将订阅数据存储在本地数据库中，能高效支持数千个订阅源。它与 org-mode 等 Emacs 特性集成，可以使用 eww 或外部浏览器显示订阅内容。

# EMACS CONFIGURATION

```elisp
;; Add feeds
(setq elfeed-feeds
      '("https://news.ycombinator.com/rss"
        "https://planet.emacslife.com/atom.xml"
        ("https://example.com/blog" blog tech)))

;; With elfeed-org (org-mode integration)
(elfeed-org)
(setq rmh-elfeed-org-files '("~/.emacs.d/elfeed.org"))
```

# KEYBINDINGS

```
g         - Refresh view
G         - Update all feeds
s         - Edit search filter
b         - Open entry in browser
r         - Mark as read (remove unread tag)
u         - Mark as unread
+         - Add tag
-         - Remove tag
RET       - Open selected entry
n / p     - Next / previous entry
q         - Quit elfeed or close entry
```

# CONFIGURATION

**~/.emacs.d/init.el** 或 **~/.emacs**
> 使用 Emacs Lisp 配置订阅源和设置（setq elfeed-feeds）。

**~/.elfeed/**（默认数据库位置）
> 本地订阅数据库和缓存条目。

**~/.emacs.d/elfeed.org**（配合 elfeed-org）
> 使用 elfeed-org 集成时管理订阅源的 Org-mode 文件。

# CAVEATS

仅限 Emacs 的应用。要求 Emacs 24.3+。大量订阅源可能拖慢初始同步。不支持移动端同步（可通过 elfeed-protocol 使用 Fever/NewsBlur）。对不熟悉订阅源的 Emacs 用户有一定学习曲线。

# HISTORY

Elfeed 由 **Christopher Wellons**（skeeto）于 **2013 年**前后创建。它的设计目标是成为一个轻量级的 Emacs 原生订阅阅读器，充分发挥 Emacs 在文本处理和可扩展性方面的优势。

# INSTALL

```aur: yay -S elfeed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[emacs](/man/emacs)(1), [newsboat](/man/newsboat)(1)
