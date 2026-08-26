# TAGLINE

浏览 UNIX 用户和组的 TUI

# TLDR

**启动用户和组浏览器**

```ugm```

# SYNOPSIS

**ugm**

# DESCRIPTION

**ugm** 提供基于终端的界面，用于查看 UNIX 用户和组的信息。它让你通过键盘导航浏览用户列表、用户详情和组成员关系。使用 **Tab** 在用户视图和组视图之间切换，**/** 搜索，**q** 退出。对于需要快速直观查看用户与组数据的系统管理员尤其有用。

# CAVEATS

从系统数据库（/etc/passwd 和 /etc/group）读取用户和组信息。不支持修改用户或组；它是只读的。

# HISTORY

**ugm** 由 **ariasmn** 开发，使用 **Go** 和 Bubble Tea TUI 框架编写。

# INSTALL

```apk: sudo apk add ugm```

```nix: nix profile install nixpkgs#ugm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id](/man/id)(1), [groups](/man/groups)(1), [getent](/man/getent)(1)
