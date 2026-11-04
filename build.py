"""Timepie のサイト（トップ・プライバシーポリシー・サポート）を書き出す。問い合わせ先は EMAIL を変えて流し直す。"""
EMAIL = 'timepie.app@gmail.com'
OPERATOR = 'Timepie 開発者'
ENACTED = '2026年11月5日'

def mail():
    return f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

def page(file, title, current, body):
    links = ''.join(
        f'<a href="{href}"{" aria-current=page" if href == current else ""}>{label}</a>'
        for href, label in [('privacy.html', 'プライバシー'), ('support.html', 'サポート')])
    html = f'''<!DOCTYPE html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="icon" href="icon.svg"><link rel="stylesheet" href="style.css"></head>
<body><div class="wrap">
<nav><a href="./"><img src="icon.svg" alt=""></a><a class="name" href="./">Timepie</a><div class="links">{links}</div></nav>
{body}
<footer><span>© 2026 {OPERATOR}</span><a href="privacy.html">プライバシーポリシー</a><a href="support.html">サポート</a></footer>
</div></body></html>
'''
    open(file, 'w').write(html)

page('index.html', 'Timepie — 稼働時間と収入を、押すだけで記録', './', '''
<div class="hero"><img src="icon.svg" alt="Timepie のアイコン"><h1>Timepie</h1>
<p class="lead">稼働時間と収入を、押すだけで記録</p>
<span class="badge">App Store で近日公開</span></div>
<div class="feats">
<div class="feat"><b>押すだけで計測</b><span>クライアントのカードを押して開始、もう一度押して停止</span></div>
<div class="feat"><b>今月の収入がすぐ分かる</b><span>時給・丸め・税の設定から、その場で計算</span></div>
<div class="feat"><b>ウィジェットとロック画面</b><span>アプリを開かずに始めて、止められる</span></div>
<div class="feat"><b>月末の明細は PDF で</b><span>クライアントごとの稼働明細を出力</span></div>
<div class="feat"><b>機種を変えても、そのまま</b><span>Apple でログインすると、無料でクラウドに保存</span></div>
<div class="feat"><b>買い切りの Pro</b><span>クライアントを何件でも。月の目標と年のまとめも</span></div>
</div>
''')

page('privacy.html', 'プライバシーポリシー — Timepie', 'privacy.html', f'''
<h1>プライバシーポリシー</h1>
<p class="meta">運営者：{OPERATOR}　／　制定日：{ENACTED}</p>
<p style="margin-top:18px">Timepie（以下「このアプリ」）が、どんな情報をどこに置き、何に使うかを説明します。</p>

<h2>1. サインインしないで使う場合</h2>
<p>記録はすべてこの端末の中に保存します。運営者にも、ほかの会社にも送りません。</p>
<p>購入（買い切り）は Apple の App Store が扱います。運営者は支払いの情報を受け取りません。</p>

<h2>2. サインインして「クラウドに保存」を使う場合に預かる情報</h2>
<p>設定の「クラウドに保存」で Apple でサインインすると、ほかの端末と同じ記録を使えるように、次の情報をクラウドに保存します。</p>
<ul>
<li>サインインした利用者を見分ける番号（Apple から名前とメールアドレスは受け取りません）</li>
<li>記録：開始・終了・休憩の時刻、メモ</li>
<li>クライアント：名前、宛名、色、画像、時給、丸めと税の設定、書き出した月の金額</li>
<li>作業の種類</li>
<li>発行者情報：氏名または屋号、登録番号、住所、メールアドレス（入力した項目だけ）</li>
<li>月の目標</li>
<li>最後に書き込んだ端末の種類（iPhone か iPad か）</li>
</ul>
<p>また、クラウドとやり取りするときに、端末の種類・OS・アプリの情報が Google に送られます。これは Google がサービスの改善に使うもので、上の情報とは結び付けられません。</p>
<p>不正な利用を防ぐため、クラウドとやり取りするときに、このアプリが正しいものかを Apple の App Attest で確かめ、その結果を Google の Firebase App Check に送ります。この確かめには、上の情報は使いません。</p>

<h2>3. 何に使うか</h2>
<p>ほかの端末との同期と、機種変更のときの引き継ぎだけに使います。広告・分析には使わず、売ることもしません。</p>

<h2>4. どこに置くか</h2>
<p>Google の Firebase（Firebase Authentication と Cloud Firestore）に置きます。置き場所は米国です。</p>
<p>Google での扱いは、<a href="https://policies.google.com/privacy">Google のプライバシーポリシー</a>と <a href="https://firebase.google.com/support/privacy">Firebase のプライバシーとセキュリティの説明</a>をご覧ください。</p>
<p>法令にもとづく場合を除き、ほかの会社に渡しません。</p>

<h2>5. 消し方</h2>
<ul>
<li><b>記録などを1件消す</b>：クラウドからもすぐに消えます。ただし、消したものの識別番号・消した時刻・消した端末の種類だけは、ほかの端末に「消した」と伝えるために残ります（中身は残りません）。</li>
<li><b>ログアウト</b>：クラウドの記録も、端末の記録も残ります。</li>
<li><b>アカウントを削除</b>（設定の「クラウドに保存」の画面から）：クラウドの記録とアカウントを消し、Apple でのサインインの連携を取り消します。クラウドには、アカウントの番号と「削除した」という印だけが残ります（記録の中身は残りません）。各端末の記録は残ります。</li>
<li><b>端末の記録を消す</b>：このアプリを削除すると、端末の記録も消えます。</li>
</ul>

<h2>6. お問い合わせ</h2>
<p>このポリシーと、預かった情報の扱いについてのお問い合わせは、{mail()} までお送りください。運営者の住所などは、お求めがあれば遅滞なくお答えします。</p>

<h2>7. このポリシーを変えるとき</h2>
<p>変えるときは、このページで知らせます。</p>
''')

page('support.html', 'サポート — Timepie', 'support.html', f'''
<h1>サポート</h1>
<p>困ったときは、まず下のよくある質問をご覧ください。解決しないときは、{mail()} までお送りください。</p>

<h2>よくある質問</h2>
<h3>ログインしないで使えますか？</h3>
<p>使えます。記録はこの iPhone の中に保存されます。クラウドに保存したいときだけ、Apple でログインしてください。</p>

<h3>機種を変えたとき、記録を引き継ぐには？</h3>
<p>前の iPhone で、設定 → クラウドとバックアップ → クラウドに保存 から Apple でログインしておきます。新しい iPhone でも同じ Apple Account でログインすると、記録が戻ります。クラウドに保存しない場合は、設定 → クラウドとバックアップ の「バックアップを書き出す」で作ったファイルから復元できます。</p>

<h3>無料で使える範囲は？</h3>
<p>クライアント2件までなら、計測・記録・レポート・明細の出力・クラウドに保存をすべて無料で使えます。Timepie Pro（買い切り）を買うと、クライアントを何件でも登録でき、月の目標と年のまとめも使えます。</p>

<h3>機種を変えたら Pro が使えなくなりました</h3>
<p>設定の Timepie Pro の欄にある「購入を復元」を押してください。購入したときと同じ Apple Account で App Store にサインインしている必要があります。</p>

<h3>ホーム画面にウィジェットを置くには？</h3>
<p>ホーム画面の空いているところを長押しして「編集」→「ウィジェットを追加」から Timepie を選びます。ロック画面とコントロールセンターにも置けます。</p>

<h3>アカウントを削除するには？</h3>
<p>設定 → クラウドとバックアップ → クラウドに保存 →「アカウントを削除」から消せます。クラウドの記録は消えますが、iPhone の中の記録は残ります。くわしくは<a href="privacy.html">プライバシーポリシー</a>の「5. 消し方」をご覧ください。</p>

<h2>お問い合わせ</h2>
<div class="box"><p>メール：{mail()}</p><p class="meta">お使いの iPhone の機種と iOS のバージョン、アプリのバージョン（設定のいちばん下）を添えていただけると、早くお答えできます。</p></div>
''')
print('ok')
