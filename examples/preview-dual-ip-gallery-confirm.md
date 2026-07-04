# 双 IP Gallery 预览 · 人工确认清单

> **状态：待确认** — 确认前请勿 `git commit` / 勿当最终交付。

## 飞书在线预览

全文重建后打开：[小石头 IP 配图 Skill 使用指南](https://m2miovoqda.feishu.cn/docx/UZaWdBpyLoQi6Hx37TKcWx2rnmd)

重点看三节：

| 节 | 标题 | 本地样张 |
| --- | --- | --- |
| #15 | 双 IP · 知识卡主讲 | `assets/examples/gallery/gallery-dual-ip-knowledge-card.png` |
| #17 | 双 IP · 手绘分镜对比 | `assets/examples/gallery/gallery-dual-ip-handdrawn-comic-compare.png` |
| #18 | 双 IP · 手绘系统拆解 | `assets/examples/gallery/gallery-dual-ip-handdrawn-system-map.png` |

## Confirm Gate（Agent 自检摘要）

### #15 知识卡（v3b）

| 项 | 结果 |
| --- | --- |
| 小石头 L1–L4 / E1–E2 | PASS — 四格同胶囊比例，无嘴，白圆眼 |
| 老杨 P1–P7 | PASS — 正面线稿，浅框眼镜，米色 T |
| 跨图稳定（对 #17） | PASS — 同为 flat 线稿风（v3 写实版已弃用） |

### #17 分镜对比（v5）

| 项 | 结果 |
| --- | --- |
| 小石头 | PASS — 无嘴，失败/修正靠动作+汗滴 |
| 老杨 | PASS — 浅灰框，左兜+右持马克笔 |

### #18 系统拆解（v5b，锚 #17）

| 项 | 结果 |
| --- | --- |
| 小石头 A/B | PASS — 形体一致，分工不同 |
| 老杨 | PASS — 与 #17 同套 IP（穿搭/姿势/框型） |

**批次结论：`CONFIRMED`（待你肉眼复核）**

## 人工确认打勾

- [ ] 飞书 #15 / #17 / #18 三节图与文案对齐
- [ ] 三节老杨 **跨图** 像同一人（眼镜/发型/穿搭/线稿风）
- [ ] 小石头 **无嘴**，四肢锚点正常
- [ ] 无 prompt 泄漏词（如 SERIES BATCH LOCK）
- [ ] 同意将当前 gallery 三图 + 规则改动一并提交

## 确认后操作（由你发起）

```bash
# 1. 若飞书需再同步（改图后）
bash _feishu-update.sh

# 2. 你确认后再 commit（示例）
git add assets/examples/gallery/gallery-dual-ip-*.png \
        scene-skill-core/references/common-character-lock.md \
        scene-skill-core/references/handdrawn-qa-checklist.md \
        scene-skill-core/references/physical-qa-checklist.md \
        scene-skill-core/references/common-qa-repair.md \
        scene-skill-core/references/common-generation-templates.md \
        scene-skill-core/references/knowledge-card-mode.md \
        scene-skill-core/ip-profiles/default-little-stone/character.md \
        scene-skill-core/ip-profiles/default-little-stone/persona-author-identity.md \
        scene-skill-core/SKILL.md \
        examples/preview-dual-ip-gallery-confirm.md \
        _feishu-update.sh _feishu-doc-intro.xml
git commit -m "..."
```

## 生成版本留档（Cursor assets，未入仓）

| 文件 | 说明 |
| --- | --- |
| `gallery-dual-ip-knowledge-card-v3b.png` | #15 采用 |
| `gallery-dual-ip-handdrawn-comic-compare-v5.png` | #17 采用 |
| `gallery-dual-ip-handdrawn-system-map-v5b.png` | #18 采用 |
| `v3` / `v4` / `v5` 其他 | 弃用或仅作对比 |

---

## 全身 IP 样张（新增 · 待确认）

路径均在 `assets/examples/gallery/`：

| 文件 | 用途 | Agent 自检 |
| --- | --- | --- |
| `gallery-dual-ip-fullbody-handdrawn-stand.png` | 双 IP 全身并列 ·「老杨讲，小石头干」 | PASS |
| `gallery-dual-ip-fullbody-handdrawn-walkthrough.png` | 全身 · 老杨指流程 + 小石头拉反馈 | PASS |
| `gallery-dual-ip-fullbody-handdrawn-handoff.png` | 全身 · 老杨蹲身递卡协作 | PASS |
| `gallery-dual-ip-fullbody-physical-stand.png` | 实物 · 风格化 3D 老杨 + flat 小石头同框 | PASS |
| `gallery-little-stone-fullbody-actions-row.png` | 小石头全身五动作（站/跑/拉/接/倔） | PASS |

- [ ] 手绘三张老杨与 #17 线稿风一致
- [ ] 小石头全身无嘴、胶囊比例批内一致
- [ ] 实物同框小石头仍为 flat 2D 贴纸（非 3D 灰石）

确认后 `git add` 时一并加入 `gallery-dual-ip-fullbody-*.png` 与 `gallery-little-stone-fullbody-actions-row.png`。
