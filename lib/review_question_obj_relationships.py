# begin to build a simple program that models Instagram
# you should have a User class, a Photo class and a comment class


class User:
    def __init__(self, name):
        self.name = name


class Photo:
    all = []

    def __init__(self):
        self.comments = []
        Photo.all.append(self)

    def make_comment(self, text):
        self.comments.append(Comment(text))


class Comment:
    def __init__(self, text):
        self.text = text

    def all(self):
        return [comment.text for comment in Photo.all]


sandwich_photo = Photo()
sophie = User("Sophie")
sandwich_photo.user = sophie
sandwich_photo.user.name
# => "Sophie"
sophie.photos
# => [#<Photo:0x00007fae2880b370>]


sandwich_photo.comments
# => []

sandwich_photo.make_comment(
    "this is such a beautiful photo of your lunch!! I love photos of other people's lunch"
)
sandwich_photo.comments
# => [#<Comment:0x00007fae28043700>]

Comment.all
# => [#<Comment:0x00007fae28043700>]
