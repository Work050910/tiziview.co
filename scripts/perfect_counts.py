# -*- coding: utf-8 -*-
import glob
import re

extra_tips = {
    'content/categories/airport-reviews/4k-streaming-netflix-airport.md': "\n\n### 影视发烧友进阶建议\n在 Apple TV 或电视盒子上观看时，建议开启客户端内置的 Fake-IP 模式与自动故障转移功能，确保在某条专线维护时能无缝自动切线，保障全家观影不被打断。\n",
    'content/categories/airport-reviews/chatgpt-native-ip-airport.md': "\n\n### 账号长效防封实用建议\n切记在同一台设备上固定使用同一个专线节点的地区登录 OpenAI 账号。尽量避免在短时间内跨国频繁切换节点，以防止触发 OpenAI 风控系统的异地登录保护。\n",
    'content/categories/airport-reviews/cross-border-remote-work-airport.md': "\n\n### 跨国远程协同网络安全小贴士\n对于经常使用 Zoom 或 Google Meet 进行跨国视频会议的远程团队，建议在路由器或客户端中将会议流量单独划归至低延迟专线策略组，实现高清音视频零卡顿。\n",
    'content/categories/airport-reviews/high-bandwidth-large-traffic-airport.md': "\n\n### 大文件传输优化指南\n在进行数十 GB 的跨国大文件下载或云盘同步时，推荐使用支持多线程下载的工具（如 Aria2），并选择离本地物理距离最近的香港或日本专线节点以拉满带宽。\n",
    'content/categories/airport-reviews/monthly-pay-cheap-airport.md': "\n\n### 月付用户省钱实用心法\n建议在日历中设置到期提醒，在套餐到期前两天核验当前线路的真实晚高峰体验。若体验满意可继续续费；若遇到突发降速则可随时从容更换其他优质服务。\n",
    'content/categories/airport-reviews/multi-device-family-office-airport.md': "\n\n### 多设备并发分配技巧\n在家庭或小型办公室环境下，可以将手机等移动设备连接至主干专线，电视盒子等大流量流媒体终端连接至大流量中继，实现带宽资源的合理最大化利用。\n",
    'content/categories/airport-reviews/trojan-protocol-stable-nodes.md': "\n\n### Trojan 协议排障小技巧\n若在连接 Trojan 节点时遇到证书报错提示，请首先检查本机系统时间是否精准同步。大多数证书错误均源于系统时钟与机房时钟偏差过大导致的握手失败。\n",
    'content/categories/ios/sing-box-ios-configuration.md': "\n\n### iOS 客户端后台保活技巧\n在 iPhone 设置中确认已开启后台 App 刷新，并在低电量模式下注意及时充电，以防止 iOS 系统底层为了节能而强制挂起代理数据隧道。\n",
    'content/categories/mac/mihomo-party-mac-complete-guide.md': "\n\n### Mac 菜单栏极简操作建议\n可以将常用的香港与日本节点设置为置顶收藏，这样在顶部状态栏点击图标时无需展开庞大的全局列表，一键即可完成无缝切线操作。\n",
    'content/categories/mac/sing-box-mac-tutorial.md': "\n\n### 提升终端开发效率小妙招\n在终端中使用 Git 或 Homebrew 时，配合 Sing-box 的系统网络扩展模式，无需单独配置 http_proxy 环境变量即可自动享受全系统层面的透明加速。\n",
    'content/categories/windows/sing-box-windows-client-guide.md': "\n\n### Windows 启动项优化建议\n将客户端设置为开机以系统服务模式静默启动，并在任务栏托盘中保留状态图标，既不干扰日常桌面视线，又能确保开机即刻畅享高速连接。\n"
}

for path, text_to_add in extra_tips.items():
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if "## 🏆 2026 核心机场推荐榜单" in content:
        parts = content.split("## 🏆 2026 核心机场推荐榜单")
        new_content = parts[0].strip() + text_to_add + "\n## 🏆 2026 核心机场推荐榜单" + parts[1]
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(new_content)

# Fix airport-node-timeout-fix.md which was 1205
timeout_path = 'content/categories/faq/airport-node-timeout-fix.md'
with open(timeout_path, 'r', encoding='utf-8') as fp:
    t_content = fp.read()
t_content = t_content.replace('很多小白此时第一反应就是“天塌了，机场肯定跑路了！”。', '')
t_content = t_content.replace('按照以下经过实战检验的“排错四步诊断法”逐一排查，绝大多数超时报错都能在几分钟内迎刃而解', '按照以下排错四步诊断法排查，绝大多数超时报错均可迎刃而解')
with open(timeout_path, 'w', encoding='utf-8') as fp:
    fp.write(t_content)

print("Tuned perfect counts.")
