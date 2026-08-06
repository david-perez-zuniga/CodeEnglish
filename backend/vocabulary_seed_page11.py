from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Navigator", "es": "Navegador"},
    {"en": "Darkness", "es": "Oscuridad"},
    {"en": "Sight", "es": "Vista"},
    {"en": "Coast", "es": "Costa"},
    {"en": "Shape", "es": "Forma"},
    {"en": "Unknown seas", "es": "Mares desconocidos"},
    {"en": "Routes", "es": "Rutas"},
    {"en": "Commerce", "es": "Comercio"},
    {"en": "Whole world", "es": "Todo el mundo"},
    {"en": "Amateur", "es": "Aficionado, principiante"},
    {"en": "Hobby", "es": "Pasa tiempo"},
    {"en": "Variety", "es": "Variedad"},
    {"en": "Performer", "es": "Artista"},
    {"en": "Millionaire", "es": "Millonario"},
    {"en": "Subsidy", "es": "Subsidio"},
    {"en": "(to)Imagine", "es": "Imaginar"},
    {"en": "(to)Compare", "es": "Comparar"},
    {"en": "(to)Approach", "es": "Aproximar, enfoque"},
    {"en": "(to)Develop", "es": "Desarrollar"},
    {"en": "(to)Provide", "es": "Proveer"},
    {"en": "(to)Breathe", "es": "Respirar"},
    {"en": "(to)Maintain", "es": "Mantener"},
    {"en": "(to)Remain", "es": "Permanecer"},
    {"en": "(to)Supply", "es": "Suministrar"},
    {"en": "(to)Afford", "es": "Tener medios para hacer algo"},
    {"en": "(to)Recognize", "es": "Reconocer"},
    {"en": "(to)Cut back", "es": "Disminuir, reducir"},
    {"en": "(to)Land", "es": "Aterrizar, traer a la orilla"},
    {"en": "(to)Gain", "es": "Ganar"},
    {"en": "(to)Bind", "es": "Amarrar, encuadernar"},
    {"en": "Distances", "es": "Distancias"},
    {"en": "Satellite", "es": "Satélite"},
    {"en": "Dust", "es": "Polvo"},
    {"en": "Beyond", "es": "Mas allá"},
    {"en": "Light year", "es": "Año luz"},
    {"en": "Star", "es": "Estrella"},
    {"en": "Galaxy", "es": "Galaxia"},
    {"en": "Clouds", "es": "Nubes"},
    {"en": "Somewhere", "es": "Alguna parte"},
    {"en": "Nearly", "es": "Casi, por poco"},
    {"en": "Atomic power", "es": "Poder atómico"},
    {"en": "Close", "es": "Cerca"},
    {"en": "Journey", "es": "Viaje"},
    {"en": "Complicated", "es": "Complicado"},
    {"en": "Astronauts", "es": "Astronautas"},
    {"en": "Helmet", "es": "Casco"},
    {"en": "Suits", "es": "Trajes"},
    {"en": "Distinction", "es": "Distinción"},
    {"en": "Inner", "es": "Interno"},
    {"en": "Outer", "es": "Exterior"},
    {"en": "Mercury", "es": "Mercurio"},
    {"en": "Venus", "es": "Venus"},
    {"en": "Mars", "es": "Martes"},
    {"en": "Jupiter", "es": "Júpiter"},
    {"en": "Neptune", "es": "Neptuno"},
    {"en": "Saturn", "es": "Saturno"},
    {"en": "Uranus", "es": "Urano"},
    {"en": "Pluto", "es": "Plutón"},
    {"en": "Space probes", "es": "Pruebas espaciales"},
    {"en": "Rocky", "es": "Rocoso"},
    {"en": "Thin", "es": "Delgado"},
    {"en": "Jet plane", "es": "Jet"},
    {"en": "Europeans", "es": "Europeos"},
    {"en": "Even", "es": "Aun"},
    {"en": "Colonists", "es": "Colonizadores, colonos"},
    {"en": "Humanity", "es": "Humanidad"},
    {"en": "Voyage", "es": "Viaje"},
    {"en": "Moon", "es": "Luna"},
    {"en": "Earth", "es": "Tierra"},
    {"en": "Instruments", "es": "Instrumentos"},
    {"en": "Useful", "es": "Útil, provechoso"},
    {"en": "Nature", "es": "Naturaleza"},
    {"en": "Satellite", "es": "Satélite"},
    {"en": "Perhaps", "es": "Tal vez"},
    {"en": "Toward", "es": "Hacia"},
    {"en": "Colony", "es": "Colonia"},
    {"en": "Urgent", "es": "Urgente"},
    {"en": "Immediate", "es": "Inmediato"},
    {"en": "Advantage", "es": "Ventaja"},
    {"en": "Solar system", "es": "Sistema solar"},
    {"en": "Length", "es": "Duración, longitud"},
    {"en": "Radiation", "es": "Radiación"},
    {"en": "Pieces of matter", "es": "Pedazos de materia"},
    {"en": "Humans", "es": "Humanos"},
    {"en": "Environment", "es": "Medio ambiente"},
    {"en": "So far", "es": "Hasta hoy"},
    {"en": "Expense", "es": "Gasto"},
    {"en": "Russian", "es": "Ruso"},
    {"en": "Return", "es": "Devolución"},
    {"en": "Billon", "es": "Billón"},
    {"en": "Tiny", "es": "Pequeño"},
    {"en": "Ship", "es": "Barco"},
    {"en": "Crew", "es": "Tripulación"},
    {"en": "Loads", "es": "Cargas"},
    {"en": "Spices", "es": "Condimentos"},
    {"en": "Valuable", "es": "Valioso"},
    {"en": "Fishing", "es": "Pesca"},
    {"en": "In front on", "es": "En frente de"},
    {"en": "(to)Get off", "es": "Salir(trabajo)"},
    {"en": "(to)Find out", "es": "Averiguar"}
]


async def seed_page_11():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 11)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=11,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 11"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 11 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 11 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 11")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_11())
