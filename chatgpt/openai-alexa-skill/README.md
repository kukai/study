# openai-alexa-skill

OpenAI APIを叩いて自家製ChatGPTページを作る

## TODO

- [x] 資料に沿ってskill登録
- [x] 使ってみる
- コスト計測、計算
- slsを再検討、samやtfとの比較検討
  - 使いやすさ、簡潔さ
  - デバッグ方法の調査
  - 別タスクとして実施する方が良い

## Setup

```
sls alexa auth
sls deploy

sls alexa update
sls alexa build
# Alexa developer consoleのテストタブで状態を「開発中」にする
```