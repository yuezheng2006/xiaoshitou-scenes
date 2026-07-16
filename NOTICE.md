# Notice

## 项目性质

`xiaoshitou-scenes` 是一个开源 Codex Skill 项目（核心包 + 文档 + 参考图），MIT 许可。

- 可用于学习、测试与配图工作流参考；商标、品牌资产与作者形象边界见下文。
- **不代表**任何雇主或第三方的官方产品、品牌或对外发布物。

## 默认 IP Profile

本仓库默认 profile 为 **default-little-stone**，其中 **小石头** 是原创配图角色规范（`#f39800` 胶囊体、flat 2D 简笔、物理动作叙事）。详见 `scene-skill-core/ip-profiles/default-little-stone/profile.md` 与 `scene-skill-core/ip-profiles/default-little-stone/character.md`。

无品牌角色路径：`scene-skill-core/ip-profiles/none/`。

**角色形象授权与 MIT 代码授权分离**，详见 [IP-NOTICE.md](IP-NOTICE.md)。

## 上游致谢

双模式生图工作流改编自 Ian / helloianneo 的原始配图项目：

- 实物图模式：Ian / helloianneo 实物场景工作流。
- 手绘图模式：Ian / helloianneo 手绘解释工作流。

详见 [README.md](README.md#致谢)。

## 商标与品牌资产

- 小石头的主色与命名有内部品牌来源；除这一层来源说明外，本仓库默认**不展开具体公司或业务详情**，以避免敏感信息外泄。
- 公开仓库不保留真实品牌 Logo 源文件；若用户明确要求工牌、展会或物料场景中的真实 Logo，需由用户在本地私有资产区自行提供并确认授权。
- 仓库不应包含其他第三方注册商标、展会实拍或官方 Logo 源文件。
- 生成结果若涉及真实品牌、Logo 或商业标识，使用者需自行确保合规；本仓库不提供品牌授权。

## 仓库资产

| 路径 | 内容 |
| --- | --- |
| `scene-skill-core/assets/masters/` | 母版 `01`–`06` |
| `scene-skill-core/ip-profiles/default-little-stone/assets/character/` | 默认主角色设定图、动作扩展与模式校准图 |
| `scene-skill-core/ip-profiles/default-little-stone/assets/persona/` | 老杨：全景 panorama、spec、actions、handdrawn；金渐层猫设定在 panorama |
| `scene-skill-core/ip-profiles/none/` | 无品牌角色 stub |

安装 Skill 时复制整个 `scene-skill-core/` 即可。仓库不应包含、不分发任何真人照片；`assets/persona/private/` 保留在 `.gitignore` 中作为防线，防止真人照片被误提交。

## 历史遗留资产提醒

早期提交（`bd401b0`）中曾把一张作者真人照片 `assets/persona/author-persona-ref.jpg` 提交进公开仓库并推送。2026-07-02 已通过 `git filter-repo` 重写历史、彻底移除该文件并强制推送。若你持有更早的旧 clone，请删除后重新 clone。发布前仍需复核当前 persona 规范图，确保其中不再包含照片级反例或可识别真人素材。
