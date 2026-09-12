# Causette.Joli 商品名クイズ

新人バイト研修用。商品写真を見て Coeur de Fleur Nail Color の商品名（【 】内キーワード）を4択で当てるテスト。

## 使い方

`index.html` をブラウザで開くだけ（ダブルクリック可）。スマホでは AirDrop などで送って「ファイル」アプリから開く。

- 出題数を 10 / 20 / 全部 から選んで「はじめる」
- 写真タップで拡大
- 終了後、間違えた商品を復習リストで確認 → 「間違えた問題だけ復習」で再挑戦
- 自己ベストは端末内（localStorage）に保存

## データ

- 対象: Coeur de Fleur Nail Color 系 43点（通常 / BENI / SHUNKAN Series）
- 取得元: https://www.causettejoli.jp/view/category/all_items （2026-09 時点）
- 画像は causettejoli.jp の CDN を直接参照。**ネット接続が必要**。ダウンロードはしていない。

### データ更新のしかた

`index.html` 内の `RAW` 配列を編集する。1行 = `["【】内キーワード", "画像ファイル名", "normal|beni|shunkan"]`。
画像ファイル名は商品ページ画像URLの `itemimages/` 以降。

## 今後

- まずローカルで動作確認（この状態）
- OKなら新人へ配布（HTML1枚を渡す or 限定公開Webページ化）
