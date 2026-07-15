from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Please", "es": "Por favor"},
    {"en": "Word", "es": "Palabra"},
    {"en": "Package", "es": "Paquete"},
    {"en": "Day", "es": "Día"},
    {"en": "Week", "es": "Semana"},
    {"en": "Workday", "es": "Día de trabajo"},
    {"en": "Monday", "es": "Lunes"},
    {"en": "Tuesday", "es": "Martes"},
    {"en": "Wednesday", "es": "Miércoles"},
    {"en": "Thursday", "es": "Jueves"},
    {"en": "Friday", "es": "Viernes"},
    {"en": "Saturday", "es": "Sábado"},
    {"en": "Sunday", "es": "Domingo"},
    {"en": "Last", "es": "Último"},
    {"en": "Weekend", "es": "Fin de semana"},
    {"en": "Tired", "es": "Cansado"},
    {"en": "Idea", "es": "Idea"},
    {"en": "Polite", "es": "Cortesía, amabilidad"},
    {"en": "(to)Begin", "es": "Comenzar"},
    {"en": "(to)Get out of", "es": "Salir de"},
    {"en": "(to)Go home", "es": "Ir a casa"},
    {"en": "(to)Eat dinner", "es": "Cenar"},
    {"en": "Last night", "es": "Anoche"},
    {"en": "What kind?", "es": "¿Qué clase, que tipo?"},
    {"en": "Business school", "es": "Escuela de comercio"},
    {"en": "Too", "es": "También"},
    {"en": "Near", "es": "Cerca"},
    {"en": "Film", "es": "Película"},
    {"en": "French", "es": "Francés"},
    {"en": "Finally", "es": "Finalmente"},
    {"en": "Midnight", "es": "Media noche"},
    {"en": "Western", "es": "Del oeste"},
    {"en": "Movie", "es": "Cine"},
    {"en": "(to) Come in", "es": "Venir, entrar"},
    {"en": "(to) Put", "es": "Poner"},
    {"en": "Subjects", "es": "Materias"},
    {"en": "A long way", "es": "Lejos, distante"},
    {"en": "Old", "es": "Viejo"},
    {"en": "All right", "es": "Bien"},
    {"en": "(to) Start", "es": "Comenzar"},
    {"en": "(to) End", "es": "Finalizar"},
    {"en": "(to) Talk", "es": "Hablar"},
    {"en": "(to) Ask", "es": "Preguntar, pedir"},
    {"en": "(to) Assign", "es": "Asignar"},
    {"en": "(to) Finish", "es": "Finalizar"},
    {"en": "(to) Excuse", "es": "Disculpar"},
    {"en": "Yesterday", "es": "Ayer"},
    {"en": "High school", "es": "Secundaria"},
    {"en": "First", "es": "Primero"},
    {"en": "Second", "es": "Segundo"},
    {"en": "At noon", "es": "A medio día"},
    {"en": "Literature", "es": "Literatura"},
    {"en": "History", "es": "Historia"},
    {"en": "Homework", "es": "Tarea en casa"},
    {"en": "A great deal of", "es": "Una gran cantidad..."},
    {"en": "All", "es": "Todo (a)"},
    {"en": "Half", "es": "Mitad"},
    {"en": "Before", "es": "Antes"},
    {"en": "To", "es": "A, hacia, por, para"},
    {"en": "What is the matter?", "es": "¿Qué pasa?, ¿qué sucede?"},
    {"en": "That is too bad", "es": "Qué lástima"},
    {"en": "After", "es": "Después"},
    {"en": "(to) Be late", "es": "Estar retrasado"},
    {"en": "(to) Be busy", "es": "Estar ocupado"},
    {"en": "(to) Be absent", "es": "Estar ausente"},
    {"en": "(to) Be on vacation", "es": "Estar de vacaciones"},
    {"en": "(to) Be tired", "es": "Estar cansado"},
    {"en": "(to) Help", "es": "Ayudar"},
    {"en": "(to) Carry", "es": "Llevar, acarrear"},
    {"en": "(to) Get to", "es": "Llegar a"},
    {"en": "(to) Go over", "es": "Finalizar"},
    {"en": "(to) Understand", "es": "Entender"},
    {"en": "(to) Miss", "es": "Extrañar, perder"},
    {"en": "There was", "es": "Había, hubo"},
    {"en": "There were", "es": "Habían, hubieron"},
    {"en": "A lot of", "es": "Mucho(a) (os) (as)"},
    {"en": "Clerk", "es": "Dependiente"},
    {"en": "Several", "es": "Varios"},
    {"en": "How many?", "es": "¿Cuántos(as)?"},
    {"en": "What was the matter?", "es": "¿Qué sucedió?"},
    {"en": "(to)Wear", "es": "Vestir"},
    {"en": "(to)Rain", "es": "Llover"},
    {"en": "(to)Deliver", "es": "Entregar"},
    {"en": "(to)Receive", "es": "Recibir"},
    {"en": "(to)Sort", "es": "Clasificar"},
    {"en": "A few", "es": "Pocos"},
    {"en": "Minutes", "es": "Minutos"},
    {"en": "Woman", "es": "Mujer"},
    {"en": "Now", "es": "Ahora"},
    {"en": "Coat", "es": "Abrigo"},
    {"en": "Closet", "es": "Armario"},
    {"en": "Umbrella", "es": "Sombrilla"},
    {"en": "Cold", "es": "Frío"},
    {"en": "Late", "es": "Tarde"},
    {"en": "Mailman", "es": "Cartero"},
    {"en": "Mail", "es": "Correo"},
    {"en": "Month", "es": "Mes"},
    {"en": "Year", "es": "Año"},
    {"en": "January", "es": "Enero"},
    {"en": "February", "es": "Febrero"},
    {"en": "March", "es": "Marzo"},
    {"en": "April", "es": "Abril"},
    {"en": "May", "es": "Mayo"},
    {"en": "June", "es": "Junio"},
]


async def seed_page_2():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 2)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=2,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 2"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 2 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 2 already has {len(existing_vocab)} vocabulary items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for vocab_item in vocabulary_data:
                vocab = Vocabulary(
                    pages_id=page.id,
                    word=vocab_item["en"],
                    meaning=vocab_item["es"]
                )
                session.add(vocab)

            await session.commit()
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 2")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_2())
