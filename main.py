from database import Database
from writeAJson import writeAJson
from personModel import BookModel
from cli import BookCLI

db = Database(database="relatorio_05", collection="livros")
booknModel = BookModel(database=db)


bookCLI = BookCLI(booknModel)
bookCLI.run()
