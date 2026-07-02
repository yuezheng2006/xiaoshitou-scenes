# Notice

## 项目性质

**小石头 IP 配图** 是作者的个人开源项目（Codex Skill + 文档 + 参考图），MIT 许可。

- 仅供学习与个人/团队内部配图工作流参考。
- **不代表**任何雇主或第三方的官方产品、品牌或对外发布物。

## 小石头 IP

**小石头 (Little Stone)** 为本仓库整理的原创配图角色规范（`#f39200` 胶囊体、flat 2D 简笔、物理动作叙事）。详见 `little-stone-scenes/references/common-little-stone-ip.md`。

## 上游致谢

双模式生图工作流改编自 Ian / helloianneo 的原始配图项目：

- 实物图模式：Ian / helloianneo 实物场景工作流。
- 手绘图模式：Ian / helloianneo 手绘解释工作流。

详见 [README.md](README.md#致谢)。

## 商标与品牌资产

- 小石头的 `#f39200` 取自雷石品牌橙，命名亦源自「雷石」；除这一层血脉外，本仓库默认**不展开雷石公司业务详情**，以避免敏感信息外泄。
- 仓库内保留一套**可选**品牌 Logo / 参考资产，**默认不启用**，也不在公开示例中展示；仅在用户明确要求工牌、展会或物料场景时使用。
- 仓库不应包含其他第三方注册商标、展会实拍或官方 Logo 源文件。
- 生成结果若涉及真实品牌、Logo 或商业标识，使用者需自行确保合规；本仓库不提供品牌授权。

## 仓库资产

| 路径 | 内容 |
| --- | --- |
| `little-stone-scenes/assets/brand/` | 小石头角色锚点，以及可选品牌 Logo / 参考资产（默认不启用） |
| `little-stone-scenes/assets/examples/` | 母版 `01`–`06` |
| `little-stone-scenes/assets/persona/` | 作者数字形象**风格化**资产（轻 Q 3D 规范说明图/动作扩展图、手绘版参考图），不含可识别真实肖像细节 |

安装 Skill 时复制整个 `little-stone-scenes/` 即可。仓库不包含、不分发任何真人照片；`assets/persona/private/` 保留在 `.gitignore` 中作为防线，防止真人照片被误提交。

## 历史遗留资产提醒

早期提交（`bd401b0`）中曾把一张作者真人照片 `assets/persona/author-persona-ref.jpg` 提交进公开仓库并推送。2026-07-02 已通过 `git filter-repo` 重写历史、彻底移除该文件并强制推送；当前仓库工作区与全部历史中均不再包含真人照片。若你持有更早的旧 clone，请删除后重新 clone。
