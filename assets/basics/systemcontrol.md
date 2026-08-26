# 系统控制

## 锁定屏幕
```[dbus-send](/man/dbus-send) --type=method_call --dest=org.freedesktop.ScreenSaver /ScreenSaver org.freedesktop.ScreenSaver.Lock```

## 解锁屏幕
```[dbus-send](/man/dbus-send) --type=method_call --dest=org.freedesktop.ScreenSaver /ScreenSaver org.freedesktop.ScreenSaver.SetActive boolean:false```

## 重启系统
```[reboot](/man/reboot)```
```[shutdown](/man/shutdown) -r```
```[systemctl](/man/systemctl) reboot```

## 关闭系统
```[poweroff](/man/poweroff)```
```[shutdown](/man/shutdown) -h now```
```[reboot](/man/reboot) -p```
```[systemctl](/man/systemctl) poweroff```
```[halt](/man/halt)```

## 在指定时间关机
```[shutdown](/man/shutdown) -h 18:45 "Server is going down for maintenance"```

## 停止蓝牙服务
```[service](/man/service) bluetooth stop```
```[systemctl](/man/systemctl) stop bluetooth```

## 启动蓝牙服务
```[service](/man/service) bluetooth start```
```[systemctl](/man/systemctl) start bluetooth```

## 停止 Wi-Fi 服务
```[nmcli](/man/nmcli) nm wifi off```

## 启动 Wi-Fi 服务
```[nmcli](/man/nmcli) nm wifi on```

## 关闭显示器
```[xset](/man/xset) dpms force off```

## 挂起系统
```[systemctl](/man/systemctl) suspend```
```[pm-suspend](/man/pm-suspend)```

## 休眠系统
```[systemctl](/man/systemctl) hibernate```

## 列出正在运行的服务
```[systemctl](/man/systemctl) list-units --type=service```
```[service](/man/service) --status-all```

## 启动某个服务
```[systemctl](/man/systemctl) start [serviceName]```
```[service](/man/service) [serviceName] start```

## 停止某个服务
```[systemctl](/man/systemctl) stop [serviceName]```
```[service](/man/service) [serviceName] stop```

## 设置服务开机自启
```[systemctl](/man/systemctl) enable [serviceName]```

## 查看服务日志
```[journalctl](/man/journalctl) -u [serviceName]```
