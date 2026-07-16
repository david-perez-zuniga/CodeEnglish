from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "July", "es": "Julio"},
    {"en": "August", "es": "Agosto"},
    {"en": "September", "es": "Septiembre"},
    {"en": "October", "es": "Octubre"},
    {"en": "November", "es": "Noviembre"},
    {"en": "December", "es": "Diciembre"},
    {"en": "(to) Graduate", "es": "Graduarse"},
    {"en": "College student", "es": "Estudiante universitario"},
    {"en": "Engineer", "es": "Ingeniero"},
    {"en": "University", "es": "Universidad"},
    {"en": "When?", "es": "¿Cuando?"},
    {"en": "Next year", "es": "El próximo año"},
    {"en": "Science", "es": "Ciencia"},
    {"en": "Math", "es": "Matemática"},
    {"en": "Course", "es": "Curso"},
    {"en": "Advanced physics", "es": "Física avanzada"},
    {"en": "Chemistry", "es": "Química"},
    {"en": "Over the weekend", "es": "Durante el fin de semana"},
    {"en": "Friends", "es": "Amigos"},
    {"en": "Exam", "es": "Examen"},
    {"en": "Weather", "es": "Tiempo climatológico"},
    {"en": "Sick", "es": "Enfermo"},
    {"en": "Anybody", "es": "Alguien, cualquiera"},
    {"en": "Nobody", "es": "Nadie"},
    {"en": "Alone", "es": "Solo"},
    {"en": "Letter", "es": "Carta"},
    {"en": "Post office", "es": "Oficina postal"},
    {"en": "That is too bad", "es": "Que lastima"},
    {"en": "I think so", "es": "Así lo creo"},
    {"en": "(to)Drive", "es": "Conducir"},
    {"en": "(to)Listen", "es": "Escuchar"},
    {"en": "(to)Hear", "es": "Oír"},
    {"en": "(to)Stop", "es": "Detenerse"},
    {"en": "(to)Direct", "es": "Dirigir"},
    {"en": "(to)Motion", "es": "Hacer señas"},
    {"en": "(to)Go ahead", "es": "Ir de frente"},
    {"en": "(to)Blow", "es": "Soplar"},
    {"en": "(to)Look for", "es": "Buscar"},
    {"en": "(to)Park", "es": "Parquear"},
    {"en": "(to)Find", "es": "Encontrar"},
    {"en": "Radio", "es": "Radio"},
    {"en": "Traffic", "es": "Tráfico"},
    {"en": "Report", "es": "Reporte"},
    {"en": "Red light", "es": "Luz roja"},
    {"en": "Policeman", "es": "Policía"},
    {"en": "Driver", "es": "Conductor"},
    {"en": "Horn", "es": "Bocina"},
    {"en": "Bad", "es": "Malo"},
    {"en": "Place", "es": "Lugar"},
    {"en": "Easy", "es": "Fácil"},
    {"en": "Difficult", "es": "Difícil"},
    {"en": "Parking place", "es": "Lugar de parqueo"},
    {"en": "Whose", "es": "De quién"},
    {"en": "Telephone", "es": "Teléfono"},
    {"en": "Typewriter", "es": "Máquina de escribir"},
    {"en": "There", "es": "Ahí"},
    {"en": "Small", "es": "Pequeño"},
    {"en": "Behind", "es": "Detrás de"},
    {"en": "Drawer", "es": "Gaveta"},
    {"en": "Top", "es": "La parte mas alta"},
    {"en": "Middle", "es": "En medio"},
    {"en": "Bottom", "es": "La parte mas baja"},
    {"en": "String", "es": "Cuerda, mecate"},
    {"en": "Envelope", "es": "Sobre de carta"},
    {"en": "Sunny", "es": "Soleado"},
    {"en": "Warm", "es": "Caluroso"},
    {"en": "Pleasant", "es": "Agradable"},
    {"en": "Season", "es": "Estación de tiempo"},
    {"en": "Nice", "es": "Agradable, placentero"},
    {"en": "(to) Work", "es": "Trabajar"},
    {"en": "(to) Go skiing", "es": "Ir a esquiar"},
    {"en": "(to)Snow", "es": "Nevar"},
    {"en": "(to)Swim", "es": "Nadar"},
    {"en": "(to)Ski", "es": "Esquiar"},
    {"en": "Vacation", "es": "Vacaciones"},
    {"en": "Two weeks off", "es": "2 semanas de vacaciones"},
    {"en": "Sports", "es": "Deportes"},
    {"en": "Ice skating", "es": "Patinaje sobre hielo"},
    {"en": "Hotel", "es": "Hotel"},
    {"en": "Mountains", "es": "Montañas"},
    {"en": "A lot", "es": "Muchos"},
    {"en": "Beach", "es": "Playa"},
    {"en": "Couple", "es": "Pareja"},
    {"en": "(to)Happen", "es": "Ocurrir, suceder"},
    {"en": "(to)Go down", "es": "Bajar, descender"},
    {"en": "(to)Go up", "es": "Subir, ascender"},
    {"en": "(to)Move", "es": "Mudarse, moverse"},
    {"en": "Company", "es": "Compañía"},
    {"en": "Building", "es": "Edificio"},
    {"en": "Skyscraper", "es": "Rascacielos"},
    {"en": "Downtown", "es": "Centro de la ciudad"},
    {"en": "High", "es": "Alto"},
    {"en": "Stories", "es": "Pisos"},
    {"en": "Ground floor", "es": "Planta baja"},
    {"en": "Shop", "es": "Tienda"},
    {"en": "Underground", "es": "Subterraneo, Clandestine"},
    {"en": "Elevator", "es": "Elevador"},
    {"en": "Convenient", "es": "Conveniente"},
    {"en": "Location", "es": "Ubicación"},
    {"en": "Subway station", "es": "Estación del metro"},
]


async def seed_page_3():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 3)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=3,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 3"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 3 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 3 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 3")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_3())
