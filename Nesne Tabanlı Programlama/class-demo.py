# Comment isminde bir sınıf oluşturunuz.
# Commment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self,username, text, likes, dislikes):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = Comment('Ali Aluc', 'I like it :)', 5400, 42)
c2 = Comment('Saban Dalgic', 'Very poor man ahahaha', 2, 4261)
c3 = Comment('Kenan Yanik', 'Shut your big mouth man', 640, 890)
c4 = Comment('Steve Ronney', 'Such an ambitious performance', 54000, 31)
c5 = Comment('Collen Colley', 'If I were you, I would not do that', 54, 42)

comments = [c1,c2,c3,c4,c5]

for c in comments:
    print(f"{c.username}: {c.text} |{c.likes} , {c.dislikes}|")
