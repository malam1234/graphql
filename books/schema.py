import graphene
from graphene_django import DjangoObjectType
from .models.books import Books

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "author", "date", "published_date")

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    book = graphene.Field(BooksType, id=graphene.Int(required=True))

    def resolve_all_books(root, info):
        return Books.objects.all()

    def resolve_book(root, info, id):
        try:
            return Books.objects.get(pk=id)
        except Books.DoesNotExist:
            return None


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        date = graphene.types.datetime.Date(required=False)
        published_date = graphene.types.datetime.Date(required=True)

    book = graphene.Field(BooksType)

    def mutate(self, info, title, author, published_date, date=None):
        book = Books(title=title, author=author, published_date=published_date, date=date)
        book.save()
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
