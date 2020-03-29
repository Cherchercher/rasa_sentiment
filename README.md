# rasa_addon

rasa_contrib is a addon package for [rasa](https://github.com/RasaHQ/rasa).
it does text classification of sentiment and emotion.

## component

Currently, it includes:

- sentiment_analysis

  TextCNN based sentiment analyzer, based on NLTK

- emotion_analysis

  Multi-channel, multi-label emotion analyzer, inspired by [tlkh](https://github.com/tlkh/text-emotion-classification)

## how to use it

Using the class path to the place where you should given a component name in config.yaml. This is a feature of rasa, see here for more document from rasa official document.

For example, your config.yml can be:

```yaml
language: "en"

pipeline:
  - name: "rasa_addon.nlu.analyzer.SentimentAnalyzer"
```
