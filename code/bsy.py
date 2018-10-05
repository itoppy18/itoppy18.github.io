from bs4 import BeautifulSoup, Comment

html = """
<html>
 <head>
   <title>タイトル</title>
   <script type="text/javascript"><![CDATA[
   alert('hoge');
   ]]>
   </script>
 </head>
 <body>
   <!-- コメント -->
   <h1>見出し</h1>
   <div>本文</div>
 </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")

# コメントタグの除去
for comment in soup(text=lambda x: isinstance(x, Comment)):
    comment.extract()

# scriptタグの除去
for script in soup.find_all('script', src=False):
    script.decompose()

# テキストだけの抽出
for text in soup.find_all(text=True):
    if text.strip():
        print(text)
