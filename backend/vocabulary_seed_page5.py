from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to)Approve", "es": "Aprobar"},
    {"en": "Sister", "es": "Hermana"},
    {"en": "Just", "es": "Justamente"},
    {"en": "Research", "es": "Investigación"},
    {"en": "Chemist", "es": "Químico"},
    {"en": "Birthday", "es": "Cumpleaños"},
    {"en": "Adviser", "es": "Consejero"},
    {"en": "Schedule", "es": "Horario"},
    {"en": "Grades", "es": "Notas, calificaciones"},
    {"en": "In addition to", "es": "Además de"},
    {"en": "Office", "es": "Oficina"},
    {"en": "(to)Stay at home", "es": "Permanecer en casa"},
    {"en": "(to)Feel", "es": "Sentir"},
    {"en": "(to)See", "es": "Ver"},
    {"en": "(to)Say", "es": "Decir"},
    {"en": "(to)Send", "es": "Enviar"},
    {"en": "(to)Order", "es": "Ordenar"},
    {"en": "(to)Get dirty", "es": "Ensuciarse"},
    {"en": "(to)Get hot", "es": "Hacer calor"},
    {"en": "(to)Be careful", "es": "Ser cuidadoso"},
    {"en": "(to)Hurt", "es": "Lastimar"},
    {"en": "(to)Handle", "es": "Manejar, Manipular"},
    {"en": "(to)Relax", "es": "Relajarse"},
    {"en": "All day", "es": "Todo el día"},
    {"en": "Office supplies", "es": "Suministro de oficina"},
    {"en": "Inventory", "es": "Inventario"},
    {"en": "Anyone", "es": "Alguien, cualquiera"},
    {"en": "Speed limit", "es": "Límite de velocidad"},
    {"en": "Miles", "es": "Millas"},
    {"en": "Per hour", "es": "Por hora"},
    {"en": "At home", "es": "En casa"},
    {"en": "Far", "es": "Lejos"},
    {"en": "Heart", "es": "Corazón"},
    {"en": "(to)Bother", "es": "Molestar"},
    {"en": "(to)Go out", "es": "Salir"},
    {"en": "(to)Weigh", "es": "Pesar"},
    {"en": "(to)Joke", "es": "Bromear"},
    {"en": "(to)Smile", "es": "Sonreír"},
    {"en": "Wet", "es": "Húmedo"},
    {"en": "Feet", "es": "Pies"},
    {"en": "Inch", "es": "Pulgada"},
    {"en": "Yard", "es": "Yarda"},
    {"en": "Meter", "es": "Metro"},
    {"en": "Distance", "es": "Distancia"},
    {"en": "Foot", "es": "Pie"},
    {"en": "Trip", "es": "Viaje"},
    {"en": "Snow", "es": "Nieve"},
    {"en": "The same to you", "es": "Igualmente"},
    {"en": "(to)Elect", "es": "Elegir"},
    {"en": "(to)Run", "es": "Lanzar una candidatura"},
    {"en": "(to)Win", "es": "Ganar"},
    {"en": "(to)Represent", "es": "Representar"},
    {"en": "(to)Join to", "es": "Unirse a"},
    {"en": "(to)Shake hand", "es": "Dar la mano"},
    {"en": "(to)Back", "es": "Respaldar"},
    {"en": "(to)Appeal", "es": "Interesar, convencer"},
    {"en": "Official", "es": "Oficial, funcionario"},
    {"en": "Government", "es": "Gobierno"},
    {"en": "Are held", "es": "Son llevados a cabo"},
    {"en": "Candidate", "es": "Candidato"},
    {"en": "Office", "es": "Puesto público, oficina"},
    {"en": "City Council", "es": "Consejo de la ciudad"},
    {"en": "Laws", "es": "Leyes"},
    {"en": "Politicians", "es": "Políticos"},
    {"en": "Politics", "es": "Política"},
    {"en": "Busy", "es": "Ocupado"},
    {"en": "Frequent", "es": "Frecuente"},
    {"en": "Often", "es": "A menudo"},
    {"en": "Voters", "es": "Votantes"},
    {"en": "Background", "es": "Descendencia"},
    {"en": "Speech", "es": "Discurso"},
    {"en": "Still", "es": "Aún"},
    {"en": "Ambitious", "es": "Ambicioso"},
    {"en": "Already", "es": "Ya"},
    {"en": "Rally", "es": "Concentración política"},
    {"en": "Glad", "es": "Alegre, contento"},
    {"en": "Career", "es": "Carrera"},
    {"en": "(to)Replace", "es": "Reemplazar"},
    {"en": "(to)Dig", "es": "Excavar"},
    {"en": "(to)Operate", "es": "Operar"},
    {"en": "(to)Lift", "es": "Levantar"},
    {"en": "(to)Construct", "es": "Construir"},
    {"en": "Hard", "es": "Difícil, duro"},
    {"en": "Interested", "es": "Interesado(a)"},
    {"en": "The best", "es": "El mejor, la mejor"},
    {"en": "Poor", "es": "Pobre"},
    {"en": "Fair", "es": "Regular"},
    {"en": "Either", "es": "Tampoco"},
    {"en": "Fun", "es": "Diversión"},
    {"en": "Pound", "es": "Libra"},
    {"en": "Kilogram", "es": "Kilogramo"},
    {"en": "Light", "es": "Liviano"},
    {"en": "Heavy", "es": "Pesado"},
    {"en": "Weight", "es": "Peso"},
    {"en": "Tall", "es": "Alto"},
    {"en": "Date", "es": "Cita"},
    {"en": "Serious", "es": "Serio"},
    {"en": "Assignment", "es": "Asignación"},
    {"en": "Afraid", "es": "Con miedo"},
    {"en": "Smart", "es": "Inteligente"},
    {"en": "(to)Contain", "es": "Contener"},
]


async def seed_page_5():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 5)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=5,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 5"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 5 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 5 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 5")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_5())
