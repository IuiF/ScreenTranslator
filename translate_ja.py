#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys

# 英語→日本語の翻訳マッピング
translations = {
    # CaptureAreaEditor
    "Translate:": "翻訳:",
    "Save (can capture via hotkey)": "保存 (ホットキーでキャプチャ可能)",
    "Use auto corrections": "自動修正を使用",
    "Recognize:": "認識:",
    "⇵": "⇵",

    # CaptureAreaSelector
    "Right click on selection - customize\nLeft click on selection - process\nEnter - process all selections\nEsc - cancel\nCtrl - keep selecting": "右クリック - カスタマイズ\n左クリック - 処理\nEnter - すべて処理\nEsc - キャンセル\nCtrl - 選択を続ける",
    "Capture all": "すべてキャプチャ",
    "Cancel": "キャンセル",

    # Errors
    "Failed to init hunspell engine: %1": "Hunspellエンジンの初期化に失敗: %1",
    "No source language set": "ソース言語が設定されていません",
    "No target language set": "ターゲット言語が設定されていません",
    "Hunspell path not exists\n%1": "Hunspellパスが存在しません\n%1",
    "No .aff or .dic files for hunspell\nin %1": "Hunspell用の.affまたは.dicファイルがありません\n%1",

    # Main
    "OCR and translation tool": "OCR・翻訳ツール",
    "Screen translator started": "Screen Translatorが起動しました",
    "The last result was copied to the clipboard.": "最後の結果がクリップボードにコピーされました。",
    "Another instance is running. Lock file is busy.": "別のインスタンスが実行中です。ロックファイルがビジー状態です。",
    "Current version might be outdated.\nCheck for updates to silence this warning": "現在のバージョンが古い可能性があります。\nこの警告を消すには更新を確認してください",
    "Failed to set log file: %1": "ログファイルの設定に失敗: %1",
    "Incorrect settings found. Go to Settings": "不正な設定が見つかりました。設定を確認してください",
    "Updates available": "更新が利用可能です",

    # Languages
    "Afrikaans": "アフリカーンス語",
    "Albanian": "アルバニア語",
    "Amharic": "アムハラ語",
    "Arabic": "アラビア語",
    "Armenian": "アルメニア語",
    "Azerbaijani": "アゼルバイジャン語",
    "Basque": "バスク語",
    "Belarusian": "ベラルーシ語",
    "Bengali": "ベンガル語",
    "Bosnian": "ボスニア語",
    "Bulgarian": "ブルガリア語",
    "Burmese": "ミャンマー語",
    "Catalan": "カタルーニャ語",
    "Cebuano": "セブアノ語",
    "Chinese": "中国語",
    "Chinese (Simplified)": "中国語 (簡体字)",
    "Chinese (Traditional)": "中国語 (繁体字)",
    "Corsican": "コルシカ語",
    "Croatian": "クロアチア語",
    "Czech": "チェコ語",
    "Danish": "デンマーク語",
    "Dutch": "オランダ語",
    "English": "英語",
    "Esperanto": "エスペラント語",
    "Estonian": "エストニア語",
    "Filipino": "フィリピン語",
    "Finnish": "フィンランド語",
    "French": "フランス語",
    "Frisian": "フリジア語",
    "Galician": "ガリシア語",
    "Georgian": "ジョージア語",
    "German": "ドイツ語",
    "Greek": "ギリシャ語",
    "Gujarati": "グジャラート語",
    "Haitian Creole": "ハイチ・クレオール語",
    "Hausa": "ハウサ語",
    "Hawaiian": "ハワイ語",
    "Hebrew": "ヘブライ語",
    "Hindi": "ヒンディー語",
    "Hmong": "モン語",
    "Hungarian": "ハンガリー語",
    "Icelandic": "アイスランド語",
    "Igbo": "イボ語",
    "Indonesian": "インドネシア語",
    "Irish": "アイルランド語",
    "Italian": "イタリア語",
    "Japanese": "日本語",
    "Javanese": "ジャワ語",
    "Kannada": "カンナダ語",
    "Kazakh": "カザフ語",
    "Khmer": "クメール語",
    "Korean": "韓国語",
    "Kurdish": "クルド語",
    "Kyrgyz": "キルギス語",
    "Lao": "ラオ語",
    "Latin": "ラテン語",
    "Latvian": "ラトビア語",
    "Lithuanian": "リトアニア語",
    "Luxembourgish": "ルクセンブルク語",
    "Macedonian": "マケドニア語",
    "Malagasy": "マダガスカル語",
    "Malay": "マレー語",
    "Malayalam": "マラヤーラム語",
    "Maltese": "マルタ語",
    "Maori": "マオリ語",
    "Marathi": "マラーティー語",
    "Mongolian": "モンゴル語",
    "Nepali": "ネパール語",
    "Norwegian": "ノルウェー語",
    "Pashto": "パシュトー語",
    "Persian": "ペルシア語",
    "Polish": "ポーランド語",
    "Portuguese": "ポルトガル語",
    "Punjabi": "パンジャーブ語",
    "Romanian": "ルーマニア語",
    "Russian": "ロシア語",
    "Samoan": "サモア語",
    "Scots Gaelic": "スコットランド・ゲール語",
    "Serbian": "セルビア語",
    "Sesotho": "ソト語",
    "Shona": "ショナ語",
    "Sindhi": "シンド語",
    "Sinhala": "シンハラ語",
    "Slovak": "スロバキア語",
    "Slovenian": "スロベニア語",
    "Somali": "ソマリ語",
    "Spanish": "スペイン語",
    "Sundanese": "スンダ語",
    "Swahili": "スワヒリ語",
    "Swedish": "スウェーデン語",
    "Tajik": "タジク語",
    "Tamil": "タミル語",
    "Telugu": "テルグ語",
    "Thai": "タイ語",
    "Turkish": "トルコ語",
    "Ukrainian": "ウクライナ語",
    "Urdu": "ウルドゥー語",
    "Uzbek": "ウズベク語",
    "Vietnamese": "ベトナム語",
    "Welsh": "ウェールズ語",
    "Xhosa": "コサ語",
    "Yiddish": "イディッシュ語",
    "Yoruba": "ヨルバ語",
    "Zulu": "ズールー語",

    # ResultEditor
    "Close": "閉じる",
    "Copy translated": "翻訳をコピー",
    "Copy recognized": "認識結果をコピー",

    # SettingsEditor
    "Settings": "設定",
    "General": "全般",
    "This page contains general program settings": "このページにはプログラムの全般設定が含まれます",
    "Recognition": "認識",
    "This page contains text recognition settings. It shows the available languages that program can convert from image to text": "このページにはテキスト認識設定が含まれます。画像からテキストに変換できる利用可能な言語を表示します",
    "Correction": "修正",
    "This page contains recognized text correction settings. It allows to fix some errors after recognition.\nHunspell searches for words that are similar to recognized ones in its dictionary.\nUser correction allows to manually fix some frequently happening mistakes.\nUser correction occurs before hunspell correction if both are enabled": "このページには認識テキストの修正設定が含まれます。認識後の一部のエラーを修正できます。\nHunspellは辞書内で認識された単語と類似する単語を検索します。\nユーザー修正では頻繁に発生するミスを手動で修正できます。\n両方が有効な場合、ユーザー修正はHunspell修正の前に実行されます",
    "Translation": "翻訳",
    "This page contains settings, related to translation of the recognized text. Translation is done via enabled (checked) translation services. If one fails, then second one will be used and so on. If translator hangs it will be treated as failed after given timeout": "このページには認識テキストの翻訳に関する設定が含まれます。翻訳は有効化（チェック）された翻訳サービスを通じて行われます。1つが失敗した場合、2つ目が使用されます。翻訳サービスがハングした場合、指定されたタイムアウト後に失敗として扱われます",
    "Representation": "表示",
    "This page contains result representation settings": "このページには結果の表示設定が含まれます",
    "Update": "更新",
    "This page allow to install/update/remove program resources": "このページではプログラムリソースのインストール/更新/削除ができます",
    "Help": "ヘルプ",

    # General page
    "User Interface": "ユーザーインターフェース",
    "Language:": "言語:",
    "Shortcuts": "ショートカット",
    "Capture": "キャプチャ",
    "Repeat capture": "繰り返しキャプチャ",
    "Show last result": "最後の結果を表示",
    "Copy result to clipboard": "結果をクリップボードにコピー",
    "Capture saved areas": "保存エリアをキャプチャ",
    "Proxy": "プロキシ",
    "Type:": "種類:",
    "Address:": "アドレス:",
    "Port:": "ポート:",
    "User:": "ユーザー:",
    "Password:": "パスワード:",
    "save password (unsafe)": "パスワードを保存 (安全でない)",
    "Show message on program start": "プログラム起動時にメッセージを表示",
    "Run at system start": "システム起動時に実行",
    "Portable (store data in same folder)": "ポータブル (データを同じフォルダに保存)",
    "Write trace file": "トレースファイルを書き込む",
    "Disabled": "無効",
    "System": "システム",
    "SOCKS 5": "SOCKS 5",
    "HTTP": "HTTP",

    # Recognition page
    "Tessdata path:": "Tessdataパス:",
    "Default language:": "デフォルト言語:",

    # Correction page
    "Use auto corrections (hunspell)": "自動修正を使用 (hunspell)",
    "Hunspell dictionaries path:": "Hunspell辞書パス:",
    "Use user substitutions": "ユーザー置換を使用",
    "User substitutions": "ユーザー置換",

    # Translation page
    "Translate text": "テキストを翻訳",
    "Ignore SSL errors": "SSLエラーを無視",
    "Single translator timeout:": "単一翻訳サービスのタイムアウト:",
    " secs": " 秒",
    "Language:": "言語:",
    "Translators path:": "翻訳サービスパス:",
    "Translators": "翻訳サービス",
    "<b>NOTE! Some translators might require the translation window to be visible. You can make it using the \"Show translator\" entry in the tray icon's context menu</b>": "<b>注意! 一部の翻訳サービスは翻訳ウィンドウが表示されている必要があります。トレイアイコンのコンテキストメニューから「翻訳サービスを表示」を使用できます</b>",

    # Representation page
    "Result type": "結果の種類",
    "Tray": "トレイ",
    "Window": "ウィンドウ",
    "Result window": "結果ウィンドウ",
    "Font:": "フォント:",
    "Font size:": "フォントサイズ:",
    "Font color:": "フォントカラー:",
    "Background:": "背景:",
    "Show image": "画像を表示",
    "Show recognized": "認識結果を表示",
    "Sample text": "サンプルテキスト",

    # Update page
    "Update check interval (days):": "更新確認間隔 (日):",
    "0 - disabled": "0 - 無効",
    "Check now": "今すぐ確認",

    # About
    "<p>Optical character recognition (OCR) and translation tool</p>": "<p>光学文字認識 (OCR) および翻訳ツール</p>",
    "<p>Version: %1</p>": "<p>バージョン: %1</p>",
    "<p>Setup instructions: <a href=\"%1\">%1</a></p>": "<p>セットアップ手順: <a href=\"%1\">%1</a></p>",
    "<p>Changelog: <a href=\"%1\">%2</a></p>": "<p>変更履歴: <a href=\"%1\">%2</a></p>",
    "<p>License: <a href=\"%3\">MIT</a></p>": "<p>ライセンス: <a href=\"%3\">MIT</a></p>",
    "<p>Author: Gres (<a href=\"mailto:%1\">%1</a>)</p>": "<p>作者: Gres (<a href=\"mailto:%1\">%1</a>)</p>",
    "<p>Issues: <a href=\"%1\">%1</a></p>": "<p>課題: <a href=\"%1\">%1</a></p>",

    # Help text
    "The program workflow consists of the following steps:\n1. Selection on the screen area\n2. Recognition of the selected area\n3. Correction of the recognized text (optional)\n4. Translation of the corrected text (optional)\nUser interaction is only required for step 1.\nSteps 2, 3 and 4 require additional data that can be downloaded from the updates page.\n\nAt first start, go to the updates page and install desired recognition languages and translators and, optionally, hunspell dictionaries.\nThen set default recognition and translation languages, enable some (or all) translators and the \"translate text\" setting, if needed.": "プログラムのワークフローは以下のステップで構成されます:\n1. 画面領域の選択\n2. 選択領域の認識\n3. 認識テキストの修正 (オプション)\n4. 修正テキストの翻訳 (オプション)\nユーザーの操作が必要なのはステップ1のみです。\nステップ2、3、4には更新ページからダウンロードできる追加データが必要です。\n\n初回起動時は、更新ページに移動して希望する認識言語と翻訳サービス、およびオプションでHunspell辞書をインストールしてください。\nその後、デフォルトの認識言語と翻訳言語を設定し、必要に応じて翻訳サービスを有効化して「テキストを翻訳」設定を有効にしてください。",

    # SettingsValidator
    "No recognition language installed": "認識言語がインストールされていません",
    "No recognition language selected": "認識言語が選択されていません",
    "No translator installed": "翻訳サービスがインストールされていません",
    "No translator selected": "翻訳サービスが選択されていません",
    "No translation language selected": "翻訳言語が選択されていません",

    # SubstitutionsTable
    "Language": "言語",
    "Source": "ソース",
    "Target": "ターゲット",
    "\\ for \\ symbol, \\n for newline": "\\ は \\ 記号、\\n は改行を表します",

    # TrayIcon
    "Show settings": "設定を表示",
    "Show translator": "翻訳サービスを表示",
    "Quit": "終了",

    # Updater components
    "app": "アプリ",
    "recognizers": "認識エンジン",
    "correction": "修正",
    "translators": "翻訳サービス",

    # Portable mode
    "Portable changed. Apply settings first": "ポータブルモードが変更されました。先に設定を適用してください",
}

def translate_file(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    for context in root.findall('context'):
        for message in context.findall('message'):
            source_elem = message.find('source')
            translation_elem = message.find('translation')

            if source_elem is not None and translation_elem is not None:
                source_text = source_elem.text
                if source_text in translations:
                    translation_elem.text = translations[source_text]
                    if 'type' in translation_elem.attrib:
                        del translation_elem.attrib['type']

    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Translated {len(translations)} entries")

if __name__ == '__main__':
    input_file = '/home/iuif/dev/Advanced_Screen_Translator/share/translations/screentranslator_ja.ts'
    output_file = input_file
    translate_file(input_file, output_file)
